from setuptools import setup, find_packages

setup(
    name="jason-lee-tools",
    version="0.3.0",
    author="Jason Lee",
    author_email="master@lifang.fun",
    description="sdk for ali(Jason Lee)'s environment",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/neulf/ali-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],
)
