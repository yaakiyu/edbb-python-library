from setuptools import setup
import edbb

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name="edbb",
    version=edbb.__version__,
    author="yaakiyu",
    author_email="yaakiyu.yaakiyu@gmail.com",
    description="EDBB Python Package",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["edbb"],
    install_requires=["discord.py", "python-dotenv"],
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)