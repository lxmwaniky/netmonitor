from setuptools import setup, find_packages

setup(
    name="netmonitor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "python-nmap>=0.7.1",
        "speedtest-cli>=2.1.3",
        "psutil>=5.9.5",
        "requests>=2.32.3",
        "netifaces>=0.11.0"
    ],
    entry_points={
        'console_scripts': [
            'netmonitor=monitor:main',
        ],
    },
    python_requires=">=3.9",
    include_package_data=True,
)