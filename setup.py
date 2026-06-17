from setuptools import find_packages,setup
# it will automatically find all the list of packages available in the 
# machine learning application

# setup consists of the parameters of the projects.

from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup (

name = "mlproject",
version="0.0.1",
author="Ketan Nibandhe",
author_email="nibandheketn2354@gmail.com",
packages = find_packages(),
# what find_packages do is that in the project folders it will searh for which folders
# have __init.py file and that folders will be considered as a packages
#entire project developement will happeninside the src folder
install_requires=get_requirements('requirement.txt'),

)


