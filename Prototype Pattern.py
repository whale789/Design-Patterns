#原型模式
import copy

# 抽象原型类
class Prototype:
    def clone(self):
        pass

# 具体原型类
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        # 使用浅拷贝创建新对象
        return copy.copy(self)

    def __str__(self):
        return f"这是一个数： {self.value}"

# 客户端代码
original_object = ConcretePrototype(value=10)

# 使用原型模式复制对象
copied_object = original_object.clone()

# 修改原型对象的属性
original_object.value = 20

# 打印结果
print(f"原来的数据: {original_object}")
print(f"复制后的数据: {copied_object}")
