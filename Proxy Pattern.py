#代理模式

# 具体运算类
class MathOperation:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# 代理类
class MathOperationProxy:
    def __init__(self):
        self.math_operation = MathOperation()

    def add(self, x, y):
        print("Before addition operation")
        result = self.math_operation.add(x, y)
        print("After addition operation")
        return result

    def subtract(self, x, y):
        print("Before subtraction operation")
        result = self.math_operation.subtract(x, y)
        print("After subtraction operation")
        return result

    def multiply(self, x, y):
        print("Before multiplication operation")
        result = self.math_operation.multiply(x, y)
        print("After multiplication operation")
        return result

    def divide(self, x, y):
        print("Before division operation")
        result = self.math_operation.divide(x, y)
        print("After division operation")
        return result

# 客户端代码
proxy = MathOperationProxy()

result_add = proxy.add(5, 3)
result_subtract = proxy.subtract(5, 3)
result_multiply = proxy.multiply(5, 3)
result_divide = proxy.divide(10, 2)

# 打印结果
print(f"5 + 3 = {result_add}")
print(f"5 - 3 = {result_subtract}")
print(f"5 * 3 = {result_multiply}")
print(f"10 / 2 = {result_divide}")
