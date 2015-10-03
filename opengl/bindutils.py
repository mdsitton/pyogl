import ctypes as ct
from ctypes.util import find_library

import platform
osName = platform.system()

# list to keep refrences to c strings around
_stringRef = []


def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))


def cast_ptr(obj, ptrType):
    return ct.cast(obj, ct.POINTER(ptrType))


def to_c_str(text, extList=False):
    ''' Convert python strings to null terminated c strings. '''
    # We only want to keep the cString data around for 1 call
    if not extList and len(_stringRef) != 0:
        _stringRef.remove(_stringRef[0])
    cStr = ct.create_string_buffer(text.encode(encoding='UTF-8'))
    _stringRef.append(cStr)
    return ct.cast(ct.pointer(cStr), ct.POINTER(ct.c_char))


def conv_list(listIn, cType):
    ''' Convert a python list into a ctypes array '''
    return (cType * len(listIn))(*listIn)


def conv_list_2d(listIn, cType):
    ''' Convert a python 2d list into a ctypes 2d array '''
    xlength = len(listIn)
    ylength = len(listIn[0])

    arrayOut = (cType * ylength * xlength)()

    for x in range(xlength):
        for y in range(ylength):
            arrayOut[x][y] = listIn[x][y]

    return arrayOut


def define_function(libName, name, returnType, params):
    '''Helper function to help in binding functions'''
    if osName == "Windows":
        function = ct.WINFUNCTYPE(returnType, *params)
        lib = ct.WinDLL(libName)
    elif osName == "Darwin" or osName == "Linux":
        function = ct.FUNCTYPE(returnType, *params)
        lib = ct.CDLL(find_library(libName))

    address = getattr(lib, name)
    new_func = ct.cast(address, function)

    return new_func


if osName == "Windows":
    glGetProcAddress = define_function('opengl32', 'wglGetProcAddress',
            ct.POINTER(ct.c_int), (ct.c_char_p,))

elif osName in ('Linux', 'Darwin', 'Windows'):
    from sdl2 import SDL_GL_GetProcAddress
    glGetProcAddress = SDL_GL_GetProcAddress


class _BindGL(object):
    def __init__(self):
        self.osName = platform.system()

        if self.osName == 'Linux':
            libFound = find_library('GL')
            self.lib = ct.CDLL(libFound)
            self.funcType = ct.CFUNCTYPE
        elif self.osName == 'Windows':
            libFound = find_library('opengl32')
            self.lib = ct.WinDLL(libFound)
            self.funcType = ct.WINFUNCTYPE
        elif self.osName == 'Darwin': # Mac OS X
            libraryPath = '/System/Library/Frameworks/OpenGL.framework'
            libFound = find_library(libraryPath)
            self.lib = ct.CDLL(libFound)
            self.funcType = ct.CFUNCTYPE

    def gl_func(self, name, returnType, paramTypes):
        ''' Define and load an opengl function '''
        function = self.funcType(returnType, *paramTypes)

        try:
            address = getattr(self.lib, name)
        except AttributeError:
            name = name.encode(encoding='UTF-8')
            address = glGetProcAddress(name)

        return ct.cast(address, function)


_glbind = _BindGL()
gl_func = _glbind.gl_func

__all__ = ['gl_func', 'define_function']
