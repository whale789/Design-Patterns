#访问者模式

from abc import ABC, abstractmethod

# 抽象元素接口
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 具体元素A，表示操作数
class OperandElement(Element):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_operand(self)

# 具体元素B，表示运算符
class OperatorElement(Element):
    def __init__(self, symbol):
        self.symbol = symbol

    def accept(self, visitor):
        return visitor.visit_operator(self)

# 抽象访问者接口
class Visitor(ABC):
    @abstractmethod
    def visit_operand(self, operand):
        pass

    @abstractmethod
    def visit_operator(self, operator):
        pass

# 具体访问者A，表示求值操作
class EvaluateVisitor(Visitor):
    def visit_operand(self, operand):
        return operand.value

    def visit_operator(self, operator):
        return operator.symbol

# 具体访问者B，表示打印操作
class PrintVisitor(Visitor):
    def visit_operand(self, operand):
        return str(operand.value)

    def visit_operator(self, operator):
        return operator.symbol

# 对象结构，包含元素的集合
class ObjectStructure:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def accept(self, visitor):
        result = []
        for element in self.elements:
            result.append(element.accept(visitor))
        return result

# 客户端代码
# 创建对象结构
expression = ObjectStructure()
expression.add_element(OperandElement(5))
expression.add_element(OperatorElement('+'))
expression.add_element(OperandElement(3))
expression.add_element(OperatorElement('*'))
expression.add_element(OperandElement(2))
expression.add_element(OperatorElement('='))
expression.add_element(OperandElement(11))

# 创建访问者
evaluate_visitor = EvaluateVisitor()
print_visitor = PrintVisitor()

# 使用访问者进行求值操作
result = expression.accept(evaluate_visitor)
print(f"Evaluation result: {result}")

# 使用访问者进行打印操作
expression_str = ' '.join(expression.accept(print_visitor))
print(f"Expression: {expression_str}")
