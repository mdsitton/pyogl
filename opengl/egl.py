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

#### EGL VERSION 1.0 ####
def init_egl_version_1_0():
    # set_func('eglChooseConfig', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLint), ct.POINTER(t.EGLConfig), t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglCopyBuffers', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLNativePixmapType))
    # set_func('eglCreateContext', t.EGLContext, (t.EGLDisplay, t.EGLConfig, t.EGLContext, ct.POINTER(t.EGLint)))
    # set_func('eglCreatePbufferSurface', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.EGLint)))
    # set_func('eglCreatePixmapSurface', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, t.EGLNativePixmapType, ct.POINTER(t.EGLint)))
    # set_func('eglCreateWindowSurface', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, t.EGLNativeWindowType, ct.POINTER(t.EGLint)))
    # set_func('eglDestroyContext', t.EGLBoolean, (t.EGLDisplay, t.EGLContext))
    # set_func('eglDestroySurface', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface))
    # set_func('eglGetConfigAttrib', t.EGLBoolean, (t.EGLDisplay, t.EGLConfig, t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglGetConfigs', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLConfig), t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglGetCurrentDisplay', t.EGLDisplay, ())
    # set_func('eglGetCurrentSurface', t.EGLSurface, (t.EGLint,))
    # set_func('eglGetDisplay', t.EGLDisplay, (t.EGLNativeDisplayType,))
    # set_func('eglGetError', t.EGLint, ())
    # set_func('eglGetProcAddress', t.__eglMustCastToProperFunctionPointerType, (ct.POINTER(t.CHAR),))
    # set_func('eglInitialize', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLint), ct.POINTER(t.EGLint)))
    # set_func('eglMakeCurrent', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLSurface, t.EGLContext))
    # set_func('eglQueryContext', t.EGLBoolean, (t.EGLDisplay, t.EGLContext, t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglQueryString', ct.POINTER(t.CHAR), (t.EGLDisplay, t.EGLint))
    # set_func('eglQuerySurface', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglSwapBuffers', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface))
    # set_func('eglTerminate', t.EGLBoolean, (t.EGLDisplay,))
    # set_func('eglWaitGL', t.EGLBoolean, ())
    # set_func('eglWaitNative', t.EGLBoolean, (t.EGLint,))
    set_enum("EGL_ALPHA_SIZE", 0x3021)
    set_enum("EGL_BAD_ACCESS", 0x3002)
    set_enum("EGL_BAD_ALLOC", 0x3003)
    set_enum("EGL_BAD_ATTRIBUTE", 0x3004)
    set_enum("EGL_BAD_CONFIG", 0x3005)
    set_enum("EGL_BAD_CONTEXT", 0x3006)
    set_enum("EGL_BAD_CURRENT_SURFACE", 0x3007)
    set_enum("EGL_BAD_DISPLAY", 0x3008)
    set_enum("EGL_BAD_MATCH", 0x3009)
    set_enum("EGL_BAD_NATIVE_PIXMAP", 0x300A)
    set_enum("EGL_BAD_NATIVE_WINDOW", 0x300B)
    set_enum("EGL_BAD_PARAMETER", 0x300C)
    set_enum("EGL_BAD_SURFACE", 0x300D)
    set_enum("EGL_BLUE_SIZE", 0x3022)
    set_enum("EGL_BUFFER_SIZE", 0x3020)
    set_enum("EGL_CONFIG_CAVEAT", 0x3027)
    set_enum("EGL_CONFIG_ID", 0x3028)
    set_enum("EGL_CORE_NATIVE_ENGINE", 0x305B)
    set_enum("EGL_DEPTH_SIZE", 0x3025)
#     set_enum("EGL_DONT_CARE", ((EGLint)-1))
    set_enum("EGL_DRAW", 0x3059)
    set_enum("EGL_EXTENSIONS", 0x3055)
    set_enum("EGL_FALSE", 0)
    set_enum("EGL_GREEN_SIZE", 0x3023)
    set_enum("EGL_HEIGHT", 0x3056)
    set_enum("EGL_LARGEST_PBUFFER", 0x3058)
    set_enum("EGL_LEVEL", 0x3029)
    set_enum("EGL_MAX_PBUFFER_HEIGHT", 0x302A)
    set_enum("EGL_MAX_PBUFFER_PIXELS", 0x302B)
    set_enum("EGL_MAX_PBUFFER_WIDTH", 0x302C)
    set_enum("EGL_NATIVE_RENDERABLE", 0x302D)
    set_enum("EGL_NATIVE_VISUAL_ID", 0x302E)
    set_enum("EGL_NATIVE_VISUAL_TYPE", 0x302F)
    set_enum("EGL_NONE", 0x3038)
    set_enum("EGL_NON_CONFORMANT_CONFIG", 0x3051)
    set_enum("EGL_NOT_INITIALIZED", 0x3001)
#     set_enum("EGL_NO_CONTEXT", ((EGLContext)0))
#     set_enum("EGL_NO_DISPLAY", ((EGLDisplay)0))
#     set_enum("EGL_NO_SURFACE", ((EGLSurface)0))
    set_enum("EGL_PBUFFER_BIT", 0x0001)
    set_enum("EGL_PIXMAP_BIT", 0x0002)
    set_enum("EGL_READ", 0x305A)
    set_enum("EGL_RED_SIZE", 0x3024)
    set_enum("EGL_SAMPLES", 0x3031)
    set_enum("EGL_SAMPLE_BUFFERS", 0x3032)
    set_enum("EGL_SLOW_CONFIG", 0x3050)
    set_enum("EGL_STENCIL_SIZE", 0x3026)
    set_enum("EGL_SUCCESS", 0x3000)
    set_enum("EGL_SURFACE_TYPE", 0x3033)
    set_enum("EGL_TRANSPARENT_BLUE_VALUE", 0x3035)
    set_enum("EGL_TRANSPARENT_GREEN_VALUE", 0x3036)
    set_enum("EGL_TRANSPARENT_RED_VALUE", 0x3037)
    set_enum("EGL_TRANSPARENT_RGB", 0x3052)
    set_enum("EGL_TRANSPARENT_TYPE", 0x3034)
    set_enum("EGL_TRUE", 1)
    set_enum("EGL_VENDOR", 0x3053)
    set_enum("EGL_VERSION", 0x3054)
    set_enum("EGL_WIDTH", 0x3057)
    set_enum("EGL_WINDOW_BIT", 0x0004)


#### EGL VERSION 1.1 ####
def init_egl_version_1_1():
    # set_func('eglBindTexImage', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint))
    # set_func('eglReleaseTexImage', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint))
    # set_func('eglSurfaceAttrib', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, t.EGLint))
    # set_func('eglSwapInterval', t.EGLBoolean, (t.EGLDisplay, t.EGLint))
    set_enum("EGL_BACK_BUFFER", 0x3084)
    set_enum("EGL_BIND_TO_TEXTURE_RGB", 0x3039)
    set_enum("EGL_BIND_TO_TEXTURE_RGBA", 0x303A)
    set_enum("EGL_CONTEXT_LOST", 0x300E)
    set_enum("EGL_MIN_SWAP_INTERVAL", 0x303B)
    set_enum("EGL_MAX_SWAP_INTERVAL", 0x303C)
    set_enum("EGL_MIPMAP_TEXTURE", 0x3082)
    set_enum("EGL_MIPMAP_LEVEL", 0x3083)
    set_enum("EGL_NO_TEXTURE", 0x305C)
    set_enum("EGL_TEXTURE_2D", 0x305F)
    set_enum("EGL_TEXTURE_FORMAT", 0x3080)
    set_enum("EGL_TEXTURE_RGB", 0x305D)
    set_enum("EGL_TEXTURE_RGBA", 0x305E)
    set_enum("EGL_TEXTURE_TARGET", 0x3081)


