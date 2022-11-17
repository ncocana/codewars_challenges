# import another directory's module
from src.permute_a_palindrome import permute_a_palindrome
import pytest


@pytest.mark.permute_a_palindrome
def test_permute_a_palindrome():
    assert permute_a_palindrome("a") == True
    assert permute_a_palindrome("aa") == True
    assert permute_a_palindrome("aaa") == True
    assert permute_a_palindrome("baa") == True
    assert permute_a_palindrome("aab") == True
    assert permute_a_palindrome("baabcd") == False
    assert permute_a_palindrome("racecars") == False
    assert permute_a_palindrome("abcdefghba") == False
    assert permute_a_palindrome("") == True