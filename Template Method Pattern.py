#模板方法模式

from abc import ABC, abstractmethod

# 抽象模板类
class TemplateOperation(ABC):
    def operate(self, x, y):
        result = self.step1(x, y)
        result = self.step2(result)
        return result

    @abstractmethod
    def step1(self, x, y):
        pass

    @abstractmethod
    def step2(self, result):
        pass

# 具体模板类A，实现加法和乘法
class ConcreteOperationA(TemplateOperation):
    def step1(self, x, y):
        return x + y

    def step2(self, result):
        return result * 2

# 具体模板类B，实现减法和除法
class ConcreteOperationB(TemplateOperation):
    def step1(self, x, y):
        return x - y

    def step2(self, result):
        if result != 0:
            return result / 2
        else:
            return 0

# 客户端代码
# 使用具体模板类A，执行加法和乘法运算
operation_a = ConcreteOperationA()
result_a = operation_a.operate(5, 3)

# 使用具体模板类B，执行减法和除法运算
operation_b = ConcreteOperationB()
result_b = operation_b.operate(5, 3)

# 打印结果
print(f"先做加法，然后将和乘2: {result_a}")
print(f"先做减法，然后将差除2: {result_b}")
