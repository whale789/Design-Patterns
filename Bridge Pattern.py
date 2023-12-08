# 桥接模式

from abc import ABC, abstractmethod


# 实现部分的接口
class Implementor(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass


# 具体实现部分A
class ConcreteImplementorA(Implementor):
    def operate(self, x, y):
        return x + y


# 具体实现部分B
class ConcreteImplementorB(Implementor):
    def operate(self, x, y):
        return x - y


# 抽象部分的接口
class Abstraction(ABC):
    def __init__(self, implementor):
        self.implementor = implementor

    @abstractmethod
    def operate(self, x, y):
        pass


# 具体抽象部分A
class RefinedAbstractionA(Abstraction):
    def operate(self, x, y):
        result = self.implementor.operate(x, y)
        return f"加法运算结果: {result}"


# 具体抽象部分B
class RefinedAbstractionB(Abstraction):
    def operate(self, x, y):
        result = self.implementor.operate(x, y)
        return f"减法运算结果: {result}"


# 客户端代码
implementor_a = ConcreteImplementorA()
implementor_b = ConcreteImplementorB()

abstraction_a = RefinedAbstractionA(implementor_a)
abstraction_b = RefinedAbstractionB(implementor_b)

print(abstraction_a.operate(5, 3))  # 使用具体实现部分A
print(abstraction_b.operate(5, 3))  # 使用具体实现部分B
