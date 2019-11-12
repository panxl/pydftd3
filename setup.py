"""
Wrapper for the DFTD3 program
"""
from setuptools import setup


short_description = __doc__.split("\n")

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = "\n".join(short_description[2:])

setup(
    name="pydftd3",
    version="1.0",
    author="Xiaoliang Pan",
    author_email="panxl@panxl.net",
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panxl/pydftd3",
    packages=["pydftd3"],
    package_data={"pydftd3": ["libdftd3.so"]},
    zip_safe=False,
)
