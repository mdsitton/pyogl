
supportedTypes = ['GLenum',
        'GLbitfield',
        'GLuint',
        'GLint',
        'GLsizei',
        'GLboolean',
        'GLbyte',
        'GLshort',
        'GLubyte',
        'GLushort',
        'GLulong',
        'GLfloat',
        'GLclampf',
        'GLdouble',
        'GLclampd',
        'GLvoid',
        'GLchar',
        'GLintptr',
        'GLsizeiptr',
        'GLhandleARB',
        'GLcharARB',
        'GLhalfARB',
        'GLhalfNV',
        'void']

codeHeader = '''\'\'\'
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
\'\'\'
import sys
import ctypes as ct

from ed2d.bindutils import gl_func

c_ptrdiff_t = ct.c_ssize_t

GLenum = ct.c_uint
GLbitfield = ct.c_uint
GLuint = ct.c_uint
GLint = ct.c_int
GLsizei = ct.c_int
GLboolean = ct.c_ubyte
GLbyte = ct.c_char
GLshort = ct.c_short
GLubyte = ct.c_ubyte
GLushort = ct.c_ushort
GLulong = ct.c_ulong
GLfloat = ct.c_float
GLclampf = ct.c_float
GLdouble = ct.c_double
GLclampd = ct.c_double
void = GLvoid = None
GLchar = ct.c_char

GLintptr = c_ptrdiff_t
GLsizeiptr = c_ptrdiff_t

GLhandleARB = ct.c_uint
GLcharARB = ct.c_char

GLhalfARB = ct.c_ushort
GLhalfNV = ct.c_ushort

'''

enum = '{0} = {1}\n'

funcHeader = '''
def init():
    gl = sys.modules['ed2d.opengl.gl']

    noParms = ()
'''
func = '    gl.{0} = gl_func( \'{0}\', {1}, ({2}))\n'

pointer = 'ct.POINTER({0})'

def gen_binding(enums, commands):
    code = []
    code.append(codeHeader)

    for name, value in enums.items():
        code.append(enum.format(name, value))

    code.append(funcHeader)


    for name, typeInfo in commands.items():
        rtnType = typeInfo['return'][:]
        params = typeInfo['parms']

        commentFunction = False

        # generate return type string

        # Remove const declarations from types since its not very
        # enfocable with python.
        consCorrect = 0
        for i, item in enumerate(rtnType[:]):
            if 'const' == item:
                rtnType.remove('const')
                consCorrect += 1
            elif 'const' in item:
                rtnType[i-consCorrect] = ''.join(item.split('const'))


        # Handle pointers
        rtnPtrCount = 0

        if '*' in rtnType:
            rtnPtrLoc = rtnType.index('*')
        elif '**' in rtnType:
            rtnPtrLoc = rtnType.index('**')
        else:
            rtnPtrLoc = None
        if rtnPtrLoc is not None:
            rtnPtrStr = rtnType[rtnPtrLoc]
            rtnPtrCount = rtnPtrStr.count('*')
            rtnType.remove('*'*rtnPtrCount)

        rtnStr = rtnType[0]

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

            # Remove const declarations from types since its not very
            # enfocable with python.
            # TODO - This is basically copy paste from above... 
            consCorrect = 0
            for i, item in enumerate(parType[:]):
                if 'const' == item:
                    parType.remove('const')
                    consCorrect += 1
                elif 'const' in item:
                    parType[i-consCorrect] = ''.join(item.split('const'))

            # Handle pointers
            # TODO - This is basically copy paste from above... 
            parPtrCount = 0

            if '*' in parType:
                parPtrLoc = parType.index('*')
            elif '**' in parType:
                parPtrLoc = parType.index('**')
            else:
                parPtrLoc = None
            if parPtrLoc is not None:
                parPtrStr = parType[parPtrLoc]
                parPtrCount = parPtrStr.count('*')
                parType.remove('*'*parPtrCount)


            parStr = parType[0]

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