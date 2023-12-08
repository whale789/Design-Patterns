#观察者模式

from abc import ABC, abstractmethod

# 抽象主题接口
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# 具体主题，表示运算的结果
class Calculator(Subject):
    def __init__(self):
        self._result = 0
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._result)

    def set_result(self, result):
        self._result = result
        self.notify_observers()

# 抽象观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, result):
        pass

# 具体观察者，打印运算结果
class PrintObserver(Observer):
    def update(self, result):
        print(f"Result: {result}")

# 具体观察者，记录运算结果
class LogObserver(Observer):
    def update(self, result):
        with open("log.txt", "a") as log_file:
            log_file.write(f"Result: {result}\n")

# 客户端代码
calculator = Calculator()

# 添加观察者
print_observer = PrintObserver()
log_observer = LogObserver()

calculator.add_observer(print_observer)
calculator.add_observer(log_observer)

# 模拟运算并通知观察者
calculator.set_result(5 + 3)
calculator.set_result(5 * 3)

# 移除观察者
calculator.remove_observer(log_observer)

# 模拟运算并通知观察者
calculator.set_result(10 / 2)
