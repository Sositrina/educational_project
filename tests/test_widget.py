import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def mask_card() -> str:
    return mask_account_card("Visa Platinum 7000792289606361")


def test_mask_card_compare(mask_card) -> None:
    assert mask_card == "Visa Platinum 7000 79** **** 6361"
    assert len(mask_card) == 33

@pytest.mark.parametrize("card", "expected",
                         [("Visa Platinum 7000 79** **** 6361", ""),
                          ("Visa Platinum 7000 79** **** 6361", "VisaPlatinum700079******6361"),
                          ("Visa Platinum 7000 79** **** 6361", "Visa Platinum"),
                          ("Visa Platinum 7000 79** **** 6361", "7000 79** **** 6361"),
                          ("Visa Platinum 7000 79** **** 6361", "43246764")])


def test_card_wrong(card, expected) -> None:
    assert mask_account_card == "Неверные данные"



@pytest.fixture
def mask_check() -> str:
    return get_date("Счет 73654108430135874305")

def test_mask_check_compare(mask_check) -> None:
    assert mask_check == "Счет **4305"

def test_mask_check_length(mask_check) -> None:
    assert len(mask_check) == 11

@pytest.mark.parametrize("check", "expected",
                         [("Счет **4305", ""),
                          ("Счет **4305", "Счет**4305"),
                          ("Счет **4305", "Счет"),
                          ("Счет **4305", "**4305"),
                          ("**4305", "43246764")])


def test_mask_check_wrong(check, expected):
    assert get_date == "Неверные данные"