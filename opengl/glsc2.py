'''
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
'''
import ctypes as ct

from opengl.bindutils import gl_func
from opengl import gltypes as t

def set_func(name, returnType, paramTypes):
    '''gl_func wrapper that inserts function in globals.'''
    globals()[name] = gl_func(name, returnType, paramTypes)

def set_enum(name, value):
    globals()[name] = value

noParms = ()

#### GLSC2 VERSION 2.0 ####
def init_gl_sc_version_2_0():
    set_func('glActiveTexture', t.void, (t.GLenum,))
    set_func('glBindBuffer', t.void, (t.GLenum, t.GLuint))
    set_func('glBindFramebuffer', t.void, (t.GLenum, t.GLuint))
    set_func('glBindRenderbuffer', t.void, (t.GLenum, t.GLuint))
    set_func('glBindTexture', t.void, (t.GLenum, t.GLuint))
    set_func('glBlendColor', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glBlendEquation', t.void, (t.GLenum,))
    set_func('glBlendEquationSeparate', t.void, (t.GLenum, t.GLenum))
    set_func('glBlendFunc', t.void, (t.GLenum, t.GLenum))
    set_func('glBlendFuncSeparate', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLenum))
    set_func('glBufferData', t.void, (t.GLenum, t.GLsizeiptr, ct.POINTER(t.void), t.GLenum))
    set_func('glBufferSubData', t.void, (t.GLenum, t.GLintptr, t.GLsizeiptr, ct.POINTER(t.void)))
    set_func('glCheckFramebufferStatus', t.GLenum, (t.GLenum,))
    set_func('glClear', t.void, (t.GLbitfield,))
    set_func('glClearColor', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glClearDepthf', t.void, (t.GLfloat,))
    set_func('glClearStencil', t.void, (t.GLint,))
    set_func('glColorMask', t.void, (t.GLboolean, t.GLboolean, t.GLboolean, t.GLboolean))
    set_func('glCompressedTexSubImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glCreateProgram', t.GLuint, ())
    set_func('glCullFace', t.void, (t.GLenum,))
    set_func('glDepthFunc', t.void, (t.GLenum,))
    set_func('glDepthMask', t.void, (t.GLboolean,))
    set_func('glDepthRangef', t.void, (t.GLfloat, t.GLfloat))
    set_func('glDisable', t.void, (t.GLenum,))
    set_func('glDisableVertexAttribArray', t.void, (t.GLuint,))
    set_func('glDrawArrays', t.void, (t.GLenum, t.GLint, t.GLsizei))
    set_func('glDrawRangeElements', t.void, (t.GLenum, t.GLuint, t.GLuint, t.GLsizei, t.GLenum, ct.POINTER(t.void)))
    set_func('glEnable', t.void, (t.GLenum,))
    set_func('glEnableVertexAttribArray', t.void, (t.GLuint,))
    set_func('glFinish', t.void, ())
    set_func('glFlush', t.void, ())
    set_func('glFramebufferRenderbuffer', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint))
    set_func('glFramebufferTexture2D', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint, t.GLint))
    set_func('glFrontFace', t.void, (t.GLenum,))
    set_func('glGenBuffers', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenerateMipmap', t.void, (t.GLenum,))
    set_func('glGenFramebuffers', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenRenderbuffers', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenTextures', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGetAttribLocation', t.GLint, (t.GLuint, ct.POINTER(t.GLchar)))
    set_func('glGetBooleanv', t.void, (t.GLenum, ct.POINTER(t.GLboolean)))
    set_func('glGetBufferParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetError', t.GLenum, ())
    set_func('glGetFloatv', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetFramebufferAttachmentParameteriv', t.void, (t.GLenum, t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetGraphicsResetStatus', t.GLenum, ())
    set_func('glGetIntegerv', t.void, (t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetProgramiv', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetRenderbufferParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetString', ct.POINTER(t.GLubyte), (t.GLenum,))
    set_func('glGetTexParameterfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetTexParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetnUniformfv', t.void, (t.GLuint, t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glGetnUniformiv', t.void, (t.GLuint, t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_func('glGetUniformLocation', t.GLint, (t.GLuint, ct.POINTER(t.GLchar)))
    set_func('glGetVertexAttribfv', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetVertexAttribiv', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetVertexAttribPointerv', t.void, (t.GLuint, t.GLenum, ct.POINTER(ct.POINTER(t.void))))
    set_func('glHint', t.void, (t.GLenum, t.GLenum))
    set_func('glIsEnabled', t.GLboolean, (t.GLenum,))
    set_func('glLineWidth', t.void, (t.GLfloat,))
    set_func('glPixelStorei', t.void, (t.GLenum, t.GLint))
    set_func('glPolygonOffset', t.void, (t.GLfloat, t.GLfloat))
    set_func('glProgramBinary', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.void), t.GLsizei))
    set_func('glReadnPixels', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glRenderbufferStorage', t.void, (t.GLenum, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glSampleCoverage', t.void, (t.GLfloat, t.GLboolean))
    set_func('glScissor', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei))
    set_func('glStencilFunc', t.void, (t.GLenum, t.GLint, t.GLuint))
    set_func('glStencilFuncSeparate', t.void, (t.GLenum, t.GLenum, t.GLint, t.GLuint))
    set_func('glStencilMask', t.void, (t.GLuint,))
    set_func('glStencilMaskSeparate', t.void, (t.GLenum, t.GLuint))
    set_func('glStencilOp', t.void, (t.GLenum, t.GLenum, t.GLenum))
    set_func('glStencilOpSeparate', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLenum))
    set_func('glTexStorage2D', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glTexParameterf', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glTexParameterfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glTexParameteri', t.void, (t.GLenum, t.GLenum, t.GLint))
    set_func('glTexParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glTexSubImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, ct.POINTER(t.void)))
    set_func('glUniform1f', t.void, (t.GLint, t.GLfloat))
    set_func('glUniform1fv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glUniform1i', t.void, (t.GLint, t.GLint))
    set_func('glUniform1iv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_func('glUniform2f', t.void, (t.GLint, t.GLfloat, t.GLfloat))
    set_func('glUniform2fv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glUniform2i', t.void, (t.GLint, t.GLint, t.GLint))
    set_func('glUniform2iv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_func('glUniform3f', t.void, (t.GLint, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glUniform3fv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glUniform3i', t.void, (t.GLint, t.GLint, t.GLint, t.GLint))
    set_func('glUniform3iv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_func('glUniform4f', t.void, (t.GLint, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glUniform4fv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glUniform4i', t.void, (t.GLint, t.GLint, t.GLint, t.GLint, t.GLint))
    set_func('glUniform4iv', t.void, (t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_func('glUniformMatrix2fv', t.void, (t.GLint, t.GLsizei, t.GLboolean, ct.POINTER(t.GLfloat)))
    set_func('glUniformMatrix3fv', t.void, (t.GLint, t.GLsizei, t.GLboolean, ct.POINTER(t.GLfloat)))
    set_func('glUniformMatrix4fv', t.void, (t.GLint, t.GLsizei, t.GLboolean, ct.POINTER(t.GLfloat)))
    set_func('glUseProgram', t.void, (t.GLuint,))
    set_func('glVertexAttrib1f', t.void, (t.GLuint, t.GLfloat))
    set_func('glVertexAttrib1fv', t.void, (t.GLuint, ct.POINTER(t.GLfloat)))
    set_func('glVertexAttrib2f', t.void, (t.GLuint, t.GLfloat, t.GLfloat))
    set_func('glVertexAttrib2fv', t.void, (t.GLuint, ct.POINTER(t.GLfloat)))
    set_func('glVertexAttrib3f', t.void, (t.GLuint, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glVertexAttrib3fv', t.void, (t.GLuint, ct.POINTER(t.GLfloat)))
    set_func('glVertexAttrib4f', t.void, (t.GLuint, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glVertexAttrib4fv', t.void, (t.GLuint, ct.POINTER(t.GLfloat)))
    set_func('glVertexAttribPointer', t.void, (t.GLuint, t.GLint, t.GLenum, t.GLboolean, t.GLsizei, ct.POINTER(t.void)))
    set_func('glViewport', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei))
    set_enum("GL_DEPTH_BUFFER_BIT", 0x00000100)
    set_enum("GL_STENCIL_BUFFER_BIT", 0x00000400)
    set_enum("GL_COLOR_BUFFER_BIT", 0x00004000)
    set_enum("GL_FALSE", 0)
    set_enum("GL_TRUE", 1)
    set_enum("GL_POINTS", 0x0000)
    set_enum("GL_LINES", 0x0001)
    set_enum("GL_LINE_LOOP", 0x0002)
    set_enum("GL_LINE_STRIP", 0x0003)
    set_enum("GL_TRIANGLES", 0x0004)
    set_enum("GL_TRIANGLE_STRIP", 0x0005)
    set_enum("GL_TRIANGLE_FAN", 0x0006)
    set_enum("GL_ZERO", 0)
    set_enum("GL_ONE", 1)
    set_enum("GL_SRC_COLOR", 0x0300)
    set_enum("GL_ONE_MINUS_SRC_COLOR", 0x0301)
    set_enum("GL_SRC_ALPHA", 0x0302)
    set_enum("GL_ONE_MINUS_SRC_ALPHA", 0x0303)
    set_enum("GL_DST_ALPHA", 0x0304)
    set_enum("GL_ONE_MINUS_DST_ALPHA", 0x0305)
    set_enum("GL_DST_COLOR", 0x0306)
    set_enum("GL_ONE_MINUS_DST_COLOR", 0x0307)
    set_enum("GL_SRC_ALPHA_SATURATE", 0x0308)
    set_enum("GL_FUNC_ADD", 0x8006)
    set_enum("GL_BLEND_EQUATION", 0x8009)
    set_enum("GL_BLEND_EQUATION_RGB", 0x8009)
    set_enum("GL_BLEND_EQUATION_ALPHA", 0x883D)
    set_enum("GL_FUNC_SUBTRACT", 0x800A)
    set_enum("GL_FUNC_REVERSE_SUBTRACT", 0x800B)
    set_enum("GL_BLEND_DST_RGB", 0x80C8)
    set_enum("GL_BLEND_SRC_RGB", 0x80C9)
    set_enum("GL_BLEND_DST_ALPHA", 0x80CA)
    set_enum("GL_BLEND_SRC_ALPHA", 0x80CB)
    set_enum("GL_CONSTANT_COLOR", 0x8001)
    set_enum("GL_ONE_MINUS_CONSTANT_COLOR", 0x8002)
    set_enum("GL_CONSTANT_ALPHA", 0x8003)
    set_enum("GL_ONE_MINUS_CONSTANT_ALPHA", 0x8004)
    set_enum("GL_BLEND_COLOR", 0x8005)
    set_enum("GL_ARRAY_BUFFER", 0x8892)
    set_enum("GL_ELEMENT_ARRAY_BUFFER", 0x8893)
    set_enum("GL_ARRAY_BUFFER_BINDING", 0x8894)
    set_enum("GL_ELEMENT_ARRAY_BUFFER_BINDING", 0x8895)
    set_enum("GL_STREAM_DRAW", 0x88E0)
    set_enum("GL_STATIC_DRAW", 0x88E4)
    set_enum("GL_DYNAMIC_DRAW", 0x88E8)
    set_enum("GL_BUFFER_SIZE", 0x8764)
    set_enum("GL_BUFFER_USAGE", 0x8765)
    set_enum("GL_CURRENT_VERTEX_ATTRIB", 0x8626)
    set_enum("GL_FRONT", 0x0404)
    set_enum("GL_BACK", 0x0405)
    set_enum("GL_FRONT_AND_BACK", 0x0408)
    set_enum("GL_TEXTURE_2D", 0x0DE1)
    set_enum("GL_CULL_FACE", 0x0B44)
    set_enum("GL_BLEND", 0x0BE2)
    set_enum("GL_DITHER", 0x0BD0)
    set_enum("GL_STENCIL_TEST", 0x0B90)
    set_enum("GL_DEPTH_TEST", 0x0B71)
    set_enum("GL_SCISSOR_TEST", 0x0C11)
    set_enum("GL_POLYGON_OFFSET_FILL", 0x8037)
    set_enum("GL_SAMPLE_ALPHA_TO_COVERAGE", 0x809E)
    set_enum("GL_SAMPLE_COVERAGE", 0x80A0)
    set_enum("GL_NO_ERROR", 0)
    set_enum("GL_INVALID_ENUM", 0x0500)
    set_enum("GL_INVALID_VALUE", 0x0501)
    set_enum("GL_INVALID_OPERATION", 0x0502)
    set_enum("GL_OUT_OF_MEMORY", 0x0505)
    set_enum("GL_INVALID_FRAMEBUFFER_OPERATION", 0x0506)
    set_enum("GL_CONTEXT_LOST", 0x0507)
    set_enum("GL_CW", 0x0900)
    set_enum("GL_CCW", 0x0901)
    set_enum("GL_LINE_WIDTH", 0x0B21)
    set_enum("GL_ALIASED_POINT_SIZE_RANGE", 0x846D)
    set_enum("GL_ALIASED_LINE_WIDTH_RANGE", 0x846E)
    set_enum("GL_CULL_FACE_MODE", 0x0B45)
    set_enum("GL_FRONT_FACE", 0x0B46)
    set_enum("GL_DEPTH_RANGE", 0x0B70)
    set_enum("GL_DEPTH_WRITEMASK", 0x0B72)
    set_enum("GL_DEPTH_CLEAR_VALUE", 0x0B73)
    set_enum("GL_DEPTH_FUNC", 0x0B74)
    set_enum("GL_STENCIL_CLEAR_VALUE", 0x0B91)
    set_enum("GL_STENCIL_FUNC", 0x0B92)
    set_enum("GL_STENCIL_FAIL", 0x0B94)
    set_enum("GL_STENCIL_PASS_DEPTH_FAIL", 0x0B95)
    set_enum("GL_STENCIL_PASS_DEPTH_PASS", 0x0B96)
    set_enum("GL_STENCIL_REF", 0x0B97)
    set_enum("GL_STENCIL_VALUE_MASK", 0x0B93)
    set_enum("GL_STENCIL_WRITEMASK", 0x0B98)
    set_enum("GL_STENCIL_BACK_FUNC", 0x8800)
    set_enum("GL_STENCIL_BACK_FAIL", 0x8801)
    set_enum("GL_STENCIL_BACK_PASS_DEPTH_FAIL", 0x8802)
    set_enum("GL_STENCIL_BACK_PASS_DEPTH_PASS", 0x8803)
    set_enum("GL_STENCIL_BACK_REF", 0x8CA3)
    set_enum("GL_STENCIL_BACK_VALUE_MASK", 0x8CA4)
    set_enum("GL_STENCIL_BACK_WRITEMASK", 0x8CA5)
    set_enum("GL_VIEWPORT", 0x0BA2)
    set_enum("GL_SCISSOR_BOX", 0x0C10)
    set_enum("GL_COLOR_CLEAR_VALUE", 0x0C22)
    set_enum("GL_COLOR_WRITEMASK", 0x0C23)
    set_enum("GL_UNPACK_ALIGNMENT", 0x0CF5)
    set_enum("GL_PACK_ALIGNMENT", 0x0D05)
    set_enum("GL_MAX_TEXTURE_SIZE", 0x0D33)
    set_enum("GL_MAX_VIEWPORT_DIMS", 0x0D3A)
    set_enum("GL_SUBPIXEL_BITS", 0x0D50)
    set_enum("GL_RED_BITS", 0x0D52)
    set_enum("GL_GREEN_BITS", 0x0D53)
    set_enum("GL_BLUE_BITS", 0x0D54)
    set_enum("GL_ALPHA_BITS", 0x0D55)
    set_enum("GL_DEPTH_BITS", 0x0D56)
    set_enum("GL_STENCIL_BITS", 0x0D57)
    set_enum("GL_POLYGON_OFFSET_UNITS", 0x2A00)
    set_enum("GL_POLYGON_OFFSET_FACTOR", 0x8038)
    set_enum("GL_TEXTURE_BINDING_2D", 0x8069)
    set_enum("GL_SAMPLE_BUFFERS", 0x80A8)
    set_enum("GL_SAMPLES", 0x80A9)
    set_enum("GL_SAMPLE_COVERAGE_VALUE", 0x80AA)
    set_enum("GL_SAMPLE_COVERAGE_INVERT", 0x80AB)
    set_enum("GL_NUM_COMPRESSED_TEXTURE_FORMATS", 0x86A2)
    set_enum("GL_COMPRESSED_TEXTURE_FORMATS", 0x86A3)
    set_enum("GL_DONT_CARE", 0x1100)
    set_enum("GL_FASTEST", 0x1101)
    set_enum("GL_NICEST", 0x1102)
    set_enum("GL_GENERATE_MIPMAP_HINT", 0x8192)
    set_enum("GL_BYTE", 0x1400)
    set_enum("GL_UNSIGNED_BYTE", 0x1401)
    set_enum("GL_SHORT", 0x1402)
    set_enum("GL_UNSIGNED_SHORT", 0x1403)
    set_enum("GL_INT", 0x1404)
    set_enum("GL_UNSIGNED_INT", 0x1405)
    set_enum("GL_FLOAT", 0x1406)
    set_enum("GL_RED", 0x1903)
    set_enum("GL_RG", 0x8227)
    set_enum("GL_RGB", 0x1907)
    set_enum("GL_RGBA", 0x1908)
    set_enum("GL_UNSIGNED_SHORT_4_4_4_4", 0x8033)
    set_enum("GL_UNSIGNED_SHORT_5_5_5_1", 0x8034)
    set_enum("GL_UNSIGNED_SHORT_5_6_5", 0x8363)
    set_enum("GL_MAX_VERTEX_ATTRIBS", 0x8869)
    set_enum("GL_MAX_VERTEX_UNIFORM_VECTORS", 0x8DFB)
    set_enum("GL_MAX_VARYING_VECTORS", 0x8DFC)
    set_enum("GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS", 0x8B4D)
    set_enum("GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS", 0x8B4C)
    set_enum("GL_MAX_TEXTURE_IMAGE_UNITS", 0x8872)
    set_enum("GL_MAX_FRAGMENT_UNIFORM_VECTORS", 0x8DFD)
    set_enum("GL_LINK_STATUS", 0x8B82)
    set_enum("GL_SHADING_LANGUAGE_VERSION", 0x8B8C)
    set_enum("GL_CURRENT_PROGRAM", 0x8B8D)
    set_enum("GL_NEVER", 0x0200)
    set_enum("GL_LESS", 0x0201)
    set_enum("GL_EQUAL", 0x0202)
    set_enum("GL_LEQUAL", 0x0203)
    set_enum("GL_GREATER", 0x0204)
    set_enum("GL_NOTEQUAL", 0x0205)
    set_enum("GL_GEQUAL", 0x0206)
    set_enum("GL_ALWAYS", 0x0207)
    set_enum("GL_KEEP", 0x1E00)
    set_enum("GL_REPLACE", 0x1E01)
    set_enum("GL_INCR", 0x1E02)
    set_enum("GL_DECR", 0x1E03)
    set_enum("GL_INVERT", 0x150A)
    set_enum("GL_INCR_WRAP", 0x8507)
    set_enum("GL_DECR_WRAP", 0x8508)
    set_enum("GL_VENDOR", 0x1F00)
    set_enum("GL_RENDERER", 0x1F01)
    set_enum("GL_VERSION", 0x1F02)
    set_enum("GL_EXTENSIONS", 0x1F03)
    set_enum("GL_NEAREST", 0x2600)
    set_enum("GL_LINEAR", 0x2601)
    set_enum("GL_NEAREST_MIPMAP_NEAREST", 0x2700)
    set_enum("GL_LINEAR_MIPMAP_NEAREST", 0x2701)
    set_enum("GL_NEAREST_MIPMAP_LINEAR", 0x2702)
    set_enum("GL_LINEAR_MIPMAP_LINEAR", 0x2703)
    set_enum("GL_TEXTURE_MAG_FILTER", 0x2800)
    set_enum("GL_TEXTURE_MIN_FILTER", 0x2801)
    set_enum("GL_TEXTURE_WRAP_S", 0x2802)
    set_enum("GL_TEXTURE_WRAP_T", 0x2803)
    set_enum("GL_TEXTURE_IMMUTABLE_FORMAT", 0x912F)
    set_enum("GL_TEXTURE", 0x1702)
    set_enum("GL_TEXTURE0", 0x84C0)
    set_enum("GL_TEXTURE1", 0x84C1)
    set_enum("GL_TEXTURE2", 0x84C2)
    set_enum("GL_TEXTURE3", 0x84C3)
    set_enum("GL_TEXTURE4", 0x84C4)
    set_enum("GL_TEXTURE5", 0x84C5)
    set_enum("GL_TEXTURE6", 0x84C6)
    set_enum("GL_TEXTURE7", 0x84C7)
    set_enum("GL_TEXTURE8", 0x84C8)
    set_enum("GL_TEXTURE9", 0x84C9)
    set_enum("GL_TEXTURE10", 0x84CA)
    set_enum("GL_TEXTURE11", 0x84CB)
    set_enum("GL_TEXTURE12", 0x84CC)
    set_enum("GL_TEXTURE13", 0x84CD)
    set_enum("GL_TEXTURE14", 0x84CE)
    set_enum("GL_TEXTURE15", 0x84CF)
    set_enum("GL_TEXTURE16", 0x84D0)
    set_enum("GL_TEXTURE17", 0x84D1)
    set_enum("GL_TEXTURE18", 0x84D2)
    set_enum("GL_TEXTURE19", 0x84D3)
    set_enum("GL_TEXTURE20", 0x84D4)
    set_enum("GL_TEXTURE21", 0x84D5)
    set_enum("GL_TEXTURE22", 0x84D6)
    set_enum("GL_TEXTURE23", 0x84D7)
    set_enum("GL_TEXTURE24", 0x84D8)
    set_enum("GL_TEXTURE25", 0x84D9)
    set_enum("GL_TEXTURE26", 0x84DA)
    set_enum("GL_TEXTURE27", 0x84DB)
    set_enum("GL_TEXTURE28", 0x84DC)
    set_enum("GL_TEXTURE29", 0x84DD)
    set_enum("GL_TEXTURE30", 0x84DE)
    set_enum("GL_TEXTURE31", 0x84DF)
    set_enum("GL_ACTIVE_TEXTURE", 0x84E0)
    set_enum("GL_REPEAT", 0x2901)
    set_enum("GL_CLAMP_TO_EDGE", 0x812F)
    set_enum("GL_MIRRORED_REPEAT", 0x8370)
    set_enum("GL_SAMPLER_2D", 0x8B5E)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_ENABLED", 0x8622)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_SIZE", 0x8623)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_STRIDE", 0x8624)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_TYPE", 0x8625)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_NORMALIZED", 0x886A)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_POINTER", 0x8645)
    set_enum("GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING", 0x889F)
    set_enum("GL_IMPLEMENTATION_COLOR_READ_TYPE", 0x8B9A)
    set_enum("GL_IMPLEMENTATION_COLOR_READ_FORMAT", 0x8B9B)
    set_enum("GL_NUM_PROGRAM_BINARY_FORMATS", 0x87FE)
    set_enum("GL_PROGRAM_BINARY_FORMATS", 0x87FF)
    set_enum("GL_LOW_FLOAT", 0x8DF0)
    set_enum("GL_MEDIUM_FLOAT", 0x8DF1)
    set_enum("GL_HIGH_FLOAT", 0x8DF2)
    set_enum("GL_LOW_INT", 0x8DF3)
    set_enum("GL_MEDIUM_INT", 0x8DF4)
    set_enum("GL_HIGH_INT", 0x8DF5)
    set_enum("GL_FRAMEBUFFER", 0x8D40)
    set_enum("GL_RENDERBUFFER", 0x8D41)
    set_enum("GL_R8", 0x8229)
    set_enum("GL_RG8", 0x822B)
    set_enum("GL_RGB8", 0x8051)
    set_enum("GL_RGBA8", 0x8058)
    set_enum("GL_RGBA4", 0x8056)
    set_enum("GL_RGB5_A1", 0x8057)
    set_enum("GL_RGB565", 0x8D62)
    set_enum("GL_DEPTH_COMPONENT16", 0x81A5)
    set_enum("GL_STENCIL_INDEX8", 0x8D48)
    set_enum("GL_RENDERBUFFER_WIDTH", 0x8D42)
    set_enum("GL_RENDERBUFFER_HEIGHT", 0x8D43)
    set_enum("GL_RENDERBUFFER_INTERNAL_FORMAT", 0x8D44)
    set_enum("GL_RENDERBUFFER_RED_SIZE", 0x8D50)
    set_enum("GL_RENDERBUFFER_GREEN_SIZE", 0x8D51)
    set_enum("GL_RENDERBUFFER_BLUE_SIZE", 0x8D52)
    set_enum("GL_RENDERBUFFER_ALPHA_SIZE", 0x8D53)
    set_enum("GL_RENDERBUFFER_DEPTH_SIZE", 0x8D54)
    set_enum("GL_RENDERBUFFER_STENCIL_SIZE", 0x8D55)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE", 0x8CD0)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME", 0x8CD1)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL", 0x8CD2)
    set_enum("GL_COLOR_ATTACHMENT0", 0x8CE0)
    set_enum("GL_DEPTH_ATTACHMENT", 0x8D00)
    set_enum("GL_STENCIL_ATTACHMENT", 0x8D20)
    set_enum("GL_NONE", 0)
    set_enum("GL_FRAMEBUFFER_COMPLETE", 0x8CD5)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT", 0x8CD6)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT", 0x8CD7)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS", 0x8CD9)
    set_enum("GL_FRAMEBUFFER_UNSUPPORTED", 0x8CDD)
    set_enum("GL_FRAMEBUFFER_UNDEFINED", 0x8219)
    set_enum("GL_FRAMEBUFFER_BINDING", 0x8CA6)
    set_enum("GL_RENDERBUFFER_BINDING", 0x8CA7)
    set_enum("GL_MAX_RENDERBUFFER_SIZE", 0x84E8)
    set_enum("GL_GUILTY_CONTEXT_RESET", 0x8253)
    set_enum("GL_INNOCENT_CONTEXT_RESET", 0x8254)
    set_enum("GL_UNKNOWN_CONTEXT_RESET", 0x8255)
    set_enum("GL_CONTEXT_ROBUST_ACCESS", 0x90F3)
    set_enum("GL_RESET_NOTIFICATION_STRATEGY", 0x8256)
    set_enum("GL_LOSE_CONTEXT_ON_RESET", 0x8252)


#### GL_EXT_TEXTURE_COMPRESSION_S3TC ####
def init_gl_ext_texture_compression_s3tc():
    set_enum("GL_COMPRESSED_RGB_S3TC_DXT1_EXT", 0x83F0)
    set_enum("GL_COMPRESSED_RGBA_S3TC_DXT1_EXT", 0x83F1)
    set_enum("GL_COMPRESSED_RGBA_S3TC_DXT3_EXT", 0x83F2)
    set_enum("GL_COMPRESSED_RGBA_S3TC_DXT5_EXT", 0x83F3)


#### GL_OES_DEPTH24 ####
def init_gl_oes_depth24():
    set_enum("GL_DEPTH_COMPONENT24_OES", 0x81A6)


#### GL_OES_DEPTH32 ####
def init_gl_oes_depth32():
    set_enum("GL_DEPTH_COMPONENT32_OES", 0x81A7)


#### GL_OES_RGB8_RGBA8 ####
def init_gl_oes_rgb8_rgba8():
    set_enum("GL_RGB8_OES", 0x8051)
    set_enum("GL_RGBA8_OES", 0x8058)


#### GL_OES_STANDARD_DERIVATIVES ####
def init_gl_oes_standard_derivatives():
    set_enum("GL_FRAGMENT_SHADER_DERIVATIVE_HINT_OES", 0x8B8B)


def init():
    init_gl_sc_version_2_0()
    init_gl_ext_texture_compression_s3tc()
    init_gl_oes_depth24()
    init_gl_oes_depth32()
    init_gl_oes_rgb8_rgba8()
    init_gl_oes_standard_derivatives()

