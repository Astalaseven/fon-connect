import os
from setuptools import setup
from fon.meta import __version__

description = "Connect easily to FON Belgacom Network"
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
    long_description = description

requirements = []
with open("requirements.txt") as r:
    requirements = list(map(lambda x: x.strip(), r.read().split('\n')))

setup(
    name='fon',
    packages=['fon'],
    version=__version__,
    description=description,
    long_description=long_description,
    author='Gatien Bovyn',
    author_email='nikita.marchant@gmail.com',
    url='https://github.com/Astalaseven/fon-connect',
    keywords=['fon', 'command-line', 'belgacomfon', 'login'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['fon=fon.cli:main'],
    }
)
