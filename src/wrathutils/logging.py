# The MIT License (MIT)
# Python Wrath Utils Copyright (c) 2016 Trent Spears
from time import strftime
from enum import Enum

class TimestampFormat(Enum):
    """
    An enum describing the format to write a timestamp.
    """
    """
    Standard global time/date format. [DD/MM/YYYY][HH:MM:SS]
    """
    STANDARD = 0
    """
    United States standard time/date format. [MM/DD/YYYY][HH:MM:SS]
    """
    US = 1

def get_timestamp(timestampFormat = TimestampFormat.STANDARD):
    """
    Returns the current time and dateformatted as speicifed by TimestampFormat.
    timestampFormat: The format to return the timestamp string in, as specified by TimestampFormat enum.
    """
    if timestampFormat == TimestampFormat.STANDARD:
        return strftime("[%d/%m/%Y][%H:%M:%S]")
    else:
        return strftime("[%m/%d/%Y][%H:%M:%S]")

class LogFilter:
    """
    Class for developer to override and specify what gets printed and/or logged.
    """
    def filter_console(self, log_string):
        """
        Function to filter what is printed to the console. What is returned will be printed.
        Nothing will be printed if None is returned.
        """
        return log_string

    def filter_log(self, log_string):
        """
        Function to filter what is logged to the log file. What is returned will be written to file.
        Nothing will be written to file if None is returned.
        """
        return log_string

class Logger:
    """
    Utility logging class with timestamp, filtering, and file I/O capabilities.
    """
    fout = None
    fil = None
    time = True
    tsFormat = None
    console = True
    nlc = True
    nlf = True
    
    def __init__(self, logFile = None, logFilter = None, timeStamp = True, timestampFormat = TimestampFormat.STANDARD, writeConsole = True):
        """
        Constructor.
        logFile: The string path/name of the file to log messages to. Messages will not be written to file if None is specified. None by default.
        logFilter: An object of a LogFilter subclass to specify what to filter. Messages will not be filtered if None is specified. None by default.
        timeStamp: All messages that prints a new line will be prefaced with a timestamp if True. True by default.
        timestampFormat: The format to use when writing timestamps, as specified by TimestampFormat enum. TimestampFormat.STANDARD by default.
        writeConsole: Boolean to determine if messages should be written to standard output. True by default.
        """
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
        """
        Closes the log file writer. After this method is run, messages will not be written to the log file.
        """
        if self.fout is not None and not self.fout.closed:
            self.fout.close()

    def is_closed(self):
        """
        Specifies whether or not the Logger object is still writing to file.
        """
        return self.fout is None or self.fout.closed

    def print(self, message):
        """
        Outputs a message without adding a new line as appropriate by object configuration.
        message: The message to log.
        """
        message = str(message)
        tm = get_timestamp()
            
        if self.console is True:
            finmsg = self.fil.filter_console(message)
            if finmsg is not None:
                if self.time and self.nlc:
                    print(tm + " " + finmsg, end='')
                    self.nlc = False
                else:
                    print(finmsg, end='')
                if finmsg[-1:] == "\n":
                    self.nlc = True

        if self.fout is not None and not self.fout.closed:
            finmsg = self.fil.filter_log(message)
            if finmsg is not None:
                if self.time and self.nlf:
                    self.fout.write(tm + finmsg)
                    self.nlf = False
                else:
                    self.fout.write(finmsg)
                if finmsg[-1:] == "\n":
                    self.nlf = True

    def println(self, message):
        """
        Outputs a message and adds a new line following the message as appropriate by object configuration.
        message: The message to log.
        """
        message = str(message)
        self.print(message + "\n")
