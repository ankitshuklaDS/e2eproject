from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

    return requirements


setup(name="e2eproject",
      version="0.01",
      description="This is e2e project",
      author="Ankit Shukla",
      author_email="ntssp2011@gmail.com",
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
)
