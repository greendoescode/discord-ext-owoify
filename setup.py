from setuptools import setup, find_packages
import re



version = '0.0.5-a'



setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/discord-ext-owoify/',
      version=version,
      packages=['discord.ext.owoify'],
      license='MIT',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
<<<<<<< HEAD
      download_url = 'https://github.com/GreenDiscord/discord-ext-owoify/archive/v0.0.6-a.tar.gz',
=======
>>>>>>> b18e74a6eec7f2bccb56750ff7d9b1d2d61a8e63
      description='An extension module to owoify text',
      install_requires=['discord.py>=1.2.5'],
      python_requires='>=3.5.3'
)

