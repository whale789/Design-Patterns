# 享元模式

# 享元工厂类，负责创建和管理享元对象
class OperandFactory:
    _operands = {}

    @classmethod
    def get_operand(cls, value):
        if value not in cls._operands:
            cls._operands[value] = Operand(value)
        return cls._operands[value]


# 享元类，表示操作数
class Operand:
    def __init__(self, value):
        self.value = value

    def operate(self, other, operator):
        if operator == '+':
            return self.value + other.value
        elif operator == '-':
            return self.value - other.value
        elif operator == '*':
            return self.value * other.value
        elif operator == '/':
            if other.value == 0:
                raise ValueError("Cannot divide by zero")
            return self.value / other.value


# 客户端代码
operand_factory = OperandFactory()

operand_5 = operand_factory.get_operand(5)
operand_3 = operand_factory.get_operand(3)

result_add = operand_5.operate(operand_3, '+')
result_subtract = operand_5.operate(operand_3, '-')
result_multiply = operand_5.operate(operand_3, '*')
result_divide = operand_5.operate(operand_3, '/')

# 打印结果
print(f"5 + 3 = {result_add}")
print(f"5 - 3 = {result_subtract}")
print(f"5 * 3 = {result_multiply}")
print(f"5 / 3 = {result_divide}")
