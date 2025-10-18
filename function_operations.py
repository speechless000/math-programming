def function_operations():
    """函数操作与变换"""
    print("\n=== 函数操作与变换 ===\n")
    
    # 1. 函数组合
    def compose(f, g):
        """函数组合: f(g(x))"""
        def composed(x):
            return f(g(x))
        return composed
    
    # 2. 函数平移
    def shift_function(f, horizontal=0, vertical=0):
        """函数平移"""
        def shifted(x):
            return f(x - horizontal) + vertical
        return shifted
    
    # 3. 函数缩放
    def scale_function(f, horizontal=1, vertical=1):
        """函数缩放"""
        def scaled(x):
            return vertical * f(x / horizontal)
        return scaled
    
    # 4. 函数求导（数值方法）
    def derivative(f, h=1e-5):
        """数值求导"""
        def df(x):
            return (f(x + h) - f(x - h)) / (2 * h)
        return df
    
    # 测试函数操作
    def original_func(x):
        return x ** 2
    
    print("原始函数: f(x) = x²")
    print(f"f(2) = {original_func(2)}")
    
    # 函数组合
    g = lambda x: x + 1
    fog = compose(original_func, g)  # f(g(x)) = (x+1)²
    print(f"\n1. 函数组合 f(g(x)) = (x+1)²")
    print(f"   f(g(2)) = {fog(2)}")
    
    # 函数平移
    shifted = shift_function(original_func, horizontal=1, vertical=2)  # (x-1)² + 2
    print(f"\n2. 函数平移: f(x-1) + 2")
    print(f"   在 x=2: {shifted(2)}")
    
    # 函数缩放
    scaled = scale_function(original_func, horizontal=2, vertical=3)  # 3*(x/2)²
    print(f"\n3. 函数缩放: 3f(x/2) = 3*(x/2)²")
    print(f"   在 x=4: {scaled(4)}")
    
    # 数值求导
    df = derivative(original_func)  # 2x
    print(f"\n4. 数值导数: f'(x) ≈ 2x")
    print(f"   f'(2) ≈ {df(2):.6f} (理论值: 4.0)")

function_operations()