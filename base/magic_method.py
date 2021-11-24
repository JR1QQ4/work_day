#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class BaseMethod:
    def __new__(cls, *args, **kwargs):
        """
        使用类创建对象时，底层会自动调用这个方法来完成对象的创建
        如果方法中没没有创建对象，也没有返回对象，那么最终创建的对象打印为 None
        一般情况下我们都不会自己去重定义，只有在有特定的需求时才会去用，比如要修改或者控制类创建对象行为时，如实现单例类等等
        """
        print("__________new 方法__________")

    def __init__(self):
        print("__________init 方法__________")


class SingleMethod:
    instance = None

    def __new__(cls, *args, **kwargs):
        print("__________new 方法__________")
        if cls.instance is None:
            # Python3 下的三种写法
            # cls.instance = super(SingleMethod, cls).__new__(cls)
            # cls.instance = super(SingleMethod, cls).__new__(cls, *args, **kwargs)
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("__________init 方法__________")


if __name__ == '__main__':
    # a = BaseMethod()  # __________new 方法__________
    # print(a)  # None

    b = SingleMethod()
    c = SingleMethod()
    print(id(b), id(c))  # 1901947769800 1901947769800


























