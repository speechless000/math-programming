def mathematical_functions():
    """数学函数实现"""
    print("\n=== 数学函数实现 ===\n")
    
    import math
    
    # 1. 多项式函数
    def polynomial(coefficients):
        """创建多项式函数"""
        def poly_func(x):
            result = 0
            for i, coef in enumerate(coefficients):
                result += coef * (x ** i)
            return result
        return poly_func
    
    # 2. 三角函数组合
    def trigonometric_combo(amplitude=1, frequency=1, phase=0):
        """创建三角函数组合"""
        def trig_func(x):
            return amplitude * math.sin(frequency * x + phase)
        return trig_func
    
    # 3. 指数函数
    def exponential_function(base=math.e):
        """创建指数函数"""
        def exp_func(x):
            return base ** x
        return exp_func
    
    # 4. 分段函数
    def piecewise_function():
        """创建分段函数"""
        def piecewise(x):
            if x < 0:
                return x ** 2          # 抛物线
            elif 0 <= x < 2:
                return 2 * x + 1       # 直线
            else:
                return math.log(x)     # 对数
        return piecewise
    
    # 测试函数
    print("1. 多项式函数:")
    quadratic = polynomial([1, -2, 1])  # x^2 - 2x + 1
    print(f"   f(x) = x² - 2x + 1")
    print(f"   f(1) = {quadratic(1)}, f(2) = {quadratic(2)}")
    
    print("\n2. 三角函数:")
    sine_wave = trigonometric_combo(amplitude=2, frequency=2)
    print(f"   f(x) = 2sin(2x)")
    print(f"   f(π/4) = {sine_wave(math.pi/4):.3f}")
    
    print("\n3. 指数函数:")
    exp_func = exponential_function(2)  # 2^x
    print(f"   f(x) = 2^x")
    print(f"   f(3) = {exp_func(3)}, f(4) = {exp_func(4)}")
    
    print("\n4. 分段函数:")
    piecewise = piecewise_function()
    test_points = [-1, 0, 1, 3]
    for x in test_points:
        print(f"   f({x}) = {piecewise(x):.3f}")

mathematical_functions()