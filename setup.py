from setuptools import setup
import re



version = '0.0.2.1-a'

longdescription = open("README.md", "r").read()

setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/discord-ext-owoify',
      version=version,
      packages=['discord.ext.owoify'],
      license='MIT',
      long_description=longdescription,
      download_url = 'https://github.com/GreenDiscord/discord-ext-owoify/archive/v0.0.2.1.0-a.tar.gz',
      description='An extension module to owoify text',
      install_requires=['discord.py>=1.2.5'],
      python_requires='>=3.5.3'
)
