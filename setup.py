from setuptools import setup

add_keywords = dict(
    entry_points={
        'console_scripts' : ['caesar=caesar.mail:main'],
    },)

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.md')
    long_description = fhan.read()
    fhan.close()


setup(
    name ='caesar',
    version='0.1.1',
    packages=['caesar'],
    license='GPLv3',
    description="",
    long_description=long_description,
    url='https://github.com/tanjot/caesar',
    author='Tanjot Kaur',
    author_email="tanjot28@gmail.com",
    install_requires=requires,
    **add_keywords
)



