# Пример файла с результатами (с готовой функцией управления), 
# который нужно залить по ссылке https://www.dropbox.com/request/hCtzOaqvFZoTMYKpDf4P


__author__ = "Иванов Иван Иванович СМ17-52" # автор 
__email__ = "iii@mailz.ru"                  # email 

dependencies = {                           # Словарь (str->str) с необходимыми для функции зависимостями "имя пакета в pip"->"версия"
    "tensorflow": "1.15",
    "scipy": "1.18.1"
}

import tensorflow as tf
import scipy
import math

def brain_foo(input_dict):
    """Собственно сама функция управления, которая будет импортирована 
    и использована для тестов (для дуэлей с другими участниками)

    Имя её должно быть именно 'brain_foo'
    """
    return {}

class SomeHelperClass(object):
    """Другой необходимыый для работы пользовательский класс
    """
    pass

def some_other_foo(*args, **kwargs):
    """Всякая другая функция
    """
    pass