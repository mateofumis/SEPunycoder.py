from setuptools import setup, find_packages

setup(
    name='sepunycoder',
    version='3.0.0',
    packages=find_packages(),
    description='A simple script to convert normal-text to Cyrillic-text. This allows hackers to obfuscate text in puny-code format which can lead into a lot of multiple Phishing attacks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mateofumis/SEPunycoder.py',
    author='Mateo Fumis',
    author_email='mateofumis1@gmail.com',
    include_package_data=True,
    package_data={'sepunycoder': ['punycode_chars.json']},
    entry_points={
        'console_scripts': [
            'sepunycoder=sepunycoder.main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
