import mailconfig, sys
from SharedNames import appname, windows
from ListWindows import MailServer, MailFile

srvrname = mailconfig.popservername or 'Server'


class MailServerWindow(MailServer, windows.MainWindow):
    def __init__(self):
        windows.MainWindow.__init__(self, appname, srvrname)
        MailServer.__init__(self)

if __name__ == "__main__":
    mymailclient = MailServerWindow()
    mymailclient.mainloop()