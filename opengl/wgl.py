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

#### WGL VERSION 1.0 ####
def init_wgl_version_1_0():
#     set_func('ChoosePixelFormat', t.int, (t.HDC, ct.POINTER(t.PIXELFORMATDESCRIPTOR)))
#     set_func('DescribePixelFormat', t.int, (t.HDC, t.int, t.UINT, ct.POINTER(t.PIXELFORMATDESCRIPTOR)))
#     set_func('GetEnhMetaFilePixelFormat', t.UINT, (t.HENHMETAFILE, ct.POINTER(t.PIXELFORMATDESCRIPTOR)))
#     set_func('GetPixelFormat', t.int, (t.HDC,))
#     set_func('SetPixelFormat', t.BOOL, (t.HDC, t.int, ct.POINTER(t.PIXELFORMATDESCRIPTOR)))
#     set_func('SwapBuffers', t.BOOL, (t.HDC,))
#     set_func('wglCopyContext', t.BOOL, (t.HGLRC, t.HGLRC, t.UINT))
#     set_func('wglCreateContext', t.HGLRC, (t.HDC,))
#     set_func('wglCreateLayerContext', t.HGLRC, (t.HDC, t.int))
#     set_func('wglDeleteContext', t.BOOL, (t.HGLRC,))
#     set_func('wglDescribeLayerPlane', t.BOOL, (t.HDC, t.int, t.int, t.UINT, ct.POINTER(t.LAYERPLANEDESCRIPTOR)))
#     set_func('wglGetCurrentContext', t.HGLRC, ())
#     set_func('wglGetCurrentDC', t.HDC, ())
#     set_func('wglGetLayerPaletteEntries', t.int, (t.HDC, t.int, t.int, t.int, ct.POINTER(t.COLORREF)))
#     set_func('wglGetProcAddress', t.PROC, (t.LPCSTR,))
#     set_func('wglMakeCurrent', t.BOOL, (t.HDC, t.HGLRC))
#     set_func('wglRealizeLayerPalette', t.BOOL, (t.HDC, t.int, t.BOOL))
#     set_func('wglSetLayerPaletteEntries', t.int, (t.HDC, t.int, t.int, t.int, ct.POINTER(t.COLORREF)))
#     set_func('wglShareLists', t.BOOL, (t.HGLRC, t.HGLRC))
#     set_func('wglSwapLayerBuffers', t.BOOL, (t.HDC, t.UINT))
#     set_func('wglUseFontBitmaps', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD))
#     set_func('wglUseFontBitmapsA', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD))
#     set_func('wglUseFontBitmapsW', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD))
#     set_func('wglUseFontOutlines', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD, t.FLOAT, t.FLOAT, t.int, t.LPGLYPHMETRICSFLOAT))
#     set_func('wglUseFontOutlinesA', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD, t.FLOAT, t.FLOAT, t.int, t.LPGLYPHMETRICSFLOAT))
#     set_func('wglUseFontOutlinesW', t.BOOL, (t.HDC, t.DWORD, t.DWORD, t.DWORD, t.FLOAT, t.FLOAT, t.int, t.LPGLYPHMETRICSFLOAT))
    set_enum("WGL_FONT_LINES", 0)
    set_enum("WGL_FONT_POLYGONS", 1)
    set_enum("WGL_SWAP_MAIN_PLANE", 0x00000001)
    set_enum("WGL_SWAP_OVERLAY1", 0x00000002)
    set_enum("WGL_SWAP_OVERLAY2", 0x00000004)
    set_enum("WGL_SWAP_OVERLAY3", 0x00000008)
    set_enum("WGL_SWAP_OVERLAY4", 0x00000010)
    set_enum("WGL_SWAP_OVERLAY5", 0x00000020)
    set_enum("WGL_SWAP_OVERLAY6", 0x00000040)
    set_enum("WGL_SWAP_OVERLAY7", 0x00000080)
    set_enum("WGL_SWAP_OVERLAY8", 0x00000100)
    set_enum("WGL_SWAP_OVERLAY9", 0x00000200)
    set_enum("WGL_SWAP_OVERLAY10", 0x00000400)
    set_enum("WGL_SWAP_OVERLAY11", 0x00000800)
    set_enum("WGL_SWAP_OVERLAY12", 0x00001000)
    set_enum("WGL_SWAP_OVERLAY13", 0x00002000)
    set_enum("WGL_SWAP_OVERLAY14", 0x00004000)
    set_enum("WGL_SWAP_OVERLAY15", 0x00008000)
    set_enum("WGL_SWAP_UNDERLAY1", 0x00010000)
    set_enum("WGL_SWAP_UNDERLAY2", 0x00020000)
    set_enum("WGL_SWAP_UNDERLAY3", 0x00040000)
    set_enum("WGL_SWAP_UNDERLAY4", 0x00080000)
    set_enum("WGL_SWAP_UNDERLAY5", 0x00100000)
    set_enum("WGL_SWAP_UNDERLAY6", 0x00200000)
    set_enum("WGL_SWAP_UNDERLAY7", 0x00400000)
    set_enum("WGL_SWAP_UNDERLAY8", 0x00800000)
    set_enum("WGL_SWAP_UNDERLAY9", 0x01000000)
    set_enum("WGL_SWAP_UNDERLAY10", 0x02000000)
    set_enum("WGL_SWAP_UNDERLAY11", 0x04000000)
    set_enum("WGL_SWAP_UNDERLAY12", 0x08000000)
    set_enum("WGL_SWAP_UNDERLAY13", 0x10000000)
    set_enum("WGL_SWAP_UNDERLAY14", 0x20000000)
    set_enum("WGL_SWAP_UNDERLAY15", 0x40000000)


#### WGL VERSION 1.0 ####
def init_wgl_3dfx_multisample():
    set_enum("WGL_SAMPLE_BUFFERS_3DFX", 0x2060)
    set_enum("WGL_SAMPLES_3DFX", 0x2061)


