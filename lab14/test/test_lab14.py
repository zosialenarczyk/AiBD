from lab14 import hello, extract_sentiment, text_contain_word, bubble_sort
import pytest

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day","I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)
    assert sentiment > 0


testdata = [('There is a duck in this text', 'duck', True),('There is nothing here', 'duck', False)]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output


testdata = [[2, 5, 8, 1, 4, 6, 3, 9, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

def test_bubble_sort(testdata):

    got = bubble_sort(testdata[0])
    assert got == testdata[1]
    