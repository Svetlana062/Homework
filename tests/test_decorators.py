import os

import pytest

from src.decorators import log


@pytest.fixture
def temp_log_file():
    """Фикстура для создания временного лог-файла."""
    filename = "mylog.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


@pytest.mark.parametrize(
    "args, expected_message",
    [
        ((1, 2), "my_function ok"),
        ((3, 4), "my_function ok"),
        (("4", "7"), "my_func error: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('1', '9'), {}"),
        (("ijv", 8), "my_func error: unsupported operand type(s) for /: 'str' and 'int'. Inputs: ('1', '9'), {}"),
    ],
)
def test_log_success(temp_log_file, capsys, args, expected_message):
    """Тесты на результат обработки вводных данных."""

    @log(temp_log_file)
    def my_func(x, y):
        assert x + y
