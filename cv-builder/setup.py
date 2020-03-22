from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='cv-builder',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="build template cvs",
    license="Proprietary",
    author="ansir",
    author_email='Email Address',
    url='https://github.com/cvbuilder1/cv-builder',
    packages=['cv-builder'],
    entry_points={
        'console_scripts': [
            'cv-builder=cv-builder.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='cv-builder',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
