from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flask-pocket",
    version="1.0.2", 
    py_modules=["flask_pocket"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "pocketbase"
    ],
    description="Flask extension to integrate PocketBase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="codewithmpia",
    author_email="codewithmpia@gmail.com",
    url="https://github.com/codewithmpia/flask_pocket",
    project_urls={
        "Source": "https://github.com/codewithmpia/flask_pocket",
        "Tracker": "https://github.com/codewithmpia/flask_pocket/issues",
        "Author": "https://github.com/codewithmpia",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Flask"
    ],
)