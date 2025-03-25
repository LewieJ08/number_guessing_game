from setuptools import setup, find_packages

setup(
    name="number_guessing_game",
    version="1.0.0",
    packages=find_packages(),  # Automatically finds package directories
    install_requires=[],  # No external dependencies needed
    entry_points={  
        "console_scripts": [
            "number-guessing-game=number_guessing_game.main:main"  # Links CLI command to main()
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple CLI based number guessing game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/number_guessing_game",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)