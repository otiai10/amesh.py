from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='amesh',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='みんな大好き東京アメッシュ',
    author='Hiromu OCHIAI',
    author_email='otiai10@gmail.com',
    url='https://github.com/otiai10/amesh.py',
    keywords=['amesh', 'python'],
    install_requires=requirements,
    scripts=[
        'bin/amesh'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
