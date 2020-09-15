import setuptools

setuptools.setup(
    name="flightaware-history-rolandcrosby",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=["lxml>=4.5", "MechanicalSoup>=0.12"],
    python_requires=">=3.8",
)