'''
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
'''
import sys
import ctypes as ct

from opengl.bindutils import gl_func
from opengl import gltypes as t

def set_func(name, returnType, paramTypes):
    '''gl_func wrapper that inserts function in globals.'''
    globals()[name] = gl_func(name, returnType, paramTypes)

def set_enum(name, value):
    globals()[name] = value

noParms = ()

#### GLX VERSION 1.0 ####
def init_glx_version_1_0():
#     set_func('glXChooseVisual', ct.POINTER(t.XVisualInfo), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
#     set_func('glXCreateContext', t.GLXContext, (ct.POINTER(t.Display), ct.POINTER(t.XVisualInfo), t.GLXContext, t.Bool))
#     set_func('glXDestroyContext', t.void, (ct.POINTER(t.Display), t.GLXContext))
#     set_func('glXMakeCurrent', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.GLXContext))
#     set_func('glXCopyContext', t.void, (ct.POINTER(t.Display), t.GLXContext, t.GLXContext, t.ULONG))
#     set_func('glXSwapBuffers', t.void, (ct.POINTER(t.Display), t.GLXDrawable))
#     set_func('glXCreateGLXPixmap', t.GLXPixmap, (ct.POINTER(t.Display), ct.POINTER(t.XVisualInfo), t.Pixmap))
#     set_func('glXDestroyGLXPixmap', t.void, (ct.POINTER(t.Display), t.GLXPixmap))
#     set_func('glXQueryExtension', t.Bool, (ct.POINTER(t.Display), ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXQueryVersion', t.Bool, (ct.POINTER(t.Display), ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXIsDirect', t.Bool, (ct.POINTER(t.Display), t.GLXContext))
#     set_func('glXGetConfig', t.INT, (ct.POINTER(t.Display), ct.POINTER(t.XVisualInfo), t.INT, ct.POINTER(t.INT)))
#     set_func('glXGetCurrentContext', t.GLXContext, ())
#     set_func('glXGetCurrentDrawable', t.GLXDrawable, ())
    set_func('glXWaitGL', t.void, ())
    set_func('glXWaitX', t.void, ())
#     set_func('glXUseXFont', t.void, (t.Font, t.INT, t.INT, t.INT))
    set_enum("GLX_EXTENSION_NAME", "GLX")
    set_enum("GLX_PbufferClobber", 0)
    set_enum("GLX_BufferSwapComplete", 1)
    set_enum("__GLX_NUMBER_EVENTS", 17)
    set_enum("GLX_BAD_SCREEN", 1)
    set_enum("GLX_BAD_ATTRIBUTE", 2)
    set_enum("GLX_NO_EXTENSION", 3)
    set_enum("GLX_BAD_VISUAL", 4)
    set_enum("GLX_BAD_CONTEXT", 5)
    set_enum("GLX_BAD_VALUE", 6)
    set_enum("GLX_BAD_ENUM", 7)
    set_enum("GLX_USE_GL", 1)
    set_enum("GLX_BUFFER_SIZE", 2)
    set_enum("GLX_LEVEL", 3)
    set_enum("GLX_RGBA", 4)
    set_enum("GLX_DOUBLEBUFFER", 5)
    set_enum("GLX_STEREO", 6)
    set_enum("GLX_AUX_BUFFERS", 7)
    set_enum("GLX_RED_SIZE", 8)
    set_enum("GLX_GREEN_SIZE", 9)
    set_enum("GLX_BLUE_SIZE", 10)
    set_enum("GLX_ALPHA_SIZE", 11)
    set_enum("GLX_DEPTH_SIZE", 12)
    set_enum("GLX_STENCIL_SIZE", 13)
    set_enum("GLX_ACCUM_RED_SIZE", 14)
    set_enum("GLX_ACCUM_GREEN_SIZE", 15)
    set_enum("GLX_ACCUM_BLUE_SIZE", 16)
    set_enum("GLX_ACCUM_ALPHA_SIZE", 17)


#### GLX VERSION 1.1 ####
def init_glx_version_1_1():
#     set_func('glXQueryExtensionsString', ct.POINTER(t.CHAR), (ct.POINTER(t.Display), t.INT))
#     set_func('glXQueryServerString', ct.POINTER(t.CHAR), (ct.POINTER(t.Display), t.INT, t.INT))
#     set_func('glXGetClientString', ct.POINTER(t.CHAR), (ct.POINTER(t.Display), t.INT))
    set_enum("GLX_VENDOR", 0x1)
    set_enum("GLX_VERSION", 0x2)
    set_enum("GLX_EXTENSIONS", 0x3)


#### GLX VERSION 1.2 ####
def init_glx_version_1_2():
#     set_func('glXGetCurrentDisplay', ct.POINTER(t.Display), ())
    pass

