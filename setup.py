from setuptools import setup

setup(
    name='representjs',
    version='1.0',
    packages=["representjs"],
    python_requires=">=3.7",
    install_requires=[
        "fire",
        "graphviz",
        #"jsbeautifier",
        "jsonlines",
        "pyjsparser",
        #"tqdm==4.50.0",
        #"requests",
        "regex",
        "loguru",
        "pyarrow",

        # Data
        "matplotlib",
        "numpy",
        #"pandas",
        "seaborn",

        # PyTorch
        "pytorch-lightning",
        #"torch",
        "torchtext",
        "wandb",

        # NLP dependencies
        #"sentencepiece",
        "sacremoses",
        #"transformers>=2.5.1",
        #"tokenizers",
        "datasets",
    ],
    extras_require={"test": ["pytest"]}
)
