from logic_utils import check_guess
from logic_utils import parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# ---------------------------------------------------------------------------
# Added tests for the bugs fixed in check_guess.
# check_guess now returns (outcome, message) with correctly pointing hints.
# ---------------------------------------------------------------------------

def test_check_guess_returns_tuple():
    # Bug: previously returned a single string, which broke `outcome, message = ...`
    result = check_guess(50, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_winning_outcome_and_message():
    # Bug: previously returned "Win!" so update_score's `== "Win"` never matched
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_too_high_outcome_and_hint_points_lower():
    # Bug: guess > secret was mislabeled and the hint told you to go HIGHER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_outcome_and_hint_points_higher():
    # Bug: guess < secret incorrectly returned "Too High" and hint said LOWER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# ---------------------------------------------------------------------------
# Added tests for the bug fixed in parse_guess.
# Input must now fall within the game's [low, high] range.
# ---------------------------------------------------------------------------

def test_parse_guess_valid_in_range():
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_below_range_rejected():
    # Bug: previously any number was accepted, even outside 1..100
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err


def test_parse_guess_above_range_rejected():
    ok, value, err = parse_guess("150", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err


def test_parse_guess_accepts_lower_boundary():
    ok, value, err = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1


def test_parse_guess_accepts_upper_boundary():
    ok, value, err = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100


def test_parse_guess_respects_difficulty_range():
    # On Easy (1..20), 25 is out of range and should be rejected
    ok, value, err = parse_guess("25", 1, 20)
    assert ok is False
    assert "between 1 and 20" in err


def test_parse_guess_empty_input():
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert err == "Enter a guess."


def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert err == "That is not a number."
