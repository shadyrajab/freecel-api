from setuptools import setup, find_packages
from client.client import Client

Client = Client

setup(
    name = 'freecel',
    version = '0.1',
    packages = find_packages(),
    author = 'Shady Rajab',
    install_requires = [
        'pandas'
    ]
)
