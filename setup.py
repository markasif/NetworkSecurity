from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """
    This function helps to return the list of requirenments
    """
    requirement_list:List[str]=[]
    try:
        with open("requirenment.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements!= '.e':
                    requirement_list.append(requirements)
    except FileNotFoundError:
        print("File not Found")

    return requirement_list

setup(
    name="CyberSecurity",
    version="0.0.1",
    author="Mohammed Asif",
    author_email="apasif243@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement()
)