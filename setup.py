from setuptools import setup


setup(
    name='lutz_demo',
    version='0.0.1',
    description='Interpretation of some examples from "Programming in Python" '
                'book by Mark Lutz',
    author='Valerii Kovalchuk',
    author_email='kovvalole@gmail.com',
    url='https://github.com/pannkotsky/lutz_demo',
    packages=['demo'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'person-list = demo.shell:person_list',
            'person-get = demo.shell:person_get',
            'person-add = demo.shell:person_add'
        ]
    },
    classifiers=[
        'Programming Language :: Python3',
    ],
)