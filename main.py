

class Stek:

    def __init__(self, _list):
        self._list = _list

    def is_empty(self):
        "проверка стека на пустоту. Метод возвращает True или False"
        for i in self._list:
            if '(' == i:
                return False
            else:
                return True
    
    def push(self):
        "добавляет новый элемент на вершину стека. Метод ничего не возвращает"
        pass

    def pop(self):
        "удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"
        pass

    def peek(self):
        "возвращает верхний элемент стека, но не удаляет его. Стек не меняется"
        pass

    def size(self):
        "возвращает количество элементов в стеке"
        return len(self._list)

    def __str__(self):
        if len(self._list) % 2 == 0:
            return 'Сбалансированно'
        elif len(self._list) % 2 != 0:
            return 'Несбалансированно'
        else:
            return None

res = ['(', '(', ')', ')']

if __name__ == '__main__':
    Stek(res)