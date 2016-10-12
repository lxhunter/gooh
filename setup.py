from setuptools import setup

setup(name='gooh',
      version='1.0.5',
      description='Language agnostic semantic versioner using git tags',
      url='http://github.com/lxhunter/gooh',
      download_url = 'http://github.com/lxhunter/gooh/tarball/1.0.5',
      author='Alexander Jaeger',
      author_email='alexander.jaeger@me.com',
      license='MIT',
      scripts=['bin/gooh'],
      zip_safe=False,
      install_requires=[
          'semantic_version', 'sh', 'PyYAML']
      )
