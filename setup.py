from setuptools import setup

installation_requirements = [
    "openai-agents==0.13.1",
    "loguru==0.7.3",
    "neo4j==5.28.3",
    "google-genai==1.68.0"
]

setup(
    version="1.9",
    name="freeflock_contraptions",
    description="A collection of contraptions",
    author="(~)",
    url="https://github.com/freeflock/contraptions",
    package_dir={"": "packages"},
    packages=["freeflock_contraptions"],
    install_requires=installation_requirements,
)