#### WGL VERSION 1.0 ####
def init_wgl_3dl_stereo_control():
#     set_func('wglSetStereoEmitterState3DL', t.BOOL, (t.HDC, t.UINT))
    set_enum("WGL_STEREO_EMITTER_ENABLE_3DL", 0x2055)
    set_enum("WGL_STEREO_EMITTER_DISABLE_3DL", 0x2056)
    set_enum("WGL_STEREO_POLARITY_NORMAL_3DL", 0x2057)
    set_enum("WGL_STEREO_POLARITY_INVERT_3DL", 0x2058)


#### WGL VERSION 1.0 ####
def init_wgl_amd_gpu_association():
#     set_func('wglGetGPUIDsAMD', t.UINT, (t.UINT, ct.POINTER(t.UINT)))
#     set_func('wglGetGPUInfoAMD', t.INT, (t.UINT, t.int, t.GLenum, t.UINT, ct.POINTER(t.void)))
#     set_func('wglGetContextGPUIDAMD', t.UINT, (t.HGLRC,))
#     set_func('wglCreateAssociatedContextAMD', t.HGLRC, (t.UINT,))
#     set_func('wglCreateAssociatedContextAttribsAMD', t.HGLRC, (t.UINT, t.HGLRC, ct.POINTER(t.int)))
#     set_func('wglDeleteAssociatedContextAMD', t.BOOL, (t.HGLRC,))
#     set_func('wglMakeAssociatedContextCurrentAMD', t.BOOL, (t.HGLRC,))
#     set_func('wglGetCurrentAssociatedContextAMD', t.HGLRC, ())
#     set_func('wglBlitContextFramebufferAMD', t.VOID, (t.HGLRC, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLint, t.GLbitfield, t.GLenum))
    set_enum("WGL_GPU_VENDOR_AMD", 0x1F00)
    set_enum("WGL_GPU_RENDERER_STRING_AMD", 0x1F01)
    set_enum("WGL_GPU_OPENGL_VERSION_STRING_AMD", 0x1F02)
    set_enum("WGL_GPU_FASTEST_TARGET_GPUS_AMD", 0x21A2)
    set_enum("WGL_GPU_RAM_AMD", 0x21A3)
    set_enum("WGL_GPU_CLOCK_AMD", 0x21A4)
    set_enum("WGL_GPU_NUM_PIPES_AMD", 0x21A5)
    set_enum("WGL_GPU_NUM_SIMD_AMD", 0x21A6)
    set_enum("WGL_GPU_NUM_RB_AMD", 0x21A7)
    set_enum("WGL_GPU_NUM_SPI_AMD", 0x21A8)


#### WGL VERSION 1.0 ####
def init_wgl_arb_buffer_region():
#     set_func('wglCreateBufferRegionARB', t.HANDLE, (t.HDC, t.int, t.UINT))
#     set_func('wglDeleteBufferRegionARB', t.VOID, (t.HANDLE,))
#     set_func('wglSaveBufferRegionARB', t.BOOL, (t.HANDLE, t.int, t.int, t.int, t.int))
#     set_func('wglRestoreBufferRegionARB', t.BOOL, (t.HANDLE, t.int, t.int, t.int, t.int, t.int, t.int))
    set_enum("WGL_FRONT_COLOR_BUFFER_BIT_ARB", 0x00000001)
    set_enum("WGL_BACK_COLOR_BUFFER_BIT_ARB", 0x00000002)
    set_enum("WGL_DEPTH_BUFFER_BIT_ARB", 0x00000004)
    set_enum("WGL_STENCIL_BUFFER_BIT_ARB", 0x00000008)


#### WGL VERSION 1.0 ####
def init_wgl_arb_context_flush_control():
    set_enum("WGL_CONTEXT_RELEASE_BEHAVIOR_ARB", 0x2097)
    set_enum("WGL_CONTEXT_RELEASE_BEHAVIOR_NONE_ARB", 0)
    set_enum("WGL_CONTEXT_RELEASE_BEHAVIOR_FLUSH_ARB", 0x2098)


#### WGL VERSION 1.0 ####
def init_wgl_arb_create_context():
#     set_func('wglCreateContextAttribsARB', t.HGLRC, (t.HDC, t.HGLRC, ct.POINTER(t.int)))
    set_enum("WGL_CONTEXT_DEBUG_BIT_ARB", 0x00000001)
    set_enum("WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB", 0x00000002)
    set_enum("WGL_CONTEXT_MAJOR_VERSION_ARB", 0x2091)
    set_enum("WGL_CONTEXT_MINOR_VERSION_ARB", 0x2092)
    set_enum("WGL_CONTEXT_LAYER_PLANE_ARB", 0x2093)
    set_enum("WGL_CONTEXT_FLAGS_ARB", 0x2094)
    set_enum("ERROR_INVALID_VERSION_ARB", 0x2095)


#### WGL VERSION 1.0 ####
def init_wgl_arb_create_context_profile():
    set_enum("WGL_CONTEXT_PROFILE_MASK_ARB", 0x9126)
    set_enum("WGL_CONTEXT_CORE_PROFILE_BIT_ARB", 0x00000001)
    set_enum("WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB", 0x00000002)
    set_enum("ERROR_INVALID_PROFILE_ARB", 0x2096)


#### WGL VERSION 1.0 ####
def init_wgl_arb_create_context_robustness():
    set_enum("WGL_CONTEXT_ROBUST_ACCESS_BIT_ARB", 0x00000004)
    set_enum("WGL_LOSE_CONTEXT_ON_RESET_ARB", 0x8252)
    set_enum("WGL_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB", 0x8256)
    set_enum("WGL_NO_RESET_NOTIFICATION_ARB", 0x8261)


#### WGL VERSION 1.0 ####
def init_wgl_arb_extensions_string():
#     set_func('wglGetExtensionsStringARB', ct.POINTER(t.char), (t.HDC,))


#### WGL VERSION 1.0 ####
def init_wgl_arb_framebuffer_srgb():
    set_enum("WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB", 0x20A9)


#### WGL VERSION 1.0 ####
def init_wgl_arb_make_current_read():
#     set_func('wglMakeContextCurrentARB', t.BOOL, (t.HDC, t.HDC, t.HGLRC))
#     set_func('wglGetCurrentReadDCARB', t.HDC, ())
    set_enum("ERROR_INVALID_PIXEL_TYPE_ARB", 0x2043)
    set_enum("ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB", 0x2054)


