typedef struct {
    int width;
    int height;
} TerminalSize;

TerminalSize terminal_size(void);

#ifdef TERMINAL_H_IMPLEMENTATION

    #ifdef _WIN32

        #include <windows.h>

        TerminalSize terminal_size(void)
        {
            CONSOLE_SCREEN_BUFFER_INFO csbi;
            TerminalSize size = {0, 0};

            if (GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi))
            {
                size.width  = csbi.srWindow.Right  - csbi.srWindow.Left + 1;
                size.height = csbi.srWindow.Bottom - csbi.srWindow.Top  + 1;
            }

            return size;
        }

    #else

        #include <sys/ioctl.h>
        #include <unistd.h>

        TerminalSize terminal_size(void)
        {
            struct winsize ws;
            TerminalSize size = {0, 0};

            if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &ws) == 0)
            {
                size.width = ws.ws_col;
                size.height = ws.ws_row;
            }

            return size;
        }

    #endif

#endif