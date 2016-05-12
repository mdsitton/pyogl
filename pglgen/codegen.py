from collections import OrderedDict

from opengl import gltypes

from pglgen import regparse

# Get list of supported types automatically
supportedTypes = [item for item in dir(gltypes) if item[0] != '_' and item != 'ct']
codeHeader = '''\'\'\'
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
\'\'\'
import ctypes as ct

from opengl.bindutils import gl_func
from opengl import gltypes as t

def set_func(name, returnType, paramTypes):
    \'\'\'gl_func wrapper that inserts function in globals.\'\'\'
    globals()[name] = gl_func(name, returnType, paramTypes)

def set_enum(name, value):
    globals()[name] = value

noParms = ()
'''

enum = '    set_enum("{0}", {1})\n'

funcTemplate = '''
def {0}():
{1}
'''
initTemplate = '''
def init():
{0}
'''

func = '    set_func(\'{0}\', {1}, ({2}))\n'
commentedFunc = '    # set_func(\'{0}\', {1}, ({2}))\n'

pointer = 'ct.POINTER({0})'


def filter_const(typeInfo):
    '''
    Remove const declarations from types since its not very
    enfocable with python.
    '''

    # This counts how many const have been removed to
    # compensate for the new index location
    consCorrect = 0

    for i, item in enumerate(typeInfo[:]):
        if 'const' == item:
            typeInfo.remove('const')
            consCorrect += 1
        elif 'const' in item:
            typeInfo[i-consCorrect] = ''.join(item.split('const')).strip()

    # return typeStr


def filter_pointer(typeInfo):
    '''
    Filters out pointers from the type info list
    returns the number of pointers found and removed.
    '''
    ptrLocs = [i for i, item in enumerate(typeInfo) if '*' in item]

    ptrCount = 0

    if ptrLocs:
        for i in ptrLocs:
            ptrStr = typeInfo[i]
            ptrCount += ptrStr.count('*')
            typeInfo.remove(ptrStr)

    return ptrCount

def parse_type(typeInfo):
    #print (typeInfo)

    # generate return type string must be done before pointers.
    filter_const(typeInfo)

    # Handle pointers
    ptrCount = filter_pointer(typeInfo)
    typeStr = typeInfo[0] # There will only be a single value in typeInfo
    baseTypeStr = typeStr
    if typeStr:
        if typeStr == 'int':
            baseTypeStr = 'INT'
        elif typeStr == 'char':
            baseTypeStr = 'CHAR'
        elif typeStr == 'float':
            baseTypeStr = 'FLOAT'
        elif typeStr == 'unsigned int':
            baseTypeStr = 'UINT'
        elif typeStr == 'unsigned long':
            baseTypeStr = 'ULONG'
        typeStr = 't.'+baseTypeStr

    # add the found number of pointers to the object.
    if ptrCount:
        for i in range(ptrCount):
            typeStr = pointer.format(typeStr)


    #print (typeStr, baseTypeStr)

    return typeStr, baseTypeStr


def gen_func_code(enums, commands):
    functionCode = []
    nonCommented = False

    for name, typeInfo in commands.items():
        rtnType = typeInfo['return'][:]
        params = typeInfo['parms']

        commentFunction = False

        rtnStr, baseRtnType = parse_type(rtnType)

        # Mark the function  to be commented out out if we do
        # not currently support any of the datatypes needed
        if baseRtnType not in supportedTypes:
            commentFunction = True

        # generate param list string
        parmItems = []
        for parName, parType in params:
            # Fix issue where if a function was generated twice it would be
            # missing pointers. This was because the same list was being passed
            # by reference all the way to the parseType function where it was
            # modified...
            parTypeCpy = parType[:]

            parStr, baseType = parse_type(parTypeCpy)

            # Mark the function to be commented out out if we do
            # not currently support any of the datatypes needed
            if baseType not in supportedTypes:
                commentFunction = True

            parmItems.append(parStr)

        # Add a comma to the end of a single argument because tuples..
        if len(parmItems) == 1:
            parmStr = '{0},'.format(parmItems[0])
        else:
            parmStr = ', '.join(parmItems)

        # Comment out function if marked.
        if commentFunction:
            funcCode = commentedFunc.format(name, rtnStr, parmStr)
        else:
            nonCommented = True
            funcCode = func.format(name, rtnStr, parmStr)

        functionCode.append(funcCode)

    for name, value in enums.items():
        if '(' in value or ')' in value:
            functionCode.append('# {0}'.format(enum.format(name, value)))
        else:
            nonCommented = True
            functionCode.append(enum.format(name, value))

    if not nonCommented:
        functionCode.append('    pass')

    return ''.join(functionCode)

def gen_bindings(apis):
    for api in apis:
        code = gen_binding(*regparse.parse_registry('{0}.xml'.format(api)))

        for subapi, outputCode in code.items():
            with open('./opengl/{}.py'.format(subapi), 'w') as glFile:
                glFile.write(outputCode)

def gen_binding(enums, commands, features, extensions):
    '''Generate the binding code using the dictionaries passed in'''

    initNames = {}
    code = {}
    for api, apiNames in features.items():
        code[api] = []
        initNames[api] = []
        code[api].append(codeHeader)
        for verName, verFeatures in apiNames.items():

            version = verFeatures['info']['version']

            code[api].append('\n#### {} VERSION {} ####'.format(api.upper(), version))

            featureCmds = OrderedDict()
            featureEnums = OrderedDict()

            for name, featureData in verFeatures.items():
                if name == 'info':
                    continue
                for c in featureData['require']['command']:
                    featureCmds[c] = commands[c]
                for e in featureData['require']['enum']:
                    featureEnums[e] = enums[e]

            funcName = 'init_' + verName.lower()
            initNames[api].append(funcName)

            funcCode = gen_func_code(featureEnums, featureCmds)

            code[api].append(funcTemplate.format(funcName, funcCode))

    #print (extensions)
    for api, extNames in extensions.items():
        for extName, extFeature in extNames.items():
            code[api].append('\n#### {} ####'.format(extName.upper()))

            extCmds = OrderedDict()
            extEnums = OrderedDict()
            for extData in extFeature.values():
                for c in extData['command']:
                    extCmds[c] = commands[c]
                for e in extData['enum']:
                    extEnums[e] = enums[e]

            funcName = 'init_' + extName.lower()
            initNames[api].append(funcName)
            funcCode = gen_func_code(extEnums, extCmds)

            code[api].append(funcTemplate.format(funcName, funcCode))

    for api, names in initNames.items():
        initCode = []
        for initName in names:
            initCode.append('    {}()\n'.format(initName))

        code[api].append(initTemplate.format(''.join(initCode)))

    return {api: ''.join(sepCode) for api, sepCode in code.items()}
