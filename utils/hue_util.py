from phue import Bridge

def initializeHue(ip):
    try:
        b = Bridge(ip)
        b.connect()
        return True
    except:
        return False

def collectHueLights(ip):
    b = Bridge(ip)
    lights = b.get_light_objects("name")
    return b, lights

def getLightAttributes(light):
    attr = {}
    attr['light'] = light
    attr['hue'] = light.hue
    attr['saturation'] = light.saturation
    attr['brightness'] = light.brightness
    attr['on'] = light.on
    print(f"{light.name} is currently at [{attr['hue']}, {attr['saturation']}, {attr['brightness']}, {attr['on']}]")
    return attr

def changeLightColor(light, hue, saturation, brightness, on):
    light.on = on
    light.hue = hue
    light.saturation = saturation
    light.brightness = brightness
    print(f"{light.name} was changed to [{hue}, {saturation}, {brightness}, {on}]")

if __name__ == "__main__":
    print("This is a utility script and not intended as a standalone application.")