#### EGL VERSION 1.2 ####
def init_egl_version_1_2():
    # set_func('eglBindAPI', t.EGLBoolean, (t.EGLenum,))
    # set_func('eglQueryAPI', t.EGLenum, ())
    # set_func('eglCreatePbufferFromClientBuffer', t.EGLSurface, (t.EGLDisplay, t.EGLenum, t.EGLClientBuffer, t.EGLConfig, ct.POINTER(t.EGLint)))
    # set_func('eglReleaseThread', t.EGLBoolean, ())
    # set_func('eglWaitClient', t.EGLBoolean, ())
    set_enum("EGL_ALPHA_FORMAT", 0x3088)
    set_enum("EGL_ALPHA_FORMAT_NONPRE", 0x308B)
    set_enum("EGL_ALPHA_FORMAT_PRE", 0x308C)
    set_enum("EGL_ALPHA_MASK_SIZE", 0x303E)
    set_enum("EGL_BUFFER_PRESERVED", 0x3094)
    set_enum("EGL_BUFFER_DESTROYED", 0x3095)
    set_enum("EGL_CLIENT_APIS", 0x308D)
    set_enum("EGL_COLORSPACE", 0x3087)
    set_enum("EGL_COLORSPACE_sRGB", 0x3089)
    set_enum("EGL_COLORSPACE_LINEAR", 0x308A)
    set_enum("EGL_COLOR_BUFFER_TYPE", 0x303F)
    set_enum("EGL_CONTEXT_CLIENT_TYPE", 0x3097)
    set_enum("EGL_DISPLAY_SCALING", 10000)
    set_enum("EGL_HORIZONTAL_RESOLUTION", 0x3090)
    set_enum("EGL_LUMINANCE_BUFFER", 0x308F)
    set_enum("EGL_LUMINANCE_SIZE", 0x303D)
    set_enum("EGL_OPENGL_ES_BIT", 0x0001)
    set_enum("EGL_OPENVG_BIT", 0x0002)
    set_enum("EGL_OPENGL_ES_API", 0x30A0)
    set_enum("EGL_OPENVG_API", 0x30A1)
    set_enum("EGL_OPENVG_IMAGE", 0x3096)
    set_enum("EGL_PIXEL_ASPECT_RATIO", 0x3092)
    set_enum("EGL_RENDERABLE_TYPE", 0x3040)
    set_enum("EGL_RENDER_BUFFER", 0x3086)
    set_enum("EGL_RGB_BUFFER", 0x308E)
    set_enum("EGL_SINGLE_BUFFER", 0x3085)
    set_enum("EGL_SWAP_BEHAVIOR", 0x3093)
#     set_enum("EGL_UNKNOWN", ((EGLint)-1))
    set_enum("EGL_VERTICAL_RESOLUTION", 0x3091)


#### EGL VERSION 1.3 ####
def init_egl_version_1_3():
    set_enum("EGL_CONFORMANT", 0x3042)
    set_enum("EGL_CONTEXT_CLIENT_VERSION", 0x3098)
    set_enum("EGL_MATCH_NATIVE_PIXMAP", 0x3041)
    set_enum("EGL_OPENGL_ES2_BIT", 0x0004)
    set_enum("EGL_VG_ALPHA_FORMAT", 0x3088)
    set_enum("EGL_VG_ALPHA_FORMAT_NONPRE", 0x308B)
    set_enum("EGL_VG_ALPHA_FORMAT_PRE", 0x308C)
    set_enum("EGL_VG_ALPHA_FORMAT_PRE_BIT", 0x0040)
    set_enum("EGL_VG_COLORSPACE", 0x3087)
    set_enum("EGL_VG_COLORSPACE_sRGB", 0x3089)
    set_enum("EGL_VG_COLORSPACE_LINEAR", 0x308A)
    set_enum("EGL_VG_COLORSPACE_LINEAR_BIT", 0x0020)


#### EGL VERSION 1.4 ####
def init_egl_version_1_4():
    # set_func('eglGetCurrentContext', t.EGLContext, ())
#     set_enum("EGL_DEFAULT_DISPLAY", ((EGLNativeDisplayType)0))
    set_enum("EGL_MULTISAMPLE_RESOLVE_BOX_BIT", 0x0200)
    set_enum("EGL_MULTISAMPLE_RESOLVE", 0x3099)
    set_enum("EGL_MULTISAMPLE_RESOLVE_DEFAULT", 0x309A)
    set_enum("EGL_MULTISAMPLE_RESOLVE_BOX", 0x309B)
    set_enum("EGL_OPENGL_API", 0x30A2)
    set_enum("EGL_OPENGL_BIT", 0x0008)
    set_enum("EGL_SWAP_BEHAVIOR_PRESERVED_BIT", 0x0400)


#### EGL VERSION 1.5 ####
def init_egl_version_1_5():
    # set_func('eglCreateSync', t.EGLSync, (t.EGLDisplay, t.EGLenum, ct.POINTER(t.EGLAttrib)))
    # set_func('eglDestroySync', t.EGLBoolean, (t.EGLDisplay, t.EGLSync))
    # set_func('eglClientWaitSync', t.EGLint, (t.EGLDisplay, t.EGLSync, t.EGLint, t.EGLTime))
    # set_func('eglGetSyncAttrib', t.EGLBoolean, (t.EGLDisplay, t.EGLSync, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglCreateImage', t.EGLImage, (t.EGLDisplay, t.EGLContext, t.EGLenum, t.EGLClientBuffer, ct.POINTER(t.EGLAttrib)))
    # set_func('eglDestroyImage', t.EGLBoolean, (t.EGLDisplay, t.EGLImage))
    # set_func('eglGetPlatformDisplay', t.EGLDisplay, (t.EGLenum, ct.POINTER(t.void), ct.POINTER(t.EGLAttrib)))
    # set_func('eglCreatePlatformWindowSurface', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.void), ct.POINTER(t.EGLAttrib)))
    # set_func('eglCreatePlatformPixmapSurface', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.void), ct.POINTER(t.EGLAttrib)))
    # set_func('eglWaitSync', t.EGLBoolean, (t.EGLDisplay, t.EGLSync, t.EGLint))
    set_enum("EGL_CONTEXT_MAJOR_VERSION", 0x3098)
    set_enum("EGL_CONTEXT_MINOR_VERSION", 0x30FB)
    set_enum("EGL_CONTEXT_OPENGL_PROFILE_MASK", 0x30FD)
    set_enum("EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY", 0x31BD)
    set_enum("EGL_NO_RESET_NOTIFICATION", 0x31BE)
    set_enum("EGL_LOSE_CONTEXT_ON_RESET", 0x31BF)
    set_enum("EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT", 0x00000001)
    set_enum("EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT", 0x00000002)
    set_enum("EGL_CONTEXT_OPENGL_DEBUG", 0x31B0)
    set_enum("EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE", 0x31B1)
    set_enum("EGL_CONTEXT_OPENGL_ROBUST_ACCESS", 0x31B2)
    set_enum("EGL_OPENGL_ES3_BIT", 0x00000040)
    set_enum("EGL_CL_EVENT_HANDLE", 0x309C)
    set_enum("EGL_SYNC_CL_EVENT", 0x30FE)
    set_enum("EGL_SYNC_CL_EVENT_COMPLETE", 0x30FF)
    set_enum("EGL_SYNC_PRIOR_COMMANDS_COMPLETE", 0x30F0)
    set_enum("EGL_SYNC_TYPE", 0x30F7)
    set_enum("EGL_SYNC_STATUS", 0x30F1)
    set_enum("EGL_SYNC_CONDITION", 0x30F8)
    set_enum("EGL_SIGNALED", 0x30F2)
    set_enum("EGL_UNSIGNALED", 0x30F3)
    set_enum("EGL_SYNC_FLUSH_COMMANDS_BIT", 0x0001)
    set_enum("EGL_FOREVER", 0xFFFFFFFFFFFFFFFF)
    set_enum("EGL_TIMEOUT_EXPIRED", 0x30F5)
    set_enum("EGL_CONDITION_SATISFIED", 0x30F6)
#     set_enum("EGL_NO_SYNC", ((EGLSync)0))
    set_enum("EGL_SYNC_FENCE", 0x30F9)
    set_enum("EGL_GL_COLORSPACE", 0x309D)
    set_enum("EGL_GL_COLORSPACE_SRGB", 0x3089)
    set_enum("EGL_GL_COLORSPACE_LINEAR", 0x308A)
    set_enum("EGL_GL_RENDERBUFFER", 0x30B9)
    set_enum("EGL_GL_TEXTURE_2D", 0x30B1)
    set_enum("EGL_GL_TEXTURE_LEVEL", 0x30BC)
    set_enum("EGL_GL_TEXTURE_3D", 0x30B2)
    set_enum("EGL_GL_TEXTURE_ZOFFSET", 0x30BD)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X", 0x30B3)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X", 0x30B4)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y", 0x30B5)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y", 0x30B6)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z", 0x30B7)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z", 0x30B8)
    set_enum("EGL_IMAGE_PRESERVED", 0x30D2)
#     set_enum("EGL_NO_IMAGE", ((EGLImage)0))


