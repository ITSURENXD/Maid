#include <windows.h>
#include <gdiplus.h>
using namespace Gdiplus;

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    // Initialize GDI+
    GdiplusStartupInput gdiplusStartupInput;
    ULONG_PTR gdiplusToken;
    GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);

    // Create the main window
    const wchar_t* className = L"DesktopAnimationWindowClass";
    const wchar_t* windowTitle = L"Desktop Animation";
    HWND hwnd;
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = className;
    RegisterClass(&wc);
    hwnd = CreateWindowEx(0, className, windowTitle, WS_POPUP, 0, 0, 0, 0, NULL, NULL, hInstance, NULL);
    ShowWindow(hwnd, nCmdShow);

    // Message loop
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Clean up GDI+
    GdiplusShutdown(gdiplusToken);
    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        case WM_CREATE:
        {
            // Initialize the animation
            SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE);
            SetLayeredWindowAttributes(hwnd, RGB(255, 255, 255), 0, LWA_COLORKEY);
            SetTimer(hwnd, 1, 10, NULL);
            break;
        }

        case WM_TIMER:
        {
            // Perform animation updates here
            // You can use GDI+ to draw your animation on the window's DC (device context)
            // For example:
            HDC hdc;
            PAINTSTRUCT ps;
            hdc = BeginPaint(hwnd, &ps);
            Graphics graphics(hdc);
            graphics.Clear(Color::Transparent);
            // Draw your animation using GDI+ methods like DrawImage, DrawString, etc.
            // Example:
            SolidBrush brush(Color::Red);
            graphics.FillEllipse(&brush, 100, 100, 200, 200);
            EndPaint(hwnd, &ps);
            break;
        }

        case WM_DESTROY:
        {
            // Clean up and exit
            KillTimer(hwnd, 1);
            PostQuitMessage(0);
            break;
        }
    }

    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}