#ifndef INFO_H
#define INFO_H

typedef struct {
    const char *language;
    int standard;
    const char *compiler;
    const char *operating_system;
} Info_t;

#if defined(__cplusplus)
# define INFO_LANGUAGE "C++"
# if __cplusplus >= 202002L
#  define INFO_STANDARD 20
# elif __cplusplus >= 201703L
#  define INFO_STANDARD 17
# elif __cplusplus >= 201103L
#  define INFO_STANDARD 11
# else
#  define INFO_STANDARD 98
# endif
#elif defined(__STDC__)
# define INFO_LANGUAGE "C"
# if defined(__STDC_VERSION__) 
#  if (__STDC_VERSION__ >= 202311L)
#   define INFO_STANDARD 23
#  elif (__STDC_VERSION__ >= 201112L)
#   define INFO_STANDARD 11
#  elif (__STDC_VERSION__ >= 199901L)
#   define INFO_STANDARD 99
#  else
#   define INFO_STANDARD 90
#  endif
# endif
#else
# define INFO_LANGUAGE "Unknown"
# define INFO_STANDARD 0
#endif

#if defined(__clang__)
# define INFO_COMPILER "Clang"
#elif defined(__GNUC__)
# define INFO_COMPILER "GCC"
#elif defined(_MSC_VER)
# define INFO_COMPILER "MSVC"
#else
# define INFO_COMPILER "Unknown"
#endif

#if defined(_WIN32)
# define INFO_OS "Windows"
#elif defined(__linux__)
# define INFO_OS "Linux"
#elif defined(__APPLE__)
# define INFO_OS "macOS"
#else
# define INFO_OS "Unknown"
#endif

static const Info_t INFO = {
    INFO_LANGUAGE,
    INFO_STANDARD,
    INFO_COMPILER,
    INFO_OS
};

#endif