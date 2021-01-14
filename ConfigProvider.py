from configparser import ConfigParser
import os.path

CONFIG_FILENAME = "config.ini"

def getDefaultSettings():
    config_object = ConfigParser()
    config_object['TimeDisplay'] = {
        "server": "localhost",
        "port_amcp": 5250,
        "port_osc": 6250,
        "channel": 1,
        "layer": 10
    }
    return config_object


if not os.path.isfile(CONFIG_FILENAME):
    config_object = getDefaultSettings()
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

def getCurrentSettings():
    config_object = ConfigParser()
    config_object.read(CONFIG_FILENAME)
    return dict(config_object['TimeDisplay'])

def UpdateSetting(setting, newValue):
    config_object = ConfigParser()
    config_object.read(CONFIG_FILENAME)
    config_object['TimeDisplay'][setting] = newValue

    with open(CONFIG_FILENAME, 'w') as conf:
        config_object.write(conf)