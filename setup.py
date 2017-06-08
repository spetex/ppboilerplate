try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Python Project Boilerplate',
    'description': 'Opinionated python project setup',
    'author': 'Petr Sahula',
    'license': 'BSDv3',
    'url': 'https://www.github.com/spetex/python-project-boilerplate',
    'download_url': 'https://www.github.com/spetex/python-project-boilerplate',
    'author_email': 'pete.sahula@icloud.com',
    'version': '1.0',
    'packages': ['ppboilerplate'],
    'scripts': [],
    'test_suite': 'tests',
    'setup_requires': ['pytest_runner'],
    'tests_require': ['pytest'],
}

setup(**config)
