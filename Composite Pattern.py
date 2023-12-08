# 组合模式

from abc import ABC, abstractmethod


# 抽象组件接口
class Component(ABC):
    @abstractmethod
    def operate(self):
        pass


# 叶子节点，表示操作数
class Operand(Component):
    def __init__(self, value):
        self.value = value

    def operate(self):
        return self.value


# 叶子节点，表示运算符
class Operator(Component):
    def __init__(self, operator):
        self.operator = operator

    def operate(self):
        return self.operator


# 组合节点，表示复杂的数学表达式
class Expression(Component):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def operate(self):
        result = ""
        for child in self.children:
            result += str(child.operate()) + " "
        return result.strip()


# 客户端代码
# 构建数学表达式：(5 + 3) * 2
expression = Expression()

# 创建叶子节点
operand1 = Operand(5)
operand2 = Operand(3)
operator_add = Operator('+')
operator_multiply = Operator('*')
operator_equal = Operator('=')

# 组合节点添加子节点
expression.add_child(Operator('('))
expression.add_child(operand1)
expression.add_child(operator_add)
expression.add_child(operand2)
expression.add_child(Operator(')'))
expression.add_child(operator_multiply)
expression.add_child(Operand(2))
expression.add_child(operator_equal)
expression.add_child(Operand(16))

# 打印结果
print(f"数学表达式为: {expression.operate()}")
