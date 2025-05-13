from setuptools import find_packages, setup

setup(
    name="medical-chatbot-GALE",
    version="0.0.1",
    author="Sean Spencer",
    author_email="seang.spencer@mail.utoronto.ca",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "pandas",
        "numpy",
        "scikit-learn",
        "nltk",
        "beautifulsoup4",
        "requests",
        "python-dotenv",
        "tqdm"
    ])