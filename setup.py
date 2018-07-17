from setuptools import setup

setup(
    name='masonite_deploy',
    packages=[
        'masonite_heroku',
        'masonite_heroku.commands',
        'masonite_heroku.providers',
    ],
    version='0.0.1',
    install_requires=[], 
    description='Masonite deployment for Heroku',
    author='Joseph Mancuso',
    author_email='idmann509@gmail.com',
    url='https://github.com/MasoniteFramework/masonite',
    keywords=['python web framework', 'python3', 'masonite'],
    classifiers=[],
    include_package_data=True,
)
