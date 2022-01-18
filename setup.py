import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='vultr-python',
    version='0.1.5',
    description='Python 3 wrapper for the Vultr API v2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cssnr/vultr-python',
    author='Shane',
    author_email='shane@sapps.me',
    py_modules=['vultr'],
    install_requires=['requests'],
    python_requires='>=3.5',
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    project_urls={
        'Documentation': 'https://vultr-python.sapps.me/',
        'Source': 'https://github.com/cssnr/vultr-python',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
