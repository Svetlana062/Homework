from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который автоматически регистрирует детали выполнения функций"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Function {func} started")
            message_for_log = ""
            try:
                # После выполнения функции сообщение будет выводиться в терминал или записано в файл
                result = func(*args, **kwargs)
                message_for_log = f"{func.__name__} ok"
            except Exception as e:
                message_for_log = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                if filename:  # если задан параметр filename
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message_for_log + "\n")
                else:
                    print(message_for_log)
            print(f"Function {func} finished")
            return result

        return wrapper

    return decorator
