#命令模式
from abc import ABC, abstractmethod

# 抽象命令接口
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# 具体命令A，执行加法
class AddCommand(Command):
    def __init__(self, receiver, operand):
        self.receiver = receiver
        self.operand = operand

    def execute(self):
        self.receiver.add(self.operand)

    def undo(self):
        self.receiver.subtract(self.operand)

# 具体命令B，执行减法
class SubtractCommand(Command):
    def __init__(self, receiver, operand):
        self.receiver = receiver
        self.operand = operand

    def execute(self):
        self.receiver.subtract(self.operand)

    def undo(self):
        self.receiver.add(self.operand)

# 接收者，负责执行具体的运算操作
class CalculatorReceiver:
    def __init__(self):
        self.result = 0

    def add(self, operand):
        self.result += operand

    def subtract(self, operand):
        self.result -= operand

# 客户端代码
# 创建接收者
calculator = CalculatorReceiver()

# 创建具体命令对象
add_command = AddCommand(calculator, 5)
subtract_command = SubtractCommand(calculator, 3)

# 执行命令
add_command.execute()
print(f"Result after addition: {calculator.result}")

subtract_command.execute()
print(f"Result after subtraction: {calculator.result}")

# 撤销命令
subtract_command.undo()
print(f"Result after undo: {calculator.result}")
