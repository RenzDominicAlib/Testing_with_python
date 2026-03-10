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