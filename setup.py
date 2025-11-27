from setuptools import setup
import edbb


setup(
    name="edbb",
    version=edbb.__version__,
    author="yaakiyu",
    author_email="yaakiyu.yaakiyu@gmail.com",
    description="EDBB Python Package",
    packages=["edbb"],
    install_requires=["discord.py", "python-dotenv"],
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)