#### EGL_ANDROID_BLOB_CACHE ####
def init_egl_android_blob_cache():
    # set_func('eglSetBlobCacheFuncsANDROID', t.void, (t.EGLDisplay, t.EGLSetBlobFuncANDROID, t.EGLGetBlobFuncANDROID))
    pass

#### EGL_ANDROID_FRAMEBUFFER_TARGET ####
def init_egl_android_framebuffer_target():
    set_enum("EGL_FRAMEBUFFER_TARGET_ANDROID", 0x3147)


#### EGL_ANDROID_IMAGE_NATIVE_BUFFER ####
def init_egl_android_image_native_buffer():
    set_enum("EGL_NATIVE_BUFFER_ANDROID", 0x3140)


#### EGL_ANDROID_NATIVE_FENCE_SYNC ####
def init_egl_android_native_fence_sync():
    # set_func('eglDupNativeFenceFDANDROID', t.EGLint, (t.EGLDisplay, t.EGLSyncKHR))
    set_enum("EGL_SYNC_NATIVE_FENCE_ANDROID", 0x3144)
    set_enum("EGL_SYNC_NATIVE_FENCE_FD_ANDROID", 0x3145)
    set_enum("EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID", 0x3146)
    set_enum("EGL_NO_NATIVE_FENCE_FD_ANDROID", -1)


#### EGL_ANDROID_RECORDABLE ####
def init_egl_android_recordable():
    set_enum("EGL_RECORDABLE_ANDROID", 0x3142)


#### EGL_ANGLE_D3D_SHARE_HANDLE_CLIENT_BUFFER ####
def init_egl_angle_d3d_share_handle_client_buffer():
    set_enum("EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE", 0x3200)


#### EGL_ANGLE_DEVICE_D3D ####
def init_egl_angle_device_d3d():
    set_enum("EGL_D3D9_DEVICE_ANGLE", 0x33A0)
    set_enum("EGL_D3D11_DEVICE_ANGLE", 0x33A1)


#### EGL_ANGLE_QUERY_SURFACE_POINTER ####
def init_egl_angle_query_surface_pointer():
    # set_func('eglQuerySurfacePointerANGLE', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, ct.POINTER(ct.POINTER(t.void))))
    pass

#### EGL_ANGLE_SURFACE_D3D_TEXTURE_2D_SHARE_HANDLE ####
def init_egl_angle_surface_d3d_texture_2d_share_handle():
    set_enum("EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE", 0x3200)


#### EGL_ANGLE_WINDOW_FIXED_SIZE ####
def init_egl_angle_window_fixed_size():
    set_enum("EGL_FIXED_SIZE_ANGLE", 0x3201)


#### EGL_ARM_PIXMAP_MULTISAMPLE_DISCARD ####
def init_egl_arm_pixmap_multisample_discard():
    set_enum("EGL_DISCARD_SAMPLES_ARM", 0x3286)


#### EGL_EXT_BUFFER_AGE ####
def init_egl_ext_buffer_age():
    set_enum("EGL_BUFFER_AGE_EXT", 0x313D)


#### EGL_EXT_CREATE_CONTEXT_ROBUSTNESS ####
def init_egl_ext_create_context_robustness():
    set_enum("EGL_CONTEXT_OPENGL_ROBUST_ACCESS_EXT", 0x30BF)
    set_enum("EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_EXT", 0x3138)
    set_enum("EGL_NO_RESET_NOTIFICATION_EXT", 0x31BE)
    set_enum("EGL_LOSE_CONTEXT_ON_RESET_EXT", 0x31BF)


#### EGL_EXT_DEVICE_BASE ####
def init_egl_ext_device_base():
    # set_func('eglQueryDeviceAttribEXT', t.EGLBoolean, (t.EGLDeviceEXT, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglQueryDeviceStringEXT', ct.POINTER(t.CHAR), (t.EGLDeviceEXT, t.EGLint))
    # set_func('eglQueryDevicesEXT', t.EGLBoolean, (t.EGLint, ct.POINTER(t.EGLDeviceEXT), ct.POINTER(t.EGLint)))
    # set_func('eglQueryDisplayAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLint, ct.POINTER(t.EGLAttrib)))
#     set_enum("EGL_NO_DEVICE_EXT", ((EGLDeviceEXT)(0)))
    set_enum("EGL_BAD_DEVICE_EXT", 0x322B)
    set_enum("EGL_DEVICE_EXT", 0x322C)


#### EGL_EXT_DEVICE_DRM ####
def init_egl_ext_device_drm():
    set_enum("EGL_DRM_DEVICE_FILE_EXT", 0x3233)


#### EGL_EXT_DEVICE_ENUMERATION ####
def init_egl_ext_device_enumeration():
    # set_func('eglQueryDevicesEXT', t.EGLBoolean, (t.EGLint, ct.POINTER(t.EGLDeviceEXT), ct.POINTER(t.EGLint)))
    pass

#### EGL_EXT_DEVICE_OPENWF ####
def init_egl_ext_device_openwf():
    set_enum("EGL_OPENWF_DEVICE_ID_EXT", 0x3237)


#### EGL_EXT_DEVICE_QUERY ####
def init_egl_ext_device_query():
    # set_func('eglQueryDeviceAttribEXT', t.EGLBoolean, (t.EGLDeviceEXT, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglQueryDeviceStringEXT', ct.POINTER(t.CHAR), (t.EGLDeviceEXT, t.EGLint))
    # set_func('eglQueryDisplayAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLint, ct.POINTER(t.EGLAttrib)))
#     set_enum("EGL_NO_DEVICE_EXT", ((EGLDeviceEXT)(0)))
    set_enum("EGL_BAD_DEVICE_EXT", 0x322B)
    set_enum("EGL_DEVICE_EXT", 0x322C)


#### EGL_EXT_IMAGE_DMA_BUF_IMPORT ####
def init_egl_ext_image_dma_buf_import():
    set_enum("EGL_LINUX_DMA_BUF_EXT", 0x3270)
    set_enum("EGL_LINUX_DRM_FOURCC_EXT", 0x3271)
    set_enum("EGL_DMA_BUF_PLANE0_FD_EXT", 0x3272)
    set_enum("EGL_DMA_BUF_PLANE0_OFFSET_EXT", 0x3273)
    set_enum("EGL_DMA_BUF_PLANE0_PITCH_EXT", 0x3274)
    set_enum("EGL_DMA_BUF_PLANE1_FD_EXT", 0x3275)
    set_enum("EGL_DMA_BUF_PLANE1_OFFSET_EXT", 0x3276)
    set_enum("EGL_DMA_BUF_PLANE1_PITCH_EXT", 0x3277)
    set_enum("EGL_DMA_BUF_PLANE2_FD_EXT", 0x3278)
    set_enum("EGL_DMA_BUF_PLANE2_OFFSET_EXT", 0x3279)
    set_enum("EGL_DMA_BUF_PLANE2_PITCH_EXT", 0x327A)
    set_enum("EGL_YUV_COLOR_SPACE_HINT_EXT", 0x327B)
    set_enum("EGL_SAMPLE_RANGE_HINT_EXT", 0x327C)
    set_enum("EGL_YUV_CHROMA_HORIZONTAL_SITING_HINT_EXT", 0x327D)
    set_enum("EGL_YUV_CHROMA_VERTICAL_SITING_HINT_EXT", 0x327E)
    set_enum("EGL_ITU_REC601_EXT", 0x327F)
    set_enum("EGL_ITU_REC709_EXT", 0x3280)
    set_enum("EGL_ITU_REC2020_EXT", 0x3281)
    set_enum("EGL_YUV_FULL_RANGE_EXT", 0x3282)
    set_enum("EGL_YUV_NARROW_RANGE_EXT", 0x3283)
    set_enum("EGL_YUV_CHROMA_SITING_0_EXT", 0x3284)
    set_enum("EGL_YUV_CHROMA_SITING_0_5_EXT", 0x3285)


#### EGL_EXT_MULTIVIEW_WINDOW ####
def init_egl_ext_multiview_window():
    set_enum("EGL_MULTIVIEW_VIEW_COUNT_EXT", 0x3134)


