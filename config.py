import configparser
import os

config = configparser.ConfigParser()

#create section openAI
config.add_section("openAI")

#add key pair in openAI
config.set("openAI","openAIKey","openAIkeyValue")

#create section confulenceAPI

config.add_section("confulenceAPI")

#add key pair in confulenceAPI
config.set("confulenceAPI","apiKey","https://space.tobdarwin.com/")
config.set("confulenceAPI","apiToken","")
config.set("confulenceAPI","apiSpace","IWG")

# SAVE CONFIG FILE
#change path according to your setting
with open(r"D:\chatbot\LangChainBot\configurations.ini", 'w') as configfileObj:
    config.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()
