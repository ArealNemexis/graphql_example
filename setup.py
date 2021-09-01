from setuptools import setup, find_packages

dev_requirements = [
    'pylint',
    'loguru'
]

requiriments = [
    'graphene>=2.0',
    'graphql-core<3',
    'fastapi',
    'uvicorn[standard]',
    'pymongo==3.12.0'
]

NAME = 'hello_graphQL'
VERSION = '0.0.1'
setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=requiriments,
    extras_require={
        'dev': dev_requirements,
    }
)
