from setuptools import setup

setup(
    name="sh_cryptographic_mod_loader",
    license=open("LICENSE").read(),
    version="0.1.0",
    packages=["src"],
    install_requires=["sh-mod-loader==0.0.1"],
    author="SeniorShadifer",
    description="Simple ModLoader for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SeniorShadifer/CryptographicModLoader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