#### EGL_EXT_OUTPUT_BASE ####
def init_egl_ext_output_base():
    # set_func('eglGetOutputLayersEXT', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLAttrib), ct.POINTER(t.EGLOutputLayerEXT), t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglGetOutputPortsEXT', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLAttrib), ct.POINTER(t.EGLOutputPortEXT), t.EGLint, ct.POINTER(t.EGLint)))
    # set_func('eglOutputLayerAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLOutputLayerEXT, t.EGLint, t.EGLAttrib))
    # set_func('eglQueryOutputLayerAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLOutputLayerEXT, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglQueryOutputLayerStringEXT', ct.POINTER(t.CHAR), (t.EGLDisplay, t.EGLOutputLayerEXT, t.EGLint))
    # set_func('eglOutputPortAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLOutputPortEXT, t.EGLint, t.EGLAttrib))
    # set_func('eglQueryOutputPortAttribEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLOutputPortEXT, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglQueryOutputPortStringEXT', ct.POINTER(t.CHAR), (t.EGLDisplay, t.EGLOutputPortEXT, t.EGLint))
#     set_enum("EGL_NO_OUTPUT_LAYER_EXT", ((EGLOutputLayerEXT)0))
#     set_enum("EGL_NO_OUTPUT_PORT_EXT", ((EGLOutputPortEXT)0))
    set_enum("EGL_BAD_OUTPUT_LAYER_EXT", 0x322D)
    set_enum("EGL_BAD_OUTPUT_PORT_EXT", 0x322E)
    set_enum("EGL_SWAP_INTERVAL_EXT", 0x322F)


#### EGL_EXT_OUTPUT_DRM ####
def init_egl_ext_output_drm():
    set_enum("EGL_DRM_CRTC_EXT", 0x3234)
    set_enum("EGL_DRM_PLANE_EXT", 0x3235)
    set_enum("EGL_DRM_CONNECTOR_EXT", 0x3236)


#### EGL_EXT_OUTPUT_OPENWF ####
def init_egl_ext_output_openwf():
    set_enum("EGL_OPENWF_PIPELINE_ID_EXT", 0x3238)
    set_enum("EGL_OPENWF_PORT_ID_EXT", 0x3239)


#### EGL_EXT_PLATFORM_BASE ####
def init_egl_ext_platform_base():
    # set_func('eglGetPlatformDisplayEXT', t.EGLDisplay, (t.EGLenum, ct.POINTER(t.void), ct.POINTER(t.EGLint)))
    # set_func('eglCreatePlatformWindowSurfaceEXT', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.void), ct.POINTER(t.EGLint)))
    # set_func('eglCreatePlatformPixmapSurfaceEXT', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.void), ct.POINTER(t.EGLint)))
    pass

#### EGL_EXT_PLATFORM_DEVICE ####
def init_egl_ext_platform_device():
    set_enum("EGL_PLATFORM_DEVICE_EXT", 0x313F)


#### EGL_EXT_PLATFORM_WAYLAND ####
def init_egl_ext_platform_wayland():
    set_enum("EGL_PLATFORM_WAYLAND_EXT", 0x31D8)


#### EGL_EXT_PLATFORM_X11 ####
def init_egl_ext_platform_x11():
    set_enum("EGL_PLATFORM_X11_EXT", 0x31D5)
    set_enum("EGL_PLATFORM_X11_SCREEN_EXT", 0x31D6)


#### EGL_EXT_PROTECTED_CONTENT ####
def init_egl_ext_protected_content():
    set_enum("EGL_PROTECTED_CONTENT_EXT", 0x32C0)


#### EGL_EXT_PROTECTED_SURFACE ####
def init_egl_ext_protected_surface():
    set_enum("EGL_PROTECTED_CONTENT_EXT", 0x32C0)


#### EGL_EXT_STREAM_CONSUMER_EGLOUTPUT ####
def init_egl_ext_stream_consumer_egloutput():
    # set_func('eglStreamConsumerOutputEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLOutputLayerEXT))
    pass

#### EGL_EXT_SWAP_BUFFERS_WITH_DAMAGE ####
def init_egl_ext_swap_buffers_with_damage():
    # set_func('eglSwapBuffersWithDamageEXT', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLint), t.EGLint))
    pass

#### EGL_EXT_YUV_SURFACE ####
def init_egl_ext_yuv_surface():
    set_enum("EGL_YUV_ORDER_EXT", 0x3301)
    set_enum("EGL_YUV_NUMBER_OF_PLANES_EXT", 0x3311)
    set_enum("EGL_YUV_SUBSAMPLE_EXT", 0x3312)
    set_enum("EGL_YUV_DEPTH_RANGE_EXT", 0x3317)
    set_enum("EGL_YUV_CSC_STANDARD_EXT", 0x330A)
    set_enum("EGL_YUV_PLANE_BPP_EXT", 0x331A)
    set_enum("EGL_YUV_BUFFER_EXT", 0x3300)
    set_enum("EGL_YUV_ORDER_YUV_EXT", 0x3302)
    set_enum("EGL_YUV_ORDER_YVU_EXT", 0x3303)
    set_enum("EGL_YUV_ORDER_YUYV_EXT", 0x3304)
    set_enum("EGL_YUV_ORDER_UYVY_EXT", 0x3305)
    set_enum("EGL_YUV_ORDER_YVYU_EXT", 0x3306)
    set_enum("EGL_YUV_ORDER_VYUY_EXT", 0x3307)
    set_enum("EGL_YUV_ORDER_AYUV_EXT", 0x3308)
    set_enum("EGL_YUV_SUBSAMPLE_4_2_0_EXT", 0x3313)
    set_enum("EGL_YUV_SUBSAMPLE_4_2_2_EXT", 0x3314)
    set_enum("EGL_YUV_SUBSAMPLE_4_4_4_EXT", 0x3315)
    set_enum("EGL_YUV_DEPTH_RANGE_LIMITED_EXT", 0x3318)
    set_enum("EGL_YUV_DEPTH_RANGE_FULL_EXT", 0x3319)
    set_enum("EGL_YUV_CSC_STANDARD_601_EXT", 0x330B)
    set_enum("EGL_YUV_CSC_STANDARD_709_EXT", 0x330C)
    set_enum("EGL_YUV_CSC_STANDARD_2020_EXT", 0x330D)
    set_enum("EGL_YUV_PLANE_BPP_0_EXT", 0x331B)
    set_enum("EGL_YUV_PLANE_BPP_8_EXT", 0x331C)
    set_enum("EGL_YUV_PLANE_BPP_10_EXT", 0x331D)


#### EGL_HI_CLIENTPIXMAP ####
def init_egl_hi_clientpixmap():
    # set_func('eglCreatePixmapSurfaceHI', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, ct.POINTER(t.struct)))
    set_enum("EGL_CLIENT_PIXMAP_POINTER_HI", 0x8F74)


#### EGL_HI_COLORFORMATS ####
def init_egl_hi_colorformats():
    set_enum("EGL_COLOR_FORMAT_HI", 0x8F70)
    set_enum("EGL_COLOR_RGB_HI", 0x8F71)
    set_enum("EGL_COLOR_RGBA_HI", 0x8F72)
    set_enum("EGL_COLOR_ARGB_HI", 0x8F73)


#### EGL_IMG_CONTEXT_PRIORITY ####
def init_egl_img_context_priority():
    set_enum("EGL_CONTEXT_PRIORITY_LEVEL_IMG", 0x3100)
    set_enum("EGL_CONTEXT_PRIORITY_HIGH_IMG", 0x3101)
    set_enum("EGL_CONTEXT_PRIORITY_MEDIUM_IMG", 0x3102)
    set_enum("EGL_CONTEXT_PRIORITY_LOW_IMG", 0x3103)


#### EGL_IMG_IMAGE_PLANE_ATTRIBS ####
def init_egl_img_image_plane_attribs():
    set_enum("EGL_NATIVE_BUFFER_MULTIPLANE_SEPARATE_IMG", 0x3105)
    set_enum("EGL_NATIVE_BUFFER_PLANE_OFFSET_IMG", 0x3106)


#### EGL_KHR_CL_EVENT ####
def init_egl_khr_cl_event():
    set_enum("EGL_CL_EVENT_HANDLE_KHR", 0x309C)
    set_enum("EGL_SYNC_CL_EVENT_KHR", 0x30FE)
    set_enum("EGL_SYNC_CL_EVENT_COMPLETE_KHR", 0x30FF)


#### EGL_KHR_CL_EVENT2 ####
def init_egl_khr_cl_event2():
    # set_func('eglCreateSync64KHR', t.EGLSyncKHR, (t.EGLDisplay, t.EGLenum, ct.POINTER(t.EGLAttribKHR)))
    set_enum("EGL_CL_EVENT_HANDLE_KHR", 0x309C)
    set_enum("EGL_SYNC_CL_EVENT_KHR", 0x30FE)
    set_enum("EGL_SYNC_CL_EVENT_COMPLETE_KHR", 0x30FF)


