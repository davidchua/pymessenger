from setuptools import setup

installation_requirements = [
    'requests',
    'requests-toolbelt',
    'six'
]

try:
    import enum
    del enum
except ImportError:
    installation_requirements.append('enum')

setup(
    name='pymessenger',
    packages=['pymessenger'],
    version='1.0.1',
    install_requires=installation_requirements,
    description="Python Wrapper for Facebook Messenger Platform",
    author='David Chua, Felix Clone',
    author_email='zhchua@gmail.com',
    url='https://github.com/felixcheruiyot/pymessenger/',
    download_url='https://github.com/felixcheruiyot/pymessenger/tarball/master',
    keywords=['facebook messenger', 'python', 'wrapper', 'bot', 'messenger bot'],
    classifiers=[],
)
