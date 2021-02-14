import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cutsets",                     
    version="1.2",                       
    author="Umair Siddique",                 
    url="https://github.com/iamumairs/fault-tree-mcs",
    description="Computation of minimal cutsets using MOCUS Algorithm",
    long_description=long_description,     
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    licence="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',          
    py_modules=["cutsets"],           
    package_dir={'':'src'},      
    install_requires=["pandas"]
)