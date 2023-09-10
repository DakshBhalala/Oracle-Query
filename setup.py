from setuptools import setup, find_packages

# Package metadata
PACKAGE_NAME = 'oracuery'
VERSION = '1.1.0'
DESCRIPTION = 'Python module for generating SQL queries'
LONG_DESCRIPTION = '''
Oracuery is a comprehensive Python module that simplifies database interaction by providing a set of powerful functions to generate SQL queries effortlessly. Whether you're working with databases in your web application, data analysis project, or any Python-based application, oracuery streamlines the process, saving you time and reducing the complexity of writing SQL queries.
'''

# Author information
AUTHOR = 'BDAKSHP'
AUTHOR_EMAIL = 'bhalaladaksh613@gmail.com'

# Package dependencies (NONE)
INSTALL_REQUIRES = []

# Package distribution details
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    url='https://github.com/DakshBhalala/Oracle-Query.git',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
    ],
    keywords='SQL database query',
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/DakshBhalala/Oracle-Query/blob/main/README.md',
        'Source Code': 'https://github.com/DakshBhalala/Oracle-Query',
        'Bug Tracker': 'https://github.com/DakshBhalala/Oracle-Query/issues',
    },
    entry_points={
        'console_scripts': [
            'oracuery-cli = oracuery.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.sql'],  # Include SQL files in the package
    },
    zip_safe=False,
    platforms=['any'],
    extras_require={
        'dev': [
            'pytest',
            'sphinx',
            'coverage',
        ],
    },
)
