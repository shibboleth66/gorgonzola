import setuptools

# Versioning Info
major = '0'
minor = '1'
patch = '3'

# Set semantic version
version = ".".join([major, minor, patch])

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gorgonzola",
    version=version,
    author="Ben Gallagher",
    author_email="shibboleth@me.com",
    description="AWS Boto3 helper functions for multi-account control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shibboleth66/gorgonzola",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'boto3>=1.9.96'
    ]
)

# Execute this with the following command.
# python setup.py sdist bdist_wheel
