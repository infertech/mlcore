from setuptools import setup, find_packages
from os import path

base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mlcore',
    version='0.0.0',

    description='Library for MLCore platform usage',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/intropy-developers/mlcore',
    author='Intropy',
    author_email='intropy.official@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='machine-learning',
    packages=find_packages(),
    python_requires='>=3.7,<4',
)
