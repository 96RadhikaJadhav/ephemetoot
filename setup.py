from setuptools import setup, find_packages

setup(name='ephemetoot',
      version='2.0.0',
      url='https://github.com/hughrun/ephemetoot',
      license='GPL-3.0-or-later',
      packages=find_packages(),
      scripts=['bin/ephemetoot'],
      install_requires=['Mastodon.py', 'pyyaml'],
      zip_safe=False,
      author='Hugh Rundle',
      author_email='hugh@hughrundle.net',
      description='A command line tool for selectively deleting old toots.',
      keywords='mastodon, mastodon api',
      project_urls={
        'Source Code': 'https://github.com/hughrun/ephemetoot',
        'Documentation': 'https://github.com/hughrun/ephemetoot'
      }
)