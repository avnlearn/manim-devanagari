import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="manim_devangari",
    version="1.0",
    author="AvN Learn",
    author_email="avnlearn@gmail.com",
    description="A package for manim",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package=setuptools.find_packages(),
    install_requires=["mamin"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