#### WGL VERSION 1.0 ####
def init_wgl_arb_multisample():
    set_enum("WGL_SAMPLE_BUFFERS_ARB", 0x2041)
    set_enum("WGL_SAMPLES_ARB", 0x2042)


#### WGL VERSION 1.0 ####
def init_wgl_arb_pbuffer():
#     set_func('wglCreatePbufferARB', t.HPBUFFERARB, (t.HDC, t.int, t.int, t.int, ct.POINTER(t.int)))
#     set_func('wglGetPbufferDCARB', t.HDC, (t.HPBUFFERARB,))
#     set_func('wglReleasePbufferDCARB', t.int, (t.HPBUFFERARB, t.HDC))
#     set_func('wglDestroyPbufferARB', t.BOOL, (t.HPBUFFERARB,))
#     set_func('wglQueryPbufferARB', t.BOOL, (t.HPBUFFERARB, t.int, ct.POINTER(t.int)))
    set_enum("WGL_DRAW_TO_PBUFFER_ARB", 0x202D)
    set_enum("WGL_MAX_PBUFFER_PIXELS_ARB", 0x202E)
    set_enum("WGL_MAX_PBUFFER_WIDTH_ARB", 0x202F)
    set_enum("WGL_MAX_PBUFFER_HEIGHT_ARB", 0x2030)
    set_enum("WGL_PBUFFER_LARGEST_ARB", 0x2033)
    set_enum("WGL_PBUFFER_WIDTH_ARB", 0x2034)
    set_enum("WGL_PBUFFER_HEIGHT_ARB", 0x2035)
    set_enum("WGL_PBUFFER_LOST_ARB", 0x2036)


#### WGL VERSION 1.0 ####
def init_wgl_arb_pixel_format():
#     set_func('wglGetPixelFormatAttribivARB', t.BOOL, (t.HDC, t.int, t.int, t.UINT, ct.POINTER(t.int), ct.POINTER(t.int)))
#     set_func('wglGetPixelFormatAttribfvARB', t.BOOL, (t.HDC, t.int, t.int, t.UINT, ct.POINTER(t.int), ct.POINTER(t.FLOAT)))
#     set_func('wglChoosePixelFormatARB', t.BOOL, (t.HDC, ct.POINTER(t.int), ct.POINTER(t.FLOAT), t.UINT, ct.POINTER(t.int), ct.POINTER(t.UINT)))
    set_enum("WGL_NUMBER_PIXEL_FORMATS_ARB", 0x2000)
    set_enum("WGL_DRAW_TO_WINDOW_ARB", 0x2001)
    set_enum("WGL_DRAW_TO_BITMAP_ARB", 0x2002)
    set_enum("WGL_ACCELERATION_ARB", 0x2003)
    set_enum("WGL_NEED_PALETTE_ARB", 0x2004)
    set_enum("WGL_NEED_SYSTEM_PALETTE_ARB", 0x2005)
    set_enum("WGL_SWAP_LAYER_BUFFERS_ARB", 0x2006)
    set_enum("WGL_SWAP_METHOD_ARB", 0x2007)
    set_enum("WGL_NUMBER_OVERLAYS_ARB", 0x2008)
    set_enum("WGL_NUMBER_UNDERLAYS_ARB", 0x2009)
    set_enum("WGL_TRANSPARENT_ARB", 0x200A)
    set_enum("WGL_TRANSPARENT_RED_VALUE_ARB", 0x2037)
    set_enum("WGL_TRANSPARENT_GREEN_VALUE_ARB", 0x2038)
    set_enum("WGL_TRANSPARENT_BLUE_VALUE_ARB", 0x2039)
    set_enum("WGL_TRANSPARENT_ALPHA_VALUE_ARB", 0x203A)
    set_enum("WGL_TRANSPARENT_INDEX_VALUE_ARB", 0x203B)
    set_enum("WGL_SHARE_DEPTH_ARB", 0x200C)
    set_enum("WGL_SHARE_STENCIL_ARB", 0x200D)
    set_enum("WGL_SHARE_ACCUM_ARB", 0x200E)
    set_enum("WGL_SUPPORT_GDI_ARB", 0x200F)
    set_enum("WGL_SUPPORT_OPENGL_ARB", 0x2010)
    set_enum("WGL_DOUBLE_BUFFER_ARB", 0x2011)
    set_enum("WGL_STEREO_ARB", 0x2012)
    set_enum("WGL_PIXEL_TYPE_ARB", 0x2013)
    set_enum("WGL_COLOR_BITS_ARB", 0x2014)
    set_enum("WGL_RED_BITS_ARB", 0x2015)
    set_enum("WGL_RED_SHIFT_ARB", 0x2016)
    set_enum("WGL_GREEN_BITS_ARB", 0x2017)
    set_enum("WGL_GREEN_SHIFT_ARB", 0x2018)
    set_enum("WGL_BLUE_BITS_ARB", 0x2019)
    set_enum("WGL_BLUE_SHIFT_ARB", 0x201A)
    set_enum("WGL_ALPHA_BITS_ARB", 0x201B)
    set_enum("WGL_ALPHA_SHIFT_ARB", 0x201C)
    set_enum("WGL_ACCUM_BITS_ARB", 0x201D)
    set_enum("WGL_ACCUM_RED_BITS_ARB", 0x201E)
    set_enum("WGL_ACCUM_GREEN_BITS_ARB", 0x201F)
    set_enum("WGL_ACCUM_BLUE_BITS_ARB", 0x2020)
    set_enum("WGL_ACCUM_ALPHA_BITS_ARB", 0x2021)
    set_enum("WGL_DEPTH_BITS_ARB", 0x2022)
    set_enum("WGL_STENCIL_BITS_ARB", 0x2023)
    set_enum("WGL_AUX_BUFFERS_ARB", 0x2024)
    set_enum("WGL_NO_ACCELERATION_ARB", 0x2025)
    set_enum("WGL_GENERIC_ACCELERATION_ARB", 0x2026)
    set_enum("WGL_FULL_ACCELERATION_ARB", 0x2027)
    set_enum("WGL_SWAP_EXCHANGE_ARB", 0x2028)
    set_enum("WGL_SWAP_COPY_ARB", 0x2029)
    set_enum("WGL_SWAP_UNDEFINED_ARB", 0x202A)
    set_enum("WGL_TYPE_RGBA_ARB", 0x202B)
    set_enum("WGL_TYPE_COLORINDEX_ARB", 0x202C)


