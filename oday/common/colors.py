#  __                                                  __                       _         __                
# |/  |                /                               /  |    |                / |       /  |               
# |   | ___       ___ (  ___  ___  ___  ___  ___      (   | ___| ___           (__/      (   | _ _  ___  ___ 
# |   )|___) \  )|___)| |   )|   )|___)|   )|___      |   )|   )|   )\   )      / \)     |   )| | )|   )|   )
# |__/ |__    \/ |__  | |__/ |__/ |__  |     __/      |__/ |__/ |__/| \_/      |__/\     |__/ |  / |__/||    
#                           |                                         /                                     
# Design & Implementation SQL Inection Scanner .
# The Project for Education purpose only :).
# Final Year Software Enigeering at SPU .

from oday.common.lib import os, init, Fore, Back, Style
is_nt = bool(os.name == "nt")
init(autoreset=True, convert=is_nt)
# colors foreground text:
cyan = Fore.CYAN
green = Fore.GREEN
white = Fore.WHITE
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
black = Fore.BLACK
bright_cyan = Fore.LIGHTCYAN_EX
bright_green = Fore.LIGHTGREEN_EX
bright_white = Fore.LIGHTWHITE_EX
bright_red = Fore.LIGHTRED_EX
bright_blue = Fore.LIGHTBLUE_EX
bright_yellow = Fore.LIGHTYELLOW_EX
bright_magenta = Fore.LIGHTMAGENTA_EX
bright_black = Fore.LIGHTBLACK_EX


# colors background text:
background_cyan = Back.CYAN
background_green = Back.GREEN
background_white = Back.WHITE
background_red = Back.RED
background_blue = Back.BLUE
background_yellow = Back.YELLOW
background_magenta = Back.MAGENTA
background_black = Back.BLACK
background_reset = Back.RESET

level_map = {
    "INFO": {
        "color": "green",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "WARNING": {
        "color": "yellow",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "ERROR": {
        "color": "red",
        "faint": False,
        "bold": True,
        "normal": False,
        "background": "",
    },
    "CRITICAL": {
        "color": "white",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "red",
    },
    "DEBUG": {
        "color": "blue",
        "faint": False,
        "bold": True,
        "normal": False,
        "background": "",
    },
    "SUCCESS": {
        "color": "white",
        "faint": True if is_nt else False,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "NOTICE": {
        "color": "bright_black" if is_nt else "bright_white",
        "faint": False,
        "bold": True if is_nt else False,
        "normal": False,
        "background": "",
    },
    "PAYLOAD": {
        "color": "cyan",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "START": {
        "color": "green",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "END": {
        "color": "green",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "TRAFFIC_IN": {
        "color": "bright_black",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "magenta",
    },
    "TRAFFIC_OUT": {
        "color": "magenta",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
}

color_map = {
    "white": white,
    "black": black,
    "cyan": cyan,
    "green": green,
    "magenta": magenta,
    "blue": blue,
    "yellow": yellow,
    "red": red,
    "bright_cyan": bright_cyan,
    "bright_green": bright_green,
    "bright_white": bright_white,
    "bright_red": bright_red,
    "bright_blue": bright_blue,
    "bright_yellow": bright_yellow,
    "bright_magenta": bright_magenta,
    "bright_black": bright_black,
}
bgcolor_map = {
    "white": background_white,
    "black": background_black,
    "cyan": background_cyan,
    "green": background_green,
    "magenta": background_magenta,
    "blue": background_blue,
    "yellow": background_yellow,
    "red": background_red,
}


DIM = Style.DIM
BRIGHT = Style.BRIGHT
NORMAL = Style.NORMAL
RESET = Style.RESET_ALL
if is_nt:
    nc = f"{RESET}{bright_black}"
    mc = f"{RESET}{DIM}{white}"
else:
    nc = f"{RESET}{bright_white}"
    mc = f"{RESET}{DIM}{bright_white}"
bw = f"{RESET}{white}"


def colorize(
    string,
    color="white",
    background="",
    bold=False,
    faint=False,
    normal=False,
    reset=True,
):
    if bold:
        style = BRIGHT
    if faint:
        style = DIM
    if normal:
        style = NORMAL
    if not bold and not faint and not normal:
        style = NORMAL

    if color in color_map:
        color = color_map.get(color)
    if background in bgcolor_map:
        background = bgcolor_map.get(background)
        string = f"{background}{string}{RESET}"
    if reset:
        text = f"{color}{style}{string}{RESET}"
    else:
        text = f"{color}{style}{string}"
    return text
