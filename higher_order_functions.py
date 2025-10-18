def higher_order_functions():
    """高阶函数详解"""
    print("\n=== 高阶函数 ===\n")
    
    # 1. 函数作为参数
    def apply_operation(func, numbers):
        """应用函数到数字列表"""
        return [func(x) for x in numbers]
    
    # 2. 函数作为返回值
    def create_multiplier(factor):
        """创建乘法器函数"""
        def multiplier(x):
            return x * factor
        return multiplier
    
    # 3. 函数装饰器
    def timer_decorator(func):
        """计时装饰器"""
        import time
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.6f}秒")
            return result
        return wrapper
    
    # 4. 函数柯里化
    def curry_function(func):
        """函数柯里化"""
        def curried(*args):
            if len(args) >= func.__code__.co_argcount:
                return func(*args)
            else:
                return lambda *more_args: curried(*(args + more_args))
        return curried
    
    # 使用高阶函数
    numbers = [1, 2, 3, 4, 5]
    
    print("1. 函数作为参数:")
    squared = apply_operation(lambda x: x**2, numbers)
    print(f"   平方: {squared}")
    
    print("\n2. 函数作为返回值:")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"   2倍: {double(5)}, 3倍: {triple(5)}")
    
    print("\n3. 装饰器应用:")
    @timer_decorator
    def slow_function():
        """模拟耗时函数"""
        import time
        time.sleep(0.1)
        return "完成"
    
    result = slow_function()
    print(f"   结果: {result}")
    
    print("\n4. 柯里化:")
    @curry_function
    def polynomial_curried(a, b, c, x):
        """柯里化多项式"""
        return a*x**2 + b*x + c
    
    # 逐步应用参数
    step1 = polynomial_curried(1)      # 设置 a=1
    step2 = step1(2)                   # 设置 b=2  
    step3 = step2(3)                   # 设置 c=3
    final = step3(4)                   # 计算 x=4
    print(f"   柯里化计算: {final}")

higher_order_functions()