import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='automated_checklist_utils',
    version="0.0.1",
    author="Fabio Alexandre",
    author_email='fabio.silva@samsung.com',
    description="A set of auxiliary functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.sec.samsung.net/SIDIA-REQ/automated_checklist_utils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
