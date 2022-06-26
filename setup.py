from setuptools import find_packages, setup


setup(
    name='freecad_aplan_benchmark',
    version='0.0.1',
    author='Martijn Cramer',
    author_email='martijn.cramer@outlook.com',
    packages=find_packages(),
    url='https://github.com/martcram/FreeCAD-APLAN-benchmark',
    license='LGPL-2.1',
    description='Package for benchmarking FreeCAD APLAN\'s solvers',
    long_description=open('README.md').read(),
    install_requires=[]
)
