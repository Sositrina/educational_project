import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_card() -> str:
    return get_mask_card_number(7000792289606361)


def test_get_mask_card_number(mask_card: str) -> None:
    assert len(mask_card) == 19
    assert mask_card.startswith("7000")
    assert mask_card.endswith("6361")


@pytest.mark.parametrize(
    "element",
    [
        0,
        12345678909042374986327,
    ],
)
def test_mask_card_wrong_number(element: int) -> None:
    expected = "Номер карты неверный"
    assert get_mask_card_number(element) == expected


@pytest.fixture
def mask_account() -> str:
    return get_mask_account(73654108430135874305)


def test_get_mask_account(mask_account: str) -> None:
    assert len(mask_account) == 6


@pytest.mark.parametrize("element", [0, 12345678909042374986327])
def test_mask_account_wong(element: int) -> None:
    expected = "Номер счета неверный"
    assert get_mask_account(element) == expected
