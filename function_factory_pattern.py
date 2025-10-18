def function_factory_pattern():
    """函数工厂模式"""
    print("\n=== 函数工厂模式 ===\n")
    
    import math
    # 1. 数学函数工厂
    def math_function_factory(function_type, **params):
        """数学函数工厂"""
        import math
        
        factories = {
            'polynomial': lambda: _create_polynomial(**params),
            'trigonometric': lambda: _create_trigonometric(**params),
            'exponential': lambda: _create_exponential(**params),
            'logarithmic': lambda: _create_logarithmic(**params)
        }
        
        if function_type not in factories:
            raise ValueError(f"不支持的函数类型: {function_type}")
        
        return factories[function_type]()
    
    def _create_polynomial(coefficients):
        """创建多项式函数"""
        def polynomial(x):
            return sum(coef * (x ** i) for i, coef in enumerate(coefficients))
        return polynomial
    
    def _create_trigonometric(func_type='sin', amplitude=1, frequency=1, phase=0):
        """创建三角函数"""
        trig_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan
        }
        
        def trigonometric(x):
            return amplitude * trig_functions[func_type](frequency * x + phase)
        return trigonometric
    
    def _create_exponential(base=math.e):
        """创建指数函数"""
        def exponential(x):
            return base ** x
        return exponential
    
    def _create_logarithmic(base=math.e):
        """创建对数函数"""
        def logarithmic(x):
            if x <= 0:
                raise ValueError("对数函数定义域为 x > 0")
            return math.log(x) / math.log(base)
        return logarithmic
    
    # 使用函数工厂
    print("函数工厂创建:")
    
    # 创建多项式
    poly_factory = math_function_factory('polynomial', coefficients=[1, -2, 1])
    print(f"  多项式 f(x) = x² - 2x + 1")
    print(f"  f(1) = {poly_factory(1)}, f(2) = {poly_factory(2)}")
    
    # 创建三角函数
    sine_factory = math_function_factory('trigonometric', func_type='sin', 
                                       amplitude=2, frequency=2)
    print(f"\n  三角函数 f(x) = 2sin(2x)")
    print(f"  f(π/4) = {sine_factory(math.pi/4):.3f}")
    
    # 创建指数函数
    exp_factory = math_function_factory('exponential', base=2)
    print(f"\n  指数函数 f(x) = 2^x")
    print(f"  f(3) = {exp_factory(3)}, f(4) = {exp_factory(4)}")

function_factory_pattern()

def strategy_pattern():
    """策略模式与回调函数"""
    print("\n=== 策略模式 ===\n")
    
    # 数值积分策略
    class IntegrationStrategy:
        """积分策略基类"""
        
        def integrate(self, func, a, b, n=1000):
            raise NotImplementedError("子类必须实现integrate方法")
    
    class RectangleStrategy(IntegrationStrategy):
        """矩形法积分策略"""
        
        def integrate(self, func, a, b, n=1000):
            h = (b - a) / n
            return sum(func(a + i * h) for i in range(n)) * h
    
    class TrapezoidalStrategy(IntegrationStrategy):
        """梯形法积分策略"""
        
        def integrate(self, func, a, b, n=1000):
            h = (b - a) / n
            x_values = [a + i * h for i in range(n + 1)]
            y_values = [func(x) for x in x_values]
            return h * (0.5 * y_values[0] + sum(y_values[1:-1]) + 0.5 * y_values[-1])
    
    class SimpsonStrategy(IntegrationStrategy):
        """辛普森法积分策略"""
        
        def integrate(self, func, a, b, n=1000):
            if n % 2 != 0:
                n += 1
            h = (b - a) / n
            x_values = [a + i * h for i in range(n + 1)]
            y_values = [func(x) for x in x_values]
            
            result = y_values[0] + y_values[-1]
            result += 4 * sum(y_values[i] for i in range(1, n, 2))
            result += 2 * sum(y_values[i] for i in range(2, n-1, 2))
            return result * h / 3
    
    # 积分计算器
    def integrate_calculator(func, a, b, strategy: IntegrationStrategy, n=1000):
        """使用策略模式计算积分"""
        return strategy.integrate(func, a, b, n)
    
    # 测试不同策略
    test_func = lambda x: x**2  # ∫x² dx 从0到1 = 1/3
    
    strategies = {
        '矩形法': RectangleStrategy(),
        '梯形法': TrapezoidalStrategy(), 
        '辛普森法': SimpsonStrategy()
    }
    
    print("不同积分策略比较 (∫x² dx 从 0 到 1):")
    exact_value = 1/3
    
    for name, strategy in strategies.items():
        result = integrate_calculator(test_func, 0, 1, strategy)
        error = abs(result - exact_value)
        print(f"  {name}: {result:.6f} (误差: {error:.2e})")

strategy_pattern()