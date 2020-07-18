import configparser
# from utils.hue_util import initializeHue

def parseconfig(path):
    print("Checking config....")
    config = configparser.ConfigParser()
    config.read(path)
    hue_connected = config.getboolean('HUE', 'connected', fallback=False)
    hue_ip = config.get('HUE',"ip", fallback="None")
    hue_dhcp = config.getboolean('HUE','dhcp', fallback=True)
    macWindow = config.get('OS', 'macWindow', fallback="CptHost")
    windowsWindow = config.get('OS', 'windowsWindow', fallback="CptHost")
    config['OS'] = {'macWindow': macWindow, 'windowsWindow':windowsWindow}
    lightsToChange = config.get('HUE', 'lightsToChange').replace("'","’")

    if hue_ip == 'None' or hue_dhcp == True:
        print(hue_ip, hue_dhcp)
        new_ip = input("What is the IP of the Hue Bridge?\n")
        new_dhcp = input("Is the hue bridge set to DHCP? (yes/no)\n")
        config['HUE']['ip'] = new_ip
        config['HUE']['dhcp'] = new_dhcp
        hue_ip = config.get('HUE',"ip", fallback="None")
        hue_dhcp = config.getboolean('HUE','dhcp', fallback='yes')
    if not hue_connected:
        input("We'll need to connect to your Hue for the first time; can you press the button on your Hue Bridge?\nPress 'enter' to proceed. ")
        connected = initializeHue(hue_ip)
        if connected:
            config['HUE']['connected'] = 'True'
            print("Successfully configured!")
        else:
            print('Failed to connect... close the program to try again.')
    with open(path, 'w') as f:
        config.write(f)
    return config


if __name__ == "__main__":
    parseconfig("config.ini")