#### EGL_KHR_CONFIG_ATTRIBS ####
def init_egl_khr_config_attribs():
    set_enum("EGL_CONFORMANT_KHR", 0x3042)
    set_enum("EGL_VG_COLORSPACE_LINEAR_BIT_KHR", 0x0020)
    set_enum("EGL_VG_ALPHA_FORMAT_PRE_BIT_KHR", 0x0040)


#### EGL_KHR_CREATE_CONTEXT ####
def init_egl_khr_create_context():
    set_enum("EGL_CONTEXT_MAJOR_VERSION_KHR", 0x3098)
    set_enum("EGL_CONTEXT_MINOR_VERSION_KHR", 0x30FB)
    set_enum("EGL_CONTEXT_FLAGS_KHR", 0x30FC)
    set_enum("EGL_CONTEXT_OPENGL_PROFILE_MASK_KHR", 0x30FD)
    set_enum("EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_KHR", 0x31BD)
    set_enum("EGL_NO_RESET_NOTIFICATION_KHR", 0x31BE)
    set_enum("EGL_LOSE_CONTEXT_ON_RESET_KHR", 0x31BF)
    set_enum("EGL_CONTEXT_OPENGL_DEBUG_BIT_KHR", 0x00000001)
    set_enum("EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE_BIT_KHR", 0x00000002)
    set_enum("EGL_CONTEXT_OPENGL_ROBUST_ACCESS_BIT_KHR", 0x00000004)
    set_enum("EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT_KHR", 0x00000001)
    set_enum("EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT_KHR", 0x00000002)
    set_enum("EGL_OPENGL_ES3_BIT", 0x00000040)
    set_enum("EGL_OPENGL_ES3_BIT_KHR", 0x00000040)


#### EGL_KHR_CREATE_CONTEXT_NO_ERROR ####
def init_egl_khr_create_context_no_error():
    set_enum("EGL_CONTEXT_OPENGL_NO_ERROR_KHR", 0x31B3)


#### EGL_KHR_DEBUG ####
def init_egl_khr_debug():
    # set_func('eglDebugMessageControlKHR', t.EGLint, (t.EGLDEBUGPROCKHR, ct.POINTER(t.EGLAttrib)))
    # set_func('eglQueryDebugKHR', t.EGLBoolean, (t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglLabelObjectKHR', t.EGLint, (t.EGLDisplay, t.EGLenum, t.EGLObjectKHR, t.EGLLabelKHR))
    set_enum("EGL_OBJECT_THREAD_KHR", 0x33B0)
    set_enum("EGL_OBJECT_DISPLAY_KHR", 0x33B1)
    set_enum("EGL_OBJECT_CONTEXT_KHR", 0x33B2)
    set_enum("EGL_OBJECT_SURFACE_KHR", 0x33B3)
    set_enum("EGL_OBJECT_IMAGE_KHR", 0x33B4)
    set_enum("EGL_OBJECT_SYNC_KHR", 0x33B5)
    set_enum("EGL_OBJECT_STREAM_KHR", 0x33B6)
    set_enum("EGL_DEBUG_MSG_CRITICAL_KHR", 0x33B9)
    set_enum("EGL_DEBUG_MSG_ERROR_KHR", 0x33BA)
    set_enum("EGL_DEBUG_MSG_WARN_KHR", 0x33BB)
    set_enum("EGL_DEBUG_MSG_INFO_KHR", 0x33BC)
    set_enum("EGL_DEBUG_CALLBACK_KHR", 0x33B8)


#### EGL_KHR_FENCE_SYNC ####
def init_egl_khr_fence_sync():
    # set_func('eglCreateSyncKHR', t.EGLSyncKHR, (t.EGLDisplay, t.EGLenum, ct.POINTER(t.EGLint)))
    # set_func('eglDestroySyncKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSyncKHR))
    # set_func('eglClientWaitSyncKHR', t.EGLint, (t.EGLDisplay, t.EGLSyncKHR, t.EGLint, t.EGLTimeKHR))
    # set_func('eglGetSyncAttribKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSyncKHR, t.EGLint, ct.POINTER(t.EGLint)))
    set_enum("EGL_SYNC_PRIOR_COMMANDS_COMPLETE_KHR", 0x30F0)
    set_enum("EGL_SYNC_CONDITION_KHR", 0x30F8)
    set_enum("EGL_SYNC_FENCE_KHR", 0x30F9)


#### EGL_KHR_GL_COLORSPACE ####
def init_egl_khr_gl_colorspace():
    set_enum("EGL_GL_COLORSPACE_KHR", 0x309D)
    set_enum("EGL_GL_COLORSPACE_SRGB_KHR", 0x3089)
    set_enum("EGL_GL_COLORSPACE_LINEAR_KHR", 0x308A)


#### EGL_KHR_GL_RENDERBUFFER_IMAGE ####
def init_egl_khr_gl_renderbuffer_image():
    set_enum("EGL_GL_RENDERBUFFER_KHR", 0x30B9)


#### EGL_KHR_GL_TEXTURE_2D_IMAGE ####
def init_egl_khr_gl_texture_2d_image():
    set_enum("EGL_GL_TEXTURE_2D_KHR", 0x30B1)
    set_enum("EGL_GL_TEXTURE_LEVEL_KHR", 0x30BC)


#### EGL_KHR_GL_TEXTURE_3D_IMAGE ####
def init_egl_khr_gl_texture_3d_image():
    set_enum("EGL_GL_TEXTURE_3D_KHR", 0x30B2)
    set_enum("EGL_GL_TEXTURE_ZOFFSET_KHR", 0x30BD)


#### EGL_KHR_GL_TEXTURE_CUBEMAP_IMAGE ####
def init_egl_khr_gl_texture_cubemap_image():
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X_KHR", 0x30B3)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X_KHR", 0x30B4)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y_KHR", 0x30B5)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_KHR", 0x30B6)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z_KHR", 0x30B7)
    set_enum("EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_KHR", 0x30B8)


#### EGL_KHR_IMAGE ####
def init_egl_khr_image():
    # set_func('eglCreateImageKHR', t.EGLImageKHR, (t.EGLDisplay, t.EGLContext, t.EGLenum, t.EGLClientBuffer, ct.POINTER(t.EGLint)))
    # set_func('eglDestroyImageKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLImageKHR))
    set_enum("EGL_NATIVE_PIXMAP_KHR", 0x30B0)
#     set_enum("EGL_NO_IMAGE_KHR", ((EGLImageKHR)0))


#### EGL_KHR_IMAGE_BASE ####
def init_egl_khr_image_base():
    # set_func('eglCreateImageKHR', t.EGLImageKHR, (t.EGLDisplay, t.EGLContext, t.EGLenum, t.EGLClientBuffer, ct.POINTER(t.EGLint)))
    # set_func('eglDestroyImageKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLImageKHR))
    set_enum("EGL_IMAGE_PRESERVED_KHR", 0x30D2)
#     set_enum("EGL_NO_IMAGE_KHR", ((EGLImageKHR)0))


#### EGL_KHR_IMAGE_PIXMAP ####
def init_egl_khr_image_pixmap():
    set_enum("EGL_NATIVE_PIXMAP_KHR", 0x30B0)


#### EGL_KHR_LOCK_SURFACE ####
def init_egl_khr_lock_surface():
    # set_func('eglLockSurfaceKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLint)))
    # set_func('eglUnlockSurfaceKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface))
    set_enum("EGL_READ_SURFACE_BIT_KHR", 0x0001)
    set_enum("EGL_WRITE_SURFACE_BIT_KHR", 0x0002)
    set_enum("EGL_LOCK_SURFACE_BIT_KHR", 0x0080)
    set_enum("EGL_OPTIMAL_FORMAT_BIT_KHR", 0x0100)
    set_enum("EGL_MATCH_FORMAT_KHR", 0x3043)
    set_enum("EGL_FORMAT_RGB_565_EXACT_KHR", 0x30C0)
    set_enum("EGL_FORMAT_RGB_565_KHR", 0x30C1)
    set_enum("EGL_FORMAT_RGBA_8888_EXACT_KHR", 0x30C2)
    set_enum("EGL_FORMAT_RGBA_8888_KHR", 0x30C3)
    set_enum("EGL_MAP_PRESERVE_PIXELS_KHR", 0x30C4)
    set_enum("EGL_LOCK_USAGE_HINT_KHR", 0x30C5)
    set_enum("EGL_BITMAP_POINTER_KHR", 0x30C6)
    set_enum("EGL_BITMAP_PITCH_KHR", 0x30C7)
    set_enum("EGL_BITMAP_ORIGIN_KHR", 0x30C8)
    set_enum("EGL_BITMAP_PIXEL_RED_OFFSET_KHR", 0x30C9)
    set_enum("EGL_BITMAP_PIXEL_GREEN_OFFSET_KHR", 0x30CA)
    set_enum("EGL_BITMAP_PIXEL_BLUE_OFFSET_KHR", 0x30CB)
    set_enum("EGL_BITMAP_PIXEL_ALPHA_OFFSET_KHR", 0x30CC)
    set_enum("EGL_BITMAP_PIXEL_LUMINANCE_OFFSET_KHR", 0x30CD)
    set_enum("EGL_LOWER_LEFT_KHR", 0x30CE)
    set_enum("EGL_UPPER_LEFT_KHR", 0x30CF)


