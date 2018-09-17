from setuptools import setup

if __name__ == '__main__':
  setup(
    name='circle',
    version='1.0.0',
    author='Tadahiro Yamamura',
    license='MIT License',
    install_requires=['click', 'sqlalchemy'],
    packages=['circle'],
    entry_points={
      'console_scripts': ['circle = circle.cli:cli']
    }
  )
