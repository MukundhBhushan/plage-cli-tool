from setuptools import setup

setup(

    name="plage",

    version="1.0.5",

    description="plage",

    long_description_content_type="text/markdown",

    #url='https://github.com/NebutechOpenSource/MLGen',

    author="Mukundh Bhushan",

    author_email="aknsmb@gmail.in",

    license="MIT",

    classifiers=[ 

    'Development Status :: 3 - Alpha',



    # Indicate who your project is intended for

    'Intended Audience :: Developers',

    'Topic :: Software Development :: Build Tools',



    # Pick your license as you wish

    "License :: OSI Approved :: MIT License",



    # Specify the Python versions you support here. In particular, ensure

    # that you indicate whether you support Python 2, Python 3 or both.

    'Programming Language :: Python :: 3',

    'Programming Language :: Python :: 3.4',

    'Programming Language :: Python :: 3.5',

    'Programming Language :: Python :: 3.6',

    'Programming Language :: Python :: 3.7',

  ],

    packages=["plage"],

    include_package_data=True,

    install_requires=["googletrans"],

    entry_points={

        "console_scripts": [

            "plage = plage.__main__:main",

        ]

    },

)