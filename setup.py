from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dcs-mission",
    version='0.6.0',
    description="A Digital Combat Simulator mission builder framework",
    long_description=long_description,
    url='https://github.com/rp-/dcs',
    author="Peinthor Rene",
    author_email="peinthor@gmail.com",
    license="GPLv3",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment :: Simulation',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='dcs digital combat simulator eagle dynamics mission framework',
    packages=['dcs', 'dcs/lua'],
    # entry_points={
    #     'console_scripts': [
    #         'dcs=dcs:main'
    #     ]
    # }
)