from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read()

setup(name='coinrpc',
      version='0.0.1',
      author='zzzzlzzzz',
      author_email='zzzzlzzzz@yandex.com',
      description='Simple and tiny coin rpc library',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/zzzzlzzzz/coinrpc',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      install_requires=requirements,
      )