#### WGL VERSION 1.0 ####
def init_wgl_arb_pixel_format_float():
    set_enum("WGL_TYPE_RGBA_FLOAT_ARB", 0x21A0)


#### WGL VERSION 1.0 ####
def init_wgl_arb_render_texture():
#     set_func('wglBindTexImageARB', t.BOOL, (t.HPBUFFERARB, t.int))
#     set_func('wglReleaseTexImageARB', t.BOOL, (t.HPBUFFERARB, t.int))
#     set_func('wglSetPbufferAttribARB', t.BOOL, (t.HPBUFFERARB, ct.POINTER(t.int)))
    set_enum("WGL_BIND_TO_TEXTURE_RGB_ARB", 0x2070)
    set_enum("WGL_BIND_TO_TEXTURE_RGBA_ARB", 0x2071)
    set_enum("WGL_TEXTURE_FORMAT_ARB", 0x2072)
    set_enum("WGL_TEXTURE_TARGET_ARB", 0x2073)
    set_enum("WGL_MIPMAP_TEXTURE_ARB", 0x2074)
    set_enum("WGL_TEXTURE_RGB_ARB", 0x2075)
    set_enum("WGL_TEXTURE_RGBA_ARB", 0x2076)
    set_enum("WGL_NO_TEXTURE_ARB", 0x2077)
    set_enum("WGL_TEXTURE_CUBE_MAP_ARB", 0x2078)
    set_enum("WGL_TEXTURE_1D_ARB", 0x2079)
    set_enum("WGL_TEXTURE_2D_ARB", 0x207A)
    set_enum("WGL_MIPMAP_LEVEL_ARB", 0x207B)
    set_enum("WGL_CUBE_MAP_FACE_ARB", 0x207C)
    set_enum("WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB", 0x207D)
    set_enum("WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB", 0x207E)
    set_enum("WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB", 0x207F)
    set_enum("WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB", 0x2080)
    set_enum("WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB", 0x2081)
    set_enum("WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB", 0x2082)
    set_enum("WGL_FRONT_LEFT_ARB", 0x2083)
    set_enum("WGL_FRONT_RIGHT_ARB", 0x2084)
    set_enum("WGL_BACK_LEFT_ARB", 0x2085)
    set_enum("WGL_BACK_RIGHT_ARB", 0x2086)
    set_enum("WGL_AUX0_ARB", 0x2087)
    set_enum("WGL_AUX1_ARB", 0x2088)
    set_enum("WGL_AUX2_ARB", 0x2089)
    set_enum("WGL_AUX3_ARB", 0x208A)
    set_enum("WGL_AUX4_ARB", 0x208B)
    set_enum("WGL_AUX5_ARB", 0x208C)
    set_enum("WGL_AUX6_ARB", 0x208D)
    set_enum("WGL_AUX7_ARB", 0x208E)
    set_enum("WGL_AUX8_ARB", 0x208F)
    set_enum("WGL_AUX9_ARB", 0x2090)


#### WGL VERSION 1.0 ####
def init_wgl_arb_robustness_application_isolation():
    set_enum("WGL_CONTEXT_RESET_ISOLATION_BIT_ARB", 0x00000008)


#### WGL VERSION 1.0 ####
def init_wgl_arb_robustness_share_group_isolation():
    set_enum("WGL_CONTEXT_RESET_ISOLATION_BIT_ARB", 0x00000008)


#### WGL VERSION 1.0 ####
def init_wgl_ati_pixel_format_float():
    set_enum("WGL_TYPE_RGBA_FLOAT_ATI", 0x21A0)


#### WGL VERSION 1.0 ####
def init_wgl_ext_create_context_es_profile():
    set_enum("WGL_CONTEXT_ES_PROFILE_BIT_EXT", 0x00000004)


#### WGL VERSION 1.0 ####
def init_wgl_ext_create_context_es2_profile():
    set_enum("WGL_CONTEXT_ES2_PROFILE_BIT_EXT", 0x00000004)


#### WGL VERSION 1.0 ####
def init_wgl_ext_depth_float():
    set_enum("WGL_DEPTH_FLOAT_EXT", 0x2040)


#### WGL VERSION 1.0 ####
def init_wgl_ext_display_color_table():
    set_func('wglCreateDisplayColorTableEXT', t.GLboolean, (t.GLushort,))
    set_func('wglLoadDisplayColorTableEXT', t.GLboolean, (ct.POINTER(t.GLushort), t.GLuint))
    set_func('wglBindDisplayColorTableEXT', t.GLboolean, (t.GLushort,))
#     set_func('wglDestroyDisplayColorTableEXT', t.VOID, (t.GLushort,))


#### WGL VERSION 1.0 ####
def init_wgl_ext_extensions_string():
#     set_func('wglGetExtensionsStringEXT', ct.POINTER(t.char), ())


#### WGL VERSION 1.0 ####
def init_wgl_ext_framebuffer_srgb():
    set_enum("WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT", 0x20A9)


#### WGL VERSION 1.0 ####
def init_wgl_ext_make_current_read():
#     set_func('wglMakeContextCurrentEXT', t.BOOL, (t.HDC, t.HDC, t.HGLRC))
#     set_func('wglGetCurrentReadDCEXT', t.HDC, ())
    set_enum("ERROR_INVALID_PIXEL_TYPE_EXT", 0x2043)


#### WGL VERSION 1.0 ####
def init_wgl_ext_multisample():
    set_enum("WGL_SAMPLE_BUFFERS_EXT", 0x2041)
    set_enum("WGL_SAMPLES_EXT", 0x2042)


