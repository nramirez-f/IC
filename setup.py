from setuptools import setup

setup(
    name="initial_conditions",
    version="0.0",
    py_modules=["__init__", "scalar"],
    install_requires=["numpy"],
    author="Nramirez",
    description="Initial Conditions for Numerical Methods",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nramirez-f/IC",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)