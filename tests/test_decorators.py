from src.decorators import log

# Функции тестирующие работу декоратора на правильность и ошибки
def test_my_function_logs(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 8)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_my_function_error(capsys):
    @log(filename="")
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (1, 0), {}\n\n"


def test_my_function_type(capsys):
    @log(filename="")
    def my_functions(x, y):
        return x - y

    my_functions("1", "2")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('1', '2'), {}\n\n"
    )
