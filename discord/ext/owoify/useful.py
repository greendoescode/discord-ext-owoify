import random

def owoifyer(text):
    message = text.replace("r", "w").replace(
        "l", "w").replace("L", "W").replace("R", "W")
    owoified = f"{message[0][0]}-{message}"
    l = random.randint(1, 2)
    if l == 2:
        owoified = f"{message}"
    return owoified