def parameter_detailed():
    """函数参数深度解析"""
    print("\n=== 函数参数详解 ===\n")
    
    # 1. 位置参数
    def power(base, exponent):
        """计算幂 - 位置参数"""
        return base ** exponent
    
    # 2. 关键字参数
    def introduce(name, age, city):
        """自我介绍 - 关键字参数"""
        return f"我叫{name}, {age}岁, 来自{city}"
    
    # 3. 默认参数
    def create_polynomial(a=1, b=0, c=0):
        """创建多项式 - 默认参数"""
        def polynomial(x):
            return a*x**2 + b*x + c
        return polynomial
    
    # 4. 可变参数 *args
    def sum_numbers(*args):
        """求和 - 可变位置参数"""
        return sum(args)
    
    # 5. 可变关键字参数 **kwargs
    def create_student(**kwargs):
        """创建学生信息 - 可变关键字参数"""
        student = {
            'name': kwargs.get('name', '未知'),
            'age': kwargs.get('age', 0),
            'major': kwargs.get('major', '未定')
        }
        return student
    
    # 调用演示
    print("1. 位置参数:", power(2, 3))                    # 2^3
    print("2. 关键字参数:", introduce(age=20, name="小明", city="北京"))
    print("3. 默认参数 - 二次函数:", create_polynomial()(2))  # x^2
    print("3. 默认参数 - 一次函数:", create_polynomial(b=2)(2)) # 2x
    
    print("4. 可变参数:", sum_numbers(1, 2, 3, 4, 5))
    print("5. 可变关键字参数:", create_student(name="小红", age=19))
    
    # 混合参数
    def mixed_parameters(a, b=2, *args, **kwargs):
        """混合参数类型"""
        result = {
            'a': a,
            'b': b,
            'args': args,
            'kwargs': kwargs
        }
        return result
    
    print("混合参数:", mixed_parameters(1, 3, 4, 5, name="test", value=10))

parameter_detailed()