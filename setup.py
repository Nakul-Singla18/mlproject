from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        requirements = [req for req in requirements if not req.startswith('-e ')]  # Remove '-e .' if present
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Nakul',
    author_email='singlanakul632@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
