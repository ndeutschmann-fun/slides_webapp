import setuptools

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slides", # Replace with your own username
    version="0.1",
    author="Nicolas Deutschmann",
    description="Javascript slide web-app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ndeutschmann-fun/slides_webapp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True
)