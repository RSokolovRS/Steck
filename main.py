# res = ['(', '(', ')', ')']

class Steck:

    def __init__(self, res):
        self.res = list(res)

    def is_empty(self):
        """проверка стека на пустоту. Метод возвращает True или False"""

        return len(self.res) != 0

    def push(self, new):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает"""
        return self.res.append(new)

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        # self._list.pop()
        return self.res.pop()

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется"""
        return self.res[-1]

    def size(self):
        """возвращает количество элементов в стеке"""
        return len(self.res)

    def __str__(self):
        if len(self.res) % 2 == 0:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'

data = '(((([{}]))))'

steck = Steck(data)

while steck.is_empty() == True:
    i = steck.pop()
    print(i)




