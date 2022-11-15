# import another directory's module
from src.duplicate_encoder import duplicate_encode
import pytest


@pytest.mark.duplicate_encode
def test_duplicate_encoder():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())","should ignore case"
    assert duplicate_encode("(( @") == "))(("