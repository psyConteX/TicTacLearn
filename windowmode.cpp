#include <windows.h>
#include <tchar.h>

int WINAPI WinMain(
    _In_ HINSTANCE hInstance,
    _In_opt_ HINSTANCE hPrevInstance,
    _In_ LPSTR lpCmdLine,
    _In_ int nCmdShow
);

LRESULT CALLBACK WndProc(
    _In_ HWND hWnd,
    _In_ UINT message,
    _In_ WPARAM wParam,
    _In_ LPARAM lParam
);

WNDCLASSEX wcex;

wcex.cbSize         = sizeof(WNDCLASSEX);
wcex.style          = CS_HREDRAW | CS_VREDRAW;
wcex.lpfnWndProc    = WndProc;
wcex.cbClsExtra     = 0;
wcex.cbWndExtra     = 0;
wcex.hInstance      = hInstance;
wcex.hIcon          = LoadIcon(wcex.hInstance, IDI_APPLICATION);
wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
wcex.lpszMenuName   = NULL;
wcex.lpszClassName  = szWindowClass;
wcex.hIconSm        = LoadIcon(wcex.hInstance, IDI_APPLICATION);

if (!RegisterClassEx(&wcex)) {
    MessageBox(Null,
        _T("Call to RegisterClassEx failed!"),
        _T("Windows Desktop Guided Tour"),
        NULL);
        
        return 1;
}

static TCHAR szWindowClass[] = _T("DesktopApp");
static TCHAR szTitle[] = _T("Windows Desktop Guided Tour Application");

// The parameters to CreateWindowEx explained:
// WS_EX_OVERLAPPEDWINDOW : An optional extended window style.
// szWindowClass: the name of the application
// szTitle: the text that appears in the title bar
// WS_OVERLAPPEDWINDOW: the type of window to create
// CW_USEDEFAULT, CW_USEDEFAULT: initial position (x, y)
// 500, 100: initial size (width, length)
// NULL: the parent of this window
// NULL: this application does not have a menu bar
// hInstance: the first parameter from WinMain
// NULL: not used in this application
HWND hWnd = CreateWindowEx(
WS_EX_OVERLAPPEDWINDOW,
   szWindowClass,
   szTitle,
   WS_OVERLAPPEDWINDOW,
   CW_USEDEFAULT, CW_USEDEFAULT,
   500, 100,
   NULL,
   NULL,
   hInstance,
   NULL
);
