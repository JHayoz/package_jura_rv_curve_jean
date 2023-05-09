import setuptools

setuptools.setup(
    name='rv_curve_jura',
    version='0.1',
    author='Jean Hayoz',
    author_email='jeanhayoz94@gmail.com',
    description='Plot all RV curves that you want!',
    packages=setuptools.find_packages(),
    install_requires=['numpy','matplotlib'],
    classifiers=['Programming Language :: Python :: 3'],
)