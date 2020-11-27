import setuptools

setuptools.setup(
    name='newsarchives',
    version='0.1.1',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='The official python wrapper for the News Archives API',
    long_description='The official pytho',
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/News-Archives',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ]
)