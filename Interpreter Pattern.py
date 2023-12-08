#解释器模型

from abc import ABC, abstractmethod

# 抽象表达式接口
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 具体表达式A，表示操作数
class OperandExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# 具体表达式B，表示运算符
class OperatorExpression(Expression):
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

    def interpret(self, context):
        if self.operator == '+':
            return self.left_operand.interpret(context) + self.right_operand.interpret(context)
        elif self.operator == '-':
            return self.left_operand.interpret(context) - self.right_operand.interpret(context)
        elif self.operator == '*':
            return self.left_operand.interpret(context) * self.right_operand.interpret(context)
        elif self.operator == '/':
            right_value = self.right_operand.interpret(context)
            if right_value != 0:
                return self.left_operand.interpret(context) / right_value
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")
            return None

# 上下文类，用于存储变量值
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable_value(self, variable):
        return self.variables.get(variable, 0)

# 客户端代码
# 创建上下文对象
context = Context()

# 构建表达式：5 + 3 * 2
expression = OperatorExpression('+', OperandExpression(5), OperatorExpression('*', OperandExpression(3), OperandExpression(2)))

# 解释并执行表达式
result = expression.interpret(context)
print(f"计算结果: {result}")
