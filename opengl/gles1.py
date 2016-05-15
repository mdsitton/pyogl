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

#### GLES1 VERSION 1.0 ####
def init_gl_version_es_cm_1_0():
    set_func('glAlphaFunc', t.void, (t.GLenum, t.GLfloat))
    set_func('glClearColor', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glClearDepthf', t.void, (t.GLfloat,))
    set_func('glClipPlanef', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glColor4f', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glDepthRangef', t.void, (t.GLfloat, t.GLfloat))
    set_func('glFogf', t.void, (t.GLenum, t.GLfloat))
    set_func('glFogfv', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glFrustumf', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glGetClipPlanef', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetFloatv', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetLightfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetMaterialfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetTexEnvfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetTexParameterfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glLightModelf', t.void, (t.GLenum, t.GLfloat))
    set_func('glLightModelfv', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glLightf', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glLightfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glLineWidth', t.void, (t.GLfloat,))
    set_func('glLoadMatrixf', t.void, (ct.POINTER(t.GLfloat),))
    set_func('glMaterialf', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glMaterialfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glMultMatrixf', t.void, (ct.POINTER(t.GLfloat),))
    set_func('glMultiTexCoord4f', t.void, (t.GLenum, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glNormal3f', t.void, (t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glOrthof', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glPointParameterf', t.void, (t.GLenum, t.GLfloat))
    set_func('glPointParameterfv', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glPointSize', t.void, (t.GLfloat,))
    set_func('glPolygonOffset', t.void, (t.GLfloat, t.GLfloat))
    set_func('glRotatef', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glScalef', t.void, (t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glTexEnvf', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glTexEnvfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glTexParameterf', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glTexParameterfv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glTranslatef', t.void, (t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glActiveTexture', t.void, (t.GLenum,))
    set_func('glAlphaFuncx', t.void, (t.GLenum, t.GLfixed))
    set_func('glBindBuffer', t.void, (t.GLenum, t.GLuint))
    set_func('glBindTexture', t.void, (t.GLenum, t.GLuint))
    set_func('glBlendFunc', t.void, (t.GLenum, t.GLenum))
    set_func('glBufferData', t.void, (t.GLenum, t.GLsizeiptr, ct.POINTER(t.void), t.GLenum))
    set_func('glBufferSubData', t.void, (t.GLenum, t.GLintptr, t.GLsizeiptr, ct.POINTER(t.void)))
    set_func('glClear', t.void, (t.GLbitfield,))
    set_func('glClearColorx', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glClearDepthx', t.void, (t.GLfixed,))
    set_func('glClearStencil', t.void, (t.GLint,))
    set_func('glClientActiveTexture', t.void, (t.GLenum,))
    set_func('glClipPlanex', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glColor4ub', t.void, (t.GLubyte, t.GLubyte, t.GLubyte, t.GLubyte))
    set_func('glColor4x', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glColorMask', t.void, (t.GLboolean, t.GLboolean, t.GLboolean, t.GLboolean))
    set_func('glColorPointer', t.void, (t.GLint, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glCompressedTexImage2D', t.void, (t.GLenum, t.GLint, t.GLenum, t.GLsizei, t.GLsizei, t.GLint, t.GLsizei, ct.POINTER(t.void)))
    set_func('glCompressedTexSubImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glCopyTexImage2D', t.void, (t.GLenum, t.GLint, t.GLenum, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLint))
    set_func('glCopyTexSubImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei))
    set_func('glCullFace', t.void, (t.GLenum,))
    set_func('glDeleteBuffers', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glDeleteTextures', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glDepthFunc', t.void, (t.GLenum,))
    set_func('glDepthMask', t.void, (t.GLboolean,))
    set_func('glDepthRangex', t.void, (t.GLfixed, t.GLfixed))
    set_func('glDisable', t.void, (t.GLenum,))
    set_func('glDisableClientState', t.void, (t.GLenum,))
    set_func('glDrawArrays', t.void, (t.GLenum, t.GLint, t.GLsizei))
    set_func('glDrawElements', t.void, (t.GLenum, t.GLsizei, t.GLenum, ct.POINTER(t.void)))
    set_func('glEnable', t.void, (t.GLenum,))
    set_func('glEnableClientState', t.void, (t.GLenum,))
    set_func('glFinish', t.void, ())
    set_func('glFlush', t.void, ())
    set_func('glFogx', t.void, (t.GLenum, t.GLfixed))
    set_func('glFogxv', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glFrontFace', t.void, (t.GLenum,))
    set_func('glFrustumx', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glGetBooleanv', t.void, (t.GLenum, ct.POINTER(t.GLboolean)))
    set_func('glGetBufferParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetClipPlanex', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGenBuffers', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenTextures', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGetError', t.GLenum, ())
    set_func('glGetFixedv', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetIntegerv', t.void, (t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetLightxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetMaterialxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetPointerv', t.void, (t.GLenum, ct.POINTER(ct.POINTER(t.void))))
    set_func('glGetString', ct.POINTER(t.GLubyte), (t.GLenum,))
    set_func('glGetTexEnviv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetTexEnvxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetTexParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetTexParameterxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glHint', t.void, (t.GLenum, t.GLenum))
    set_func('glIsBuffer', t.GLboolean, (t.GLuint,))
    set_func('glIsEnabled', t.GLboolean, (t.GLenum,))
    set_func('glIsTexture', t.GLboolean, (t.GLuint,))
    set_func('glLightModelx', t.void, (t.GLenum, t.GLfixed))
    set_func('glLightModelxv', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glLightx', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glLightxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glLineWidthx', t.void, (t.GLfixed,))
    set_func('glLoadIdentity', t.void, ())
    set_func('glLoadMatrixx', t.void, (ct.POINTER(t.GLfixed),))
    set_func('glLogicOp', t.void, (t.GLenum,))
    set_func('glMaterialx', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glMaterialxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glMatrixMode', t.void, (t.GLenum,))
    set_func('glMultMatrixx', t.void, (ct.POINTER(t.GLfixed),))
    set_func('glMultiTexCoord4x', t.void, (t.GLenum, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glNormal3x', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glNormalPointer', t.void, (t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glOrthox', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glPixelStorei', t.void, (t.GLenum, t.GLint))
    set_func('glPointParameterx', t.void, (t.GLenum, t.GLfixed))
    set_func('glPointParameterxv', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glPointSizex', t.void, (t.GLfixed,))
    set_func('glPolygonOffsetx', t.void, (t.GLfixed, t.GLfixed))
    set_func('glPopMatrix', t.void, ())
    set_func('glPushMatrix', t.void, ())
    set_func('glReadPixels', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, ct.POINTER(t.void)))
    set_func('glRotatex', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glSampleCoverage', t.void, (t.GLfloat, t.GLboolean))
    set_func('glSampleCoveragex', t.void, (t.GLclampx, t.GLboolean))
    set_func('glScalex', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glScissor', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei))
    set_func('glShadeModel', t.void, (t.GLenum,))
    set_func('glStencilFunc', t.void, (t.GLenum, t.GLint, t.GLuint))
    set_func('glStencilMask', t.void, (t.GLuint,))
    set_func('glStencilOp', t.void, (t.GLenum, t.GLenum, t.GLenum))
    set_func('glTexCoordPointer', t.void, (t.GLint, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glTexEnvi', t.void, (t.GLenum, t.GLenum, t.GLint))
    set_func('glTexEnvx', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glTexEnviv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glTexEnvxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glTexImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLint, t.GLenum, t.GLenum, ct.POINTER(t.void)))
    set_func('glTexParameteri', t.void, (t.GLenum, t.GLenum, t.GLint))
    set_func('glTexParameterx', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glTexParameteriv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glTexParameterxv', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glTexSubImage2D', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, ct.POINTER(t.void)))
    set_func('glTranslatex', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glVertexPointer', t.void, (t.GLint, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glViewport', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei))
    set_enum("GL_VERSION_ES_CL_1_0", 1)
    set_enum("GL_VERSION_ES_CM_1_1", 1)
    set_enum("GL_VERSION_ES_CL_1_1", 1)
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
    set_enum("GL_NEVER", 0x0200)
    set_enum("GL_LESS", 0x0201)
    set_enum("GL_EQUAL", 0x0202)
    set_enum("GL_LEQUAL", 0x0203)
    set_enum("GL_GREATER", 0x0204)
    set_enum("GL_NOTEQUAL", 0x0205)
    set_enum("GL_GEQUAL", 0x0206)
    set_enum("GL_ALWAYS", 0x0207)
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
    set_enum("GL_CLIP_PLANE0", 0x3000)
    set_enum("GL_CLIP_PLANE1", 0x3001)
    set_enum("GL_CLIP_PLANE2", 0x3002)
    set_enum("GL_CLIP_PLANE3", 0x3003)
    set_enum("GL_CLIP_PLANE4", 0x3004)
    set_enum("GL_CLIP_PLANE5", 0x3005)
    set_enum("GL_FRONT", 0x0404)
    set_enum("GL_BACK", 0x0405)
    set_enum("GL_FRONT_AND_BACK", 0x0408)
    set_enum("GL_FOG", 0x0B60)
    set_enum("GL_LIGHTING", 0x0B50)
    set_enum("GL_TEXTURE_2D", 0x0DE1)
    set_enum("GL_CULL_FACE", 0x0B44)
    set_enum("GL_ALPHA_TEST", 0x0BC0)
    set_enum("GL_BLEND", 0x0BE2)
    set_enum("GL_COLOR_LOGIC_OP", 0x0BF2)
    set_enum("GL_DITHER", 0x0BD0)
    set_enum("GL_STENCIL_TEST", 0x0B90)
    set_enum("GL_DEPTH_TEST", 0x0B71)
    set_enum("GL_POINT_SMOOTH", 0x0B10)
    set_enum("GL_LINE_SMOOTH", 0x0B20)
    set_enum("GL_SCISSOR_TEST", 0x0C11)
    set_enum("GL_COLOR_MATERIAL", 0x0B57)
    set_enum("GL_NORMALIZE", 0x0BA1)
    set_enum("GL_RESCALE_NORMAL", 0x803A)
    set_enum("GL_VERTEX_ARRAY", 0x8074)
    set_enum("GL_NORMAL_ARRAY", 0x8075)
    set_enum("GL_COLOR_ARRAY", 0x8076)
    set_enum("GL_TEXTURE_COORD_ARRAY", 0x8078)
    set_enum("GL_MULTISAMPLE", 0x809D)
    set_enum("GL_SAMPLE_ALPHA_TO_COVERAGE", 0x809E)
    set_enum("GL_SAMPLE_ALPHA_TO_ONE", 0x809F)
    set_enum("GL_SAMPLE_COVERAGE", 0x80A0)
    set_enum("GL_NO_ERROR", 0)
    set_enum("GL_INVALID_ENUM", 0x0500)
    set_enum("GL_INVALID_VALUE", 0x0501)
    set_enum("GL_INVALID_OPERATION", 0x0502)
    set_enum("GL_STACK_OVERFLOW", 0x0503)
    set_enum("GL_STACK_UNDERFLOW", 0x0504)
    set_enum("GL_OUT_OF_MEMORY", 0x0505)
    set_enum("GL_EXP", 0x0800)
    set_enum("GL_EXP2", 0x0801)
    set_enum("GL_FOG_DENSITY", 0x0B62)
    set_enum("GL_FOG_START", 0x0B63)
    set_enum("GL_FOG_END", 0x0B64)
    set_enum("GL_FOG_MODE", 0x0B65)
    set_enum("GL_FOG_COLOR", 0x0B66)
    set_enum("GL_CW", 0x0900)
    set_enum("GL_CCW", 0x0901)
    set_enum("GL_CURRENT_COLOR", 0x0B00)
    set_enum("GL_CURRENT_NORMAL", 0x0B02)
    set_enum("GL_CURRENT_TEXTURE_COORDS", 0x0B03)
    set_enum("GL_POINT_SIZE", 0x0B11)
    set_enum("GL_POINT_SIZE_MIN", 0x8126)
    set_enum("GL_POINT_SIZE_MAX", 0x8127)
    set_enum("GL_POINT_FADE_THRESHOLD_SIZE", 0x8128)
    set_enum("GL_POINT_DISTANCE_ATTENUATION", 0x8129)
    set_enum("GL_SMOOTH_POINT_SIZE_RANGE", 0x0B12)
    set_enum("GL_LINE_WIDTH", 0x0B21)
    set_enum("GL_SMOOTH_LINE_WIDTH_RANGE", 0x0B22)
    set_enum("GL_ALIASED_POINT_SIZE_RANGE", 0x846D)
    set_enum("GL_ALIASED_LINE_WIDTH_RANGE", 0x846E)
    set_enum("GL_CULL_FACE_MODE", 0x0B45)
    set_enum("GL_FRONT_FACE", 0x0B46)
    set_enum("GL_SHADE_MODEL", 0x0B54)
    set_enum("GL_DEPTH_RANGE", 0x0B70)
    set_enum("GL_DEPTH_WRITEMASK", 0x0B72)
    set_enum("GL_DEPTH_CLEAR_VALUE", 0x0B73)
    set_enum("GL_DEPTH_FUNC", 0x0B74)
    set_enum("GL_STENCIL_CLEAR_VALUE", 0x0B91)
    set_enum("GL_STENCIL_FUNC", 0x0B92)
    set_enum("GL_STENCIL_VALUE_MASK", 0x0B93)
    set_enum("GL_STENCIL_FAIL", 0x0B94)
    set_enum("GL_STENCIL_PASS_DEPTH_FAIL", 0x0B95)
    set_enum("GL_STENCIL_PASS_DEPTH_PASS", 0x0B96)
    set_enum("GL_STENCIL_REF", 0x0B97)
    set_enum("GL_STENCIL_WRITEMASK", 0x0B98)
    set_enum("GL_MATRIX_MODE", 0x0BA0)
    set_enum("GL_VIEWPORT", 0x0BA2)
    set_enum("GL_MODELVIEW_STACK_DEPTH", 0x0BA3)
    set_enum("GL_PROJECTION_STACK_DEPTH", 0x0BA4)
    set_enum("GL_TEXTURE_STACK_DEPTH", 0x0BA5)
    set_enum("GL_MODELVIEW_MATRIX", 0x0BA6)
    set_enum("GL_PROJECTION_MATRIX", 0x0BA7)
    set_enum("GL_TEXTURE_MATRIX", 0x0BA8)
    set_enum("GL_ALPHA_TEST_FUNC", 0x0BC1)
    set_enum("GL_ALPHA_TEST_REF", 0x0BC2)
    set_enum("GL_BLEND_DST", 0x0BE0)
    set_enum("GL_BLEND_SRC", 0x0BE1)
    set_enum("GL_LOGIC_OP_MODE", 0x0BF0)
    set_enum("GL_SCISSOR_BOX", 0x0C10)
    set_enum("GL_COLOR_CLEAR_VALUE", 0x0C22)
    set_enum("GL_COLOR_WRITEMASK", 0x0C23)
    set_enum("GL_MAX_LIGHTS", 0x0D31)
    set_enum("GL_MAX_CLIP_PLANES", 0x0D32)
    set_enum("GL_MAX_TEXTURE_SIZE", 0x0D33)
    set_enum("GL_MAX_MODELVIEW_STACK_DEPTH", 0x0D36)
    set_enum("GL_MAX_PROJECTION_STACK_DEPTH", 0x0D38)
    set_enum("GL_MAX_TEXTURE_STACK_DEPTH", 0x0D39)
    set_enum("GL_MAX_VIEWPORT_DIMS", 0x0D3A)
    set_enum("GL_MAX_TEXTURE_UNITS", 0x84E2)
    set_enum("GL_SUBPIXEL_BITS", 0x0D50)
    set_enum("GL_RED_BITS", 0x0D52)
    set_enum("GL_GREEN_BITS", 0x0D53)
    set_enum("GL_BLUE_BITS", 0x0D54)
    set_enum("GL_ALPHA_BITS", 0x0D55)
    set_enum("GL_DEPTH_BITS", 0x0D56)
    set_enum("GL_STENCIL_BITS", 0x0D57)
    set_enum("GL_POLYGON_OFFSET_UNITS", 0x2A00)
    set_enum("GL_POLYGON_OFFSET_FILL", 0x8037)
    set_enum("GL_POLYGON_OFFSET_FACTOR", 0x8038)
    set_enum("GL_TEXTURE_BINDING_2D", 0x8069)
    set_enum("GL_VERTEX_ARRAY_SIZE", 0x807A)
    set_enum("GL_VERTEX_ARRAY_TYPE", 0x807B)
    set_enum("GL_VERTEX_ARRAY_STRIDE", 0x807C)
    set_enum("GL_NORMAL_ARRAY_TYPE", 0x807E)
    set_enum("GL_NORMAL_ARRAY_STRIDE", 0x807F)
    set_enum("GL_COLOR_ARRAY_SIZE", 0x8081)
    set_enum("GL_COLOR_ARRAY_TYPE", 0x8082)
    set_enum("GL_COLOR_ARRAY_STRIDE", 0x8083)
    set_enum("GL_TEXTURE_COORD_ARRAY_SIZE", 0x8088)
    set_enum("GL_TEXTURE_COORD_ARRAY_TYPE", 0x8089)
    set_enum("GL_TEXTURE_COORD_ARRAY_STRIDE", 0x808A)
    set_enum("GL_VERTEX_ARRAY_POINTER", 0x808E)
    set_enum("GL_NORMAL_ARRAY_POINTER", 0x808F)
    set_enum("GL_COLOR_ARRAY_POINTER", 0x8090)
    set_enum("GL_TEXTURE_COORD_ARRAY_POINTER", 0x8092)
    set_enum("GL_SAMPLE_BUFFERS", 0x80A8)
    set_enum("GL_SAMPLES", 0x80A9)
    set_enum("GL_SAMPLE_COVERAGE_VALUE", 0x80AA)
    set_enum("GL_SAMPLE_COVERAGE_INVERT", 0x80AB)
    set_enum("GL_NUM_COMPRESSED_TEXTURE_FORMATS", 0x86A2)
    set_enum("GL_COMPRESSED_TEXTURE_FORMATS", 0x86A3)
    set_enum("GL_DONT_CARE", 0x1100)
    set_enum("GL_FASTEST", 0x1101)
    set_enum("GL_NICEST", 0x1102)
    set_enum("GL_PERSPECTIVE_CORRECTION_HINT", 0x0C50)
    set_enum("GL_POINT_SMOOTH_HINT", 0x0C51)
    set_enum("GL_LINE_SMOOTH_HINT", 0x0C52)
    set_enum("GL_FOG_HINT", 0x0C54)
    set_enum("GL_GENERATE_MIPMAP_HINT", 0x8192)
    set_enum("GL_LIGHT_MODEL_AMBIENT", 0x0B53)
    set_enum("GL_LIGHT_MODEL_TWO_SIDE", 0x0B52)
    set_enum("GL_AMBIENT", 0x1200)
    set_enum("GL_DIFFUSE", 0x1201)
    set_enum("GL_SPECULAR", 0x1202)
    set_enum("GL_POSITION", 0x1203)
    set_enum("GL_SPOT_DIRECTION", 0x1204)
    set_enum("GL_SPOT_EXPONENT", 0x1205)
    set_enum("GL_SPOT_CUTOFF", 0x1206)
    set_enum("GL_CONSTANT_ATTENUATION", 0x1207)
    set_enum("GL_LINEAR_ATTENUATION", 0x1208)
    set_enum("GL_QUADRATIC_ATTENUATION", 0x1209)
    set_enum("GL_BYTE", 0x1400)
    set_enum("GL_UNSIGNED_BYTE", 0x1401)
    set_enum("GL_SHORT", 0x1402)
    set_enum("GL_UNSIGNED_SHORT", 0x1403)
    set_enum("GL_FLOAT", 0x1406)
    set_enum("GL_FIXED", 0x140C)
    set_enum("GL_CLEAR", 0x1500)
    set_enum("GL_AND", 0x1501)
    set_enum("GL_AND_REVERSE", 0x1502)
    set_enum("GL_COPY", 0x1503)
    set_enum("GL_AND_INVERTED", 0x1504)
    set_enum("GL_NOOP", 0x1505)
    set_enum("GL_XOR", 0x1506)
    set_enum("GL_OR", 0x1507)
    set_enum("GL_NOR", 0x1508)
    set_enum("GL_EQUIV", 0x1509)
    set_enum("GL_INVERT", 0x150A)
    set_enum("GL_OR_REVERSE", 0x150B)
    set_enum("GL_COPY_INVERTED", 0x150C)
    set_enum("GL_OR_INVERTED", 0x150D)
    set_enum("GL_NAND", 0x150E)
    set_enum("GL_SET", 0x150F)
    set_enum("GL_EMISSION", 0x1600)
    set_enum("GL_SHININESS", 0x1601)
    set_enum("GL_AMBIENT_AND_DIFFUSE", 0x1602)
    set_enum("GL_MODELVIEW", 0x1700)
    set_enum("GL_PROJECTION", 0x1701)
    set_enum("GL_TEXTURE", 0x1702)
    set_enum("GL_ALPHA", 0x1906)
    set_enum("GL_RGB", 0x1907)
    set_enum("GL_RGBA", 0x1908)
    set_enum("GL_LUMINANCE", 0x1909)
    set_enum("GL_LUMINANCE_ALPHA", 0x190A)
    set_enum("GL_UNPACK_ALIGNMENT", 0x0CF5)
    set_enum("GL_PACK_ALIGNMENT", 0x0D05)
    set_enum("GL_UNSIGNED_SHORT_4_4_4_4", 0x8033)
    set_enum("GL_UNSIGNED_SHORT_5_5_5_1", 0x8034)
    set_enum("GL_UNSIGNED_SHORT_5_6_5", 0x8363)
    set_enum("GL_FLAT", 0x1D00)
    set_enum("GL_SMOOTH", 0x1D01)
    set_enum("GL_KEEP", 0x1E00)
    set_enum("GL_REPLACE", 0x1E01)
    set_enum("GL_INCR", 0x1E02)
    set_enum("GL_DECR", 0x1E03)
    set_enum("GL_VENDOR", 0x1F00)
    set_enum("GL_RENDERER", 0x1F01)
    set_enum("GL_VERSION", 0x1F02)
    set_enum("GL_EXTENSIONS", 0x1F03)
    set_enum("GL_MODULATE", 0x2100)
    set_enum("GL_DECAL", 0x2101)
    set_enum("GL_ADD", 0x0104)
    set_enum("GL_TEXTURE_ENV_MODE", 0x2200)
    set_enum("GL_TEXTURE_ENV_COLOR", 0x2201)
    set_enum("GL_TEXTURE_ENV", 0x2300)
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
    set_enum("GL_GENERATE_MIPMAP", 0x8191)
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
    set_enum("GL_CLIENT_ACTIVE_TEXTURE", 0x84E1)
    set_enum("GL_REPEAT", 0x2901)
    set_enum("GL_CLAMP_TO_EDGE", 0x812F)
    set_enum("GL_LIGHT0", 0x4000)
    set_enum("GL_LIGHT1", 0x4001)
    set_enum("GL_LIGHT2", 0x4002)
    set_enum("GL_LIGHT3", 0x4003)
    set_enum("GL_LIGHT4", 0x4004)
    set_enum("GL_LIGHT5", 0x4005)
    set_enum("GL_LIGHT6", 0x4006)
    set_enum("GL_LIGHT7", 0x4007)
    set_enum("GL_ARRAY_BUFFER", 0x8892)
    set_enum("GL_ELEMENT_ARRAY_BUFFER", 0x8893)
    set_enum("GL_ARRAY_BUFFER_BINDING", 0x8894)
    set_enum("GL_ELEMENT_ARRAY_BUFFER_BINDING", 0x8895)
    set_enum("GL_VERTEX_ARRAY_BUFFER_BINDING", 0x8896)
    set_enum("GL_NORMAL_ARRAY_BUFFER_BINDING", 0x8897)
    set_enum("GL_COLOR_ARRAY_BUFFER_BINDING", 0x8898)
    set_enum("GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING", 0x889A)
    set_enum("GL_STATIC_DRAW", 0x88E4)
    set_enum("GL_DYNAMIC_DRAW", 0x88E8)
    set_enum("GL_BUFFER_SIZE", 0x8764)
    set_enum("GL_BUFFER_USAGE", 0x8765)
    set_enum("GL_SUBTRACT", 0x84E7)
    set_enum("GL_COMBINE", 0x8570)
    set_enum("GL_COMBINE_RGB", 0x8571)
    set_enum("GL_COMBINE_ALPHA", 0x8572)
    set_enum("GL_RGB_SCALE", 0x8573)
    set_enum("GL_ADD_SIGNED", 0x8574)
    set_enum("GL_INTERPOLATE", 0x8575)
    set_enum("GL_CONSTANT", 0x8576)
    set_enum("GL_PRIMARY_COLOR", 0x8577)
    set_enum("GL_PREVIOUS", 0x8578)
    set_enum("GL_OPERAND0_RGB", 0x8590)
    set_enum("GL_OPERAND1_RGB", 0x8591)
    set_enum("GL_OPERAND2_RGB", 0x8592)
    set_enum("GL_OPERAND0_ALPHA", 0x8598)
    set_enum("GL_OPERAND1_ALPHA", 0x8599)
    set_enum("GL_OPERAND2_ALPHA", 0x859A)
    set_enum("GL_ALPHA_SCALE", 0x0D1C)
    set_enum("GL_SRC0_RGB", 0x8580)
    set_enum("GL_SRC1_RGB", 0x8581)
    set_enum("GL_SRC2_RGB", 0x8582)
    set_enum("GL_SRC0_ALPHA", 0x8588)
    set_enum("GL_SRC1_ALPHA", 0x8589)
    set_enum("GL_SRC2_ALPHA", 0x858A)
    set_enum("GL_DOT3_RGB", 0x86AE)
    set_enum("GL_DOT3_RGBA", 0x86AF)


#### GL_AMD_COMPRESSED_3DC_TEXTURE ####
def init_gl_amd_compressed_3dc_texture():
    set_enum("GL_3DC_X_AMD", 0x87F9)
    set_enum("GL_3DC_XY_AMD", 0x87FA)


#### GL_AMD_COMPRESSED_ATC_TEXTURE ####
def init_gl_amd_compressed_atc_texture():
    set_enum("GL_ATC_RGB_AMD", 0x8C92)
    set_enum("GL_ATC_RGBA_EXPLICIT_ALPHA_AMD", 0x8C93)
    set_enum("GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD", 0x87EE)


#### GL_APPLE_COPY_TEXTURE_LEVELS ####
def init_gl_apple_copy_texture_levels():
    set_func('glCopyTextureLevelsAPPLE', t.void, (t.GLuint, t.GLuint, t.GLint, t.GLsizei))


#### GL_APPLE_FRAMEBUFFER_MULTISAMPLE ####
def init_gl_apple_framebuffer_multisample():
    set_func('glRenderbufferStorageMultisampleAPPLE', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glResolveMultisampleFramebufferAPPLE', t.void, ())
    set_enum("GL_RENDERBUFFER_SAMPLES_APPLE", 0x8CAB)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_APPLE", 0x8D56)
    set_enum("GL_MAX_SAMPLES_APPLE", 0x8D57)
    set_enum("GL_READ_FRAMEBUFFER_APPLE", 0x8CA8)
    set_enum("GL_DRAW_FRAMEBUFFER_APPLE", 0x8CA9)
    set_enum("GL_DRAW_FRAMEBUFFER_BINDING_APPLE", 0x8CA6)
    set_enum("GL_READ_FRAMEBUFFER_BINDING_APPLE", 0x8CAA)


#### GL_APPLE_SYNC ####
def init_gl_apple_sync():
    set_func('glFenceSyncAPPLE', t.GLsync, (t.GLenum, t.GLbitfield))
    set_func('glIsSyncAPPLE', t.GLboolean, (t.GLsync,))
    set_func('glDeleteSyncAPPLE', t.void, (t.GLsync,))
    set_func('glClientWaitSyncAPPLE', t.GLenum, (t.GLsync, t.GLbitfield, t.GLuint64))
    set_func('glWaitSyncAPPLE', t.void, (t.GLsync, t.GLbitfield, t.GLuint64))
    set_func('glGetInteger64vAPPLE', t.void, (t.GLenum, ct.POINTER(t.GLint64)))
    set_func('glGetSyncivAPPLE', t.void, (t.GLsync, t.GLenum, t.GLsizei, ct.POINTER(t.GLsizei), ct.POINTER(t.GLint)))
    set_enum("GL_SYNC_OBJECT_APPLE", 0x8A53)
    set_enum("GL_MAX_SERVER_WAIT_TIMEOUT_APPLE", 0x9111)
    set_enum("GL_OBJECT_TYPE_APPLE", 0x9112)
    set_enum("GL_SYNC_CONDITION_APPLE", 0x9113)
    set_enum("GL_SYNC_STATUS_APPLE", 0x9114)
    set_enum("GL_SYNC_FLAGS_APPLE", 0x9115)
    set_enum("GL_SYNC_FENCE_APPLE", 0x9116)
    set_enum("GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE", 0x9117)
    set_enum("GL_UNSIGNALED_APPLE", 0x9118)
    set_enum("GL_SIGNALED_APPLE", 0x9119)
    set_enum("GL_ALREADY_SIGNALED_APPLE", 0x911A)
    set_enum("GL_TIMEOUT_EXPIRED_APPLE", 0x911B)
    set_enum("GL_CONDITION_SATISFIED_APPLE", 0x911C)
    set_enum("GL_WAIT_FAILED_APPLE", 0x911D)
    set_enum("GL_SYNC_FLUSH_COMMANDS_BIT_APPLE", 0x00000001)
    set_enum("GL_TIMEOUT_IGNORED_APPLE", 0xFFFFFFFFFFFFFFFF)


#### GL_APPLE_TEXTURE_FORMAT_BGRA8888 ####
def init_gl_apple_texture_format_bgra8888():
    set_enum("GL_BGRA_EXT", 0x80E1)
    set_enum("GL_BGRA8_EXT", 0x93A1)


#### GL_APPLE_TEXTURE_MAX_LEVEL ####
def init_gl_apple_texture_max_level():
    set_enum("GL_TEXTURE_MAX_LEVEL_APPLE", 0x813D)


#### GL_EXT_BLEND_MINMAX ####
def init_gl_ext_blend_minmax():
    set_enum("GL_MIN_EXT", 0x8007)
    set_enum("GL_MAX_EXT", 0x8008)


#### GL_EXT_DISCARD_FRAMEBUFFER ####
def init_gl_ext_discard_framebuffer():
    set_func('glDiscardFramebufferEXT', t.void, (t.GLenum, t.GLsizei, ct.POINTER(t.GLenum)))
    set_enum("GL_COLOR_EXT", 0x1800)
    set_enum("GL_DEPTH_EXT", 0x1801)
    set_enum("GL_STENCIL_EXT", 0x1802)


#### GL_EXT_MAP_BUFFER_RANGE ####
def init_gl_ext_map_buffer_range():
    set_func('glMapBufferRangeEXT', ct.POINTER(t.void), (t.GLenum, t.GLintptr, t.GLsizeiptr, t.GLbitfield))
    set_func('glFlushMappedBufferRangeEXT', t.void, (t.GLenum, t.GLintptr, t.GLsizeiptr))
    set_enum("GL_MAP_READ_BIT_EXT", 0x0001)
    set_enum("GL_MAP_WRITE_BIT_EXT", 0x0002)
    set_enum("GL_MAP_INVALIDATE_RANGE_BIT_EXT", 0x0004)
    set_enum("GL_MAP_INVALIDATE_BUFFER_BIT_EXT", 0x0008)
    set_enum("GL_MAP_FLUSH_EXPLICIT_BIT_EXT", 0x0010)
    set_enum("GL_MAP_UNSYNCHRONIZED_BIT_EXT", 0x0020)


#### GL_EXT_MULTI_DRAW_ARRAYS ####
def init_gl_ext_multi_draw_arrays():
    set_func('glMultiDrawArraysEXT', t.void, (t.GLenum, ct.POINTER(t.GLint), ct.POINTER(t.GLsizei), t.GLsizei))
    set_func('glMultiDrawElementsEXT', t.void, (t.GLenum, ct.POINTER(t.GLsizei), t.GLenum, ct.POINTER(ct.POINTER(t.void)), t.GLsizei))


#### GL_EXT_MULTISAMPLED_RENDER_TO_TEXTURE ####
def init_gl_ext_multisampled_render_to_texture():
    set_func('glRenderbufferStorageMultisampleEXT', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glFramebufferTexture2DMultisampleEXT', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint, t.GLint, t.GLsizei))
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT", 0x8D6C)
    set_enum("GL_RENDERBUFFER_SAMPLES_EXT", 0x8CAB)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT", 0x8D56)
    set_enum("GL_MAX_SAMPLES_EXT", 0x8D57)


#### GL_EXT_READ_FORMAT_BGRA ####
def init_gl_ext_read_format_bgra():
    set_enum("GL_BGRA_EXT", 0x80E1)
    set_enum("GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT", 0x8365)
    set_enum("GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT", 0x8366)


#### GL_EXT_ROBUSTNESS ####
def init_gl_ext_robustness():
    set_func('glGetGraphicsResetStatusEXT', t.GLenum, ())
    set_func('glReadnPixelsEXT', t.void, (t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glGetnUniformfvEXT', t.void, (t.GLuint, t.GLint, t.GLsizei, ct.POINTER(t.GLfloat)))
    set_func('glGetnUniformivEXT', t.void, (t.GLuint, t.GLint, t.GLsizei, ct.POINTER(t.GLint)))
    set_enum("GL_NO_ERROR", 0)
    set_enum("GL_GUILTY_CONTEXT_RESET_EXT", 0x8253)
    set_enum("GL_INNOCENT_CONTEXT_RESET_EXT", 0x8254)
    set_enum("GL_UNKNOWN_CONTEXT_RESET_EXT", 0x8255)
    set_enum("GL_CONTEXT_ROBUST_ACCESS_EXT", 0x90F3)
    set_enum("GL_RESET_NOTIFICATION_STRATEGY_EXT", 0x8256)
    set_enum("GL_LOSE_CONTEXT_ON_RESET_EXT", 0x8252)
    set_enum("GL_NO_RESET_NOTIFICATION_EXT", 0x8261)


#### GL_EXT_SRGB ####
def init_gl_ext_srgb():
    set_enum("GL_SRGB_EXT", 0x8C40)
    set_enum("GL_SRGB_ALPHA_EXT", 0x8C42)
    set_enum("GL_SRGB8_ALPHA8_EXT", 0x8C43)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT", 0x8210)


#### GL_EXT_TEXTURE_COMPRESSION_DXT1 ####
def init_gl_ext_texture_compression_dxt1():
    set_enum("GL_COMPRESSED_RGB_S3TC_DXT1_EXT", 0x83F0)
    set_enum("GL_COMPRESSED_RGBA_S3TC_DXT1_EXT", 0x83F1)


#### GL_EXT_TEXTURE_FILTER_ANISOTROPIC ####
def init_gl_ext_texture_filter_anisotropic():
    set_enum("GL_TEXTURE_MAX_ANISOTROPY_EXT", 0x84FE)
    set_enum("GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT", 0x84FF)


#### GL_EXT_TEXTURE_FORMAT_BGRA8888 ####
def init_gl_ext_texture_format_bgra8888():
    set_enum("GL_BGRA_EXT", 0x80E1)


#### GL_EXT_TEXTURE_LOD_BIAS ####
def init_gl_ext_texture_lod_bias():
    set_enum("GL_MAX_TEXTURE_LOD_BIAS_EXT", 0x84FD)
    set_enum("GL_TEXTURE_FILTER_CONTROL_EXT", 0x8500)
    set_enum("GL_TEXTURE_LOD_BIAS_EXT", 0x8501)


#### GL_EXT_TEXTURE_STORAGE ####
def init_gl_ext_texture_storage():
    set_func('glTexStorage1DEXT', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei))
    set_func('glTexStorage2DEXT', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glTexStorage3DEXT', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei, t.GLsizei))
    set_func('glTextureStorage1DEXT', t.void, (t.GLuint, t.GLenum, t.GLsizei, t.GLenum, t.GLsizei))
    set_func('glTextureStorage2DEXT', t.void, (t.GLuint, t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glTextureStorage3DEXT', t.void, (t.GLuint, t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei, t.GLsizei))
    set_enum("GL_TEXTURE_IMMUTABLE_FORMAT_EXT", 0x912F)
    set_enum("GL_ALPHA8_EXT", 0x803C)
    set_enum("GL_LUMINANCE8_EXT", 0x8040)
    set_enum("GL_LUMINANCE8_ALPHA8_EXT", 0x8045)
    set_enum("GL_RGBA32F_EXT", 0x8814)
    set_enum("GL_RGB32F_EXT", 0x8815)
    set_enum("GL_ALPHA32F_EXT", 0x8816)
    set_enum("GL_LUMINANCE32F_EXT", 0x8818)
    set_enum("GL_LUMINANCE_ALPHA32F_EXT", 0x8819)
    set_enum("GL_RGBA16F_EXT", 0x881A)
    set_enum("GL_RGB16F_EXT", 0x881B)
    set_enum("GL_ALPHA16F_EXT", 0x881C)
    set_enum("GL_LUMINANCE16F_EXT", 0x881E)
    set_enum("GL_LUMINANCE_ALPHA16F_EXT", 0x881F)
    set_enum("GL_RGB10_A2_EXT", 0x8059)
    set_enum("GL_RGB10_EXT", 0x8052)
    set_enum("GL_BGRA8_EXT", 0x93A1)
    set_enum("GL_R8_EXT", 0x8229)
    set_enum("GL_RG8_EXT", 0x822B)
    set_enum("GL_R32F_EXT", 0x822E)
    set_enum("GL_RG32F_EXT", 0x8230)
    set_enum("GL_R16F_EXT", 0x822D)
    set_enum("GL_RG16F_EXT", 0x822F)


#### GL_IMG_MULTISAMPLED_RENDER_TO_TEXTURE ####
def init_gl_img_multisampled_render_to_texture():
    set_func('glRenderbufferStorageMultisampleIMG', t.void, (t.GLenum, t.GLsizei, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glFramebufferTexture2DMultisampleIMG', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint, t.GLint, t.GLsizei))
    set_enum("GL_RENDERBUFFER_SAMPLES_IMG", 0x9133)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG", 0x9134)
    set_enum("GL_MAX_SAMPLES_IMG", 0x9135)
    set_enum("GL_TEXTURE_SAMPLES_IMG", 0x9136)


#### GL_IMG_READ_FORMAT ####
def init_gl_img_read_format():
    set_enum("GL_BGRA_IMG", 0x80E1)
    set_enum("GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG", 0x8365)


#### GL_IMG_TEXTURE_COMPRESSION_PVRTC ####
def init_gl_img_texture_compression_pvrtc():
    set_enum("GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG", 0x8C00)
    set_enum("GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG", 0x8C01)
    set_enum("GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG", 0x8C02)
    set_enum("GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG", 0x8C03)


#### GL_IMG_TEXTURE_ENV_ENHANCED_FIXED_FUNCTION ####
def init_gl_img_texture_env_enhanced_fixed_function():
    set_enum("GL_MODULATE_COLOR_IMG", 0x8C04)
    set_enum("GL_RECIP_ADD_SIGNED_ALPHA_IMG", 0x8C05)
    set_enum("GL_TEXTURE_ALPHA_MODULATE_IMG", 0x8C06)
    set_enum("GL_FACTOR_ALPHA_MODULATE_IMG", 0x8C07)
    set_enum("GL_FRAGMENT_ALPHA_MODULATE_IMG", 0x8C08)
    set_enum("GL_ADD_BLEND_IMG", 0x8C09)
    set_enum("GL_DOT3_RGBA_IMG", 0x86AF)


#### GL_IMG_USER_CLIP_PLANE ####
def init_gl_img_user_clip_plane():
    set_func('glClipPlanefIMG', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glClipPlanexIMG', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_enum("GL_CLIP_PLANE0_IMG", 0x3000)
    set_enum("GL_CLIP_PLANE1_IMG", 0x3001)
    set_enum("GL_CLIP_PLANE2_IMG", 0x3002)
    set_enum("GL_CLIP_PLANE3_IMG", 0x3003)
    set_enum("GL_CLIP_PLANE4_IMG", 0x3004)
    set_enum("GL_CLIP_PLANE5_IMG", 0x3005)
    set_enum("GL_MAX_CLIP_PLANES_IMG", 0x0D32)


#### GL_NV_FENCE ####
def init_gl_nv_fence():
    set_func('glDeleteFencesNV', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenFencesNV', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glIsFenceNV', t.GLboolean, (t.GLuint,))
    set_func('glTestFenceNV', t.GLboolean, (t.GLuint,))
    set_func('glGetFenceivNV', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glFinishFenceNV', t.void, (t.GLuint,))
    set_func('glSetFenceNV', t.void, (t.GLuint, t.GLenum))
    set_enum("GL_ALL_COMPLETED_NV", 0x84F2)
    set_enum("GL_FENCE_STATUS_NV", 0x84F3)
    set_enum("GL_FENCE_CONDITION_NV", 0x84F4)


#### GL_OES_EGL_IMAGE ####
def init_gl_oes_egl_image():
    set_func('glEGLImageTargetTexture2DOES', t.void, (t.GLenum, t.GLeglImageOES))
    set_func('glEGLImageTargetRenderbufferStorageOES', t.void, (t.GLenum, t.GLeglImageOES))


#### GL_OES_EGL_IMAGE_EXTERNAL ####
def init_gl_oes_egl_image_external():
    set_enum("GL_TEXTURE_EXTERNAL_OES", 0x8D65)
    set_enum("GL_TEXTURE_BINDING_EXTERNAL_OES", 0x8D67)
    set_enum("GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES", 0x8D68)


#### GL_OES_BLEND_EQUATION_SEPARATE ####
def init_gl_oes_blend_equation_separate():
    set_func('glBlendEquationSeparateOES', t.void, (t.GLenum, t.GLenum))
    set_enum("GL_BLEND_EQUATION_RGB_OES", 0x8009)
    set_enum("GL_BLEND_EQUATION_ALPHA_OES", 0x883D)


#### GL_OES_BLEND_FUNC_SEPARATE ####
def init_gl_oes_blend_func_separate():
    set_func('glBlendFuncSeparateOES', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLenum))
    set_enum("GL_BLEND_DST_RGB_OES", 0x80C8)
    set_enum("GL_BLEND_SRC_RGB_OES", 0x80C9)
    set_enum("GL_BLEND_DST_ALPHA_OES", 0x80CA)
    set_enum("GL_BLEND_SRC_ALPHA_OES", 0x80CB)


#### GL_OES_BLEND_SUBTRACT ####
def init_gl_oes_blend_subtract():
    set_func('glBlendEquationOES', t.void, (t.GLenum,))
    set_enum("GL_BLEND_EQUATION_OES", 0x8009)
    set_enum("GL_FUNC_ADD_OES", 0x8006)
    set_enum("GL_FUNC_SUBTRACT_OES", 0x800A)
    set_enum("GL_FUNC_REVERSE_SUBTRACT_OES", 0x800B)


#### GL_OES_BYTE_COORDINATES ####
def init_gl_oes_byte_coordinates():
    set_enum("GL_BYTE", 0x1400)


#### GL_OES_COMPRESSED_ETC1_RGB8_TEXTURE ####
def init_gl_oes_compressed_etc1_rgb8_texture():
    set_enum("GL_ETC1_RGB8_OES", 0x8D64)


#### GL_OES_COMPRESSED_PALETTED_TEXTURE ####
def init_gl_oes_compressed_paletted_texture():
    set_enum("GL_PALETTE4_RGB8_OES", 0x8B90)
    set_enum("GL_PALETTE4_RGBA8_OES", 0x8B91)
    set_enum("GL_PALETTE4_R5_G6_B5_OES", 0x8B92)
    set_enum("GL_PALETTE4_RGBA4_OES", 0x8B93)
    set_enum("GL_PALETTE4_RGB5_A1_OES", 0x8B94)
    set_enum("GL_PALETTE8_RGB8_OES", 0x8B95)
    set_enum("GL_PALETTE8_RGBA8_OES", 0x8B96)
    set_enum("GL_PALETTE8_R5_G6_B5_OES", 0x8B97)
    set_enum("GL_PALETTE8_RGBA4_OES", 0x8B98)
    set_enum("GL_PALETTE8_RGB5_A1_OES", 0x8B99)


#### GL_OES_DEPTH24 ####
def init_gl_oes_depth24():
    set_enum("GL_DEPTH_COMPONENT24_OES", 0x81A6)


#### GL_OES_DEPTH32 ####
def init_gl_oes_depth32():
    set_enum("GL_DEPTH_COMPONENT32_OES", 0x81A7)


#### GL_OES_DRAW_TEXTURE ####
def init_gl_oes_draw_texture():
    set_func('glDrawTexsOES', t.void, (t.GLshort, t.GLshort, t.GLshort, t.GLshort, t.GLshort))
    set_func('glDrawTexiOES', t.void, (t.GLint, t.GLint, t.GLint, t.GLint, t.GLint))
    set_func('glDrawTexxOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glDrawTexsvOES', t.void, (ct.POINTER(t.GLshort),))
    set_func('glDrawTexivOES', t.void, (ct.POINTER(t.GLint),))
    set_func('glDrawTexxvOES', t.void, (ct.POINTER(t.GLfixed),))
    set_func('glDrawTexfOES', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glDrawTexfvOES', t.void, (ct.POINTER(t.GLfloat),))
    set_enum("GL_TEXTURE_CROP_RECT_OES", 0x8B9D)


#### GL_OES_ELEMENT_INDEX_UINT ####
def init_gl_oes_element_index_uint():
    set_enum("GL_UNSIGNED_INT", 0x1405)


#### GL_OES_FIXED_POINT ####
def init_gl_oes_fixed_point():
    set_func('glAlphaFuncxOES', t.void, (t.GLenum, t.GLfixed))
    set_func('glClearColorxOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glClearDepthxOES', t.void, (t.GLfixed,))
    set_func('glClipPlanexOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glColor4xOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glDepthRangexOES', t.void, (t.GLfixed, t.GLfixed))
    set_func('glFogxOES', t.void, (t.GLenum, t.GLfixed))
    set_func('glFogxvOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glFrustumxOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glGetClipPlanexOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetFixedvOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetTexEnvxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetTexParameterxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glLightModelxOES', t.void, (t.GLenum, t.GLfixed))
    set_func('glLightModelxvOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glLightxOES', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glLightxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glLineWidthxOES', t.void, (t.GLfixed,))
    set_func('glLoadMatrixxOES', t.void, (ct.POINTER(t.GLfixed),))
    set_func('glMaterialxOES', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glMaterialxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glMultMatrixxOES', t.void, (ct.POINTER(t.GLfixed),))
    set_func('glMultiTexCoord4xOES', t.void, (t.GLenum, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glNormal3xOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glOrthoxOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glPointParameterxvOES', t.void, (t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glPointSizexOES', t.void, (t.GLfixed,))
    set_func('glPolygonOffsetxOES', t.void, (t.GLfixed, t.GLfixed))
    set_func('glRotatexOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glScalexOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glTexEnvxOES', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glTexEnvxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glTexParameterxOES', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glTexParameterxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glTranslatexOES', t.void, (t.GLfixed, t.GLfixed, t.GLfixed))
    set_func('glGetLightxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetMaterialxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glPointParameterxOES', t.void, (t.GLenum, t.GLfixed))
    set_func('glSampleCoveragexOES', t.void, (t.GLclampx, t.GLboolean))
    set_enum("GL_FIXED_OES", 0x140C)


#### GL_OES_FRAMEBUFFER_OBJECT ####
def init_gl_oes_framebuffer_object():
    set_func('glIsRenderbufferOES', t.GLboolean, (t.GLuint,))
    set_func('glBindRenderbufferOES', t.void, (t.GLenum, t.GLuint))
    set_func('glDeleteRenderbuffersOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenRenderbuffersOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glRenderbufferStorageOES', t.void, (t.GLenum, t.GLenum, t.GLsizei, t.GLsizei))
    set_func('glGetRenderbufferParameterivOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glIsFramebufferOES', t.GLboolean, (t.GLuint,))
    set_func('glBindFramebufferOES', t.void, (t.GLenum, t.GLuint))
    set_func('glDeleteFramebuffersOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenFramebuffersOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glCheckFramebufferStatusOES', t.GLenum, (t.GLenum,))
    set_func('glFramebufferRenderbufferOES', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint))
    set_func('glFramebufferTexture2DOES', t.void, (t.GLenum, t.GLenum, t.GLenum, t.GLuint, t.GLint))
    set_func('glGetFramebufferAttachmentParameterivOES', t.void, (t.GLenum, t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGenerateMipmapOES', t.void, (t.GLenum,))
    set_enum("GL_NONE_OES", 0)
    set_enum("GL_FRAMEBUFFER_OES", 0x8D40)
    set_enum("GL_RENDERBUFFER_OES", 0x8D41)
    set_enum("GL_RGBA4_OES", 0x8056)
    set_enum("GL_RGB5_A1_OES", 0x8057)
    set_enum("GL_RGB565_OES", 0x8D62)
    set_enum("GL_DEPTH_COMPONENT16_OES", 0x81A5)
    set_enum("GL_RENDERBUFFER_WIDTH_OES", 0x8D42)
    set_enum("GL_RENDERBUFFER_HEIGHT_OES", 0x8D43)
    set_enum("GL_RENDERBUFFER_INTERNAL_FORMAT_OES", 0x8D44)
    set_enum("GL_RENDERBUFFER_RED_SIZE_OES", 0x8D50)
    set_enum("GL_RENDERBUFFER_GREEN_SIZE_OES", 0x8D51)
    set_enum("GL_RENDERBUFFER_BLUE_SIZE_OES", 0x8D52)
    set_enum("GL_RENDERBUFFER_ALPHA_SIZE_OES", 0x8D53)
    set_enum("GL_RENDERBUFFER_DEPTH_SIZE_OES", 0x8D54)
    set_enum("GL_RENDERBUFFER_STENCIL_SIZE_OES", 0x8D55)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES", 0x8CD0)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES", 0x8CD1)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES", 0x8CD2)
    set_enum("GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES", 0x8CD3)
    set_enum("GL_COLOR_ATTACHMENT0_OES", 0x8CE0)
    set_enum("GL_DEPTH_ATTACHMENT_OES", 0x8D00)
    set_enum("GL_STENCIL_ATTACHMENT_OES", 0x8D20)
    set_enum("GL_FRAMEBUFFER_COMPLETE_OES", 0x8CD5)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES", 0x8CD6)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES", 0x8CD7)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES", 0x8CD9)
    set_enum("GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES", 0x8CDA)
    set_enum("GL_FRAMEBUFFER_UNSUPPORTED_OES", 0x8CDD)
    set_enum("GL_FRAMEBUFFER_BINDING_OES", 0x8CA6)
    set_enum("GL_RENDERBUFFER_BINDING_OES", 0x8CA7)
    set_enum("GL_MAX_RENDERBUFFER_SIZE_OES", 0x84E8)
    set_enum("GL_INVALID_FRAMEBUFFER_OPERATION_OES", 0x0506)


#### GL_OES_MAPBUFFER ####
def init_gl_oes_mapbuffer():
    set_func('glMapBufferOES', ct.POINTER(t.void), (t.GLenum, t.GLenum))
    set_func('glUnmapBufferOES', t.GLboolean, (t.GLenum,))
    set_func('glGetBufferPointervOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(ct.POINTER(t.void))))
    set_enum("GL_WRITE_ONLY_OES", 0x88B9)
    set_enum("GL_BUFFER_ACCESS_OES", 0x88BB)
    set_enum("GL_BUFFER_MAPPED_OES", 0x88BC)
    set_enum("GL_BUFFER_MAP_POINTER_OES", 0x88BD)


#### GL_OES_MATRIX_GET ####
def init_gl_oes_matrix_get():
    set_enum("GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES", 0x898D)
    set_enum("GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES", 0x898E)
    set_enum("GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES", 0x898F)


#### GL_OES_MATRIX_PALETTE ####
def init_gl_oes_matrix_palette():
    set_func('glCurrentPaletteMatrixOES', t.void, (t.GLuint,))
    set_func('glLoadPaletteFromModelViewMatrixOES', t.void, ())
    set_func('glMatrixIndexPointerOES', t.void, (t.GLint, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_func('glWeightPointerOES', t.void, (t.GLint, t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_enum("GL_MAX_VERTEX_UNITS_OES", 0x86A4)
    set_enum("GL_MAX_PALETTE_MATRICES_OES", 0x8842)
    set_enum("GL_MATRIX_PALETTE_OES", 0x8840)
    set_enum("GL_MATRIX_INDEX_ARRAY_OES", 0x8844)
    set_enum("GL_WEIGHT_ARRAY_OES", 0x86AD)
    set_enum("GL_CURRENT_PALETTE_MATRIX_OES", 0x8843)
    set_enum("GL_MATRIX_INDEX_ARRAY_SIZE_OES", 0x8846)
    set_enum("GL_MATRIX_INDEX_ARRAY_TYPE_OES", 0x8847)
    set_enum("GL_MATRIX_INDEX_ARRAY_STRIDE_OES", 0x8848)
    set_enum("GL_MATRIX_INDEX_ARRAY_POINTER_OES", 0x8849)
    set_enum("GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES", 0x8B9E)
    set_enum("GL_WEIGHT_ARRAY_SIZE_OES", 0x86AB)
    set_enum("GL_WEIGHT_ARRAY_TYPE_OES", 0x86A9)
    set_enum("GL_WEIGHT_ARRAY_STRIDE_OES", 0x86AA)
    set_enum("GL_WEIGHT_ARRAY_POINTER_OES", 0x86AC)
    set_enum("GL_WEIGHT_ARRAY_BUFFER_BINDING_OES", 0x889E)


#### GL_OES_PACKED_DEPTH_STENCIL ####
def init_gl_oes_packed_depth_stencil():
    set_enum("GL_DEPTH_STENCIL_OES", 0x84F9)
    set_enum("GL_UNSIGNED_INT_24_8_OES", 0x84FA)
    set_enum("GL_DEPTH24_STENCIL8_OES", 0x88F0)


#### GL_OES_POINT_SIZE_ARRAY ####
def init_gl_oes_point_size_array():
    set_func('glPointSizePointerOES', t.void, (t.GLenum, t.GLsizei, ct.POINTER(t.void)))
    set_enum("GL_POINT_SIZE_ARRAY_OES", 0x8B9C)
    set_enum("GL_POINT_SIZE_ARRAY_TYPE_OES", 0x898A)
    set_enum("GL_POINT_SIZE_ARRAY_STRIDE_OES", 0x898B)
    set_enum("GL_POINT_SIZE_ARRAY_POINTER_OES", 0x898C)
    set_enum("GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES", 0x8B9F)


#### GL_OES_POINT_SPRITE ####
def init_gl_oes_point_sprite():
    set_enum("GL_POINT_SPRITE_OES", 0x8861)
    set_enum("GL_COORD_REPLACE_OES", 0x8862)


#### GL_OES_QUERY_MATRIX ####
def init_gl_oes_query_matrix():
    set_func('glQueryMatrixxOES', t.GLbitfield, (ct.POINTER(t.GLfixed), ct.POINTER(t.GLint)))


#### GL_OES_READ_FORMAT ####
def init_gl_oes_read_format():
    set_enum("GL_IMPLEMENTATION_COLOR_READ_TYPE_OES", 0x8B9A)
    set_enum("GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES", 0x8B9B)


#### GL_OES_REQUIRED_INTERNALFORMAT ####
def init_gl_oes_required_internalformat():
    set_enum("GL_ALPHA8_OES", 0x803C)
    set_enum("GL_DEPTH_COMPONENT16_OES", 0x81A5)
    set_enum("GL_DEPTH_COMPONENT24_OES", 0x81A6)
    set_enum("GL_DEPTH24_STENCIL8_OES", 0x88F0)
    set_enum("GL_DEPTH_COMPONENT32_OES", 0x81A7)
    set_enum("GL_LUMINANCE4_ALPHA4_OES", 0x8043)
    set_enum("GL_LUMINANCE8_ALPHA8_OES", 0x8045)
    set_enum("GL_LUMINANCE8_OES", 0x8040)
    set_enum("GL_RGBA4_OES", 0x8056)
    set_enum("GL_RGB5_A1_OES", 0x8057)
    set_enum("GL_RGB565_OES", 0x8D62)
    set_enum("GL_RGB8_OES", 0x8051)
    set_enum("GL_RGBA8_OES", 0x8058)
    set_enum("GL_RGB10_EXT", 0x8052)
    set_enum("GL_RGB10_A2_EXT", 0x8059)


#### GL_OES_RGB8_RGBA8 ####
def init_gl_oes_rgb8_rgba8():
    set_enum("GL_RGB8_OES", 0x8051)
    set_enum("GL_RGBA8_OES", 0x8058)


#### GL_OES_SINGLE_PRECISION ####
def init_gl_oes_single_precision():
    set_func('glClearDepthfOES', t.void, (t.GLclampf,))
    set_func('glClipPlanefOES', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glDepthRangefOES', t.void, (t.GLclampf, t.GLclampf))
    set_func('glFrustumfOES', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('glGetClipPlanefOES', t.void, (t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glOrthofOES', t.void, (t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat, t.GLfloat))


#### GL_OES_STENCIL1 ####
def init_gl_oes_stencil1():
    set_enum("GL_STENCIL_INDEX1_OES", 0x8D46)


#### GL_OES_STENCIL4 ####
def init_gl_oes_stencil4():
    set_enum("GL_STENCIL_INDEX4_OES", 0x8D47)


#### GL_OES_STENCIL8 ####
def init_gl_oes_stencil8():
    set_enum("GL_STENCIL_INDEX8_OES", 0x8D48)


#### GL_OES_STENCIL_WRAP ####
def init_gl_oes_stencil_wrap():
    set_enum("GL_INCR_WRAP_OES", 0x8507)
    set_enum("GL_DECR_WRAP_OES", 0x8508)


#### GL_OES_TEXTURE_CUBE_MAP ####
def init_gl_oes_texture_cube_map():
    set_func('glTexGenfOES', t.void, (t.GLenum, t.GLenum, t.GLfloat))
    set_func('glTexGenfvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glTexGeniOES', t.void, (t.GLenum, t.GLenum, t.GLint))
    set_func('glTexGenivOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glTexGenxOES', t.void, (t.GLenum, t.GLenum, t.GLfixed))
    set_func('glTexGenxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_func('glGetTexGenfvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfloat)))
    set_func('glGetTexGenivOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glGetTexGenxvOES', t.void, (t.GLenum, t.GLenum, ct.POINTER(t.GLfixed)))
    set_enum("GL_NORMAL_MAP_OES", 0x8511)
    set_enum("GL_REFLECTION_MAP_OES", 0x8512)
    set_enum("GL_TEXTURE_CUBE_MAP_OES", 0x8513)
    set_enum("GL_TEXTURE_BINDING_CUBE_MAP_OES", 0x8514)
    set_enum("GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES", 0x8515)
    set_enum("GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES", 0x8516)
    set_enum("GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES", 0x8517)
    set_enum("GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES", 0x8518)
    set_enum("GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES", 0x8519)
    set_enum("GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES", 0x851A)
    set_enum("GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES", 0x851C)
    set_enum("GL_TEXTURE_GEN_MODE_OES", 0x2500)
    set_enum("GL_TEXTURE_GEN_STR_OES", 0x8D60)


#### GL_OES_TEXTURE_MIRRORED_REPEAT ####
def init_gl_oes_texture_mirrored_repeat():
    set_enum("GL_MIRRORED_REPEAT_OES", 0x8370)


#### GL_OES_VERTEX_ARRAY_OBJECT ####
def init_gl_oes_vertex_array_object():
    set_func('glBindVertexArrayOES', t.void, (t.GLuint,))
    set_func('glDeleteVertexArraysOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGenVertexArraysOES', t.void, (t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glIsVertexArrayOES', t.GLboolean, (t.GLuint,))
    set_enum("GL_VERTEX_ARRAY_BINDING_OES", 0x85B5)


#### GL_QCOM_DRIVER_CONTROL ####
def init_gl_qcom_driver_control():
    set_func('glGetDriverControlsQCOM', t.void, (ct.POINTER(t.GLint), t.GLsizei, ct.POINTER(t.GLuint)))
    set_func('glGetDriverControlStringQCOM', t.void, (t.GLuint, t.GLsizei, ct.POINTER(t.GLsizei), ct.POINTER(t.GLchar)))
    set_func('glEnableDriverControlQCOM', t.void, (t.GLuint,))
    set_func('glDisableDriverControlQCOM', t.void, (t.GLuint,))


#### GL_QCOM_EXTENDED_GET ####
def init_gl_qcom_extended_get():
    set_func('glExtGetTexturesQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtGetBuffersQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtGetRenderbuffersQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtGetFramebuffersQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtGetTexLevelParameterivQCOM', t.void, (t.GLuint, t.GLenum, t.GLint, t.GLenum, ct.POINTER(t.GLint)))
    set_func('glExtTexObjectStateOverrideiQCOM', t.void, (t.GLenum, t.GLenum, t.GLint))
    set_func('glExtGetTexSubImageQCOM', t.void, (t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLsizei, t.GLenum, t.GLenum, ct.POINTER(t.void)))
    set_func('glExtGetBufferPointervQCOM', t.void, (t.GLenum, ct.POINTER(ct.POINTER(t.void))))
    set_enum("GL_TEXTURE_WIDTH_QCOM", 0x8BD2)
    set_enum("GL_TEXTURE_HEIGHT_QCOM", 0x8BD3)
    set_enum("GL_TEXTURE_DEPTH_QCOM", 0x8BD4)
    set_enum("GL_TEXTURE_INTERNAL_FORMAT_QCOM", 0x8BD5)
    set_enum("GL_TEXTURE_FORMAT_QCOM", 0x8BD6)
    set_enum("GL_TEXTURE_TYPE_QCOM", 0x8BD7)
    set_enum("GL_TEXTURE_IMAGE_VALID_QCOM", 0x8BD8)
    set_enum("GL_TEXTURE_NUM_LEVELS_QCOM", 0x8BD9)
    set_enum("GL_TEXTURE_TARGET_QCOM", 0x8BDA)
    set_enum("GL_TEXTURE_OBJECT_VALID_QCOM", 0x8BDB)
    set_enum("GL_STATE_RESTORE", 0x8BDC)


#### GL_QCOM_EXTENDED_GET2 ####
def init_gl_qcom_extended_get2():
    set_func('glExtGetShadersQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtGetProgramsQCOM', t.void, (ct.POINTER(t.GLuint), t.GLint, ct.POINTER(t.GLint)))
    set_func('glExtIsProgramBinaryQCOM', t.GLboolean, (t.GLuint,))
    set_func('glExtGetProgramBinarySourceQCOM', t.void, (t.GLuint, t.GLenum, ct.POINTER(t.GLchar), ct.POINTER(t.GLint)))


#### GL_QCOM_PERFMON_GLOBAL_MODE ####
def init_gl_qcom_perfmon_global_mode():
    set_enum("GL_PERFMON_GLOBAL_MODE_QCOM", 0x8FA0)


#### GL_QCOM_TILED_RENDERING ####
def init_gl_qcom_tiled_rendering():
    set_func('glStartTilingQCOM', t.void, (t.GLuint, t.GLuint, t.GLuint, t.GLuint, t.GLbitfield))
    set_func('glEndTilingQCOM', t.void, (t.GLbitfield,))
    set_enum("GL_COLOR_BUFFER_BIT0_QCOM", 0x00000001)
    set_enum("GL_COLOR_BUFFER_BIT1_QCOM", 0x00000002)
    set_enum("GL_COLOR_BUFFER_BIT2_QCOM", 0x00000004)
    set_enum("GL_COLOR_BUFFER_BIT3_QCOM", 0x00000008)
    set_enum("GL_COLOR_BUFFER_BIT4_QCOM", 0x00000010)
    set_enum("GL_COLOR_BUFFER_BIT5_QCOM", 0x00000020)
    set_enum("GL_COLOR_BUFFER_BIT6_QCOM", 0x00000040)
    set_enum("GL_COLOR_BUFFER_BIT7_QCOM", 0x00000080)
    set_enum("GL_DEPTH_BUFFER_BIT0_QCOM", 0x00000100)
    set_enum("GL_DEPTH_BUFFER_BIT1_QCOM", 0x00000200)
    set_enum("GL_DEPTH_BUFFER_BIT2_QCOM", 0x00000400)
    set_enum("GL_DEPTH_BUFFER_BIT3_QCOM", 0x00000800)
    set_enum("GL_DEPTH_BUFFER_BIT4_QCOM", 0x00001000)
    set_enum("GL_DEPTH_BUFFER_BIT5_QCOM", 0x00002000)
    set_enum("GL_DEPTH_BUFFER_BIT6_QCOM", 0x00004000)
    set_enum("GL_DEPTH_BUFFER_BIT7_QCOM", 0x00008000)
    set_enum("GL_STENCIL_BUFFER_BIT0_QCOM", 0x00010000)
    set_enum("GL_STENCIL_BUFFER_BIT1_QCOM", 0x00020000)
    set_enum("GL_STENCIL_BUFFER_BIT2_QCOM", 0x00040000)
    set_enum("GL_STENCIL_BUFFER_BIT3_QCOM", 0x00080000)
    set_enum("GL_STENCIL_BUFFER_BIT4_QCOM", 0x00100000)
    set_enum("GL_STENCIL_BUFFER_BIT5_QCOM", 0x00200000)
    set_enum("GL_STENCIL_BUFFER_BIT6_QCOM", 0x00400000)
    set_enum("GL_STENCIL_BUFFER_BIT7_QCOM", 0x00800000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT0_QCOM", 0x01000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT1_QCOM", 0x02000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT2_QCOM", 0x04000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT3_QCOM", 0x08000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT4_QCOM", 0x10000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT5_QCOM", 0x20000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT6_QCOM", 0x40000000)
    set_enum("GL_MULTISAMPLE_BUFFER_BIT7_QCOM", 0x80000000)


#### GL_QCOM_WRITEONLY_RENDERING ####
def init_gl_qcom_writeonly_rendering():
    set_enum("GL_WRITEONLY_RENDERING_QCOM", 0x8823)


def init():
    init_gl_version_es_cm_1_0()
    init_gl_amd_compressed_3dc_texture()
    init_gl_amd_compressed_atc_texture()
    init_gl_apple_copy_texture_levels()
    init_gl_apple_framebuffer_multisample()
    init_gl_apple_sync()
    init_gl_apple_texture_format_bgra8888()
    init_gl_apple_texture_max_level()
    init_gl_ext_blend_minmax()
    init_gl_ext_discard_framebuffer()
    init_gl_ext_map_buffer_range()
    init_gl_ext_multi_draw_arrays()
    init_gl_ext_multisampled_render_to_texture()
    init_gl_ext_read_format_bgra()
    init_gl_ext_robustness()
    init_gl_ext_srgb()
    init_gl_ext_texture_compression_dxt1()
    init_gl_ext_texture_filter_anisotropic()
    init_gl_ext_texture_format_bgra8888()
    init_gl_ext_texture_lod_bias()
    init_gl_ext_texture_storage()
    init_gl_img_multisampled_render_to_texture()
    init_gl_img_read_format()
    init_gl_img_texture_compression_pvrtc()
    init_gl_img_texture_env_enhanced_fixed_function()
    init_gl_img_user_clip_plane()
    init_gl_nv_fence()
    init_gl_oes_egl_image()
    init_gl_oes_egl_image_external()
    init_gl_oes_blend_equation_separate()
    init_gl_oes_blend_func_separate()
    init_gl_oes_blend_subtract()
    init_gl_oes_byte_coordinates()
    init_gl_oes_compressed_etc1_rgb8_texture()
    init_gl_oes_compressed_paletted_texture()
    init_gl_oes_depth24()
    init_gl_oes_depth32()
    init_gl_oes_draw_texture()
    init_gl_oes_element_index_uint()
    init_gl_oes_fixed_point()
    init_gl_oes_framebuffer_object()
    init_gl_oes_mapbuffer()
    init_gl_oes_matrix_get()
    init_gl_oes_matrix_palette()
    init_gl_oes_packed_depth_stencil()
    init_gl_oes_point_size_array()
    init_gl_oes_point_sprite()
    init_gl_oes_query_matrix()
    init_gl_oes_read_format()
    init_gl_oes_required_internalformat()
    init_gl_oes_rgb8_rgba8()
    init_gl_oes_single_precision()
    init_gl_oes_stencil1()
    init_gl_oes_stencil4()
    init_gl_oes_stencil8()
    init_gl_oes_stencil_wrap()
    init_gl_oes_texture_cube_map()
    init_gl_oes_texture_mirrored_repeat()
    init_gl_oes_vertex_array_object()
    init_gl_qcom_driver_control()
    init_gl_qcom_extended_get()
    init_gl_qcom_extended_get2()
    init_gl_qcom_perfmon_global_mode()
    init_gl_qcom_tiled_rendering()
    init_gl_qcom_writeonly_rendering()