#### EGL_KHR_LOCK_SURFACE2 ####
def init_egl_khr_lock_surface2():
    set_enum("EGL_BITMAP_PIXEL_SIZE_KHR", 0x3110)


#### EGL_KHR_LOCK_SURFACE3 ####
def init_egl_khr_lock_surface3():
    # set_func('eglLockSurfaceKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLint)))
    # set_func('eglUnlockSurfaceKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface))
    # set_func('eglQuerySurface64KHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, ct.POINTER(t.EGLAttribKHR)))
    set_enum("EGL_READ_SURFACE_BIT_KHR", 0x0001)
    set_enum("EGL_WRITE_SURFACE_BIT_KHR", 0x0002)
    set_enum("EGL_LOCK_SURFACE_BIT_KHR", 0x0080)
    set_enum("EGL_OPTIMAL_FORMAT_BIT_KHR", 0x0100)
    set_enum("EGL_MATCH_FORMAT_KHR", 0x3043)
    set_enum("EGL_FORMAT_RGB_565_EXACT_KHR", 0x30C0)
    set_enum("EGL_FORMAT_RGB_565_KHR", 0x30C1)
    set_enum("EGL_FORMAT_RGBA_8888_EXACT_KHR", 0x30C2)
    set_enum("EGL_FORMAT_RGBA_8888_KHR", 0x30C3)
    set_enum("EGL_MAP_PRESERVE_PIXELS_KHR", 0x30C4)
    set_enum("EGL_LOCK_USAGE_HINT_KHR", 0x30C5)
    set_enum("EGL_BITMAP_PITCH_KHR", 0x30C7)
    set_enum("EGL_BITMAP_ORIGIN_KHR", 0x30C8)
    set_enum("EGL_BITMAP_PIXEL_RED_OFFSET_KHR", 0x30C9)
    set_enum("EGL_BITMAP_PIXEL_GREEN_OFFSET_KHR", 0x30CA)
    set_enum("EGL_BITMAP_PIXEL_BLUE_OFFSET_KHR", 0x30CB)
    set_enum("EGL_BITMAP_PIXEL_ALPHA_OFFSET_KHR", 0x30CC)
    set_enum("EGL_BITMAP_PIXEL_LUMINANCE_OFFSET_KHR", 0x30CD)
    set_enum("EGL_BITMAP_PIXEL_SIZE_KHR", 0x3110)
    set_enum("EGL_BITMAP_POINTER_KHR", 0x30C6)
    set_enum("EGL_LOWER_LEFT_KHR", 0x30CE)
    set_enum("EGL_UPPER_LEFT_KHR", 0x30CF)


#### EGL_KHR_MUTABLE_RENDER_BUFFER ####
def init_egl_khr_mutable_render_buffer():
    set_enum("EGL_MUTABLE_RENDER_BUFFER_BIT_KHR", 0x1000)


#### EGL_KHR_PARTIAL_UPDATE ####
def init_egl_khr_partial_update():
    # set_func('eglSetDamageRegionKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLint), t.EGLint))
    set_enum("EGL_BUFFER_AGE_KHR", 0x313D)


#### EGL_KHR_PLATFORM_ANDROID ####
def init_egl_khr_platform_android():
    set_enum("EGL_PLATFORM_ANDROID_KHR", 0x3141)


#### EGL_KHR_PLATFORM_GBM ####
def init_egl_khr_platform_gbm():
    set_enum("EGL_PLATFORM_GBM_KHR", 0x31D7)


#### EGL_KHR_PLATFORM_WAYLAND ####
def init_egl_khr_platform_wayland():
    set_enum("EGL_PLATFORM_WAYLAND_KHR", 0x31D8)


#### EGL_KHR_PLATFORM_X11 ####
def init_egl_khr_platform_x11():
    set_enum("EGL_PLATFORM_X11_KHR", 0x31D5)
    set_enum("EGL_PLATFORM_X11_SCREEN_KHR", 0x31D6)


#### EGL_KHR_REUSABLE_SYNC ####
def init_egl_khr_reusable_sync():
    # set_func('eglCreateSyncKHR', t.EGLSyncKHR, (t.EGLDisplay, t.EGLenum, ct.POINTER(t.EGLint)))
    # set_func('eglDestroySyncKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSyncKHR))
    # set_func('eglClientWaitSyncKHR', t.EGLint, (t.EGLDisplay, t.EGLSyncKHR, t.EGLint, t.EGLTimeKHR))
    # set_func('eglSignalSyncKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSyncKHR, t.EGLenum))
    # set_func('eglGetSyncAttribKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSyncKHR, t.EGLint, ct.POINTER(t.EGLint)))
    set_enum("EGL_SYNC_STATUS_KHR", 0x30F1)
    set_enum("EGL_SIGNALED_KHR", 0x30F2)
    set_enum("EGL_UNSIGNALED_KHR", 0x30F3)
    set_enum("EGL_TIMEOUT_EXPIRED_KHR", 0x30F5)
    set_enum("EGL_CONDITION_SATISFIED_KHR", 0x30F6)
    set_enum("EGL_SYNC_TYPE_KHR", 0x30F7)
    set_enum("EGL_SYNC_REUSABLE_KHR", 0x30FA)
    set_enum("EGL_SYNC_FLUSH_COMMANDS_BIT_KHR", 0x0001)
    set_enum("EGL_FOREVER_KHR", 0xFFFFFFFFFFFFFFFF)
#     set_enum("EGL_NO_SYNC_KHR", ((EGLSyncKHR)0))


#### EGL_KHR_STREAM ####
def init_egl_khr_stream():
    # set_func('eglCreateStreamKHR', t.EGLStreamKHR, (t.EGLDisplay, ct.POINTER(t.EGLint)))
    # set_func('eglDestroyStreamKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR))
    # set_func('eglStreamAttribKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, t.EGLint))
    # set_func('eglQueryStreamKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, ct.POINTER(t.EGLint)))
    # set_func('eglQueryStreamu64KHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, ct.POINTER(t.EGLuint64KHR)))
#     set_enum("EGL_NO_STREAM_KHR", ((EGLStreamKHR)0))
    set_enum("EGL_CONSUMER_LATENCY_USEC_KHR", 0x3210)
    set_enum("EGL_PRODUCER_FRAME_KHR", 0x3212)
    set_enum("EGL_CONSUMER_FRAME_KHR", 0x3213)
    set_enum("EGL_STREAM_STATE_KHR", 0x3214)
    set_enum("EGL_STREAM_STATE_CREATED_KHR", 0x3215)
    set_enum("EGL_STREAM_STATE_CONNECTING_KHR", 0x3216)
    set_enum("EGL_STREAM_STATE_EMPTY_KHR", 0x3217)
    set_enum("EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR", 0x3218)
    set_enum("EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR", 0x3219)
    set_enum("EGL_STREAM_STATE_DISCONNECTED_KHR", 0x321A)
    set_enum("EGL_BAD_STREAM_KHR", 0x321B)
    set_enum("EGL_BAD_STATE_KHR", 0x321C)


#### EGL_KHR_STREAM_CONSUMER_GLTEXTURE ####
def init_egl_khr_stream_consumer_gltexture():
    # set_func('eglStreamConsumerGLTextureExternalKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR))
    # set_func('eglStreamConsumerAcquireKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR))
    # set_func('eglStreamConsumerReleaseKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR))
    set_enum("EGL_CONSUMER_ACQUIRE_TIMEOUT_USEC_KHR", 0x321E)


