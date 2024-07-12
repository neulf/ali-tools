from setuptools import setup, find_packages

setup(
    name="ali-tools",
    version="0.1.0",
    author="Jason Lee",
    author_email="master@lifang.fun",
    description="sdk for ali's environment",
    long_description=open('README.md.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/neulf/ali-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests'
    ],
)
