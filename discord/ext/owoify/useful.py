import random

class NotAValidNumber(Exception):
    pass

def owoifyer(text):
    message = text.replace("r", "w").replace(
        "l", "w").replace("L", "W").replace("R", "W")
    owoified = f"{message[0][0]}-{message}"
    l = random.randint(1, 2)
    if l == 2:
        owoified = f"{message}"
    return owoified

def randemoji(number: int):
    emojis = dict([(1, "XwX"), (2, "OvO"), (3, "OwO"), (4, "UwU"), (5, ">:3"), (6, "-w-"), (7, "ÙwÚ"), (8, "CwC")])
    emoji = (emojis[number])
    if number in emoji:
        return f"{random.choice(emoji)}"
    else:
        raise NotAValidNumber(f"Number '{number}' is not a valid option")