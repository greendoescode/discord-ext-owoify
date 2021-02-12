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
    emojis = dict([("XwX", 1), ("OvO", 2), ("OwO", 3), ("UwU", 4), (">:3", 5), ("-w-", 6), ("ÙwÚ", 7), ("CwC", 8)])
    emoji = (emojis[int(number)])
    if number in emoji:
        return f"{random.choice(emoji)}"
    else:
        raise NotAValidNumber(f"Number '{number}' is not a valid option")