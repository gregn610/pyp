import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)

        errno = tox.cmdline(args=args)
        sys.exit(errno)

cwd = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(cwd, 'README.md')) as f:
        README = f.read()
except IOError:
    README = ''

tests_require = [
    'tox',
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
    install_requires=[
        'six',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=tests_require,
    test_suite="tests",
    cmdclass={'test': Tox},
)
