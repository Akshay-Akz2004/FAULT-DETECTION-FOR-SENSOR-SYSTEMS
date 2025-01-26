from setuptools import find_packages,setup
from typing import List

def get_requriements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements

setup(
    name="Fault detection on semiconductor systems",
    version='0.0.1',
    author='Akshay',
    author_email='akshayfrancis891@gmail.com',
    install_requirements=get_requriements('requirements.txt'),
    packages=find_packages(),
)