from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
VERSION = "0.0.5"

setup(
    name="sshm",
    version=VERSION,
    description="A SSH Identity Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ssh identity manager",
    author="RhythmLian",
    url="https://github.com/Rhythmicc/sshm",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["Qpro"],
    entry_points={
        "console_scripts": [
            "sshm = sshm.main:main",
        ]
    },
)
