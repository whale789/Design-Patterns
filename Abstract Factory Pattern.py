#抽象工厂模式

from abc import ABC, abstractmethod


# 抽象运算接口
class Operation(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass


# 抽象工厂接口
class OperationFactory(ABC):
    @abstractmethod
    def create_operation(self):
        pass


# 具体加法运算类
class AddOperation(Operation):
    def operate(self, x, y):
        return x + y


# 具体减法运算类
class SubtractOperation(Operation):
    def operate(self, x, y):
        return x - y


# 具体乘法运算类
class MultiplyOperation(Operation):
    def operate(self, x, y):
        return x * y


# 具体除法运算类
class DivideOperation(Operation):
    def operate(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


# 具体加法运算工厂
class AddOperationFactory(OperationFactory):
    def create_operation(self):
        return AddOperation()


# 具体减法运算工厂
class SubtractOperationFactory(OperationFactory):
    def create_operation(self):
        return SubtractOperation()


# 具体乘法运算工厂
class MultiplyOperationFactory(OperationFactory):
    def create_operation(self):
        return MultiplyOperation()


# 具体除法运算工厂
class DivideOperationFactory(OperationFactory):
    def create_operation(self):
        return DivideOperation()


# 使用示例
add_factory = AddOperationFactory()
add_operation = add_factory.create_operation()
result_add = add_operation.operate(7, 3)
print(f"7 + 3 = {result_add}")

divide_factory = DivideOperationFactory()
divide_operation = divide_factory.create_operation()
result_divide = divide_operation.operate(18, 2)
print(f"18 / 2 = {result_divide}")
