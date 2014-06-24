from setuptools import setup

setup(
    name='t',
    version='0.10',
    py_modules=['t'],
    description='t is a unix command-line todo app',
    url='http://github.com/itsnauman/t',
    author='Nauman Ahmad',
    author_email='nauman-ahmad@outlook.com',
    license='MIT',
    include_package_data=True,
    install_requires=[
        'termcolor',
        'docopt',
        'prettytable',
    ],
    entry_points='''
        [console_scripts]
        t=t:main
    ''',
)