#### GLX VERSION 1.3 ####
def init_glx_version_1_3():
#     set_func('glXGetFBConfigs', ct.POINTER(t.GLXFBConfig), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
#     set_func('glXChooseFBConfig', ct.POINTER(t.GLXFBConfig), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXGetFBConfigAttrib', t.INT, (ct.POINTER(t.Display), t.GLXFBConfig, t.INT, ct.POINTER(t.INT)))
#     set_func('glXGetVisualFromFBConfig', ct.POINTER(t.XVisualInfo), (ct.POINTER(t.Display), t.GLXFBConfig))
#     set_func('glXCreateWindow', t.GLXWindow, (ct.POINTER(t.Display), t.GLXFBConfig, t.Window, ct.POINTER(t.INT)))
#     set_func('glXDestroyWindow', t.void, (ct.POINTER(t.Display), t.GLXWindow))
#     set_func('glXCreatePixmap', t.GLXPixmap, (ct.POINTER(t.Display), t.GLXFBConfig, t.Pixmap, ct.POINTER(t.INT)))
#     set_func('glXDestroyPixmap', t.void, (ct.POINTER(t.Display), t.GLXPixmap))
#     set_func('glXCreatePbuffer', t.GLXPbuffer, (ct.POINTER(t.Display), t.GLXFBConfig, ct.POINTER(t.INT)))
#     set_func('glXDestroyPbuffer', t.void, (ct.POINTER(t.Display), t.GLXPbuffer))
#     set_func('glXQueryDrawable', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT, ct.POINTER(t.UINT)))
#     set_func('glXCreateNewContext', t.GLXContext, (ct.POINTER(t.Display), t.GLXFBConfig, t.INT, t.GLXContext, t.Bool))
#     set_func('glXMakeContextCurrent', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.GLXDrawable, t.GLXContext))
#     set_func('glXGetCurrentReadDrawable', t.GLXDrawable, ())
#     set_func('glXQueryContext', t.INT, (ct.POINTER(t.Display), t.GLXContext, t.INT, ct.POINTER(t.INT)))
#     set_func('glXSelectEvent', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.ULONG))
#     set_func('glXGetSelectedEvent', t.void, (ct.POINTER(t.Display), t.GLXDrawable, ct.POINTER(t.ULONG)))
    set_enum("GLX_WINDOW_BIT", 0x00000001)
    set_enum("GLX_PIXMAP_BIT", 0x00000002)
    set_enum("GLX_PBUFFER_BIT", 0x00000004)
    set_enum("GLX_RGBA_BIT", 0x00000001)
    set_enum("GLX_COLOR_INDEX_BIT", 0x00000002)
    set_enum("GLX_PBUFFER_CLOBBER_MASK", 0x08000000)
    set_enum("GLX_FRONT_LEFT_BUFFER_BIT", 0x00000001)
    set_enum("GLX_FRONT_RIGHT_BUFFER_BIT", 0x00000002)
    set_enum("GLX_BACK_LEFT_BUFFER_BIT", 0x00000004)
    set_enum("GLX_BACK_RIGHT_BUFFER_BIT", 0x00000008)
    set_enum("GLX_AUX_BUFFERS_BIT", 0x00000010)
    set_enum("GLX_DEPTH_BUFFER_BIT", 0x00000020)
    set_enum("GLX_STENCIL_BUFFER_BIT", 0x00000040)
    set_enum("GLX_ACCUM_BUFFER_BIT", 0x00000080)
    set_enum("GLX_CONFIG_CAVEAT", 0x20)
    set_enum("GLX_X_VISUAL_TYPE", 0x22)
    set_enum("GLX_TRANSPARENT_TYPE", 0x23)
    set_enum("GLX_TRANSPARENT_INDEX_VALUE", 0x24)
    set_enum("GLX_TRANSPARENT_RED_VALUE", 0x25)
    set_enum("GLX_TRANSPARENT_GREEN_VALUE", 0x26)
    set_enum("GLX_TRANSPARENT_BLUE_VALUE", 0x27)
    set_enum("GLX_TRANSPARENT_ALPHA_VALUE", 0x28)
    set_enum("GLX_DONT_CARE", 0xFFFFFFFF)
    set_enum("GLX_NONE", 0x8000)
    set_enum("GLX_SLOW_CONFIG", 0x8001)
    set_enum("GLX_TRUE_COLOR", 0x8002)
    set_enum("GLX_DIRECT_COLOR", 0x8003)
    set_enum("GLX_PSEUDO_COLOR", 0x8004)
    set_enum("GLX_STATIC_COLOR", 0x8005)
    set_enum("GLX_GRAY_SCALE", 0x8006)
    set_enum("GLX_STATIC_GRAY", 0x8007)
    set_enum("GLX_TRANSPARENT_RGB", 0x8008)
    set_enum("GLX_TRANSPARENT_INDEX", 0x8009)
    set_enum("GLX_VISUAL_ID", 0x800B)
    set_enum("GLX_SCREEN", 0x800C)
    set_enum("GLX_NON_CONFORMANT_CONFIG", 0x800D)
    set_enum("GLX_DRAWABLE_TYPE", 0x8010)
    set_enum("GLX_RENDER_TYPE", 0x8011)
    set_enum("GLX_X_RENDERABLE", 0x8012)
    set_enum("GLX_FBCONFIG_ID", 0x8013)
    set_enum("GLX_RGBA_TYPE", 0x8014)
    set_enum("GLX_COLOR_INDEX_TYPE", 0x8015)
    set_enum("GLX_MAX_PBUFFER_WIDTH", 0x8016)
    set_enum("GLX_MAX_PBUFFER_HEIGHT", 0x8017)
    set_enum("GLX_MAX_PBUFFER_PIXELS", 0x8018)
    set_enum("GLX_PRESERVED_CONTENTS", 0x801B)
    set_enum("GLX_LARGEST_PBUFFER", 0x801C)
    set_enum("GLX_WIDTH", 0x801D)
    set_enum("GLX_HEIGHT", 0x801E)
    set_enum("GLX_EVENT_MASK", 0x801F)
    set_enum("GLX_DAMAGED", 0x8020)
    set_enum("GLX_SAVED", 0x8021)
    set_enum("GLX_WINDOW", 0x8022)
    set_enum("GLX_PBUFFER", 0x8023)
    set_enum("GLX_PBUFFER_HEIGHT", 0x8040)
    set_enum("GLX_PBUFFER_WIDTH", 0x8041)


#### GLX VERSION 1.4 ####
def init_glx_version_1_4():
#     set_func('glXGetProcAddress', t.__GLXextFuncPtr, (ct.POINTER(t.GLubyte),))
    set_enum("GLX_SAMPLE_BUFFERS", 100000)
    set_enum("GLX_SAMPLES", 100001)


#### GLX_3DFX_MULTISAMPLE ####
def init_glx_3dfx_multisample():
    set_enum("GLX_SAMPLE_BUFFERS_3DFX", 0x8050)
    set_enum("GLX_SAMPLES_3DFX", 0x8051)


