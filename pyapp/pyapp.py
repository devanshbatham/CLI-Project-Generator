import os
import argparse


PROJECT_FILE = """
import argparse


def main():
    parser = argparse.ArgumentParser(description='CLI for PROJECT_NAME')
    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()
    print('CLI for PROJECT_NAME')
"""


SETUP_TEMPLATE = """
import io
from os import path
from setuptools import find_packages, setup

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='PROJECT_NAME',
    version=1.0,
    description='PROJECT_DESCRIPTION',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='PROJECT_AUTHOR',
    license='Apache-2.0 License',
    packages=find_packages(),
    classifiers=[
        'Topic :: Misc',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'PROJECT_NAME = PROJECT_NAME.PROJECT_NAME:main'
        ]
    },
    keywords=['PROJECT_NAME']
)
"""


def project_details():
    PROJECT_NAME = input("Project Name: ").strip()
    PROJECT_AUTHOR = input("Author: ").strip()
    PROJECT_DESCRIPTION = input("Description: ").strip()

    # create project directory in current working directory
    os.mkdir(PROJECT_NAME)
    
    # open directory PROJECT_NAME and create empty __init__.py
    with open(f'{PROJECT_NAME}/__init__.py', 'w') as f:
        f.write('')

    # open directory PROJECT_NAME and create empty PROJECT_NAME.py
    with open(f'{PROJECT_NAME}/{PROJECT_NAME}.py', 'w') as f:
        f.write(PROJECT_FILE)
    

    # make empty files README.md and LICENSE in current working directory
    with open('README.md', 'w') as f:
        f.write(PROJECT_DESCRIPTION)
    with open('LICENSE', 'w') as f:
        f.write('')

    SETUP_TEMP = SETUP_TEMPLATE.replace("PROJECT_NAME", PROJECT_NAME)
    SETUP_TEMP1 = SETUP_TEMP.replace("PROJECT_AUTHOR", PROJECT_AUTHOR)
    SETUP_TEMP2 = SETUP_TEMP1.replace("PROJECT_DESCRIPTION", PROJECT_DESCRIPTION)

    # create setup.py in current working directory and write SETUP_TEMP2

    with open('setup.py', 'w') as f:
        f.write(SETUP_TEMP2)


def main():
    # argparse stuff, store true
    parser = argparse.ArgumentParser(description='PyApp - A utility to create python CLI project structure')
    parser.add_argument('-i', '--init', action='store_true')
    args = parser.parse_args()

    # init
    if args.init:
        print('init started')
        project_details()
    else:
        print('init failed')




if __name__ == '__main__':
    main()