#### EGL_KHR_STREAM_CROSS_PROCESS_FD ####
def init_egl_khr_stream_cross_process_fd():
    # set_func('eglGetStreamFileDescriptorKHR', t.EGLNativeFileDescriptorKHR, (t.EGLDisplay, t.EGLStreamKHR))
    # set_func('eglCreateStreamFromFileDescriptorKHR', t.EGLStreamKHR, (t.EGLDisplay, t.EGLNativeFileDescriptorKHR))
#     set_enum("EGL_NO_FILE_DESCRIPTOR_KHR", ((EGLNativeFileDescriptorKHR)(-1)))
    pass

#### EGL_KHR_STREAM_FIFO ####
def init_egl_khr_stream_fifo():
    # set_func('eglQueryStreamTimeKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, ct.POINTER(t.EGLTimeKHR)))
    set_enum("EGL_STREAM_FIFO_LENGTH_KHR", 0x31FC)
    set_enum("EGL_STREAM_TIME_NOW_KHR", 0x31FD)
    set_enum("EGL_STREAM_TIME_CONSUMER_KHR", 0x31FE)
    set_enum("EGL_STREAM_TIME_PRODUCER_KHR", 0x31FF)


#### EGL_KHR_STREAM_PRODUCER_EGLSURFACE ####
def init_egl_khr_stream_producer_eglsurface():
    # set_func('eglCreateStreamProducerSurfaceKHR', t.EGLSurface, (t.EGLDisplay, t.EGLConfig, t.EGLStreamKHR, ct.POINTER(t.EGLint)))
    set_enum("EGL_STREAM_BIT_KHR", 0x0800)


#### EGL_KHR_SWAP_BUFFERS_WITH_DAMAGE ####
def init_egl_khr_swap_buffers_with_damage():
    # set_func('eglSwapBuffersWithDamageKHR', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLint), t.EGLint))
    pass

#### EGL_KHR_VG_PARENT_IMAGE ####
def init_egl_khr_vg_parent_image():
    set_enum("EGL_VG_PARENT_IMAGE_KHR", 0x30BA)


#### EGL_KHR_WAIT_SYNC ####
def init_egl_khr_wait_sync():
    # set_func('eglWaitSyncKHR', t.EGLint, (t.EGLDisplay, t.EGLSyncKHR, t.EGLint))
    pass

#### EGL_MESA_DRM_IMAGE ####
def init_egl_mesa_drm_image():
    # set_func('eglCreateDRMImageMESA', t.EGLImageKHR, (t.EGLDisplay, ct.POINTER(t.EGLint)))
    # set_func('eglExportDRMImageMESA', t.EGLBoolean, (t.EGLDisplay, t.EGLImageKHR, ct.POINTER(t.EGLint), ct.POINTER(t.EGLint), ct.POINTER(t.EGLint)))
    set_enum("EGL_DRM_BUFFER_FORMAT_MESA", 0x31D0)
    set_enum("EGL_DRM_BUFFER_USE_MESA", 0x31D1)
    set_enum("EGL_DRM_BUFFER_FORMAT_ARGB32_MESA", 0x31D2)
    set_enum("EGL_DRM_BUFFER_MESA", 0x31D3)
    set_enum("EGL_DRM_BUFFER_STRIDE_MESA", 0x31D4)
    set_enum("EGL_DRM_BUFFER_USE_SCANOUT_MESA", 0x00000001)
    set_enum("EGL_DRM_BUFFER_USE_SHARE_MESA", 0x00000002)


#### EGL_MESA_IMAGE_DMA_BUF_EXPORT ####
def init_egl_mesa_image_dma_buf_export():
    # set_func('eglExportDMABUFImageQueryMESA', t.EGLBoolean, (t.EGLDisplay, t.EGLImageKHR, ct.POINTER(t.INT), ct.POINTER(t.INT), ct.POINTER(t.EGLuint64KHR)))
    # set_func('eglExportDMABUFImageMESA', t.EGLBoolean, (t.EGLDisplay, t.EGLImageKHR, ct.POINTER(t.INT), ct.POINTER(t.EGLint), ct.POINTER(t.EGLint)))
    pass

#### EGL_MESA_PLATFORM_GBM ####
def init_egl_mesa_platform_gbm():
    set_enum("EGL_PLATFORM_GBM_MESA", 0x31D7)


#### EGL_NOK_SWAP_REGION ####
def init_egl_nok_swap_region():
    # set_func('eglSwapBuffersRegionNOK', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, ct.POINTER(t.EGLint)))
    pass

#### EGL_NOK_SWAP_REGION2 ####
def init_egl_nok_swap_region2():
    # set_func('eglSwapBuffersRegion2NOK', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, ct.POINTER(t.EGLint)))
    pass

#### EGL_NOK_TEXTURE_FROM_PIXMAP ####
def init_egl_nok_texture_from_pixmap():
    set_enum("EGL_Y_INVERTED_NOK", 0x307F)


#### EGL_NV_3DVISION_SURFACE ####
def init_egl_nv_3dvision_surface():
    set_enum("EGL_AUTO_STEREO_NV", 0x3136)


#### EGL_NV_COVERAGE_SAMPLE ####
def init_egl_nv_coverage_sample():
    set_enum("EGL_COVERAGE_BUFFERS_NV", 0x30E0)
    set_enum("EGL_COVERAGE_SAMPLES_NV", 0x30E1)


#### EGL_NV_COVERAGE_SAMPLE_RESOLVE ####
def init_egl_nv_coverage_sample_resolve():
    set_enum("EGL_COVERAGE_SAMPLE_RESOLVE_NV", 0x3131)
    set_enum("EGL_COVERAGE_SAMPLE_RESOLVE_DEFAULT_NV", 0x3132)
    set_enum("EGL_COVERAGE_SAMPLE_RESOLVE_NONE_NV", 0x3133)


#### EGL_NV_CUDA_EVENT ####
def init_egl_nv_cuda_event():
    set_enum("EGL_CUDA_EVENT_HANDLE_NV", 0x323B)
    set_enum("EGL_SYNC_CUDA_EVENT_NV", 0x323C)
    set_enum("EGL_SYNC_CUDA_EVENT_COMPLETE_NV", 0x323D)


#### EGL_NV_DEPTH_NONLINEAR ####
def init_egl_nv_depth_nonlinear():
    set_enum("EGL_DEPTH_ENCODING_NV", 0x30E2)
    set_enum("EGL_DEPTH_ENCODING_NONE_NV", 0)
    set_enum("EGL_DEPTH_ENCODING_NONLINEAR_NV", 0x30E3)


#### EGL_NV_DEVICE_CUDA ####
def init_egl_nv_device_cuda():
    set_enum("EGL_CUDA_DEVICE_NV", 0x323A)


#### EGL_NV_NATIVE_QUERY ####
def init_egl_nv_native_query():
    # set_func('eglQueryNativeDisplayNV', t.EGLBoolean, (t.EGLDisplay, ct.POINTER(t.EGLNativeDisplayType)))
    # set_func('eglQueryNativeWindowNV', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLNativeWindowType)))
    # set_func('eglQueryNativePixmapNV', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, ct.POINTER(t.EGLNativePixmapType)))
    pass

#### EGL_NV_POST_SUB_BUFFER ####
def init_egl_nv_post_sub_buffer():
    # set_func('eglPostSubBufferNV', t.EGLBoolean, (t.EGLDisplay, t.EGLSurface, t.EGLint, t.EGLint, t.EGLint, t.EGLint))
    set_enum("EGL_POST_SUB_BUFFER_SUPPORTED_NV", 0x30BE)


#### EGL_NV_STREAM_CONSUMER_GLTEXTURE_YUV ####
def init_egl_nv_stream_consumer_gltexture_yuv():
    # set_func('eglStreamConsumerGLTextureExternalAttribsNV', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLAttrib))
    set_enum("EGL_YUV_PLANE0_TEXTURE_UNIT_NV", 0x332C)
    set_enum("EGL_YUV_PLANE1_TEXTURE_UNIT_NV", 0x332D)
    set_enum("EGL_YUV_PLANE2_TEXTURE_UNIT_NV", 0x332E)
    set_enum("EGL_YUV_NUMBER_OF_PLANES_EXT", 0x3311)
    set_enum("EGL_YUV_BUFFER_EXT", 0x3300)


