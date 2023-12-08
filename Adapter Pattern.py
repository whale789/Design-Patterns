# 适配器模式
# 目标接口
class Target:
    def operate(self, x, y):
        pass


# 需要适配的类
class AdapteeAdd:
    def add(self, x, y):
        return x + y


# 适配器，将AdapteeAdd适配到Target接口
class AdapterAdd(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def operate(self, x, y):
        return self.adaptee.add(x, y)


# 客户端代码
def client_code(target):
    result = target.operate(5, 3)
    print(f"运算结果: {result}")


# 使用适配器将AdapteeAdd适配到Target接口
adaptee_add = AdapteeAdd()
adapter_add = AdapterAdd(adaptee_add)

# 调用客户端代码，不需要知道具体的实现类
client_code(adapter_add)
