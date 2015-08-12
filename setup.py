import os

from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(cwd, 'README.md')) as f:
        README = f.read()
except IOError:
    README = ''

tests_require = [
    'mock',
]

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
]

setup(
    name='pyp',
    version='2.12',
    description='The Pyed Piper - python cli pipping',
    long_description=README,
    classifiers=classifiers,
    author="Tony Rosen",
    author_email="tobyrosen@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        'testing': [
            'tox',
            'nose',
        ]
    },
    zip_safe=False,
    tests_require=tests_require,
    test_suite="tests",
)
