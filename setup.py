from setuptools import setup

installation_requirements = ['requests', 'requests-toolbelt', 'six']

try:
    import enum
    del enum
except ImportError:
    installation_requirements.append('enum')

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='pymessenger2',
    packages=['pymessenger2'],
    version='2.0.0',
    install_requires=installation_requirements,
    description="Python Wrapper for Facebook Messenger Platform",
    long_description=long_description,
    author='Charles Crete',
    author_email='cretezy@gmail.com',
    url='https://github.com/Cretezy/pymessenger2',
    license='MIT',
    download_url='https://github.com/Cretezy/pymessenger2/archive/v2.0.0.tar.gz',
    keywords=[
        'facebook messenger', 'python', 'wrapper', 'bot', 'messenger bot'
    ],
    classifiers=[], )
