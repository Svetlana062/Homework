from functools import wraps
from logging import error
from typing import Callable, Any

# Создан декоратор log, который будет автоматически регистрировать детали выполнения функций
def log(filename: str | None = None) -> Callable:
  def decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
      try:
        # После выполненя функции будет выводиться сообщение, которую будешь записывать в файл
        func(*args, **kwargs)
        message_for_log = f"{func.__name__} ok\n"
        if filename: # если задан параметр filename
          with open(filename, 'w', encoding="utf-8") as file:
            file.write(message_for_log)
        else: # если не задан параметр filename
            print(message_for_log)
      except Exception as e:
        # выполняешь действие если ошибка и записывай в log_message сообщение, которое будешь распечатывать
        error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
        if filename: # если задан параметр filename
          with open(filename, "a", encoding="utf-8") as file:
            file.write(error_message)
        else:
          print(error_message)
      return error
    return wrapper
  return decorator


# проверка декоратора
@log(filename="mylog.txt")
def my_function(x, y):
  print(f"Выполнение функции с аргументами {x} и {y}")

my_function(10, 20)


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function("1", "9")
print(my_function)