
from calc import div
try:
    result = div(100, 'jjh')
    print('расчет успешен')
    print(result)
except (ZeroDivisionError, TypeError) as er:
    # print('Деление на ноль', er)
    print(er)

try:
    result = div(100, 'gh')
    print("Расчёт проведён успешно")
except ZeroDivisionError as e:
    print("Вот такая ошибка деления произошла", e)
except TypeError as e:
    print("Вот такая ошибка обращения по ключу произошла:", e)


try:
    result = div(100, 0)
    print("Расчёт проведён успешно")
except Exception as e:
    print("Вот такая ошибка деления произошла", e)
except TypeError as e:
    print(dir(e), 0)
    print("Вот такая ошибка обращения по ключу произошла:", e)
else:
    print(result)
finally:
    print("Выполнение расчёта закончено")