#### EGL_NV_STREAM_METADATA ####
def init_egl_nv_stream_metadata():
    # set_func('eglQueryDisplayAttribNV', t.EGLBoolean, (t.EGLDisplay, t.EGLint, ct.POINTER(t.EGLAttrib)))
    # set_func('eglSetStreamMetadataNV', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLint, t.EGLint, t.EGLint, ct.POINTER(t.void)))
    # set_func('eglQueryStreamMetadataNV', t.EGLBoolean, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, t.EGLint, t.EGLint, t.EGLint, ct.POINTER(t.void)))
    set_enum("EGL_MAX_STREAM_METADATA_BLOCKS_NV", 0x3250)
    set_enum("EGL_MAX_STREAM_METADATA_BLOCK_SIZE_NV", 0x3251)
    set_enum("EGL_MAX_STREAM_METADATA_TOTAL_SIZE_NV", 0x3252)
    set_enum("EGL_PRODUCER_METADATA_NV", 0x3253)
    set_enum("EGL_CONSUMER_METADATA_NV", 0x3254)
    set_enum("EGL_PENDING_METADATA_NV", 0x3328)
    set_enum("EGL_METADATA0_SIZE_NV", 0x3255)
    set_enum("EGL_METADATA1_SIZE_NV", 0x3256)
    set_enum("EGL_METADATA2_SIZE_NV", 0x3257)
    set_enum("EGL_METADATA3_SIZE_NV", 0x3258)
    set_enum("EGL_METADATA0_TYPE_NV", 0x3259)
    set_enum("EGL_METADATA1_TYPE_NV", 0x325A)
    set_enum("EGL_METADATA2_TYPE_NV", 0x325B)
    set_enum("EGL_METADATA3_TYPE_NV", 0x325C)


#### EGL_NV_STREAM_SYNC ####
def init_egl_nv_stream_sync():
    # set_func('eglCreateStreamSyncNV', t.EGLSyncKHR, (t.EGLDisplay, t.EGLStreamKHR, t.EGLenum, ct.POINTER(t.EGLint)))
    set_enum("EGL_SYNC_TYPE_KHR", 0x30F7)
    set_enum("EGL_SYNC_NEW_FRAME_NV", 0x321F)


#### EGL_NV_SYNC ####
def init_egl_nv_sync():
    # set_func('eglCreateFenceSyncNV', t.EGLSyncNV, (t.EGLDisplay, t.EGLenum, ct.POINTER(t.EGLint)))
    # set_func('eglDestroySyncNV', t.EGLBoolean, (t.EGLSyncNV,))
    # set_func('eglFenceNV', t.EGLBoolean, (t.EGLSyncNV,))
    # set_func('eglClientWaitSyncNV', t.EGLint, (t.EGLSyncNV, t.EGLint, t.EGLTimeNV))
    # set_func('eglSignalSyncNV', t.EGLBoolean, (t.EGLSyncNV, t.EGLenum))
    # set_func('eglGetSyncAttribNV', t.EGLBoolean, (t.EGLSyncNV, t.EGLint, ct.POINTER(t.EGLint)))
    set_enum("EGL_SYNC_PRIOR_COMMANDS_COMPLETE_NV", 0x30E6)
    set_enum("EGL_SYNC_STATUS_NV", 0x30E7)
    set_enum("EGL_SIGNALED_NV", 0x30E8)
    set_enum("EGL_UNSIGNALED_NV", 0x30E9)
    set_enum("EGL_SYNC_FLUSH_COMMANDS_BIT_NV", 0x0001)
    set_enum("EGL_FOREVER_NV", 0xFFFFFFFFFFFFFFFF)
    set_enum("EGL_ALREADY_SIGNALED_NV", 0x30EA)
    set_enum("EGL_TIMEOUT_EXPIRED_NV", 0x30EB)
    set_enum("EGL_CONDITION_SATISFIED_NV", 0x30EC)
    set_enum("EGL_SYNC_TYPE_NV", 0x30ED)
    set_enum("EGL_SYNC_CONDITION_NV", 0x30EE)
    set_enum("EGL_SYNC_FENCE_NV", 0x30EF)
#     set_enum("EGL_NO_SYNC_NV", ((EGLSyncNV)0))


#### EGL_NV_SYSTEM_TIME ####
def init_egl_nv_system_time():
    # set_func('eglGetSystemTimeFrequencyNV', t.EGLuint64NV, ())
    # set_func('eglGetSystemTimeNV', t.EGLuint64NV, ())
    pass

#### EGL_TIZEN_IMAGE_NATIVE_BUFFER ####
def init_egl_tizen_image_native_buffer():
    set_enum("EGL_NATIVE_BUFFER_TIZEN", 0x32A0)


#### EGL_TIZEN_IMAGE_NATIVE_SURFACE ####
def init_egl_tizen_image_native_surface():
    set_enum("EGL_NATIVE_SURFACE_TIZEN", 0x32A1)


def init():
    init_egl_version_1_0()
    init_egl_version_1_1()
    init_egl_version_1_2()
    init_egl_version_1_3()
    init_egl_version_1_4()
    init_egl_version_1_5()
    init_egl_android_blob_cache()
    init_egl_android_framebuffer_target()
    init_egl_android_image_native_buffer()
    init_egl_android_native_fence_sync()
    init_egl_android_recordable()
    init_egl_angle_d3d_share_handle_client_buffer()
    init_egl_angle_device_d3d()
    init_egl_angle_query_surface_pointer()
    init_egl_angle_surface_d3d_texture_2d_share_handle()
    init_egl_angle_window_fixed_size()
    init_egl_arm_pixmap_multisample_discard()
    init_egl_ext_buffer_age()
    init_egl_ext_create_context_robustness()
    init_egl_ext_device_base()
    init_egl_ext_device_drm()
    init_egl_ext_device_enumeration()
    init_egl_ext_device_openwf()
    init_egl_ext_device_query()
    init_egl_ext_image_dma_buf_import()
    init_egl_ext_multiview_window()
    init_egl_ext_output_base()
    init_egl_ext_output_drm()
    init_egl_ext_output_openwf()
    init_egl_ext_platform_base()
    init_egl_ext_platform_device()
    init_egl_ext_platform_wayland()
    init_egl_ext_platform_x11()
    init_egl_ext_protected_content()
    init_egl_ext_protected_surface()
    init_egl_ext_stream_consumer_egloutput()
    init_egl_ext_swap_buffers_with_damage()
    init_egl_ext_yuv_surface()
    init_egl_hi_clientpixmap()
    init_egl_hi_colorformats()
    init_egl_img_context_priority()
    init_egl_img_image_plane_attribs()
    init_egl_khr_cl_event()
    init_egl_khr_cl_event2()
    init_egl_khr_config_attribs()
    init_egl_khr_create_context()
    init_egl_khr_create_context_no_error()
    init_egl_khr_debug()
    init_egl_khr_fence_sync()
    init_egl_khr_gl_colorspace()
    init_egl_khr_gl_renderbuffer_image()
    init_egl_khr_gl_texture_2d_image()
    init_egl_khr_gl_texture_3d_image()
    init_egl_khr_gl_texture_cubemap_image()
    init_egl_khr_image()
    init_egl_khr_image_base()
    init_egl_khr_image_pixmap()
    init_egl_khr_lock_surface()
    init_egl_khr_lock_surface2()
    init_egl_khr_lock_surface3()
    init_egl_khr_mutable_render_buffer()
    init_egl_khr_partial_update()
    init_egl_khr_platform_android()
    init_egl_khr_platform_gbm()
    init_egl_khr_platform_wayland()
    init_egl_khr_platform_x11()
    init_egl_khr_reusable_sync()
    init_egl_khr_stream()
    init_egl_khr_stream_consumer_gltexture()
    init_egl_khr_stream_cross_process_fd()
    init_egl_khr_stream_fifo()
    init_egl_khr_stream_producer_eglsurface()
    init_egl_khr_swap_buffers_with_damage()
    init_egl_khr_vg_parent_image()
    init_egl_khr_wait_sync()
    init_egl_mesa_drm_image()
    init_egl_mesa_image_dma_buf_export()
    init_egl_mesa_platform_gbm()
    init_egl_nok_swap_region()
    init_egl_nok_swap_region2()
    init_egl_nok_texture_from_pixmap()
    init_egl_nv_3dvision_surface()
    init_egl_nv_coverage_sample()
    init_egl_nv_coverage_sample_resolve()
    init_egl_nv_cuda_event()
    init_egl_nv_depth_nonlinear()
    init_egl_nv_device_cuda()
    init_egl_nv_native_query()
    init_egl_nv_post_sub_buffer()
    init_egl_nv_stream_consumer_gltexture_yuv()
    init_egl_nv_stream_metadata()
    init_egl_nv_stream_sync()
    init_egl_nv_sync()
    init_egl_nv_system_time()
    init_egl_tizen_image_native_buffer()
    init_egl_tizen_image_native_surface()

