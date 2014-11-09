from setuptools import setup, find_packages
from codecs import open
from os import path

setup(name='wordfilter',
      version='0.1.7',
      description='A small module that lets you filter strings for bad words.',
      url='https://github.com/dariusk/wordfilter',
      maintainer='Jim Witschey',
      maintainer_email='jim.witschey@gmail.com',
      license='MIT',
      packages=['wordfilter'],
      package_dir = {'': 'lib'},
      extras_require = {'test': ['pytest']},
      include_package_data = True,
      package_data={'': ['badwords.json']},
      data_files={'wordfilter': ['lib/badwords.json']}
      )
