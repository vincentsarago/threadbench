"""handler."""

import pytest


def handler(event, context):
    """handler."""
    pytest.main(
        [
            "/var/task/tests/test_benchmarks.py",
            "--benchmark-only",
            "--benchmark-autosave",
            "--benchmark-columns 'min, max, mean, median'",
            "--benchmark-sort 'min'",
        ]
    )

    return True
