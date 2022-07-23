import io
from os import path
from setuptools import find_packages, setup

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()
#Setup
setup(
    name='pyapp',
    version=1.0,
    description='A simple utility to create project structure',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Devansh Batham',
    license='Apache-2.0 License',
    packages=find_packages(),
    classifiers=[
        'Topic :: Performance',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pyapp = pyapp.pyapp:main'
        ]
    },
    keywords=['pyapp']
)
