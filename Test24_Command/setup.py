from setuptools import find_packages, setup

setup(
    name="Test24",
    version="0.0.1",
    description="Python package",
    author="Ahmad Sharif",
    author_email="theahmadsharif@gmail.com",
    license="MIT",
    entry_points={"console_scripts": ["Test24=Test24.__main__:main"]},
    packages=find_packages(),
)
