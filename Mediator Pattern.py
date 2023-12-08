#中介者模式

from abc import ABC, abstractmethod

# 抽象中介者接口
class Mediator(ABC):
    @abstractmethod
    def execute_operation(self, operand1, operator, operand2):
        pass

# 具体中介者类
class CalculatorMediator(Mediator):
    def execute_operation(self, operand1, operator, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                return operand1 / operand2
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")
            return None

# 抽象同事类
class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

# 具体同事类A，表示操作数
class OperandColleague(Colleague):
    def __init__(self, mediator, value):
        super().__init__(mediator)
        self.value = value

    def execute_operation(self, operator, operand2):
        return self.mediator.execute_operation(self.value, operator, operand2)

# 具体同事类B，表示运算符
class OperatorColleague(Colleague):
    def __init__(self, mediator, symbol):
        super().__init__(mediator)
        self.symbol = symbol

    def execute_operation(self, operand1, operand2):
        return self.mediator.execute_operation(operand1, self.symbol, operand2)

# 客户端代码
# 创建中介者
mediator = CalculatorMediator()

# 创建同事对象
operand1 = OperandColleague(mediator, 5)
operator = OperatorColleague(mediator, '+')
operand2 = OperandColleague(mediator, 3)

# 执行四则运算
result = operator.execute_operation(operand1.value, operand2.value)
print(f"计算结果: {result}")