#### GLX_AMD_GPU_ASSOCIATION ####
def init_glx_amd_gpu_association():
#     set_func('glXGetGPUIDsAMD', t.UINT, (t.UINT, ct.POINTER(t.UINT)))
#     set_func('glXGetGPUInfoAMD', t.INT, (t.UINT, t.INT, t.GLenum, t.UINT, ct.POINTER(t.void)))
#     set_func('glXGetContextGPUIDAMD', t.UINT, (t.GLXContext,))
#     set_func('glXCreateAssociatedContextAMD', t.GLXContext, (t.UINT, t.GLXContext))
#     set_func('glXCreateAssociatedContextAttribsAMD', t.GLXContext, (t.UINT, t.GLXContext, ct.POINTER(t.INT)))
#     set_func('glXDeleteAssociatedContextAMD', t.Bool, (t.GLXContext,))
#     set_func('glXMakeAssociatedContextCurrentAMD', t.Bool, (t.GLXContext,))
#     set_func('glXGetCurrentAssociatedContextAMD', t.GLXContext, ())
#     set_func('glXBlitContextFramebufferAMD', t.void, (t.GLXContext, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLbitfield, t.GLenum))
    set_enum("GLX_GPU_VENDOR_AMD", 0x1F00)
    set_enum("GLX_GPU_RENDERER_STRING_AMD", 0x1F01)
    set_enum("GLX_GPU_OPENGL_VERSION_STRING_AMD", 0x1F02)
    set_enum("GLX_GPU_FASTEST_TARGET_GPUS_AMD", 0x21A2)
    set_enum("GLX_GPU_RAM_AMD", 0x21A3)
    set_enum("GLX_GPU_CLOCK_AMD", 0x21A4)
    set_enum("GLX_GPU_NUM_PIPES_AMD", 0x21A5)
    set_enum("GLX_GPU_NUM_SIMD_AMD", 0x21A6)
    set_enum("GLX_GPU_NUM_RB_AMD", 0x21A7)
    set_enum("GLX_GPU_NUM_SPI_AMD", 0x21A8)


#### GLX_ARB_CONTEXT_FLUSH_CONTROL ####
def init_glx_arb_context_flush_control():
    set_enum("GLX_CONTEXT_RELEASE_BEHAVIOR_ARB", 0x2097)
    set_enum("GLX_CONTEXT_RELEASE_BEHAVIOR_NONE_ARB", 0)
    set_enum("GLX_CONTEXT_RELEASE_BEHAVIOR_FLUSH_ARB", 0x2098)


#### GLX_ARB_CREATE_CONTEXT ####
def init_glx_arb_create_context():
#     set_func('glXCreateContextAttribsARB', t.GLXContext, (ct.POINTER(t.Display), t.GLXFBConfig, t.GLXContext, t.Bool, ct.POINTER(t.INT)))
    set_enum("GLX_CONTEXT_DEBUG_BIT_ARB", 0x00000001)
    set_enum("GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB", 0x00000002)
    set_enum("GLX_CONTEXT_MAJOR_VERSION_ARB", 0x2091)
    set_enum("GLX_CONTEXT_MINOR_VERSION_ARB", 0x2092)
    set_enum("GLX_CONTEXT_FLAGS_ARB", 0x2094)


#### GLX_ARB_CREATE_CONTEXT_PROFILE ####
def init_glx_arb_create_context_profile():
    set_enum("GLX_CONTEXT_CORE_PROFILE_BIT_ARB", 0x00000001)
    set_enum("GLX_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB", 0x00000002)
    set_enum("GLX_CONTEXT_PROFILE_MASK_ARB", 0x9126)


#### GLX_ARB_CREATE_CONTEXT_ROBUSTNESS ####
def init_glx_arb_create_context_robustness():
    set_enum("GLX_CONTEXT_ROBUST_ACCESS_BIT_ARB", 0x00000004)
    set_enum("GLX_LOSE_CONTEXT_ON_RESET_ARB", 0x8252)
    set_enum("GLX_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB", 0x8256)
    set_enum("GLX_NO_RESET_NOTIFICATION_ARB", 0x8261)


#### GLX_ARB_FBCONFIG_FLOAT ####
def init_glx_arb_fbconfig_float():
    set_enum("GLX_RGBA_FLOAT_TYPE_ARB", 0x20B9)
    set_enum("GLX_RGBA_FLOAT_BIT_ARB", 0x00000004)


#### GLX_ARB_FRAMEBUFFER_SRGB ####
def init_glx_arb_framebuffer_srgb():
    set_enum("GLX_FRAMEBUFFER_SRGB_CAPABLE_ARB", 0x20B2)


#### GLX_ARB_GET_PROC_ADDRESS ####
def init_glx_arb_get_proc_address():
#     set_func('glXGetProcAddressARB', t.__GLXextFuncPtr, (ct.POINTER(t.GLubyte),))
    pass

#### GLX_ARB_MULTISAMPLE ####
def init_glx_arb_multisample():
    set_enum("GLX_SAMPLE_BUFFERS_ARB", 100000)
    set_enum("GLX_SAMPLES_ARB", 100001)


#### GLX_ARB_ROBUSTNESS_APPLICATION_ISOLATION ####
def init_glx_arb_robustness_application_isolation():
    set_enum("GLX_CONTEXT_RESET_ISOLATION_BIT_ARB", 0x00000008)


#### GLX_ARB_ROBUSTNESS_SHARE_GROUP_ISOLATION ####
def init_glx_arb_robustness_share_group_isolation():
    set_enum("GLX_CONTEXT_RESET_ISOLATION_BIT_ARB", 0x00000008)


#### GLX_ARB_VERTEX_BUFFER_OBJECT ####
def init_glx_arb_vertex_buffer_object():
    set_enum("GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB", 0x2095)


#### GLX_EXT_BUFFER_AGE ####
def init_glx_ext_buffer_age():
    set_enum("GLX_BACK_BUFFER_AGE_EXT", 0x20F4)


#### GLX_EXT_CREATE_CONTEXT_ES_PROFILE ####
def init_glx_ext_create_context_es_profile():
    set_enum("GLX_CONTEXT_ES_PROFILE_BIT_EXT", 0x00000004)


#### GLX_EXT_CREATE_CONTEXT_ES2_PROFILE ####
def init_glx_ext_create_context_es2_profile():
    set_enum("GLX_CONTEXT_ES2_PROFILE_BIT_EXT", 0x00000004)


#### GLX_EXT_FBCONFIG_PACKED_FLOAT ####
def init_glx_ext_fbconfig_packed_float():
    set_enum("GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT", 0x20B1)
    set_enum("GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT", 0x00000008)


#### GLX_EXT_FRAMEBUFFER_SRGB ####
def init_glx_ext_framebuffer_srgb():
    set_enum("GLX_FRAMEBUFFER_SRGB_CAPABLE_EXT", 0x20B2)


#### GLX_EXT_IMPORT_CONTEXT ####
def init_glx_ext_import_context():
#     set_func('glXGetCurrentDisplayEXT', ct.POINTER(t.Display), ())
#     set_func('glXQueryContextInfoEXT', t.INT, (ct.POINTER(t.Display), t.GLXContext, t.INT, ct.POINTER(t.INT)))
#     set_func('glXGetContextIDEXT', t.GLXContextID, (t.GLXContext,))
#     set_func('glXImportContextEXT', t.GLXContext, (ct.POINTER(t.Display), t.GLXContextID))
#     set_func('glXFreeContextEXT', t.void, (ct.POINTER(t.Display), t.GLXContext))
    set_enum("GLX_SHARE_CONTEXT_EXT", 0x800A)
    set_enum("GLX_VISUAL_ID_EXT", 0x800B)
    set_enum("GLX_SCREEN_EXT", 0x800C)


