import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cutsets",
    version="1.4",
    author="Umair Siddique",
    author_email="umair.siddique@example.com",
    url="https://github.com/iamumairs/fault-tree-mcs",
    project_urls={
        "Bug Tracker": "https://github.com/iamumairs/fault-tree-mcs/issues",
        "Documentation": "https://github.com/iamumairs/fault-tree-mcs#readme",
        "Source Code": "https://github.com/iamumairs/fault-tree-mcs",
    },
    description="Computation of minimal cutsets using MOCUS Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="fault tree MOCUS minimal cutsets reliability analysis safety",
    python_requires=">=3.6",
    py_modules=["cutsets"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": ["pytest>=6.0", "black>=21.0", "flake8>=3.9"],
    },
)