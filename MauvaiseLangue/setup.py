from setuptools import setup, find_packages

setup(
    name='MauvaiseLangue',
    version='1.0.8',  # Incremented version
    description='A Python module to scrape French insults from Wiktionary',
    author='john waia',
    author_email='johnwaia25@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,  # To include files like cache if needed
)