#### GLX_EXT_LIBGLVND ####
def init_glx_ext_libglvnd():
    set_enum("GLX_VENDOR_NAMES_EXT", 0x20F6)


#### GLX_EXT_STEREO_TREE ####
def init_glx_ext_stereo_tree():
    set_enum("GLX_STEREO_TREE_EXT", 0x20F5)
    set_enum("GLX_STEREO_NOTIFY_MASK_EXT", 0x00000001)
    set_enum("GLX_STEREO_NOTIFY_EXT", 0x00000000)


#### GLX_EXT_SWAP_CONTROL ####
def init_glx_ext_swap_control():
#     set_func('glXSwapIntervalEXT', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT))
    set_enum("GLX_SWAP_INTERVAL_EXT", 0x20F1)
    set_enum("GLX_MAX_SWAP_INTERVAL_EXT", 0x20F2)


#### GLX_EXT_SWAP_CONTROL_TEAR ####
def init_glx_ext_swap_control_tear():
    set_enum("GLX_LATE_SWAPS_TEAR_EXT", 0x20F3)


#### GLX_EXT_TEXTURE_FROM_PIXMAP ####
def init_glx_ext_texture_from_pixmap():
#     set_func('glXBindTexImageEXT', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT, ct.POINTER(t.INT)))
#     set_func('glXReleaseTexImageEXT', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT))
    set_enum("GLX_TEXTURE_1D_BIT_EXT", 0x00000001)
    set_enum("GLX_TEXTURE_2D_BIT_EXT", 0x00000002)
    set_enum("GLX_TEXTURE_RECTANGLE_BIT_EXT", 0x00000004)
    set_enum("GLX_BIND_TO_TEXTURE_RGB_EXT", 0x20D0)
    set_enum("GLX_BIND_TO_TEXTURE_RGBA_EXT", 0x20D1)
    set_enum("GLX_BIND_TO_MIPMAP_TEXTURE_EXT", 0x20D2)
    set_enum("GLX_BIND_TO_TEXTURE_TARGETS_EXT", 0x20D3)
    set_enum("GLX_Y_INVERTED_EXT", 0x20D4)
    set_enum("GLX_TEXTURE_FORMAT_EXT", 0x20D5)
    set_enum("GLX_TEXTURE_TARGET_EXT", 0x20D6)
    set_enum("GLX_MIPMAP_TEXTURE_EXT", 0x20D7)
    set_enum("GLX_TEXTURE_FORMAT_NONE_EXT", 0x20D8)
    set_enum("GLX_TEXTURE_FORMAT_RGB_EXT", 0x20D9)
    set_enum("GLX_TEXTURE_FORMAT_RGBA_EXT", 0x20DA)
    set_enum("GLX_TEXTURE_1D_EXT", 0x20DB)
    set_enum("GLX_TEXTURE_2D_EXT", 0x20DC)
    set_enum("GLX_TEXTURE_RECTANGLE_EXT", 0x20DD)
    set_enum("GLX_FRONT_LEFT_EXT", 0x20DE)
    set_enum("GLX_FRONT_RIGHT_EXT", 0x20DF)
    set_enum("GLX_BACK_LEFT_EXT", 0x20E0)
    set_enum("GLX_BACK_RIGHT_EXT", 0x20E1)
    set_enum("GLX_FRONT_EXT", 0x20DE)
    set_enum("GLX_BACK_EXT", 0x20E0)
    set_enum("GLX_AUX0_EXT", 0x20E2)
    set_enum("GLX_AUX1_EXT", 0x20E3)
    set_enum("GLX_AUX2_EXT", 0x20E4)
    set_enum("GLX_AUX3_EXT", 0x20E5)
    set_enum("GLX_AUX4_EXT", 0x20E6)
    set_enum("GLX_AUX5_EXT", 0x20E7)
    set_enum("GLX_AUX6_EXT", 0x20E8)
    set_enum("GLX_AUX7_EXT", 0x20E9)
    set_enum("GLX_AUX8_EXT", 0x20EA)
    set_enum("GLX_AUX9_EXT", 0x20EB)


#### GLX_EXT_VISUAL_INFO ####
def init_glx_ext_visual_info():
    set_enum("GLX_X_VISUAL_TYPE_EXT", 0x22)
    set_enum("GLX_TRANSPARENT_TYPE_EXT", 0x23)
    set_enum("GLX_TRANSPARENT_INDEX_VALUE_EXT", 0x24)
    set_enum("GLX_TRANSPARENT_RED_VALUE_EXT", 0x25)
    set_enum("GLX_TRANSPARENT_GREEN_VALUE_EXT", 0x26)
    set_enum("GLX_TRANSPARENT_BLUE_VALUE_EXT", 0x27)
    set_enum("GLX_TRANSPARENT_ALPHA_VALUE_EXT", 0x28)
    set_enum("GLX_NONE_EXT", 0x8000)
    set_enum("GLX_TRUE_COLOR_EXT", 0x8002)
    set_enum("GLX_DIRECT_COLOR_EXT", 0x8003)
    set_enum("GLX_PSEUDO_COLOR_EXT", 0x8004)
    set_enum("GLX_STATIC_COLOR_EXT", 0x8005)
    set_enum("GLX_GRAY_SCALE_EXT", 0x8006)
    set_enum("GLX_STATIC_GRAY_EXT", 0x8007)
    set_enum("GLX_TRANSPARENT_RGB_EXT", 0x8008)
    set_enum("GLX_TRANSPARENT_INDEX_EXT", 0x8009)


#### GLX_EXT_VISUAL_RATING ####
def init_glx_ext_visual_rating():
    set_enum("GLX_VISUAL_CAVEAT_EXT", 0x20)
    set_enum("GLX_SLOW_VISUAL_EXT", 0x8001)
    set_enum("GLX_NON_CONFORMANT_VISUAL_EXT", 0x800D)
    set_enum("GLX_NONE_EXT", 0x8000)


