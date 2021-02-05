from setuptools import setup
import re
import readme_renderer

version = '0.0.2.1-a'


setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/discord-ext-owoify',
      version=version,
      packages=['discord.ext.owoify'],
      license='MIT',
      long_description=readme_renderer.markdown.render("### discord-ext-owoify\n Simple ext package for owoifing text.\n ### Install\n Simple paste this into your terminal\n ```py python -m pip install discord-ext-owoify```\n ### Simple Use\n Firstly, import the package using\n ```py from discord.ext import owoify```"),
      download_url = 'https://github.com/GreenDiscord/discord-ext-owoify/archive/v0.0.2.1-a.tar.gz',
      description='An extension module to owoify text',
      install_requires=['discord.py>=1.2.5'],
      python_requires='>=3.5.3'
)
