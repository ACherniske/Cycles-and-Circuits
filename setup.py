from setuptools import setup, find_packages

setup(
    name="cycles-and-circuits",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "networkx>=2.8.0",
        "matplotlib>=3.5.0",
    ],
    description="A tool for generating and analyzing graphs",
    author="Aiden Pearce Cherniske",
)