from time import sleep
from utils.window_util import *
from utils.hue_util import *
from utils.config_util import parseconfig

def monitorAndMakeRed(ip, lightsToChange, window):
    print("Monitoring")
    redSettings = {'hue': 64949\
                    ,'saturation': 254\
                    ,'brightness': 254\
                    ,'on': True}
    isRed = False
    while True:
        programOpen = findWindow(window.encode('utf8'))
        if programOpen and not isRed:
            print("Connecting to Hue...")
            b, lights = collectHueLights(ip)
            print("Connected!")
            lightAttributes = [getLightAttributes(lights[light]) for light in lightsToChange]
            isRed = True
            for light in lightAttributes:
                changeLightColor(light = light['light'], **redSettings)
        elif isRed and not programOpen:
            for light in lightAttributes:
                changeLightColor(**light)
            isRed = False
        sleep(5)

def testItWithoutHue(ip, lightsToChange, window):
    print("Could not connect to Hue Bridge; proceeding to test without Hue")
    redSettings = {'hue': 64949\
                    ,'saturation': 254\
                    ,'brightness': 254\
                    ,'on': True}
    isRed = False
    while True:
        programOpen = findWindow(windowToMonitor)
        if programOpen and not isRed:
            # b, lights = collectHueLights(ip)
            # lightAttributes = [getLightAttributes(lights[light]) for light in lightsToChange]
            isRed = True
            # for light in lightAttributes:
            #     changeLightColor(light = light['light'], **redSettings)
            print("It's red now")
        elif isRed and not programOpen:
            # for light in lightAttributes:
            #     changeLightColor(**light)
            isRed = False
            print("It's back to normal")
        sleep(5)


if __name__ == "__main__":
    print("Starting up....")
    config = parseconfig('config.ini')
    windowToMonitor = config['OS']['window']
    bridgeIP = config['HUE']['ip']
    lightsToChange = config['HUE']['lightsToChange'].split(",")
    try:
        monitorAndMakeRed(bridgeIP, lightsToChange, windowToMonitor)
    except Exception as e:
        print(e)
        testItWithoutHue(bridgeIP, lightsToChange, windowToMonitor)
