# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kt18datav2", # the name that you will install via pip
    version="1.0",
    author="KT",
    author_email="term1830@gmail.com",
    description="Testing fuction",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/term1830/function3unit",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)