#### GLX_INTEL_SWAP_EVENT ####
def init_glx_intel_swap_event():
    set_enum("GLX_BUFFER_SWAP_COMPLETE_INTEL_MASK", 0x04000000)
    set_enum("GLX_EXCHANGE_COMPLETE_INTEL", 0x8180)
    set_enum("GLX_COPY_COMPLETE_INTEL", 0x8181)
    set_enum("GLX_FLIP_COMPLETE_INTEL", 0x8182)


#### GLX_MESA_AGP_OFFSET ####
def init_glx_mesa_agp_offset():
#     set_func('glXGetAGPOffsetMESA', t.UINT, (ct.POINTER(t.void),))
    pass

#### GLX_MESA_COPY_SUB_BUFFER ####
def init_glx_mesa_copy_sub_buffer():
#     set_func('glXCopySubBufferMESA', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT, t.INT, t.INT, t.INT))
    pass

#### GLX_MESA_PIXMAP_COLORMAP ####
def init_glx_mesa_pixmap_colormap():
#     set_func('glXCreateGLXPixmapMESA', t.GLXPixmap, (ct.POINTER(t.Display), ct.POINTER(t.XVisualInfo), t.Pixmap, t.Colormap))
    pass

#### GLX_MESA_QUERY_RENDERER ####
def init_glx_mesa_query_renderer():
#     set_func('glXQueryCurrentRendererIntegerMESA', t.Bool, (t.INT, ct.POINTER(t.UINT)))
#     set_func('glXQueryCurrentRendererStringMESA', ct.POINTER(t.CHAR), (t.INT,))
#     set_func('glXQueryRendererIntegerMESA', t.Bool, (ct.POINTER(t.Display), t.INT, t.INT, t.INT, ct.POINTER(t.UINT)))
#     set_func('glXQueryRendererStringMESA', ct.POINTER(t.CHAR), (ct.POINTER(t.Display), t.INT, t.INT, t.INT))
    set_enum("GLX_RENDERER_VENDOR_ID_MESA", 0x8183)
    set_enum("GLX_RENDERER_DEVICE_ID_MESA", 0x8184)
    set_enum("GLX_RENDERER_VERSION_MESA", 0x8185)
    set_enum("GLX_RENDERER_ACCELERATED_MESA", 0x8186)
    set_enum("GLX_RENDERER_VIDEO_MEMORY_MESA", 0x8187)
    set_enum("GLX_RENDERER_UNIFIED_MEMORY_ARCHITECTURE_MESA", 0x8188)
    set_enum("GLX_RENDERER_PREFERRED_PROFILE_MESA", 0x8189)
    set_enum("GLX_RENDERER_OPENGL_CORE_PROFILE_VERSION_MESA", 0x818A)
    set_enum("GLX_RENDERER_OPENGL_COMPATIBILITY_PROFILE_VERSION_MESA", 0x818B)
    set_enum("GLX_RENDERER_OPENGL_ES_PROFILE_VERSION_MESA", 0x818C)
    set_enum("GLX_RENDERER_OPENGL_ES2_PROFILE_VERSION_MESA", 0x818D)
    set_enum("GLX_RENDERER_ID_MESA", 0x818E)


#### GLX_MESA_RELEASE_BUFFERS ####
def init_glx_mesa_release_buffers():
#     set_func('glXReleaseBuffersMESA', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable))
    pass

#### GLX_MESA_SET_3DFX_MODE ####
def init_glx_mesa_set_3dfx_mode():
#     set_func('glXSet3DfxModeMESA', t.Bool, (t.INT,))
    set_enum("GLX_3DFX_WINDOW_MODE_MESA", 0x1)
    set_enum("GLX_3DFX_FULLSCREEN_MODE_MESA", 0x2)


#### GLX_NV_COPY_BUFFER ####
def init_glx_nv_copy_buffer():
#     set_func('glXCopyBufferSubDataNV', t.void, (ct.POINTER(t.Display), t.GLXContext, t.GLXContext, t.GLenum, t.GLenum, t.GLintptr, t.GLintptr, t.GLsizeiptr))
#     set_func('glXNamedCopyBufferSubDataNV', t.void, (ct.POINTER(t.Display), t.GLXContext, t.GLXContext, t.GLuint, t.GLuint, t.GLintptr, t.GLintptr, t.GLsizeiptr))
    pass

#### GLX_NV_COPY_IMAGE ####
def init_glx_nv_copy_image():
#     set_func('glXCopyImageSubDataNV', t.void, (ct.POINTER(t.Display), t.GLXContext, t.GLuint, t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.GLXContext, t.GLuint, t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLsizei))
    pass

#### GLX_NV_DELAY_BEFORE_SWAP ####
def init_glx_nv_delay_before_swap():
#     set_func('glXDelayBeforeSwapNV', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.GLfloat))
    pass

#### GLX_NV_FLOAT_BUFFER ####
def init_glx_nv_float_buffer():
    set_enum("GLX_FLOAT_COMPONENTS_NV", 0x20B0)


#### GLX_NV_MULTISAMPLE_COVERAGE ####
def init_glx_nv_multisample_coverage():
    set_enum("GLX_COVERAGE_SAMPLES_NV", 100001)
    set_enum("GLX_COLOR_SAMPLES_NV", 0x20B3)


#### GLX_NV_PRESENT_VIDEO ####
def init_glx_nv_present_video():
#     set_func('glXEnumerateVideoDevicesNV', ct.POINTER(t.UINT), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
#     set_func('glXBindVideoDeviceNV', t.INT, (ct.POINTER(t.Display), t.UINT, t.UINT, ct.POINTER(t.INT)))
    set_enum("GLX_NUM_VIDEO_SLOTS_NV", 0x20F0)


#### GLX_NV_SWAP_GROUP ####
def init_glx_nv_swap_group():
#     set_func('glXJoinSwapGroupNV', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.GLuint))
#     set_func('glXBindSwapBarrierNV', t.Bool, (ct.POINTER(t.Display), t.GLuint, t.GLuint))
#     set_func('glXQuerySwapGroupNV', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, ct.POINTER(t.GLuint), ct.POINTER(t.GLuint)))
#     set_func('glXQueryMaxSwapGroupsNV', t.Bool, (ct.POINTER(t.Display), t.INT, ct.POINTER(t.GLuint), ct.POINTER(t.GLuint)))
#     set_func('glXQueryFrameCountNV', t.Bool, (ct.POINTER(t.Display), t.INT, ct.POINTER(t.GLuint)))
#     set_func('glXResetFrameCountNV', t.Bool, (ct.POINTER(t.Display), t.INT))
    pass

