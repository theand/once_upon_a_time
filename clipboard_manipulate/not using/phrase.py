
import clipboard_lib


if __name__=='__main__':
    import sys
    if len(sys.argv) == 2 :
        str = sys.argv[1]
        clipboard_lib.setText(str)
