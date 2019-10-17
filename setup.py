from setuptools import setup

NAME = "sheetload"
VERSION = "1.0.0rc2"
DESCRIPTION = """
                sheetload is a command line tool to load sheets from google
                and upload them to snowflake
                """
REQUIRED = [
    "data_tools @ git+ssh://git@github.com/tripactions/Data_Tooling.git@v1.9.1",
    "pandas",
    "pyyaml",
    "bumpversion",
]
REQUIRES_PYTHON = ">=3.6.0"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author="Bastien Boutonnet",
    author_email="bastien.b1@gmail.com",
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    entry_points={"console_scripts": ["sheetload=sheetload.sheetload:run"]},
)
