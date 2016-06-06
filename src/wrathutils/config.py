# The MIT License (MIT)
# Python Wrath Utils Copyright (c) 2016 Trent Spears

def list_to_config_value(listVariable):
    retVal = ""
    for curVar in listVariable:
        retVal += "," + str(curVal)
    return retVal

class Config:
    """
    Class to manage, load, and save options in a key->value format.
    """
    confMap = {}
    confFile = None
    
    def __init__(self, configFile = None):
        """
        Constructor.
        configFile: The configuration file to read from/write to when no file is specified.
        """
        if configFile is not None:
            self.confFile = configFile
            self.load(configFile)
    
    def clear(self):
        """
        Clears the current configuration.
        """
        self.confMap.clear()
    
    def get(self, key, defaultValue = None):
        """
        Returns a stored value.
        defaultValue: The default value to return if the key is not present in the config.
        """
        if key in self.confMap.keys():
            return self.confMap[key]
        else:
            return defaultValue
    
    def get_as_list(self, key, defaultValue = None):
        """
        Returns a stored value as a list.
        defaultValue: The default value to return if the key is not present in the config.
        """
        if key in self.confMap.keys():
            return self.confMap[key].split(",")
        else:
            return defaultValue
    
    def get_keys(self):
        """
        Returns the keys present in the configuration map. 
        """
        return self.confMap.keys()
    
    def has_option(self, key):
        """
        key: The key to check the presence for.
        Returns true if specified key is present in the configuration.
        """
        return key in self.confMap.keys()
    
    def load(self):
        """
        Loads the config map in simple, pre-defined format used in Wrath software suite.
        Uses the file specified in the constructor, will report an error if not present.
        """
        if not self.confFile is None and len(self.confFile) > 0:
            self.load(self.confFile)
        else:
            print("] ERROR: Could not load Config! Undefined file!")
    
    def load(self, configFile):
        """
        Loads the config map in simple, pre-defined format used in Wrath software suite.
        configFile: The file to load the configuration from.
        """
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
    
    def reload(self):
        """
        Clears the current configuration and reloads it from file specified in the constructor.
        """
        self.confMap.clear()
        self.load()
        
    def reload(self, configFile):
        """
        Clears the current configuration and reloads it from file specified.
        configFile: The file to load the configuration from.
        """
        self.confMap.clear()
        self.load(configFile)
    
    def save(self):
        """
        Saves the config map in simple, pre-defined format used in Wrath software suite.
        Uses the file specified in the constructor, will report an error if not present.
        """
        if not self.confFile is None and len(self.confFile) > 0:
            self.save(self.confFile)
        else:
            print("] ERROR: Could not save Config! Undefined file!")
    
    def save(self, configFile):
        """
        Saves the config map in simple, pre-defined format used in Wrath software suite.
        configFile: The file to save the configuration to.
        """
        try:
            fileObj =  open(configFile, "w");
            for k,v in self.confMap.items():
                fileObj.write(str(k) + ": " + str(v) + "\n")
            fileObj.close()
        except IOError:
            print("] ERROR: Could not save config file '" + configFile + "'! I/O Error!")
            return
    
    def set(self, key, value):
        """
        Sets a configuration value with specified property.
        key: The key to save the value to.
        value: The value to associate with the key.
        """
        self.confMap[key] = value