#### GLX_NV_VIDEO_CAPTURE ####
def init_glx_nv_video_capture():
#     set_func('glXBindVideoCaptureDeviceNV', t.INT, (ct.POINTER(t.Display), t.UINT, t.GLXVideoCaptureDeviceNV))
#     set_func('glXEnumerateVideoCaptureDevicesNV', ct.POINTER(t.GLXVideoCaptureDeviceNV), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
#     set_func('glXLockVideoCaptureDeviceNV', t.void, (ct.POINTER(t.Display), t.GLXVideoCaptureDeviceNV))
#     set_func('glXQueryVideoCaptureDeviceNV', t.INT, (ct.POINTER(t.Display), t.GLXVideoCaptureDeviceNV, t.INT, ct.POINTER(t.INT)))
#     set_func('glXReleaseVideoCaptureDeviceNV', t.void, (ct.POINTER(t.Display), t.GLXVideoCaptureDeviceNV))
    set_enum("GLX_DEVICE_ID_NV", 0x20CD)
    set_enum("GLX_UNIQUE_ID_NV", 0x20CE)
    set_enum("GLX_NUM_VIDEO_CAPTURE_SLOTS_NV", 0x20CF)


#### GLX_NV_VIDEO_OUT ####
def init_glx_nv_video_out():
#     set_func('glXGetVideoDeviceNV', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, ct.POINTER(t.GLXVideoDeviceNV)))
#     set_func('glXReleaseVideoDeviceNV', t.INT, (ct.POINTER(t.Display), t.INT, t.GLXVideoDeviceNV))
#     set_func('glXBindVideoImageNV', t.INT, (ct.POINTER(t.Display), t.GLXVideoDeviceNV, t.GLXPbuffer, t.INT))
#     set_func('glXReleaseVideoImageNV', t.INT, (ct.POINTER(t.Display), t.GLXPbuffer))
#     set_func('glXSendPbufferToVideoNV', t.INT, (ct.POINTER(t.Display), t.GLXPbuffer, t.INT, ct.POINTER(t.ULONG), t.GLboolean))
#     set_func('glXGetVideoInfoNV', t.INT, (ct.POINTER(t.Display), t.INT, t.GLXVideoDeviceNV, ct.POINTER(t.ULONG), ct.POINTER(t.ULONG)))
    set_enum("GLX_VIDEO_OUT_COLOR_NV", 0x20C3)
    set_enum("GLX_VIDEO_OUT_ALPHA_NV", 0x20C4)
    set_enum("GLX_VIDEO_OUT_DEPTH_NV", 0x20C5)
    set_enum("GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV", 0x20C6)
    set_enum("GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV", 0x20C7)
    set_enum("GLX_VIDEO_OUT_FRAME_NV", 0x20C8)
    set_enum("GLX_VIDEO_OUT_FIELD_1_NV", 0x20C9)
    set_enum("GLX_VIDEO_OUT_FIELD_2_NV", 0x20CA)
    set_enum("GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV", 0x20CB)
    set_enum("GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV", 0x20CC)


#### GLX_OML_SWAP_METHOD ####
def init_glx_oml_swap_method():
    set_enum("GLX_SWAP_METHOD_OML", 0x8060)
    set_enum("GLX_SWAP_EXCHANGE_OML", 0x8061)
    set_enum("GLX_SWAP_COPY_OML", 0x8062)
    set_enum("GLX_SWAP_UNDEFINED_OML", 0x8063)


#### GLX_OML_SYNC_CONTROL ####
def init_glx_oml_sync_control():
#     set_func('glXGetSyncValuesOML', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, ct.POINTER(t.int64_t), ct.POINTER(t.int64_t), ct.POINTER(t.int64_t)))
#     set_func('glXGetMscRateOML', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, ct.POINTER(t.int32_t), ct.POINTER(t.int32_t)))
#     set_func('glXSwapBuffersMscOML', t.int64_t, (ct.POINTER(t.Display), t.GLXDrawable, t.int64_t, t.int64_t, t.int64_t))
#     set_func('glXWaitForMscOML', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.int64_t, t.int64_t, t.int64_t, ct.POINTER(t.int64_t), ct.POINTER(t.int64_t), ct.POINTER(t.int64_t)))
#     set_func('glXWaitForSbcOML', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.int64_t, ct.POINTER(t.int64_t), ct.POINTER(t.int64_t), ct.POINTER(t.int64_t)))
    pass

#### GLX_SGI_CUSHION ####
def init_glx_sgi_cushion():
#     set_func('glXCushionSGI', t.void, (ct.POINTER(t.Display), t.Window, t.FLOAT))
    pass

#### GLX_SGI_MAKE_CURRENT_READ ####
def init_glx_sgi_make_current_read():
#     set_func('glXMakeCurrentReadSGI', t.Bool, (ct.POINTER(t.Display), t.GLXDrawable, t.GLXDrawable, t.GLXContext))
#     set_func('glXGetCurrentReadDrawableSGI', t.GLXDrawable, ())
    pass

#### GLX_SGI_SWAP_CONTROL ####
def init_glx_sgi_swap_control():
#     set_func('glXSwapIntervalSGI', t.INT, (t.INT,))
    pass

#### GLX_SGI_VIDEO_SYNC ####
def init_glx_sgi_video_sync():
#     set_func('glXGetVideoSyncSGI', t.INT, (ct.POINTER(t.UINT),))
#     set_func('glXWaitVideoSyncSGI', t.INT, (t.INT, t.INT, ct.POINTER(t.UINT)))
    pass

#### GLX_SGIS_BLENDED_OVERLAY ####
def init_glx_sgis_blended_overlay():
    set_enum("GLX_BLENDED_RGBA_SGIS", 0x8025)


#### GLX_SGIS_MULTISAMPLE ####
def init_glx_sgis_multisample():
    set_enum("GLX_SAMPLE_BUFFERS_SGIS", 100000)
    set_enum("GLX_SAMPLES_SGIS", 100001)


#### GLX_SGIS_SHARED_MULTISAMPLE ####
def init_glx_sgis_shared_multisample():
    set_enum("GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS", 0x8026)
    set_enum("GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS", 0x8027)


