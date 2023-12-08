# 外观模式

# 外观类，提供简化的接口给客户端
class CalculatorFacade:
    def add(self, x, y):
        return Adder().add(x, y)

    def subtract(self, x, y):
        return Subtractor().subtract(x, y)

    def multiply(self, x, y):
        return Multiplier().multiply(x, y)

    def divide(self, x, y):
        return Divider().divide(x, y)


# 子系统中的具体运算类
class Adder:
    def add(self, x, y):
        return x + y


class Subtractor:
    def subtract(self, x, y):
        return x - y


class Multiplier:
    def multiply(self, x, y):
        return x * y


class Divider:
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


# 客户端代码
facade = CalculatorFacade()

# 使用外观模式进行四则运算
result_add = facade.add(5, 3)
result_subtract = facade.subtract(5, 3)
result_multiply = facade.multiply(5, 3)
result_divide = facade.divide(10, 2)

# 打印结果
print(f"5 + 3 = {result_add}")
print(f"5 - 3 = {result_subtract}")
print(f"5 * 3 = {result_multiply}")
print(f"10 / 2 = {result_divide}")
