def function_documentation():
    """函数文档与类型提示"""
    print("\n=== 函数文档与类型提示 ===\n")
    
    from typing import List, Tuple, Callable, Optional
    
    def quadratic_roots(a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:
        """
        计算二次方程的根
        
        参数:
            a: 二次项系数
            b: 一次项系数  
            c: 常数项系数
            
        返回:
            包含两个根的元组，如果没有实根则返回(None, None)
            
        示例:
            >>> quadratic_roots(1, -3, 2)
            (2.0, 1.0)
            >>> quadratic_roots(1, 0, 1)  
            (None, None)
        """
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            root = -b / (2*a)
            return root, root
        else:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            return root1, root2
    
    def create_polynomial_function(coefficients: List[float]) -> Callable[[float], float]:
        """
        创建多项式函数
        
        参数:
            coefficients: 系数列表 [a0, a1, a2, ...] 对应 a0 + a1*x + a2*x² + ...
            
        返回:
            多项式函数
            
        示例:
            >>> f = create_polynomial_function([1, 2, 1])  # x² + 2x + 1
            >>> f(1)
            4.0
        """
        def polynomial(x: float) -> float:
            result = 0.0
            for i, coef in enumerate(coefficients):
                result += coef * (x ** i)
            return result
        
        return polynomial
    
    # 测试文档化函数
    print("二次方程求根:")
    roots1 = quadratic_roots(1, -3, 2)  # x² - 3x + 2 = 0
    roots2 = quadratic_roots(1, 0, 1)   # x² + 1 = 0
    print(f"  x² - 3x + 2 = 0 的根: {roots1}")
    print(f"  x² + 1 = 0 的根: {roots2}")
    
    print("\n多项式函数:")
    poly_func = create_polynomial_function([1, 2, 1])  # x² + 2x + 1
    print(f"  f(x) = x² + 2x + 1")
    print(f"  f(1) = {poly_func(1)}, f(2) = {poly_func(2)}")
    
    # 查看函数文档
    print(f"\n函数文档:")
    print(f"  {quadratic_roots.__doc__.splitlines()[1].strip()}")

function_documentation()


def function_testing_debugging():
    """函数测试与调试"""
    print("\n=== 函数测试与调试 ===\n")
    
    import math
    from typing import Callable # 导入 Callable 用于类型提示
    
    def numerical_derivative(func: Callable[[float], float], 
                           x: float, 
                           h: float = 1e-5) -> float:
        """
        数值计算导数
        
        参数:
            func: 目标函数
            x: 求导点
            h: 步长
            
        返回:
            导数值
            
        异常:
            ValueError: 当步长不合法时
        """
        if h <= 0:
            raise ValueError("步长必须为正数")
        
        return (func(x + h) - func(x - h)) / (2 * h)
    
    def test_numerical_derivative():
        """测试数值导数函数"""
        test_cases = [
            # (函数, 测试点, 期望导数, 描述)
            (lambda x: x**2, 2, 4, "f(x)=x² 在 x=2"),
            (math.sin, math.pi/2, 0, "f(x)=sin(x) 在 x=π/2"),
            (math.exp, 0, 1, "f(x)=e^x 在 x=0"),
        ]
        
        print("数值导数测试:")
        all_passed = True
        
        for func, x, expected, description in test_cases:
            try:
                result = numerical_derivative(func, x)
                error = abs(result - expected)
                tolerance = 1e-4
                
                status = "✅ PASS" if error < tolerance else "❌ FAIL"
                print(f"  {status} {description}")
                print(f"    结果: {result:.6f}, 期望: {expected}, 误差: {error:.2e}")
                
                if error >= tolerance:
                    all_passed = False
                    
            except Exception as e:
                print(f"  ❌ ERROR {description}: {e}")
                all_passed = False
        
        return all_passed
    
    def debug_function_behavior():
        """调试函数行为"""
        def problematic_function(x):
            """有潜在问题的函数"""
            # 添加调试信息
            print(f"DEBUG: 计算 f({x})")
            
            if x < 0:
                result = math.sqrt(-x)  # 对于负数，计算sqrt(-x)
            else:
                result = math.sqrt(x)
            
            print(f"DEBUG: 结果 = {result}")
            return result
        
        print("\n函数行为调试:")
        try:
            # 正常情况
            result1 = problematic_function(4)
            print(f"  f(4) = {result1}")
            
            # 边界情况
            result2 = problematic_function(-4)
            print(f"  f(-4) = {result2}")
            
        except Exception as e:
            print(f"  捕获异常: {e}")
    
    # 运行测试和调试
    test_passed = test_numerical_derivative()
    print(f"\n所有测试{'通过' if test_passed else '失败'}")
    
    debug_function_behavior()

function_testing_debugging()