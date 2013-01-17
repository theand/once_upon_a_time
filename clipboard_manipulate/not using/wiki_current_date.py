
import clipboard_lib



if __name__=='__main__':
    import time
    now = time.localtime(time.time())
    date = time.strftime("%Y/%m/%d %H:%M", now)
    clipboard_lib.setText(date)
