from setuptools import setup

setup(name='gooh',
      version='1.0.0',
      description='Language agnostic semantic versioner using git tags',
      url='http://github.com/lxhunter/gooh',
      author='Alexander Jäger',
      author_email='alexander.jaeger@me.com',
      license='MIT',
      scripts=['bin/gooh'],
      packages=['gooh'],
      zip_safe=False
      )