#### WGL VERSION 1.0 ####
def init_wgl_ext_pbuffer():
#     set_func('wglCreatePbufferEXT', t.HPBUFFEREXT, (t.HDC, t.int, t.int, t.int, ct.POINTER(t.int)))
#     set_func('wglGetPbufferDCEXT', t.HDC, (t.HPBUFFEREXT,))
#     set_func('wglReleasePbufferDCEXT', t.int, (t.HPBUFFEREXT, t.HDC))
#     set_func('wglDestroyPbufferEXT', t.BOOL, (t.HPBUFFEREXT,))
#     set_func('wglQueryPbufferEXT', t.BOOL, (t.HPBUFFEREXT, t.int, ct.POINTER(t.int)))
    set_enum("WGL_DRAW_TO_PBUFFER_EXT", 0x202D)
    set_enum("WGL_MAX_PBUFFER_PIXELS_EXT", 0x202E)
    set_enum("WGL_MAX_PBUFFER_WIDTH_EXT", 0x202F)
    set_enum("WGL_MAX_PBUFFER_HEIGHT_EXT", 0x2030)
    set_enum("WGL_OPTIMAL_PBUFFER_WIDTH_EXT", 0x2031)
    set_enum("WGL_OPTIMAL_PBUFFER_HEIGHT_EXT", 0x2032)
    set_enum("WGL_PBUFFER_LARGEST_EXT", 0x2033)
    set_enum("WGL_PBUFFER_WIDTH_EXT", 0x2034)
    set_enum("WGL_PBUFFER_HEIGHT_EXT", 0x2035)


#### WGL VERSION 1.0 ####
def init_wgl_ext_pixel_format():
#     set_func('wglGetPixelFormatAttribivEXT', t.BOOL, (t.HDC, t.int, t.int, t.UINT, ct.POINTER(t.int), ct.POINTER(t.int)))
#     set_func('wglGetPixelFormatAttribfvEXT', t.BOOL, (t.HDC, t.int, t.int, t.UINT, ct.POINTER(t.int), ct.POINTER(t.FLOAT)))
#     set_func('wglChoosePixelFormatEXT', t.BOOL, (t.HDC, ct.POINTER(t.int), ct.POINTER(t.FLOAT), t.UINT, ct.POINTER(t.int), ct.POINTER(t.UINT)))
    set_enum("WGL_NUMBER_PIXEL_FORMATS_EXT", 0x2000)
    set_enum("WGL_DRAW_TO_WINDOW_EXT", 0x2001)
    set_enum("WGL_DRAW_TO_BITMAP_EXT", 0x2002)
    set_enum("WGL_ACCELERATION_EXT", 0x2003)
    set_enum("WGL_NEED_PALETTE_EXT", 0x2004)
    set_enum("WGL_NEED_SYSTEM_PALETTE_EXT", 0x2005)
    set_enum("WGL_SWAP_LAYER_BUFFERS_EXT", 0x2006)
    set_enum("WGL_SWAP_METHOD_EXT", 0x2007)
    set_enum("WGL_NUMBER_OVERLAYS_EXT", 0x2008)
    set_enum("WGL_NUMBER_UNDERLAYS_EXT", 0x2009)
    set_enum("WGL_TRANSPARENT_EXT", 0x200A)
    set_enum("WGL_TRANSPARENT_VALUE_EXT", 0x200B)
    set_enum("WGL_SHARE_DEPTH_EXT", 0x200C)
    set_enum("WGL_SHARE_STENCIL_EXT", 0x200D)
    set_enum("WGL_SHARE_ACCUM_EXT", 0x200E)
    set_enum("WGL_SUPPORT_GDI_EXT", 0x200F)
    set_enum("WGL_SUPPORT_OPENGL_EXT", 0x2010)
    set_enum("WGL_DOUBLE_BUFFER_EXT", 0x2011)
    set_enum("WGL_STEREO_EXT", 0x2012)
    set_enum("WGL_PIXEL_TYPE_EXT", 0x2013)
    set_enum("WGL_COLOR_BITS_EXT", 0x2014)
    set_enum("WGL_RED_BITS_EXT", 0x2015)
    set_enum("WGL_RED_SHIFT_EXT", 0x2016)
    set_enum("WGL_GREEN_BITS_EXT", 0x2017)
    set_enum("WGL_GREEN_SHIFT_EXT", 0x2018)
    set_enum("WGL_BLUE_BITS_EXT", 0x2019)
    set_enum("WGL_BLUE_SHIFT_EXT", 0x201A)
    set_enum("WGL_ALPHA_BITS_EXT", 0x201B)
    set_enum("WGL_ALPHA_SHIFT_EXT", 0x201C)
    set_enum("WGL_ACCUM_BITS_EXT", 0x201D)
    set_enum("WGL_ACCUM_RED_BITS_EXT", 0x201E)
    set_enum("WGL_ACCUM_GREEN_BITS_EXT", 0x201F)
    set_enum("WGL_ACCUM_BLUE_BITS_EXT", 0x2020)
    set_enum("WGL_ACCUM_ALPHA_BITS_EXT", 0x2021)
    set_enum("WGL_DEPTH_BITS_EXT", 0x2022)
    set_enum("WGL_STENCIL_BITS_EXT", 0x2023)
    set_enum("WGL_AUX_BUFFERS_EXT", 0x2024)
    set_enum("WGL_NO_ACCELERATION_EXT", 0x2025)
    set_enum("WGL_GENERIC_ACCELERATION_EXT", 0x2026)
    set_enum("WGL_FULL_ACCELERATION_EXT", 0x2027)
    set_enum("WGL_SWAP_EXCHANGE_EXT", 0x2028)
    set_enum("WGL_SWAP_COPY_EXT", 0x2029)
    set_enum("WGL_SWAP_UNDEFINED_EXT", 0x202A)
    set_enum("WGL_TYPE_RGBA_EXT", 0x202B)
    set_enum("WGL_TYPE_COLORINDEX_EXT", 0x202C)


#### WGL VERSION 1.0 ####
def init_wgl_ext_pixel_format_packed_float():
    set_enum("WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT", 0x20A8)


