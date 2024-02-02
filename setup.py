from setuptools import setup, find_packages
from client.client import Client

Client = Client

setup(
    name = 'freecel-api',
    version = '0.1',
    packages = find_packages()
)
