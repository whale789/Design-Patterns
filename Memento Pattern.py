#备忘录模式

from copy import deepcopy

# 备忘录类
class CalculatorMemento:
    def __init__(self, result):
        self.result = result

# 发起人类，负责执行具体的运算操作和创建备忘录
class CalculatorOriginator:
    def __init__(self):
        self.result = 0

    def add(self, operand):
        self.result += operand

    def subtract(self, operand):
        self.result -= operand

    def create_memento(self):
        return CalculatorMemento(self.result)

    def restore_from_memento(self, memento):
        self.result = memento.result

# 管理者类，负责保存和恢复备忘录
class CalculatorCareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_last_memento(self):
        if self.mementos:
            return self.mementos[-1]
        else:
            return None

# 客户端代码
# 创建发起人和管理者
calculator = CalculatorOriginator()
care_taker = CalculatorCareTaker()

# 执行运算操作
calculator.add(5)
care_taker.add_memento(calculator.create_memento())

calculator.subtract(3)
care_taker.add_memento(calculator.create_memento())

# 打印当前结果
print(f"Current result: {calculator.result}")

# 恢复到先前的状态
last_memento = care_taker.get_last_memento()
if last_memento:
    calculator.restore_from_memento(deepcopy(last_memento))

# 打印恢复后的结果
print(f"Result after restoring: {calculator.result}")