#### WGL VERSION 1.0 ####
def init_wgl_ext_swap_control():
#     set_func('wglSwapIntervalEXT', t.BOOL, (t.int,))
#     set_func('wglGetSwapIntervalEXT', t.int, ())


#### WGL VERSION 1.0 ####
def init_wgl_i3d_digital_video_control():
#     set_func('wglGetDigitalVideoParametersI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.int)))
#     set_func('wglSetDigitalVideoParametersI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.int)))
    set_enum("WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D", 0x2050)
    set_enum("WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D", 0x2051)
    set_enum("WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D", 0x2052)
    set_enum("WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D", 0x2053)


#### WGL VERSION 1.0 ####
def init_wgl_i3d_gamma():
#     set_func('wglGetGammaTableParametersI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.int)))
#     set_func('wglSetGammaTableParametersI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.int)))
#     set_func('wglGetGammaTableI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.USHORT), ct.POINTER(t.USHORT), ct.POINTER(t.USHORT)))
#     set_func('wglSetGammaTableI3D', t.BOOL, (t.HDC, t.int, ct.POINTER(t.USHORT), ct.POINTER(t.USHORT), ct.POINTER(t.USHORT)))
    set_enum("WGL_GAMMA_TABLE_SIZE_I3D", 0x204E)
    set_enum("WGL_GAMMA_EXCLUDE_DESKTOP_I3D", 0x204F)


#### WGL VERSION 1.0 ####
def init_wgl_i3d_genlock():
#     set_func('wglEnableGenlockI3D', t.BOOL, (t.HDC,))
#     set_func('wglDisableGenlockI3D', t.BOOL, (t.HDC,))
#     set_func('wglIsEnabledGenlockI3D', t.BOOL, (t.HDC, ct.POINTER(t.BOOL)))
#     set_func('wglGenlockSourceI3D', t.BOOL, (t.HDC, t.UINT))
#     set_func('wglGetGenlockSourceI3D', t.BOOL, (t.HDC, ct.POINTER(t.UINT)))
#     set_func('wglGenlockSourceEdgeI3D', t.BOOL, (t.HDC, t.UINT))
#     set_func('wglGetGenlockSourceEdgeI3D', t.BOOL, (t.HDC, ct.POINTER(t.UINT)))
#     set_func('wglGenlockSampleRateI3D', t.BOOL, (t.HDC, t.UINT))
#     set_func('wglGetGenlockSampleRateI3D', t.BOOL, (t.HDC, ct.POINTER(t.UINT)))
#     set_func('wglGenlockSourceDelayI3D', t.BOOL, (t.HDC, t.UINT))
#     set_func('wglGetGenlockSourceDelayI3D', t.BOOL, (t.HDC, ct.POINTER(t.UINT)))
#     set_func('wglQueryGenlockMaxSourceDelayI3D', t.BOOL, (t.HDC, ct.POINTER(t.UINT), ct.POINTER(t.UINT)))
    set_enum("WGL_GENLOCK_SOURCE_MULTIVIEW_I3D", 0x2044)
    set_enum("WGL_GENLOCK_SOURCE_EXTERNAL_SYNC_I3D", 0x2045)
    set_enum("WGL_GENLOCK_SOURCE_EXTERNAL_FIELD_I3D", 0x2046)
    set_enum("WGL_GENLOCK_SOURCE_EXTERNAL_TTL_I3D", 0x2047)
    set_enum("WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D", 0x2048)
    set_enum("WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D", 0x2049)
    set_enum("WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D", 0x204A)
    set_enum("WGL_GENLOCK_SOURCE_EDGE_RISING_I3D", 0x204B)
    set_enum("WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D", 0x204C)


#### WGL VERSION 1.0 ####
def init_wgl_i3d_image_buffer():
#     set_func('wglCreateImageBufferI3D', t.LPVOID, (t.HDC, t.DWORD, t.UINT))
#     set_func('wglDestroyImageBufferI3D', t.BOOL, (t.HDC, t.LPVOID))
#     set_func('wglAssociateImageBufferEventsI3D', t.BOOL, (t.HDC, ct.POINTER(t.HANDLE), ct.POINTER(t.LPVOID), ct.POINTER(t.DWORD), t.UINT))
#     set_func('wglReleaseImageBufferEventsI3D', t.BOOL, (t.HDC, ct.POINTER(t.LPVOID), t.UINT))
    set_enum("WGL_IMAGE_BUFFER_MIN_ACCESS_I3D", 0x00000001)
    set_enum("WGL_IMAGE_BUFFER_LOCK_I3D", 0x00000002)


#### WGL VERSION 1.0 ####
def init_wgl_i3d_swap_frame_lock():
#     set_func('wglEnableFrameLockI3D', t.BOOL, ())
#     set_func('wglDisableFrameLockI3D', t.BOOL, ())
#     set_func('wglIsEnabledFrameLockI3D', t.BOOL, (ct.POINTER(t.BOOL),))
#     set_func('wglQueryFrameLockMasterI3D', t.BOOL, (ct.POINTER(t.BOOL),))


#### WGL VERSION 1.0 ####
def init_wgl_i3d_swap_frame_usage():
#     set_func('wglGetFrameUsageI3D', t.BOOL, (ct.POINTER(t.float),))
#     set_func('wglBeginFrameTrackingI3D', t.BOOL, ())
#     set_func('wglEndFrameTrackingI3D', t.BOOL, ())
#     set_func('wglQueryFrameTrackingI3D', t.BOOL, (ct.POINTER(t.DWORD), ct.POINTER(t.DWORD), ct.POINTER(t.float)))


#### WGL VERSION 1.0 ####
def init_wgl_nv_copy_image():
#     set_func('wglCopyImageSubDataNV', t.BOOL, (t.HGLRC, t.GLuint, t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.HGLRC, t.GLuint, t.GLenum, t.GLint, t.GLint, t.GLint, t.GLint, t.GLsizei, t.GLsizei, t.GLsizei))


#### WGL VERSION 1.0 ####
def init_wgl_nv_delay_before_swap():
#     set_func('wglDelayBeforeSwapNV', t.BOOL, (t.HDC, t.GLfloat))


