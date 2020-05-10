import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py4knn",
    version="0.0.3",
    author="Mgs. M. Luthfi Ramadhan",
    author_email="luthfir96@gmail.com",
    description="K-Nearest Neighbors Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luthfi118/py4knn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
