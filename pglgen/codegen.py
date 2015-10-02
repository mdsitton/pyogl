from opengl import gltypes

# Get list of supported types automatically
supportedTypes = [item for item in dir(gltypes) if item[0] != '_' and item != 'ct']

codeHeader = '''\'\'\'
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
\'\'\'
import sys
import ctypes as ct

from opengl.bindutils import gl_func
from opengl.gltypes import *

'''

enum = '{0} = {1}\n'

funcHeader = '''
def init():
    gl = sys.modules['opengl.gl']

    noParms = ()
'''

func = '    gl.{0} = gl_func( \'{0}\', {1}, ({2}))\n'

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
    Filters out pointers frin the type info list
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

    # add the found number of pointers to the object.
    if ptrCount:
        for i in range(ptrCount):
            typeStr = pointer.format(typeStr)

    return typeStr


def gen_binding(enums, commands):
    '''Generate the binding code using the dictionaries passed in'''

    code = []
    code.append(codeHeader)

    for name, value in enums.items():
        code.append(enum.format(name, value))

    code.append(funcHeader)


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
            funcCode = func.format(name, rtnStr, parmStr)

        code.append(funcCode)

    codeStr = ''.join(code)

    return codeStr