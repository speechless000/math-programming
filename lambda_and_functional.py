def lambda_and_functional():
    """匿名函数与函数式编程"""
    print("\n=== 匿名函数与函数式编程 ===\n")
    
    # 1. lambda 函数
    def demonstrate_lambda():
        """lambda函数演示"""
        # 基本lambda
        square = lambda x: x ** 2
        add = lambda x, y: x + y
        
        # 在排序中使用
        points = [(1, 2), (3, 1), (2, 3), (4, 0)]
        sorted_by_y = sorted(points, key=lambda point: point[1])
        
        # 在map中使用
        numbers = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, numbers))
        
        # 在filter中使用
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        
        print("Lambda函数:")
        print(f"  square(5) = {square(5)}")
        print(f"  add(3,4) = {add(3, 4)}")
        print(f"  按y坐标排序: {sorted_by_y}")
        print(f"  平方映射: {squared}")
        print(f"  偶数过滤: {evens}")
    
    # 2. 函数式编程工具
    def functional_tools():
        """函数式编程工具"""
        from functools import reduce, partial
        
        numbers = [1, 2, 3, 4, 5]
        
        # map: 对每个元素应用函数
        squared = list(map(lambda x: x**2, numbers))
        
        # filter: 过滤元素
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        
        # reduce: 累积计算
        product = reduce(lambda x, y: x * y, numbers)
        
        # partial: 部分应用函数
        def power(base, exponent):
            return base ** exponent
        
        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)
        
        print("\n函数式编程工具:")
        print(f"  map平方: {squared}")
        print(f"  filter偶数: {evens}")
        print(f"  reduce乘积: {product}")
        print(f"  partial平方: {square(5)}, 立方: {cube(3)}")
    
    # 3. 生成器函数
    def generator_functions():
        """生成器函数"""
        def fibonacci_generator(n):
            """生成斐波那契数列"""
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        
        def function_values_generator(func, start, end, step):
            """生成函数值"""
            x = start
            while x <= end:
                yield (x, func(x))
                x += step
        
        print("\n生成器函数:")
        print("  斐波那契数列:", list(fibonacci_generator(10)))
        
        # 函数值生成器
        func_gen = function_values_generator(lambda x: x**2, 0, 2, 0.5)
        print("  函数值生成:")
        for x, y in func_gen:
            print(f"    f({x}) = {y}")
    
    demonstrate_lambda()
    functional_tools()
    generator_functions()

lambda_and_functional()