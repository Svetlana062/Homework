from unittest.mock import patch

import pytest

import main


@pytest.mark.parametrize(
    "user_input",
    [
        (["1", "executed", "нет", "нет", "нет"]),
        (["3", "PENDING", "да", "по убыванию", "нет", "да", "перевод"]),
        (["2", "canceled", "да", "по возрастанию", "да", "нет"]),
    ],
)
def test_multiple_inputs(user_input: list) -> None:
    """Тест на работу тестового модуля."""
    with patch("builtins.input", side_effect=user_input):
        main.main()


@pytest.mark.parametrize(
    "user_input",
    [(["2", "canceled", "да", "", "нет", "нет"]), (["3", "PENDING", "да", "по убыванию", "нет", "да", "blah"])],
)
def test_multiple_inputs_error(user_input: list) -> None:
    """Тест на работу тестового модуля с ошибочным вводом."""
    with patch("builtins.input", side_effect=user_input):
        main.main()
