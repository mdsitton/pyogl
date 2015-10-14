import ctypes as ct

# private non gl types
_c_ptrdiff_t = ct.c_ssize_t

class _Opaque(ct.Structure):
    pass

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
GLclampx = ct.c_int
GLdouble = ct.c_double
GLclampd = ct.c_double
void = None
GLvoid = None
GLchar = ct.c_char
GLfixed = GLint

GLintptr = _c_ptrdiff_t
GLintptrARB = _c_ptrdiff_t
GLsizeiptrARB = _c_ptrdiff_t
GLsizeiptr = _c_ptrdiff_t

GLvdpauSurfaceNV = GLintptr

GLuint64EXT = ct.c_ulonglong
GLint64EXT = ct.c_longlong

GLuint64 = ct.c_ulonglong
GLint64 = ct.c_longlong


GLhandleARB = ct.c_uint
GLcharARB = ct.c_char

GLeglImageOES = ct.c_void_p

GLhalfARB = ct.c_ushort
GLhalfNV = ct.c_ushort
GLsync = ct.POINTER(_Opaque)


__all__ = ['GLenum',
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
        'void',
        'GLvoid',
        'GLchar',
        'GLintptr',
        'GLsizeiptr',
        'GLhandleARB',
        'GLcharARB',
        'GLhalfARB',
        'GLhalfNV',
        'GLsync']
