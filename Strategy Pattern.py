#策略模式

from abc import ABC, abstractmethod

# 策略接口
class OperationStrategy(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass

# 具体策略A，实现加法
class AddStrategy(OperationStrategy):
    def operate(self, x, y):
        return x + y

# 具体策略B，实现减法
class SubtractStrategy(OperationStrategy):
    def operate(self, x, y):
        return x - y

# 具体策略C，实现乘法
class MultiplyStrategy(OperationStrategy):
    def operate(self, x, y):
        return x * y

# 具体策略D，实现除法
class DivideStrategy(OperationStrategy):
    def operate(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# 上下文类，用于执行运算
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, x, y):
        return self.strategy.operate(x, y)

# 客户端代码
# 使用具体策略A，执行加法运算
context_add = Context(AddStrategy())
result_add = context_add.execute_strategy(5, 3)

# 使用具体策略B，执行减法运算
context_subtract = Context(SubtractStrategy())
result_subtract = context_subtract.execute_strategy(5, 3)

# 使用具体策略C，执行乘法运算
context_multiply = Context(MultiplyStrategy())
result_multiply = context_multiply.execute_strategy(5, 3)

# 使用具体策略D，执行除法运算
context_divide = Context(DivideStrategy())
result_divide = context_divide.execute_strategy(10, 2)

# 打印结果
print(f"5 + 3 = {result_add}")
print(f"5 - 3 = {result_subtract}")
print(f"5 * 3 = {result_multiply}")
print(f"10 / 2 = {result_divide}")
