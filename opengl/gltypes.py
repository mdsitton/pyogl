import ctypes as ct

_c_ptrdiff_t = ct.c_ssize_t

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
void = None
GLvoid = None
GLchar = ct.c_char

GLintptr = _c_ptrdiff_t
GLsizeiptr = _c_ptrdiff_t

GLhandleARB = ct.c_uint
GLcharARB = ct.c_char

GLhalfARB = ct.c_ushort
GLhalfNV = ct.c_ushort