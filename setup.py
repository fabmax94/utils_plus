import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils-functions-plus", # Replace with your own username
    version="0.0.6",
    author="Fabio Alexandre",
    author_email="famhs@ecomp.poli.br",
    description="A set of auxiliary functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fabmax94/utils_plus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)