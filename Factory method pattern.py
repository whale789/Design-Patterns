

# 工厂方法模式

from abc import ABC, abstractmethod


# 定义运算接口
class Operation(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass


# 具体的加法运算类
class AddOperation(Operation):
    def operate(self, x, y):
        return x + y


# 具体的减法运算类
class SubtractOperation(Operation):
    def operate(self, x, y):
        return x - y


# 具体的乘法运算类
class MultiplyOperation(Operation):
    def operate(self, x, y):
        return x * y


# 具体的除法运算类
class DivideOperation(Operation):
    def operate(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


# 运算工厂
class OperationFactory:
    def create_operation(self, operator):
        if operator == '+':
            return AddOperation()
        elif operator == '-':
            return SubtractOperation()
        elif operator == '*':
            return MultiplyOperation()
        elif operator == '/':
            return DivideOperation()
        else:
            raise ValueError(f"Unsupported operator: {operator}")


# 使用示例
factory = OperationFactory()

# 创建加法运算对象
add_operation = factory.create_operation('+')
result_add = add_operation.operate(5, 3)
print(f"5 + 3 = {result_add}")

# 创建除法运算对象
divide_operation = factory.create_operation('/')
result_divide = divide_operation.operate(10, 2)
print(f"10 / 2 = {result_divide}")
