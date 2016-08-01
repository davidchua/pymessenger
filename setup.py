from setuptools import setup
setup(
  name = 'pymessenger',
  packages = ['pymessenger'],
  version = '0.0.6.0',
  install_requires=[
        'requests',
        'requests-toolbelt',
        'six'
  ],
  description = "Python Wrapper for FB Messenger Bot",
  author = 'David Chua',
  author_email = 'zhchua@gmail.com',
  url = 'https://github.com/davidchua/pymessenger',
  download_url = 'https://github.com/davidchua/pymessenger/tarball/0.0.6',
  keywords = ['facebook messenger', 'python', 'wrapper', 'bot', 'messenger bot'],
  classifiers = [],
)
