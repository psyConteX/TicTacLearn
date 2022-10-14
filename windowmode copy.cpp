#define _WIN32_WINNT 0x0501
#include <windows.h>
#include <tchar.h>

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
if (!hWnd)
{
   MessageBox(NULL,
      _T("Call to CreateWindowEx failed!"),
      _T("Windows Desktop Guided Tour"),
      NULL);

   return 1;
}