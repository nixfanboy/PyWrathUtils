# The MIT License (MIT)
# Python Wrath Utils Copyright (c) 2016 Trent Spears

class Config:
    confMap = {}
    confFile = None
    
    def __init__(self, configFile = None):
        if configFile is not None:
            self.confFile = configFile
            self.load(configFile)
    
    def get(self, key, defaultValue = None):
        if key in self.confMap.keys():
            return self.confMap[key]
        else:
            return defaultValue
    
    def getAsList(self, key, defaultValue = None):
        if key in self.confMap.keys():
            return self.confMap[key].split(",")
        else:
            return defaultValue
    
    def load(self):
        if not self.confFile is None and len(self.confFile) > 0:
            load(self.confFile)
        else:
            print("] ERROR: Could not load Config! Undefined file!")
    
    # Loads the config map in simple, pre-defined format used in Wrath software suite.
    def load(self, configFile):
        try:
            fileObj =  open(configFile, "r");
            for line in fileObj:
                if len(line) > 0 and line[0] != '#' and line[0] != ';' and line[0:1] != "//":
                    buf = line.split(": ", 1)
                    if len(buf) == 2:
                        self.confMap[buf[0]] = buf[1]
            fileObj.close()
        except IOError:
            print("] ERROR: Could not load config file '" + configFile + "'! I/O Error!")
            return
    
    def save(self):
        if not self.confFile is None and len(self.confFile) > 0:
            save(self.confFile)
        else:
            print("] ERROR: Could not save Config! Undefined file!")
    
    # Saves the config map in simple, pre-defined format used in Wrath software suite.
    def save(self, configFile):
        try:
            fileObj =  open(configFile, "w");
            for k,v in self.confMap.items():
                fileObj.write(str(k) + ": " + str(v) + "\n")
            fileObj.close()
        except IOError:
            print("] ERROR: Could not save config file '" + configFile + "'! I/O Error!")
            return
    
    def set(self, key, value):
        self.confMap[key] = value