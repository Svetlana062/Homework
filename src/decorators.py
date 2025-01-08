from functools import wraps
from logging import error
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который автоматически регистрирует детали выполнения функций"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Function {func} started")
            try:
                # После выполнения функции сообщение будет выводиться в терминал или записано в файл
                func(*args, **kwargs)
                message_for_log = f"{func.__name__} ok"
                if filename:  # если задан параметр filename
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message_for_log + "\n")
                else:  # если не задан параметр filename
                    print(message_for_log)
            except Exception as e:
                # выполняешь действие, если ошибка, записывается в файл или выводиться в консоли
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:  # если задан параметр filename
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
            print(f"Function {func} finished")
            return error

        return wrapper

    return decorator


# Проверка декораторов:
@log(filename="mylog.txt")
def my_function_1(x: int, y: int) -> int | float:
    """Сложение двух чисел."""
    return x + y


my_function_1(10, 20)


@log(filename="mylog.txt")
def my_function_2(x: int, y: int) -> int | float:
    """Деление двух чисел."""
    return x / y


my_function_2("1", "9")
