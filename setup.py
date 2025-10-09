from setuptools import setup

setup(
    name="pystablemotifs",
    version="3.0.6",
    author="Jordan Rozum",
    author_email="jcr52@psu.edu",
    description="Python package for analyzing Boolean Netowrk",
    url="https://github.com/jcrozum/pystablemotifs",
    license="MIT",
    python_requires=">=3.5",
    packages=["pystablemotifs"],
    install_requires=[
        "pyboolnet @ git+https://github.com/hklarner/pyboolnet#egg=3.0.16",
        "networkx >= 2.4.0",
        "sympy >= 1.5.1",
        "pandas >= 1.0.0",
        "numpy >= 1.19.2",
        "matplotlib >= 3.2.1",
    ],
)
