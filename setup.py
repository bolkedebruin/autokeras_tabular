from distutils.core import setup
from setuptools import find_packages

setup(
    name='autokeras_tabular',
    packages=find_packages(exclude=('tests',)),
    install_requires=['autokeras==0.3.7',
                      'lightgbm==2.2.3',
                      'numpy==1.16.1',],
    version='0.3.7',
    description='AutoML Tabular addon for deep learning',
    author='Original Author: DATA Lab at Texas A&M University',
    author_email='bdbruin@gmail.com',
    url='http://github.com/bolkedebruin/autokeras-tabular',
    download_url='https://github.com/bolkedebruin/autokeras_tabular/archive/0.3.7.tar.gz',
    keywords=['AutoML', 'keras', 'tabular'],
    classifiers=[]
)