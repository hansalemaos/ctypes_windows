import ctypes
from ctypes import wintypes as w

user32 = ctypes.WinDLL("user32")
user32.GetForegroundWindow.argtypes = ()
user32.GetForegroundWindow.restype = w.HWND
user32.ShowWindow.argtypes = w.HWND, w.BOOL
user32.ShowWindow.restype = w.BOOL


def window_HIDE(hwnd: int):
    user32.ShowWindow(hwnd, 0)


def window_NORMAL(hwnd: int):
    user32.ShowWindow(hwnd, 1)


def window_SHOWMINIMIZED(hwnd: int):
    user32.ShowWindow(hwnd, 2)


def window_MAXIMIZE(hwnd: int):
    user32.ShowWindow(hwnd, 3)


def window_SHOWNOACTIVATE(hwnd: int):
    user32.ShowWindow(hwnd, 4)


def window_SHOW(hwnd: int):
    user32.ShowWindow(hwnd, 5)


def window_MINIMIZE(hwnd: int):
    user32.ShowWindow(hwnd, 6)


def window_SHOWMINNOACTIVE(hwnd: int):
    user32.ShowWindow(hwnd, 7)


def window_SHOWNA(hwnd: int):
    user32.ShowWindow(hwnd, 8)


def window_RESTORE(hwnd: int):
    user32.ShowWindow(hwnd, 9)


def window_SHOWDEFAULT(hwnd: int):
    user32.ShowWindow(hwnd, 10)


def window_FORCEMINIMIZE(hwnd: int):
    user32.ShowWindow(hwnd, 11)


def get_resolution():
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def get_mouse_position():
    mousecursor = w.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(mousecursor))
    return mousecursor.x, mousecursor.y


def mouse_click(x=None, y=None):
    if x is not None and y is not None:
        ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


def resize_window(hwnd: int, position: tuple):
    user32.SetProcessDPIAware()
    user32.MoveWindow(hwnd, *position, True)
