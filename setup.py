from setuptools import find_packages, setup
from typing import List

DASH_e_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    
    # //This function will return the requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n','')for req in requirements]

        if DASH_e_DOT in requirements:
            requirements.remove(DASH_e_DOT)
    return requirements
        
setup(
name = 'ML_PROJECT',
version = '0.0.1',
author='rohan',
author_email='rohanpurohit70@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)



