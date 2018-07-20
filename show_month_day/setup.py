import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="show_month_day",
    version="0.0.1",
    author="Tom",
    author_email="s099064146@gmail.com",
    description="Input string of starting year, month, date and ending year, month, date.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s099064146/Practice",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)