"""handler."""

import pytest


def handler(event, context):
    """handler."""
    pytest.main(["tests/test_benchmarks.py"], ["benchmark"])
    return True
