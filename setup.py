from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.8"
DESCRIPTION = "A python module for friend.tech"
LONG_DESCRIPTION = "friendtech modules enables developers to featch info and intereact with friendtech platform using python"
# Setting up
setup(
    name="friendtech",
    version=VERSION,
    author="ItsAditya (https://itsaditya.xyz)",
    author_email="<chaudharyaditya0005@gmail.com>",
    description="A python module for friend.tech",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages("web3"),
    install_requires=[],
    keywords=[
        "friend.tech",
        "social media",
        "crypto",
        "decentralized social media"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
