from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
    #this fn returns list of requirments
    requirments=[]
    with open(file_path) as  file_obj:
        requirments=file_obj.readlines()
        [req.replace("\n"," ") for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
            
    

setup(
    name='Trend_ML',
    version='0.0.1',
    author='viswa_tej'
    author_email='boyalaguntaviswa0009@gmail.com'
    packages=find_packages(),
    install_requires=get_requirments('requirments.tx')
    
    
)