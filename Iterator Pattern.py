#迭代器模式

from abc import ABC, abstractmethod

# 抽象迭代器接口
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# 具体迭代器，用于遍历数学表达式中的操作数和运算符
class MathExpressionIterator(Iterator):
    def __init__(self, expression):
        self._expression = expression
        self._index = 0

    def has_next(self):
        return self._index < len(self._expression)

    def next(self):
        if self.has_next():
            result = self._expression[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

# 抽象聚合接口
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# 具体聚合，表示数学表达式
class MathExpression(Aggregate):
    def __init__(self):
        self._elements = []

    def add_element(self, element):
        self._elements.append(element)

    def create_iterator(self):
        return MathExpressionIterator(self._elements)

# 客户端代码
expression = MathExpression()
expression.add_element(5)
expression.add_element('+')
expression.add_element(3)
expression.add_element('*')
expression.add_element(2)
expression.add_element('=')
expression.add_element(11)

iterator = expression.create_iterator()

while iterator.has_next():
    element = iterator.next()
    print(element, end=' ')
