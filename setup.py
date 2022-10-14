import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.readlines()

setup(
    name='molecalc',
    version='0.1',
    description='MoleCalc',
    author='Sean L Seyler',
    author_email='slseyler@asu.edu',
    keywords='web chemistry asu gamess quantum',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = molecalc:main',
        ],
    },
)
