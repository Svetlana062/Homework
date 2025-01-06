from functools import wraps
from logging import error
from typing import Any, Callable


# Создан декоратор log, который будет автоматически регистрировать детали выполнения функций
def log(filename: str | None = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # После выполнения функции сообщение будет выводиться в терминал или записано в файл
                func(*args, **kwargs)
                message_for_log = f"{func.__name__} ok\n"
                if filename:  # если задан параметр filename
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message_for_log)
                else:  # если не задан параметр filename
                    print(message_for_log)
            except Exception as e:
                # выполняешь действие, если ошибка, записывается в файл или выводиться в консоли
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:  # если задан параметр filename
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)
            return error

        return wrapper

    return decorator


# проверка декоратора
@log(filename="mylog.txt")
def my_function_1(x: Any, y: Any) -> None:
    print(f"Выполнение функции с аргументами {x} и {y}")


my_function_1(10, 20)


@log(filename="mylog.txt")
def my_function_2(x: Any, y: Any) -> None:
    return x / y


my_function_2("1", "9")
print(my_function_2)
