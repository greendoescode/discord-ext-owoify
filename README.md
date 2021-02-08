[![License](https://img.shields.io/github/license/GreenDiscord/discord-ext-owoify)](https://mit-license.org/) ![version](https://img.shields.io/pypi/v/discord-ext-owoify) [![Support Server](https://img.shields.io/discord/807028485667028993.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/esARSKDMAp)

### discord-ext-owoify
Simple ext package for owoifing text.

### Install
Simple paste this into your terminal

- ```shell script
  pip install discord-ext-owoify
  ```

If you need to **update** please use the following:

- ```shell script
  pip install --upgrade discord-ext-owoify
  ```

### Simple Use
Firstly, import the package using

- ```python
  from discord.ext import owoify
  ```

Now, lets use the ```owoify.owoify()``` attribute to **owoify** your text!

- ```python
  from discord.ext import owoify

  print(await owoify.owoify("TEXT"))

  ```

Wanna decode this now? Use the ```owoify.decode()``` attribute for this module.
- ```python
  from discord.ext import owoify
  
  print(await owoify.decode("TEXT"))
  ```
  
  Note: The decode attribute is still in dev, as i need to find all words that would get owoified :) 
  
  
### Devlepoment version

To install this, you need to install from the github

- ```shell script
  pip install -U git+https://github.com/GreenDiscord/discord-ext-owoify
  ```
Thanks! Please give feedback in issues :)
