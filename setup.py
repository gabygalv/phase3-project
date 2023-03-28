from setuptools import setup, find_packages

setup(
    name = 'encounter_counter',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points = '''
    [console_scripts]
    encounter=encounter_counter:encounter_counter
    '''
)