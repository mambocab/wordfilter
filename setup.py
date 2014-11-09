from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='wordfilter',
      version='0.1.7',
      description='A small module that lets you filter strings for bad words.',
      long_description=long_description,
      url='https://github.com/dariusk/wordfilter',
      maintainer='Jim Witschey',
      maintainer_email='jim.witschey@gmail.com',
      license='MIT',
      packages=['wordfilter'],
      package_dir = {'': 'lib'},
      extras_require = {'test': ['pytest']})
