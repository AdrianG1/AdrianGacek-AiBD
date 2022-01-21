import pytest
from app import hello, extract_sentiment, text_contain_word, factorial


def test_hello():
    got = hello("Adrian")
    want = "Hello Adrian"

    assert got == want


def test_extract_sentiment():
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)

    assert sentiment > 0


testdata = ["I think today will be a great day", "I do not think this will turn out well"]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment >= 0


testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata = [
    (0, 1),
    (1, 1),
    (-4, "n < 0!"),
    (5, 120)
]


@pytest.mark.parametrize('n, expected_output', testdata)
def test_factorial(n, expected_output):
    assert factorial(n) == expected_output
