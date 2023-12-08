

#单例模式


class Calculator():
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("被除数不能为0")

# 使用示例
calculator1 = Calculator()
result1 = calculator1.add(5, 3)
print(f"加法计算结果为: {result1}")

calculator2 = Calculator()
result2 = calculator2.multiply(4, 6)
print(f"乘法计算结果为: {result2}")

calculator3=Calculator()
result3=calculator3.subtract(15,7)
print(f"减法计算结果为：{result3}")

calculator4=Calculator()
result4=calculator4.divide(24,3)
print(f"除法计算结果为：{result4}")

# 输出相同的实例ID，说明两个实例是同一个对象
print("加法实例的Id和乘法实例的Id是同一个吗？",id(calculator1) == id(calculator2))
print("减法实例的Id和除法实例的Id是同一个吗？",id(calculator3) == id(calculator4))