#### GLX_SGIX_DMBUFFER ####
def init_glx_sgix_dmbuffer():
#     set_func('glXAssociateDMPbufferSGIX', t.Bool, (ct.POINTER(t.Display), t.GLXPbufferSGIX, ct.POINTER(t.DMparams), t.DMbuffer))
    set_enum("GLX_DIGITAL_MEDIA_PBUFFER_SGIX", 0x8024)


#### GLX_SGIX_FBCONFIG ####
def init_glx_sgix_fbconfig():
#     set_func('glXGetFBConfigAttribSGIX', t.INT, (ct.POINTER(t.Display), t.GLXFBConfigSGIX, t.INT, ct.POINTER(t.INT)))
#     set_func('glXChooseFBConfigSGIX', ct.POINTER(t.GLXFBConfigSGIX), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXCreateGLXPixmapWithConfigSGIX', t.GLXPixmap, (ct.POINTER(t.Display), t.GLXFBConfigSGIX, t.Pixmap))
#     set_func('glXCreateContextWithConfigSGIX', t.GLXContext, (ct.POINTER(t.Display), t.GLXFBConfigSGIX, t.INT, t.GLXContext, t.Bool))
#     set_func('glXGetVisualFromFBConfigSGIX', ct.POINTER(t.XVisualInfo), (ct.POINTER(t.Display), t.GLXFBConfigSGIX))
#     set_func('glXGetFBConfigFromVisualSGIX', t.GLXFBConfigSGIX, (ct.POINTER(t.Display), ct.POINTER(t.XVisualInfo)))
    set_enum("GLX_WINDOW_BIT_SGIX", 0x00000001)
    set_enum("GLX_PIXMAP_BIT_SGIX", 0x00000002)
    set_enum("GLX_RGBA_BIT_SGIX", 0x00000001)
    set_enum("GLX_COLOR_INDEX_BIT_SGIX", 0x00000002)
    set_enum("GLX_DRAWABLE_TYPE_SGIX", 0x8010)
    set_enum("GLX_RENDER_TYPE_SGIX", 0x8011)
    set_enum("GLX_X_RENDERABLE_SGIX", 0x8012)
    set_enum("GLX_FBCONFIG_ID_SGIX", 0x8013)
    set_enum("GLX_RGBA_TYPE_SGIX", 0x8014)
    set_enum("GLX_COLOR_INDEX_TYPE_SGIX", 0x8015)
    set_enum("GLX_SCREEN_EXT", 0x800C)


#### GLX_SGIX_HYPERPIPE ####
def init_glx_sgix_hyperpipe():
#     set_func('glXQueryHyperpipeNetworkSGIX', ct.POINTER(t.GLXHyperpipeNetworkSGIX), (ct.POINTER(t.Display), ct.POINTER(t.INT)))
#     set_func('glXHyperpipeConfigSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, ct.POINTER(t.GLXHyperpipeConfigSGIX), ct.POINTER(t.INT)))
#     set_func('glXQueryHyperpipeConfigSGIX', ct.POINTER(t.GLXHyperpipeConfigSGIX), (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
#     set_func('glXDestroyHyperpipeConfigSGIX', t.INT, (ct.POINTER(t.Display), t.INT))
#     set_func('glXBindHyperpipeSGIX', t.INT, (ct.POINTER(t.Display), t.INT))
#     set_func('glXQueryHyperpipeBestAttribSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.INT, ct.POINTER(t.void), ct.POINTER(t.void)))
#     set_func('glXHyperpipeAttribSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.INT, ct.POINTER(t.void)))
#     set_func('glXQueryHyperpipeAttribSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.INT, ct.POINTER(t.void)))
    set_enum("GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX", 80)
    set_enum("GLX_BAD_HYPERPIPE_CONFIG_SGIX", 91)
    set_enum("GLX_BAD_HYPERPIPE_SGIX", 92)
    set_enum("GLX_HYPERPIPE_DISPLAY_PIPE_SGIX", 0x00000001)
    set_enum("GLX_HYPERPIPE_RENDER_PIPE_SGIX", 0x00000002)
    set_enum("GLX_PIPE_RECT_SGIX", 0x00000001)
    set_enum("GLX_PIPE_RECT_LIMITS_SGIX", 0x00000002)
    set_enum("GLX_HYPERPIPE_STEREO_SGIX", 0x00000003)
    set_enum("GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX", 0x00000004)
    set_enum("GLX_HYPERPIPE_ID_SGIX", 0x8030)


#### GLX_SGIX_PBUFFER ####
def init_glx_sgix_pbuffer():
#     set_func('glXCreateGLXPbufferSGIX', t.GLXPbufferSGIX, (ct.POINTER(t.Display), t.GLXFBConfigSGIX, t.UINT, t.UINT, ct.POINTER(t.INT)))
#     set_func('glXDestroyGLXPbufferSGIX', t.void, (ct.POINTER(t.Display), t.GLXPbufferSGIX))
#     set_func('glXQueryGLXPbufferSGIX', t.INT, (ct.POINTER(t.Display), t.GLXPbufferSGIX, t.INT, ct.POINTER(t.UINT)))
#     set_func('glXSelectEventSGIX', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.ULONG))
#     set_func('glXGetSelectedEventSGIX', t.void, (ct.POINTER(t.Display), t.GLXDrawable, ct.POINTER(t.ULONG)))
    set_enum("GLX_PBUFFER_BIT_SGIX", 0x00000004)
    set_enum("GLX_BUFFER_CLOBBER_MASK_SGIX", 0x08000000)
    set_enum("GLX_FRONT_LEFT_BUFFER_BIT_SGIX", 0x00000001)
    set_enum("GLX_FRONT_RIGHT_BUFFER_BIT_SGIX", 0x00000002)
    set_enum("GLX_BACK_LEFT_BUFFER_BIT_SGIX", 0x00000004)
    set_enum("GLX_BACK_RIGHT_BUFFER_BIT_SGIX", 0x00000008)
    set_enum("GLX_AUX_BUFFERS_BIT_SGIX", 0x00000010)
    set_enum("GLX_DEPTH_BUFFER_BIT_SGIX", 0x00000020)
    set_enum("GLX_STENCIL_BUFFER_BIT_SGIX", 0x00000040)
    set_enum("GLX_ACCUM_BUFFER_BIT_SGIX", 0x00000080)
    set_enum("GLX_SAMPLE_BUFFERS_BIT_SGIX", 0x00000100)
    set_enum("GLX_MAX_PBUFFER_WIDTH_SGIX", 0x8016)
    set_enum("GLX_MAX_PBUFFER_HEIGHT_SGIX", 0x8017)
    set_enum("GLX_MAX_PBUFFER_PIXELS_SGIX", 0x8018)
    set_enum("GLX_OPTIMAL_PBUFFER_WIDTH_SGIX", 0x8019)
    set_enum("GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX", 0x801A)
    set_enum("GLX_PRESERVED_CONTENTS_SGIX", 0x801B)
    set_enum("GLX_LARGEST_PBUFFER_SGIX", 0x801C)
    set_enum("GLX_WIDTH_SGIX", 0x801D)
    set_enum("GLX_HEIGHT_SGIX", 0x801E)
    set_enum("GLX_EVENT_MASK_SGIX", 0x801F)
    set_enum("GLX_DAMAGED_SGIX", 0x8020)
    set_enum("GLX_SAVED_SGIX", 0x8021)
    set_enum("GLX_WINDOW_SGIX", 0x8022)
    set_enum("GLX_PBUFFER_SGIX", 0x8023)


