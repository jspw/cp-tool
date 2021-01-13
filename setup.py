import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cp-tool",
    version="1.0.1",
    author="jspw",
    author_email="mhshifat757@gmail.com",
    description="**cp-tool** is an auto generator for solved problems at different online judges.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    license="GNU",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "cp-tool=cpTool.__main__:main",
        ]
    },
)