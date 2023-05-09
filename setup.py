import setuptools

#Let us store all the info inside the readme file in the
#long description variable. This description will be shown in test.pypi webiste
with open("README.md",'r') as fh:
    long_description=fh.read()

setuptools.setup(
    name='rv_curve_jura',
    version='0.1',
    author='Jean Hayoz',
    author_email='jeanhayoz94@gmail.com',
    description='Plot all RV curves that you want!',
    packages=setuptools.find_packages(),
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='git@github.com:JHayoz/package_jura_rv_curve_jean',
    install_requires=['numpy','matplotlib'],
    classifiers=['Programming Language :: Python :: 3'],
)