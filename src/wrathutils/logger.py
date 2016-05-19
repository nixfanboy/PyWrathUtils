# The MIT License (MIT)
# Python Wrath Utils Copyright (c) 2016 Trent Spears

from datetime import datetime
from enum import Enum

class TimestampFormat(Enum):
    STANDARD = 0
    US = 1

def getTimestamp(timestampFormat = TimestampFormat.STANDARD):
    now = datetime.now()
    if timestampFormat == TimestampFormat.STANDARD:
        return "[%02d/%02d/%02d][%02d:%02d:%02d]" % (now.date().day, now.date().month, now.date().year, now.time().hour, now.time().minute, now.time().second)
    else:
        return "[%02d/%02d/%02d][%02d:%02d:%02d]" % (now.date().month, now.date().day, now.date().year, now.time().hour, now.time().minute, now.time().second)

class LogFilter:
    def filterConsole(self, log_string):
        return log_string

    def filterLog(self, log_string):
        return log_string

class Logger:
    fout = None
    fil = None
    time = True
    tsFormat = None
    console = True
    
    def __init__(self, logFile = None, logFilter = None, timeStamp = True, timestampFormat = TimestampFormat.STANDARD, writeConsole = True):
        if logFile is not None and len(logFile) > 0:
            try:
                self.fout = open(logFile, "a")
            except IOError:
                print("] ERROR: Could not log to file '" + logFile + "'! I/O Error!")
                self.fout = None
        else:
            self.fout = None
        
        if logFilter is not None:
            self.fil = logFilter
        else:
            self.fil = LogFilter()

        self.time = timeStamp
        self.tsFormat = timestampFormat
        self.console = writeConsole

    def close(self):
        if self.fout is not None and not self.fout.closed:
            self.fout.close()

    def isClosed(self):
        return self.fout is None or self.fout.closed

    def print(self, message):
        prepp = ""
        if self.time is True:
            prepp = getTimestamp(self.tsFormat) + " "
        if self.console is True:
            finmsg = self.fil.filterConsole(message)
            if finmsg is not None:
                print(prepp + finmsg, end='')
        if self.fout is not None and not self.fout.closed:
            finmsg = self.fil.filterLog(message)
            if finmsg is not None:
                self.fout.write(prepp + finmsg)
                self.fout.flush()

    def println(self, message):
        self.print(message + "\n")
