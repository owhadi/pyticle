import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='pyticle',
    version='0.0.3',
    author='Moein Kareshk',
    author_email='mkareshk@outlook.com',
    description='A Python Library for Particle Swarm Intelligence',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/owhadi/pyticle',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['tabulate', 'numpy', 'imageio', 'matplotlib', 'joblib', 'pandas'],
    python_requires='>=3.6',
)
