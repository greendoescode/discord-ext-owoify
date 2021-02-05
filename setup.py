from setuptools import setup, find_packages
import re



version = '0.0.2.1.1-a'



setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/discord-ext-owoify',
      version=version,
      packages=find_packages(),
      license='MIT',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      download_url = 'https://github.com/GreenDiscord/discord-ext-owoify/archive/v0.0.2.2-a.tar.gz',
      description='An extension module to owoify text',
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ],
      install_requires=['discord.py>=1.2.5'],
      python_requires='>=3.5.3'
)
