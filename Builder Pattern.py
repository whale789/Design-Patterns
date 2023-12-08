# 建造者模式

from abc import ABC, abstractmethod


# 抽象建造者接口
class Builder(ABC):
    @abstractmethod
    def build_operand(self, value):
        pass

    @abstractmethod
    def build_operator(self, operator):
        pass

    @abstractmethod
    def get_result(self):
        pass


# 具体建造者实现
class ConcreteBuilder(Builder):
    def __init__(self):
        self.expression = []

    def build_operand(self, value):
        self.expression.append(value)

    def build_operator(self, operator):
        self.expression.append(operator)

    def get_result(self):
        return ''.join(str(elem) for elem in self.expression)


# 指导者（Director）类
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_operand(5)
        self.builder.build_operator('+')
        self.builder.build_operand(3)
        self.builder.build_operator('*')
        self.builder.build_operand(2)
        self.builder.build_operator('=')
        self.builder.build_operand(11)


# 客户端代码
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
result = builder.get_result()

print(f"构建一个数学表达式: {result}")
