'''
Installation script.
'''

'''
TODO:
    - pyodbc based on os
    - rename framework folder to something else
'''

from setuptools import setup, find_packages

setup(
    name="sample_module",
    version="1.0",
    # packages=find_packages(exclude=['notebooks/*', 'docs/*']),
    py_modules=['sample_module'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        # 'pyodbc',
        'pandas',
        'numpy',
        'scipy',
        'scikit-learn'
    ],

    packages=['sample_module'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.rst'],
    },

    # metadata for upload to PyPI
    # author="Me",
    # author_email="me@example.com",
    # description="This is an Example Package",
    # license="PSF",
    # keywords="hello world example examples",
    # url="http://example.com/HelloWorld/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
