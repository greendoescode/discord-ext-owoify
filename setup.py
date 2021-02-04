from setuptools import setup
import re

version = ''
with open('discord/ext/owoify/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscorx/discord-ext-owoify',
      version=version,
      packages=['discord.ext.owoify'],
      license='MIT',
      download_url = 'https://github.com/GreenDiscord/discord-ext-owoify/archive/v0.0.2-a.tar.gz',
      install_requires=['discord.py'],
      description='An extension module to owoify text',
      install_requires=['discord.py>=1.2.5'],
      python_requires='>=3.5.3'
)
