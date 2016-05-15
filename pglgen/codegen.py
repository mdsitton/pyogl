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

def parse_type(typeStr):

    typeList = []
    typePart = typeStr.partition('*')

    typeList.append(typePart[0])

    ptrStr = ''.join(typePart[1:])

    if ptrStr != '':
        pointers = ptrStr.split('*')
        del pointers[0]  # pointers start off offset by 1 position.
        pointers = ['*'+ptr for ptr in pointers]

        typeList.extend(pointers)

    typeStack = []

    for dataType in typeList:

        typeData = {}

        if 'const' in dataType:
            typeData['const'] = True
        else:
            typeData['const'] = False

        if '*' in dataType:
            typeData['type'] = 'pointer'
        else:
            typeData['type'] = dataType.replace('const', '').strip()

        typeStack.append(typeData)

    return typeStack

typeMap = {
    'int': 'INT',
    'char': 'CHAR',
    'float': 'FLOAT',
    'unsigned int': 'UINT',
    'unsigned long': 'ULONG'
}

def generate_type_str(typeData):

    baseTypeStr = None

    typeStr = ''

    for typeItem in typeData:
        dataType = typeItem['type']
        isConst = typeItem['const']

        if dataType == 'pointer':
            typeStr = pointer.format(typeStr)

        else:

            try:
                baseTypeStr = typeMap[dataType]
            except KeyError:
                baseTypeStr = dataType

            typeStr = 't.'+baseTypeStr

    return typeStr, baseTypeStr


def gen_func_code(enums, commands):
    functionCode = []
    nonCommented = False

    for name, typeInfo in commands.items():
        rtnType = typeInfo['return'][:]
        params = typeInfo['parms']

        commentFunction = False

        typeData = parse_type(rtnType)
        rtnStr, baseRtnType = generate_type_str(typeData)

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

            typeData = parse_type(parTypeCpy)
            parStr, baseType = generate_type_str(typeData)

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
