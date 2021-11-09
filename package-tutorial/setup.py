import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-Builder212",
    version="0.1.4",
    author="Builder212",
    description="A test package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Buidler212/package_tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
