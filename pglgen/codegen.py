from collections import OrderedDict

from opengl import gltypes

from pglgen import regparse

# Get list of supported types automatically
supportedTypes = [item for item in dir(gltypes) if item[0] != '_' and item != 'ct']

codeHeader = '''\'\'\'
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
\'\'\'
import sys
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
            typeInfo[i-consCorrect] = ''.join(item.split('const'))

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

    # generate return type string must be done before pointers.
    filter_const(typeInfo)

    # Handle pointers
    ptrCount = filter_pointer(typeInfo)

    typeStr = typeInfo[0]
    if typeStr:
        typeStr = 't.'+typeStr

    # add the found number of pointers to the object.
    if ptrCount:
        for i in range(ptrCount):
            typeStr = pointer.format(typeStr)

    return typeStr


def gen_func_code(enums, commands):
    functionCode = []
    nonCommented = False

    for name, typeInfo in commands.items():
        rtnType = typeInfo['return'][:]
        params = typeInfo['parms']

        commentFunction = False

        rtnStr = parse_type(rtnType)

        # Mark the function  to be commented out out if we do
        # not currently support any of the datatypes needed
        if rtnType[0] not in supportedTypes:
            commentFunction = True

        # generate param list string
        parmItems = []
        for parName, parType in params:

            parStr = parse_type(parType)

            # Mark the function  to be commented out out if we do
            # not currently support any of the datatypes needed
            if parType[0] not in supportedTypes:
                commentFunction = True

            parmItems.append(parStr)

        # Add a comma to the end of a single argument because tuples..
        if len(parmItems) == 1:
            parmStr = '{0},'.format(parmItems[0])
        else:
            parmStr = ', '.join(parmItems)

        # Comment out function if marked.
        if commentFunction:
            funcCode = '# {0}'.format(func.format(name, rtnStr, parmStr))
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

        with open('./opengl/{}.py'.format(api), 'w') as glFile:
            glFile.write(code)

def gen_binding(enums, commands, features, extensions):
    '''Generate the binding code using the dictionaries passed in'''

    initNames = []
    code = []
    code.append(codeHeader)
    for api, apiNames in features.items():
        for verName, verFeatures in apiNames.items():

            version = verFeatures['info']['version']

            code.append('\n#### {} VERSION {} ####'.format(api.upper(), version))

            featureCmds = OrderedDict()
            featureEnums = OrderedDict()

            for c in verFeatures['default']['require']['command']:
                featureCmds[c] = commands[c]
            for e in verFeatures['default']['require']['enum']:
                featureEnums[e] = enums[e]

            funcName = 'init_' + verName.lower()
            initNames.append(funcName)

            funcCode = gen_func_code(featureEnums, featureCmds)

            code.append(funcTemplate.format(funcName, funcCode))

    for name, data in extensions.items():
        code.append('\n#### {} ####'.format(name.upper()))
        extCmds = OrderedDict()
        extEnums = OrderedDict()

        for c in data['command']:
            extCmds[c] = commands[c]
        for e in data['enum']:
            extEnums[e] = enums[e]

        funcName = 'init_' + name.lower()
        initNames.append(funcName)
        funcCode = gen_func_code(extEnums, extCmds)

        code.append(funcTemplate.format(funcName, funcCode))

    initCode = []
    for i in initNames:
        initCode.append('    {}()\n'.format(i))

    code.append(initTemplate.format(''.join(initCode)))

    return ''.join(code)
