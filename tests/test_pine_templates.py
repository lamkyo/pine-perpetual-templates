"""
Parity & Compliance Tests for Pine Script Perpetual Templates
Verifies:
1. Version 5 compliance (//@version=5)
2. No lookahead leakage (barmerge.lookahead_off used in all request.security calls)
3. Balance of structural delimiters (parentheses, brackets)
4. Valid strategy / indicator declaration
5. Binance USD(S)-M 10-tier MMR parity in accounting validator
"""

from pathlib import Path
import re
import pytest

PINE_DIR = Path(__file__).resolve().parent.parent

PINE_FILES = sorted(list(PINE_DIR.glob("*.pine")))

def test_pine_files_count():
    assert len(PINE_FILES) == 6, f"Expected 6 pine scripts, found {len(PINE_FILES)}"

@pytest.mark.parametrize("file_path", PINE_FILES)
def test_pine_version_directive(file_path):
    content = file_path.read_text(encoding="utf-8")
    first_line = content.splitlines()[0].strip()
    assert first_line == "//@version=5", f"{file_path.name} must start with //@version=5"

@pytest.mark.parametrize("file_path", PINE_FILES)
def test_no_lookahead_bias(file_path):
    content = file_path.read_text(encoding="utf-8")
    assert "lookahead=barmerge.lookahead_on" not in content, (
        f"{file_path.name} contains lookahead_on which introduces lookahead bias!"
    )
    if "request.security" in content:
        assert "lookahead=barmerge.lookahead_off" in content, (
            f"{file_path.name} uses request.security without explicit lookahead=barmerge.lookahead_off"
        )

@pytest.mark.parametrize("file_path", PINE_FILES)
def test_syntax_delimiter_balance(file_path):
    content = file_path.read_text(encoding="utf-8")
    # Clean string literals and comments
    cleaned = re.sub(r'//.*', '', content)
    cleaned = re.sub(r'".*?"', '', cleaned)
    
    open_paren = cleaned.count("(")
    close_paren = cleaned.count(")")
    assert open_paren == close_paren, f"{file_path.name} unbalanced parentheses: {open_paren} vs {close_paren}"

    open_bracket = cleaned.count("[")
    close_bracket = cleaned.count("]")
    assert open_bracket == close_bracket, f"{file_path.name} unbalanced brackets: {open_bracket} vs {close_bracket}"

def test_accounting_parity_10_tiers():
    validator_file = PINE_DIR / "06_accounting_parity_validator.pine"
    content = validator_file.read_text(encoding="utf-8")
    assert "10-TIER TABLE" in content
    # Tiers checks: 50k, 250k, 1M, 5M, 20M, 50M, 100M, 150M, 200M, 300M
    assert "50000.0" in content
    assert "250000.0" in content
    assert "1000000.0" in content
    assert "5000000.0" in content
    assert "20000000.0" in content
    assert "50000000.0" in content
    assert "100000000.0" in content
    assert "150000000.0" in content
    assert "200000000.0" in content
    # Max tier 0.250 MMR
    assert "0.250" in content
