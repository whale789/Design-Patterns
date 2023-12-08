#状态模式

from abc import ABC, abstractmethod

# 抽象状态接口
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# 具体状态A，表示加法状态
class AddState(State):
    def handle(self, context):
        print(f"加法运算结果: {context.operand1} + {context.operand2} = {context.operand1 + context.operand2}")
        context.set_state(SubtractState())

# 具体状态B，表示减法状态
class SubtractState(State):
    def handle(self, context):
        print(f"减法运算结果: {context.operand1} - {context.operand2} = {context.operand1 - context.operand2}")
        context.set_state(MultiplyState())

# 具体状态C，表示乘法状态
class MultiplyState(State):
    def handle(self, context):
        print(f"乘法运算结果: {context.operand1} * {context.operand2} = {context.operand1 * context.operand2}")
        context.set_state(DivideState())

# 具体状态D，表示除法状态
class DivideState(State):
    def handle(self, context):
        if context.operand2 != 0:
            print(f"除法运算结果: {context.operand1} / {context.operand2} = {context.operand1 / context.operand2}")
        else:
            print("Cannot divide by zero")
        context.set_state(AddState())

# 上下文类，维护当前状态
class CalculatorContext:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self._state = AddState()

    def set_state(self, state):
        self._state = state

    def perform_operation(self):
        self._state.handle(self)

# 客户端代码
# 创建上下文对象
calculator = CalculatorContext(5, 3)

# 执行一系列运算操作
for _ in range(4):
    calculator.perform_operation()
