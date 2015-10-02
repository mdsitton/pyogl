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
    ptrCount = 0

    if '*' in typeInfo:
        ptrLoc = typeInfo.index('*')
    elif '**' in typeInfo:
        ptrLoc = typeInfo.index('**')
    else:
        ptrLoc = None

    if ptrLoc is not None:
        ptrStr = typeInfo[ptrLoc]
        ptrCount = ptrStr.count('*')
        typeInfo.remove('*'*ptrCount)

    return ptrCount


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

        # generate return type string must be done before pointers.
        filter_const(rtnType)


        # Handle pointers
        rtnPtrCount = filter_pointer(rtnType)

        rtnStr = rtnType[0]

        # add the found number of pointers to the object.
        if rtnPtrCount:
            for i in range(rtnPtrCount):
                rtnStr = pointer.format(rtnStr)

        # Mark the function  to be commented out out if we do
        # not currently support any of the datatypes needed
        if rtnType[0] not in supportedTypes:
            commentFunction = True

        # generate param list string
        parmItems = []
        for parName, parType in params:

            # Copy list since iterating and changing a list can get
            # finiky... I'll see if its actually needed later.
            parType = parType[:] 


            # generate return type string must be done before pointers.
            filter_const(parType)

            # Handle pointers
            parPtrCount = filter_pointer(parType)

            parStr = parType[0]
            # add the found number of pointers to the object.
            if parPtrCount:
                for i in range(parPtrCount):
                    parStr = pointer.format(parStr)

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