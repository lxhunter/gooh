import os
import sys

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "1.0.7"

def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
      name='gooh',
      version=VERSION,
      description='Language agnostic semantic versioner using git tags',
      url='http://github.com/lxhunter/gooh',
      download_url = 'http://github.com/lxhunter/gooh/tarball/1.0.6',
      author='Alexander Jaeger',
      author_email='alexander.jaeger@me.com',
      license='MIT',
      scripts=['bin/gooh'],
      zip_safe=False,
      install_requires=[
          'semantic_version',
          'sh',
          'PyYAML'
          ],
      cmdclass={
            'verify': VerifyVersionCommand,
      }
)
