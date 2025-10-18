def function_fundamentals():
    """函数基础概念演示"""
    print("=== 函数基础 ===\n")
    
    # 1. 最简单的函数
    def greet():
        """简单的问候函数"""
        return "Hello, World!"
    
    # 2. 带参数的函数
    def greet_person(name):
        """带参数的问候函数"""
        return f"Hello, {name}!"
    
    # 3. 带默认参数的函数
    def greet_with_time(name, time_of_day="day"):
        """带默认参数的函数"""
        return f"Good {time_of_day}, {name}!"
    
    # 4. 返回多个值的函数
    def calculate_stats(numbers):
        """计算统计量并返回多个值"""
        total = sum(numbers)
        count = len(numbers)
        average = total / count if count > 0 else 0
        return total, count, average
    
    # 调用函数
    print("1. 简单函数:", greet())
    print("2. 带参数函数:", greet_person("Alice"))
    print("3. 默认参数函数:", greet_with_time("Bob", "morning"))
    print("4. 默认参数(省略):", greet_with_time("Charlie"))
    
    # 多返回值接收
    numbers = [1, 2, 3, 4, 5]
    total, count, avg = calculate_stats(numbers)
    print(f"4. 多返回值: 总和={total}, 个数={count}, 平均={avg}")
    
    return greet_person

# 运行基础演示
basic_function = function_fundamentals()

def function_best_practices():
    """函数最佳实践总结"""
    print("\n=== 函数最佳实践 ===\n")
    
    practices = [
        "🎯 单一职责原则: 每个函数只做一件事",
        "📝 明确命名: 使用描述性的函数名",
        "📚 完整文档: 为函数添加docstring",
        "🎪 类型提示: 使用类型注解提高可读性",
        "🛡️ 错误处理: 合理处理异常情况",
        "🧪 单元测试: 为关键函数编写测试",
        "🔄 纯函数: 尽量避免副作用",
        "📏 适当长度: 函数不宜过长(建议<20行)",
        "🎭 参数合理: 参数不宜过多(建议<5个)",
        "✨ 返回值明确: 返回类型应该清晰"
    ]
    
    print("函数设计最佳实践:")
    for practice in practices:
        print(f"  • {practice}")
    
    # 好函数 vs 坏函数示例
    print("\n好函数示例:")
    good_example = '''
def calculate_circle_area(radius: float) -> float:
    """计算圆的面积
    
    参数:
        radius: 圆的半径
        
    返回:
        圆的面积
        
    异常:
        ValueError: 当半径为负数时
    """
    if radius < 0:
        raise ValueError("半径不能为负数")
    return math.pi * radius ** 2
'''
    print(good_example)
    
    print("\n坏函数示例:")
    bad_example = '''
def do_stuff(r, x, y, calc=True, draw=False, save=True):
    # 这个函数做了太多事情，参数过多，没有文档
    area = 3.14 * r * r
    if calc:
        result = x + y
    if draw:
        print("drawing...")
    if save:
        with open("file.txt", "w") as f:
            f.write(str(result))
    return area, result
'''
    print(bad_example)

function_best_practices()