#### WGL VERSION 1.0 ####
def init_wgl_nv_dx_interop():
#     set_func('wglDXSetResourceShareHandleNV', t.BOOL, (ct.POINTER(t.void), t.HANDLE))
#     set_func('wglDXOpenDeviceNV', t.HANDLE, (ct.POINTER(t.void),))
#     set_func('wglDXCloseDeviceNV', t.BOOL, (t.HANDLE,))
#     set_func('wglDXRegisterObjectNV', t.HANDLE, (t.HANDLE, ct.POINTER(t.void), t.GLuint, t.GLenum, t.GLenum))
#     set_func('wglDXUnregisterObjectNV', t.BOOL, (t.HANDLE, t.HANDLE))
#     set_func('wglDXObjectAccessNV', t.BOOL, (t.HANDLE, t.GLenum))
#     set_func('wglDXLockObjectsNV', t.BOOL, (t.HANDLE, t.GLint, ct.POINTER(t.HANDLE)))
#     set_func('wglDXUnlockObjectsNV', t.BOOL, (t.HANDLE, t.GLint, ct.POINTER(t.HANDLE)))
    set_enum("WGL_ACCESS_READ_ONLY_NV", 0x00000000)
    set_enum("WGL_ACCESS_READ_WRITE_NV", 0x00000001)
    set_enum("WGL_ACCESS_WRITE_DISCARD_NV", 0x00000002)


#### WGL VERSION 1.0 ####
def init_wgl_nv_float_buffer():
    set_enum("WGL_FLOAT_COMPONENTS_NV", 0x20B0)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV", 0x20B1)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV", 0x20B2)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV", 0x20B3)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV", 0x20B4)
    set_enum("WGL_TEXTURE_FLOAT_R_NV", 0x20B5)
    set_enum("WGL_TEXTURE_FLOAT_RG_NV", 0x20B6)
    set_enum("WGL_TEXTURE_FLOAT_RGB_NV", 0x20B7)
    set_enum("WGL_TEXTURE_FLOAT_RGBA_NV", 0x20B8)


#### WGL VERSION 1.0 ####
def init_wgl_nv_gpu_affinity():
#     set_func('wglEnumGpusNV', t.BOOL, (t.UINT, ct.POINTER(t.HGPUNV)))
#     set_func('wglEnumGpuDevicesNV', t.BOOL, (t.HGPUNV, t.UINT, t.PGPU_DEVICE))
#     set_func('wglCreateAffinityDCNV', t.HDC, (ct.POINTER(t.HGPUNV),))
#     set_func('wglEnumGpusFromAffinityDCNV', t.BOOL, (t.HDC, t.UINT, ct.POINTER(t.HGPUNV)))
#     set_func('wglDeleteDCNV', t.BOOL, (t.HDC,))
    set_enum("ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV", 0x20D0)
    set_enum("ERROR_MISSING_AFFINITY_MASK_NV", 0x20D1)


#### WGL VERSION 1.0 ####
def init_wgl_nv_multisample_coverage():
    set_enum("WGL_COVERAGE_SAMPLES_NV", 0x2042)
    set_enum("WGL_COLOR_SAMPLES_NV", 0x20B9)


#### WGL VERSION 1.0 ####
def init_wgl_nv_present_video():
#     set_func('wglEnumerateVideoDevicesNV', t.int, (t.HDC, ct.POINTER(t.HVIDEOOUTPUTDEVICENV)))
#     set_func('wglBindVideoDeviceNV', t.BOOL, (t.HDC, t.unsigned int, t.HVIDEOOUTPUTDEVICENV, ct.POINTER(t.int)))
#     set_func('wglQueryCurrentContextNV', t.BOOL, (t.int, ct.POINTER(t.int)))
    set_enum("WGL_NUM_VIDEO_SLOTS_NV", 0x20F0)


#### WGL VERSION 1.0 ####
def init_wgl_nv_render_depth_texture():
    set_enum("WGL_BIND_TO_TEXTURE_DEPTH_NV", 0x20A3)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV", 0x20A4)
    set_enum("WGL_DEPTH_TEXTURE_FORMAT_NV", 0x20A5)
    set_enum("WGL_TEXTURE_DEPTH_COMPONENT_NV", 0x20A6)
    set_enum("WGL_DEPTH_COMPONENT_NV", 0x20A7)


#### WGL VERSION 1.0 ####
def init_wgl_nv_render_texture_rectangle():
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV", 0x20A0)
    set_enum("WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV", 0x20A1)
    set_enum("WGL_TEXTURE_RECTANGLE_NV", 0x20A2)


#### WGL VERSION 1.0 ####
def init_wgl_nv_swap_group():
#     set_func('wglJoinSwapGroupNV', t.BOOL, (t.HDC, t.GLuint))
#     set_func('wglBindSwapBarrierNV', t.BOOL, (t.GLuint, t.GLuint))
#     set_func('wglQuerySwapGroupNV', t.BOOL, (t.HDC, ct.POINTER(t.GLuint), ct.POINTER(t.GLuint)))
#     set_func('wglQueryMaxSwapGroupsNV', t.BOOL, (t.HDC, ct.POINTER(t.GLuint), ct.POINTER(t.GLuint)))
#     set_func('wglQueryFrameCountNV', t.BOOL, (t.HDC, ct.POINTER(t.GLuint)))
#     set_func('wglResetFrameCountNV', t.BOOL, (t.HDC,))


#### WGL VERSION 1.0 ####
def init_wgl_nv_video_capture():
#     set_func('wglBindVideoCaptureDeviceNV', t.BOOL, (t.UINT, t.HVIDEOINPUTDEVICENV))
#     set_func('wglEnumerateVideoCaptureDevicesNV', t.UINT, (t.HDC, ct.POINTER(t.HVIDEOINPUTDEVICENV)))
#     set_func('wglLockVideoCaptureDeviceNV', t.BOOL, (t.HDC, t.HVIDEOINPUTDEVICENV))
#     set_func('wglQueryVideoCaptureDeviceNV', t.BOOL, (t.HDC, t.HVIDEOINPUTDEVICENV, t.int, ct.POINTER(t.int)))
#     set_func('wglReleaseVideoCaptureDeviceNV', t.BOOL, (t.HDC, t.HVIDEOINPUTDEVICENV))
    set_enum("WGL_UNIQUE_ID_NV", 0x20CE)
    set_enum("WGL_NUM_VIDEO_CAPTURE_SLOTS_NV", 0x20CF)


