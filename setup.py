from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='pycovid19',
    version='0.1.1',
    description='Protect you jupyter notebook from COVID19',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Sobir Bobiev',
    author_email='sobir.bobiev@gmail.com',
    keywords=['Jupyter Notebook', 'COVID19', 'Protective Masks'],
    url='https://github.com/sobir-git/pycovid19',
    download_url='https://pypi.org/project/pycovid19/'
)

install_requires = [
    'ipython>=5.0.0',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data=True)
