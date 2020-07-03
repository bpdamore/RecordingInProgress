import Quartz
import time
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListExcludeDesktopElements, kCGNullWindowID
from Foundation import NSSet, NSMutableSet

def windowList(wl, name):
    for v in wl:
        try:
            window = str(v.valueForKey_('kCGWindowOwnerName')).encode('utf8')
            if window == name:
                return True # remove 'encode' for Python 3.x
        except AttributeError:
            pass
    return False

def findWindow(name):
    wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
    wl = sorted(wl, key=lambda k: k.valueForKey_('kCGWindowOwnerPID'))
    return windowList(wl, name)

def _printWindowList():
    wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
    wl = sorted(wl, key=lambda k: k.valueForKey_('kCGWindowOwnerPID'))
    for v in wl:
        try:
            window = str(v.valueForKey_('kCGWindowOwnerName')).encode('utf8')
            print(window)
        except AttributeError:
            pass
    return False

if __name__ == "__main__":
    print("This is a utility script and not intended as a standalone application.")
    _printWindowList()
