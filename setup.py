from setuptools import setup

installation_requirements = ['requests', 'requests-toolbelt', 'six']

try:
    import enum
    del enum
except ImportError:
    installation_requirements.append('enum')

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()


setup(
    name='pymessenger2',
    packages=['pymessenger2'],
    version='3.0.3',
    install_requires=required,
    description="Python Wrapper for Facebook Messenger Platform",
    long_description=long_description,
    author='Charles Crete',
    author_email='cretezy@gmail.com',
    url='https://github.com/Cretezy/pymessenger2',
    license='MIT',
    download_url='https://github.com/Cretezy/pymessenger2/archive/v3.0.3.tar.gz',
    keywords=[
        'facebook messenger', 'python', 'wrapper', 'bot', 'messenger bot'
    ],
    classifiers=[], )
