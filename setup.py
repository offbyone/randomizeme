from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='randomizeme',
      version=version,
      description="iTunes Playlist Randomizer",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='itunes music',
      author='Chris Rose',
      author_email='offline@offby1.net',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