#### WGL VERSION 1.0 ####
def init_wgl_nv_video_output():
#     set_func('wglGetVideoDeviceNV', t.BOOL, (t.HDC, t.int, ct.POINTER(t.HPVIDEODEV)))
#     set_func('wglReleaseVideoDeviceNV', t.BOOL, (t.HPVIDEODEV,))
#     set_func('wglBindVideoImageNV', t.BOOL, (t.HPVIDEODEV, t.HPBUFFERARB, t.int))
#     set_func('wglReleaseVideoImageNV', t.BOOL, (t.HPBUFFERARB, t.int))
#     set_func('wglSendPbufferToVideoNV', t.BOOL, (t.HPBUFFERARB, t.int, ct.POINTER(t.unsigned), t.BOOL))
#     set_func('wglGetVideoInfoNV', t.BOOL, (t.HPVIDEODEV, ct.POINTER(t.unsigned), ct.POINTER(t.unsigned)))
    set_enum("WGL_BIND_TO_VIDEO_RGB_NV", 0x20C0)
    set_enum("WGL_BIND_TO_VIDEO_RGBA_NV", 0x20C1)
    set_enum("WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV", 0x20C2)
    set_enum("WGL_VIDEO_OUT_COLOR_NV", 0x20C3)
    set_enum("WGL_VIDEO_OUT_ALPHA_NV", 0x20C4)
    set_enum("WGL_VIDEO_OUT_DEPTH_NV", 0x20C5)
    set_enum("WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV", 0x20C6)
    set_enum("WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV", 0x20C7)
    set_enum("WGL_VIDEO_OUT_FRAME", 0x20C8)
    set_enum("WGL_VIDEO_OUT_FIELD_1", 0x20C9)
    set_enum("WGL_VIDEO_OUT_FIELD_2", 0x20CA)
    set_enum("WGL_VIDEO_OUT_STACKED_FIELDS_1_2", 0x20CB)
    set_enum("WGL_VIDEO_OUT_STACKED_FIELDS_2_1", 0x20CC)


#### WGL VERSION 1.0 ####
def init_wgl_nv_vertex_array_range():
    set_func('wglAllocateMemoryNV', ct.POINTER(t.void), (t.GLsizei, t.GLfloat, t.GLfloat, t.GLfloat))
    set_func('wglFreeMemoryNV', t.void, (ct.POINTER(t.void),))


#### WGL VERSION 1.0 ####
def init_wgl_oml_sync_control():
#     set_func('wglGetSyncValuesOML', t.BOOL, (t.HDC, ct.POINTER(t.INT64), ct.POINTER(t.INT64), ct.POINTER(t.INT64)))
#     set_func('wglGetMscRateOML', t.BOOL, (t.HDC, ct.POINTER(t.INT32), ct.POINTER(t.INT32)))
#     set_func('wglSwapBuffersMscOML', t.INT64, (t.HDC, t.INT64, t.INT64, t.INT64))
#     set_func('wglSwapLayerBuffersMscOML', t.INT64, (t.HDC, t.int, t.INT64, t.INT64, t.INT64))
#     set_func('wglWaitForMscOML', t.BOOL, (t.HDC, t.INT64, t.INT64, t.INT64, ct.POINTER(t.INT64), ct.POINTER(t.INT64), ct.POINTER(t.INT64)))
#     set_func('wglWaitForSbcOML', t.BOOL, (t.HDC, t.INT64, ct.POINTER(t.INT64), ct.POINTER(t.INT64), ct.POINTER(t.INT64)))


def init():
    init_wgl_version_1_0()
    init_wgl_3dfx_multisample()
    init_wgl_3dl_stereo_control()
    init_wgl_amd_gpu_association()
    init_wgl_arb_buffer_region()
    init_wgl_arb_context_flush_control()
    init_wgl_arb_create_context()
    init_wgl_arb_create_context_profile()
    init_wgl_arb_create_context_robustness()
    init_wgl_arb_extensions_string()
    init_wgl_arb_framebuffer_srgb()
    init_wgl_arb_make_current_read()
    init_wgl_arb_multisample()
    init_wgl_arb_pbuffer()
    init_wgl_arb_pixel_format()
    init_wgl_arb_pixel_format_float()
    init_wgl_arb_render_texture()
    init_wgl_arb_robustness_application_isolation()
    init_wgl_arb_robustness_share_group_isolation()
    init_wgl_ati_pixel_format_float()
    init_wgl_ext_create_context_es_profile()
    init_wgl_ext_create_context_es2_profile()
    init_wgl_ext_depth_float()
    init_wgl_ext_display_color_table()
    init_wgl_ext_extensions_string()
    init_wgl_ext_framebuffer_srgb()
    init_wgl_ext_make_current_read()
    init_wgl_ext_multisample()
    init_wgl_ext_pbuffer()
    init_wgl_ext_pixel_format()
    init_wgl_ext_pixel_format_packed_float()
    init_wgl_ext_swap_control()
    init_wgl_i3d_digital_video_control()
    init_wgl_i3d_gamma()
    init_wgl_i3d_genlock()
    init_wgl_i3d_image_buffer()
    init_wgl_i3d_swap_frame_lock()
    init_wgl_i3d_swap_frame_usage()
    init_wgl_nv_copy_image()
    init_wgl_nv_delay_before_swap()
    init_wgl_nv_dx_interop()
    init_wgl_nv_float_buffer()
    init_wgl_nv_gpu_affinity()
    init_wgl_nv_multisample_coverage()
    init_wgl_nv_present_video()
    init_wgl_nv_render_depth_texture()
    init_wgl_nv_render_texture_rectangle()
    init_wgl_nv_swap_group()
    init_wgl_nv_video_capture()
    init_wgl_nv_video_output()
    init_wgl_nv_vertex_array_range()
    init_wgl_oml_sync_control()

