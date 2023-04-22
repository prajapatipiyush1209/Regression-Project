from setuptools import find_packages, setup
from typing import List



HIFEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path, 'r') as f :
        read_requirements = f.readlines()
        read_requirements = [i.replace("\n", "") for i in read_requirements]
        if HIFEN_E_DOT in read_requirements:
            read_requirements.remove(HIFEN_E_DOT)

    return read_requirements



setup (name= 'RegressionProject',
       version = '0.0.1',
       author="Piyush Prajapati",
       author_email="prajapatipiyush1209@gmail.com",
       packages=find_packages(),
       install_requires = get_requirements('requirements.txt')
)



