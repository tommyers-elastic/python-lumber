import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="python-lumber",
    version="0.1a",
    description="A lumberjack client for Logstash",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tom Myers",
    author_email="thomas.myers@elastic.co",
    classifiers=[
        "License :: OSI Approved :: Apache License 2.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires=">=3.7, <4",
    install_requires=[
        'ujson==5.4.0',
    ],
    extras_require={
        "dev": ["pytest", "pytest-benchmark", "requests", "twine", "wheel"],
    },
)
