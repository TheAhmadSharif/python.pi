from setuptools import find_packages, setup

setup(
    name="test1014",
    version="0.0.4",
    description="A small example package",
    author="ahmadsharif",
    author_email="theahmadsharif@gmail.com",
    license="MIT",
    url="https://github.com/theahmadsharif",
    entry_points={"console_scripts": ["test1014=test1014.__main__:main"]},
    install_requires=[
        "numpy",
    ],
    packages=find_packages(),
)
