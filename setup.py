from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="cancerdetection",
    version="0.0.1",
    author="",
    author_email="",
    description="Kaggle - RSNA Screening Mammography Breast Cancer Detection",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mariomc2/cancerdetection",
    packages=find_packages(include=["src"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
)