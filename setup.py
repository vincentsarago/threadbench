"""Setup for threadbench."""

from setuptools import find_packages, setup

# Runtime requirements.
inst_reqs = [
    "pytest",
    "pytest-benchmark",
    "pytest-asyncio",
    "rio-tiler-crs~=2.0.2",
    "importlib_metadata",
]

setup(
    name="threadbench",
    version="0.0.1",
    python_requires=">=3",
    description=u"""Benchmark rio-tiler in threads""",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    zip_safe=False,
    install_requires=inst_reqs,
)
