import pytest

from Pytest_Unit_Testing.src import formatter


def test_format_file_size_returns_format_zero():
    assert formatter.format_file_size(0) == "0B"

def test_format_file_size_returns_format_one_byte():
    assert formatter.format_file_size(1) == "1.00 B"

def test_format_file_size_returns_format_kb():
    assert formatter.format_file_size(1024) == "1.00 KB"

def test_format_file_size_returns_format_mb():
    assert formatter.format_file_size(1024**2) == "1.00 MB"

def test_format_file_size_returns_format_gb():
    assert formatter.format_file_size(1024**3) == "1.00 GB"

def test_format_file_size_returns_format_tb():
    assert formatter.format_file_size(1024**4) == "1.00 TB"


@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        (0, "0B"),
        (1, "1.00 B"),
        (1024, "1.00 KB"),
        (1024**2, "1.00 MB"),
        (1024**3, "1.00 GB"),
        (1024**4, "1.00 TB"),
    ]
)
@pytest.mark.smoke
def test_format_file_size(size_bytes, expected_result):
    print(f'size bytes: {size_bytes}')
    print(f'expected result: {expected_result}')
    assert formatter.format_file_size(size_bytes) == expected_result




@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        pytest.param(0, "0B", id="test_format_file_size_returns_format_zero"),
        pytest.param(1, "1.00 B", id="test_format_file_size_returns_format_one_byte"),
        pytest.param(1024, "1.00 KB", id="test_format_file_size_returns_format_kb"),
        pytest.param(1024**2, "1.00 MB", id="test_format_file_size_returns_format_mb"),
        pytest.param(1024**3, "1.00 GB", id="test_format_file_size_returns_format_gb"),
        pytest.param(1024**4, "1.00 TB", id="test_format_file_size_returns_format_tb"),
    ],
)
@pytest.mark.smoke
def test_format_file_size_descriptive_id(size_bytes, expected_result):
    assert formatter.format_file_size(size_bytes) == expected_result





###### PARAMETRIZE Examples:
### 1. Single Parameter (String)
### 2. Multiple Parameters (Comma-separated String)
### 3. Multiple Parameters (List of Strings)


@pytest.mark.smoke
@pytest.mark.parametrize("n", [1, 2, 3])
def test_something(n):
    assert n > 0

@pytest.mark.smoke
@pytest.mark.parametrize("input,expected", [("3+5", 8), ("2+4", 6)])
def test_eval(input, expected):
    assert eval(input) == expected

@pytest.mark.smoke
@pytest.mark.parametrize(["arg1", "arg2"], [(1, 2), (3, 4)])
def test_multiple(arg1, arg2):
    assert arg1 < arg2
