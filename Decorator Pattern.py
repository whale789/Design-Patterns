# 装饰者模式

from abc import ABC, abstractmethod


# 抽象组件接口
class Component(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass


# 具体组件，实现基本的运算
class ConcreteComponent(Component):
    def operate(self, x, y):
        return x + y


# 抽象装饰者
class Decorator(Component):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operate(self, x, y):
        pass


# 具体装饰者A，添加乘法操作
class ConcreteDecoratorA(Decorator):
    def operate(self, x, y):
        result = self._component.operate(x, y)
        return f"{result} * {y} = {result * y}"


# 具体装饰者B，添加除法操作
class ConcreteDecoratorB(Decorator):
    def operate(self, x, y):
        result = self._component.operate(x, y)
        return f"{result} / {y} = {result / y}"


# 客户端代码
component = ConcreteComponent()

# 装饰者A，添加乘法操作
decorator_a = ConcreteDecoratorA(component)
result_a = decorator_a.operate(5, 3)
print(result_a)

# 装饰者B，添加除法操作
decorator_b = ConcreteDecoratorB(component)
result_b = decorator_b.operate(10, 2)
print(result_b)
