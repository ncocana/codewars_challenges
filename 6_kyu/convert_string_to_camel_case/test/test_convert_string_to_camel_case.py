# import another directory's module
from src.convert_string_to_camel_case import to_camel_case
import pytest


@pytest.mark.to_camel_case
def test_convert_string_to_camel_case():
    assert to_camel_case("") == ""
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"