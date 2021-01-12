from setuptools import setup, find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    long_description = f.read()

setup(
    name="certbot-plugin-duckdns",
    version="0.0.1",
    author="Lennart K",
    description="Certbot plugin for DuckDNS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lennart-k/certbot-plugin-duckdns",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    install_requires=[
        "certbot",
        "requests",
        "zope.interface"
    ],
    entry_points={
        "certbot.plugins": [
            "duckdns = certbot_plugin_duckdns.dns:Authenticator"
        ]
    }
)