#### GLX_SGIX_SWAP_BARRIER ####
def init_glx_sgix_swap_barrier():
#     set_func('glXBindSwapBarrierSGIX', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.INT))
#     set_func('glXQueryMaxSwapBarriersSGIX', t.Bool, (ct.POINTER(t.Display), t.INT, ct.POINTER(t.INT)))
    pass

#### GLX_SGIX_SWAP_GROUP ####
def init_glx_sgix_swap_group():
#     set_func('glXJoinSwapGroupSGIX', t.void, (ct.POINTER(t.Display), t.GLXDrawable, t.GLXDrawable))
    pass

#### GLX_SGIX_VIDEO_RESIZE ####
def init_glx_sgix_video_resize():
#     set_func('glXBindChannelToWindowSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.Window))
#     set_func('glXChannelRectSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.INT, t.INT, t.INT, t.INT))
#     set_func('glXQueryChannelRectSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, ct.POINTER(t.INT), ct.POINTER(t.INT), ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXQueryChannelDeltasSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, ct.POINTER(t.INT), ct.POINTER(t.INT), ct.POINTER(t.INT), ct.POINTER(t.INT)))
#     set_func('glXChannelRectSyncSGIX', t.INT, (ct.POINTER(t.Display), t.INT, t.INT, t.GLenum))
    set_enum("GLX_SYNC_FRAME_SGIX", 0x00000000)
    set_enum("GLX_SYNC_SWAP_SGIX", 0x00000001)


#### GLX_SGIX_VIDEO_SOURCE ####
def init_glx_sgix_video_source():
#     set_func('glXCreateGLXVideoSourceSGIX', t.GLXVideoSourceSGIX, (ct.POINTER(t.Display), t.INT, t.VLServer, t.VLPath, t.INT, t.VLNode))
#     set_func('glXDestroyGLXVideoSourceSGIX', t.void, (ct.POINTER(t.Display), t.GLXVideoSourceSGIX))
    pass

#### GLX_SGIX_VISUAL_SELECT_GROUP ####
def init_glx_sgix_visual_select_group():
    set_enum("GLX_VISUAL_SELECT_GROUP_SGIX", 0x8028)


#### GLX_SUN_GET_TRANSPARENT_INDEX ####
def init_glx_sun_get_transparent_index():
#     set_func('glXGetTransparentIndexSUN', t.Status, (ct.POINTER(t.Display), t.Window, t.Window, ct.POINTER(t.long)))
    pass

def init():
    init_glx_version_1_0()
    init_glx_version_1_1()
    init_glx_version_1_2()
    init_glx_version_1_3()
    init_glx_version_1_4()
    init_glx_3dfx_multisample()
    init_glx_amd_gpu_association()
    init_glx_arb_context_flush_control()
    init_glx_arb_create_context()
    init_glx_arb_create_context_profile()
    init_glx_arb_create_context_robustness()
    init_glx_arb_fbconfig_float()
    init_glx_arb_framebuffer_srgb()
    init_glx_arb_get_proc_address()
    init_glx_arb_multisample()
    init_glx_arb_robustness_application_isolation()
    init_glx_arb_robustness_share_group_isolation()
    init_glx_arb_vertex_buffer_object()
    init_glx_ext_buffer_age()
    init_glx_ext_create_context_es_profile()
    init_glx_ext_create_context_es2_profile()
    init_glx_ext_fbconfig_packed_float()
    init_glx_ext_framebuffer_srgb()
    init_glx_ext_import_context()
    init_glx_ext_libglvnd()
    init_glx_ext_stereo_tree()
    init_glx_ext_swap_control()
    init_glx_ext_swap_control_tear()
    init_glx_ext_texture_from_pixmap()
    init_glx_ext_visual_info()
    init_glx_ext_visual_rating()
    init_glx_intel_swap_event()
    init_glx_mesa_agp_offset()
    init_glx_mesa_copy_sub_buffer()
    init_glx_mesa_pixmap_colormap()
    init_glx_mesa_query_renderer()
    init_glx_mesa_release_buffers()
    init_glx_mesa_set_3dfx_mode()
    init_glx_nv_copy_buffer()
    init_glx_nv_copy_image()
    init_glx_nv_delay_before_swap()
    init_glx_nv_float_buffer()
    init_glx_nv_multisample_coverage()
    init_glx_nv_present_video()
    init_glx_nv_swap_group()
    init_glx_nv_video_capture()
    init_glx_nv_video_out()
    init_glx_oml_swap_method()
    init_glx_oml_sync_control()
    init_glx_sgi_cushion()
    init_glx_sgi_make_current_read()
    init_glx_sgi_swap_control()
    init_glx_sgi_video_sync()
    init_glx_sgis_blended_overlay()
    init_glx_sgis_multisample()
    init_glx_sgis_shared_multisample()
    init_glx_sgix_dmbuffer()
    init_glx_sgix_fbconfig()
    init_glx_sgix_hyperpipe()
    init_glx_sgix_pbuffer()
    init_glx_sgix_swap_barrier()
    init_glx_sgix_swap_group()
    init_glx_sgix_video_resize()
    init_glx_sgix_video_source()
    init_glx_sgix_visual_select_group()
    init_glx_sun_get_transparent_index()

