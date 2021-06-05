from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator-registration", "firstname"))

def readConfig(section,key):
    config= ConfigParser()
    config.read("..//Configuration//config.ini")
    return config.get(section, key)


#print(readConfig("locators","name_CSS"))
#print(readConfig("basic-info","testingsiteurl"))