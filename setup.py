from setuptools import find_packages, setup
from typing import List


hypen_e= '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[i.replace('\n','') for i in requirements]
        
        if hypen_e in requirements:
            requirements.remove(hypen_e)

setup(
    name='diamondpriceprediction',
    version='0.0.1',
    author='rajan',
    author_email='rajansingh387@gmail.com',
    install_requires= get_requirements('requirements.txt'),
    packages=find_packages()
)