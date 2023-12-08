#责任链模式

from abc import ABC, abstractmethod

# 抽象处理器
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, operation):
        pass

# 具体处理器A，处理加法
class AddHandler(Handler):
    def handle_request(self, operation):
        if operation.operator == '+':
            result = operation.operand1 + operation.operand2
            print(f"{operation.operand1} + {operation.operand2} = {result}")
        elif self.successor is not None:
            self.successor.handle_request(operation)

# 具体处理器B，处理减法
class SubtractHandler(Handler):
    def handle_request(self, operation):
        if operation.operator == '-':
            result = operation.operand1 - operation.operand2
            print(f"{operation.operand1} - {operation.operand2} = {result}")
        elif self.successor is not None:
            self.successor.handle_request(operation)

# 具体处理器C，处理乘法
class MultiplyHandler(Handler):
    def handle_request(self, operation):
        if operation.operator == '*':
            result = operation.operand1 * operation.operand2
            print(f"{operation.operand1} * {operation.operand2} = {result}")
        elif self.successor is not None:
            self.successor.handle_request(operation)

# 具体处理器D，处理除法
class DivideHandler(Handler):
    def handle_request(self, operation):
        if operation.operator == '/':
            if operation.operand2 != 0:
                result = operation.operand1 / operation.operand2
                print(f"{operation.operand1} / {operation.operand2} = {result}")
            else:
                print("Cannot divide by zero")
        elif self.successor is not None:
            self.successor.handle_request(operation)

# 请求类，封装运算信息
class Operation:
    def __init__(self, operand1, operand2, operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

# 客户端代码
# 创建责任链
add_handler = AddHandler()
subtract_handler = SubtractHandler()
multiply_handler = MultiplyHandler()
divide_handler = DivideHandler()

# 设置责任链顺序
add_handler.successor = subtract_handler
subtract_handler.successor = multiply_handler
multiply_handler.successor = divide_handler

# 创建运算请求
operation1 = Operation(5, 3, '+')
operation2 = Operation(5, 3, '-')
operation3 = Operation(5, 3, '*')
operation4 = Operation(5, 2, '/')

# 处理运算请求
add_handler.handle_request(operation1)
add_handler.handle_request(operation2)
add_handler.handle_request(operation3)
add_handler.handle_request(operation4)
