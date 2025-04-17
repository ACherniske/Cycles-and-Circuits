from setuptools import setup, find_packages

setup(
    name="Cycles and Circuits",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "networkx>=2.8.0",
        "matplotlib>=3.5.0",
    ],
    entry_points={
        'console_scripts': [
            'run=graph_analysis.cli:main',
        ],
    },
    description="A tool for generating and analyzing graphs",
    author="Aiden Pearce Cherniske",
)