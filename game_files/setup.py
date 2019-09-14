from setuptools import setup, find_packages

import game_files

setup(name="Adventure Game",

    version=game_files.__version__,
    description=(""),

    author="Arthur Abreu & Lucas Motta",
    author_email="arthurabreu@id.uff.br,"
                   "lucas_motta@id.uff.br",

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'command = dest:funcx'
                            ]
    }
)
