import pytest
import sys
import random
import index


def test_letter_first():
    words = ["skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage"]
    secret_word = random.choice(words)
    assert secret_word in words

def test_letter_second():
    assert str(int()) not in index.secret_word
