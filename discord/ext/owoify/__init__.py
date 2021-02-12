"""
The MIT License (MIT)

Copyright (c) 2021-2021 GreenDiscord

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""




import discord

import random


from .useful import owoifyer, randemoji

__version__ = '0.0.5-a'




def owoify(text):
    """
    Owoify's given text
    You need to await this function.
    """
    owoified = owoifyer(f"{text}")
    return owoified




async def discord_owo(channel, text):
    """
    Sends owoified message to a certain channel
    Please use "owoify" for other uses
    You need to await this function.
    """
    owoified = owoifyer(f"{text}")
    return await channel.send(f"{owoified}")


def decode(text):
    decoded = text.replace("hewwo", "hello").replace("Hewwo", "Hello").replace("Wuve", "Love").replace("wuve", "love").replace("Awe", "Are").replace("awe", "are").replace("wmao", "lmao").replace("Wmao", "Lmao")
    return decoded

def owo(number):
    owoemoji = randemoji(1)
    return owoemoji
