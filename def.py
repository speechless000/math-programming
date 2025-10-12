def 函数名(参数1, 参数2):
    """文档字符串（可选）"""
    # 函数体
    # 执行语句
    return #返回值  # 可选
    # 如果没有返回值，函数默认返回 None

# 示例：定义一个简单的函数
def greet(name):
    """返回问候语"""
    return f"Hello, {name}!"

# 调用函数
message = greet("Alice")
print(message)  # 输出: Hello, Alice!

#1. 代码复用
# 没有使用函数 - 重复代码
print("=== 学生1 ===")
score1 = 85
if score1 >= 90:
    print("优秀")
elif score1 >= 60:
    print("及格")
else:
    print("不及格")

print("=== 学生2 ===")
score2 = 72
if score2 >= 90:
    print("优秀")
elif score2 >= 60:
    print("及格")
else:
    print("不及格")

# 使用函数 - 消除重复
def evaluate_score(score, student_name):
    """评估学生成绩"""
    print(f"=== {student_name} ===")
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# 调用函数
result1 = evaluate_score(85, "学生1")
result2 = evaluate_score(72, "学生2")
print(result1)
print(result2)

#2. 模块化编程
# 数学分析工具包中的模块化应用
def calculate_derivative(func, x, h=1e-5):
    """数值计算导数"""
    return (func(x + h) - func(x - h)) / (2 * h)

def find_critical_points(func, start, end, step=0.1):
    """寻找临界点"""
    points = []
    x = start
    while x <= end:
        derivative = calculate_derivative(func, x)
        if abs(derivative) < 1e-6:  # 导数为零的点
            points.append((x, func(x)))
        x += step
    return points

def analyze_function(func, interval):
    """综合分析函数"""
    critical_points = find_critical_points(func, *interval)
    return {
        'critical_points': critical_points,
        'increasing': len([p for p in critical_points if p[1] > 0]),
        'decreasing': len([p for p in critical_points if p[1] < 0])
    }

# 使用模块化函数
# 数学分析工具包中的模块化应用
def calculate_derivative(func, x, h=1e-5):
    """数值计算导数"""
    return (func(x + h) - func(x - h)) / (2 * h)

def find_critical_points(func, start, end, step=0.1):
    """寻找临界点"""
    points = []
    x = start
    while x <= end:
        derivative = calculate_derivative(func, x)
        if abs(derivative) < 1e-6:  # 导数为零的点
            points.append((x, func(x)))
        x += step
    return points

def analyze_function(func, interval):
    """综合分析函数"""
    critical_points = find_critical_points(func, *interval)
    return {
        'critical_points': critical_points,
        'increasing': len([p for p in critical_points if p[1] > 0]),
        'decreasing': len([p for p in critical_points if p[1] < 0])
    }

# 使用模块化函数
def calculate_derivative(func, x, h=1e-5):
    """数值计算导数"""
    return (func(x + h) - func(x - h)) / (2 * h)
def find_critical_points(func, start, end, step=0.1):
    """寻找临界点"""
    points = []
    x = start
    while x <= end:
        derivative = calculate_derivative(func, x)
        if abs(derivative) < 1e-6:  # 导数为零的点
            points.append((x, func(x)))
        x += step
    return points
def analyze_function(func, interval):
    """综合分析函数"""
    critical_points = find_critical_points(func, *interval)
    return {
        'critical_points': critical_points,
        'increasing': len([p for p in critical_points if p[1] > 0]),
        'decreasing': len([p for p in critical_points if p[1] < 0])
    }
# 使用模块化函数
def calculate_derivative(func, x, h=1e-5):
    """数值计算导数"""
    return (func(x + h) - func(x - h)) / (2 * h)

# 使用函数提高可读性
    #难以理解的代码
data = [1, 2, 3, 4, 5]
result = sum([x**2 for x in data if x % 2 == 0]) / len([x for x in data if x % 2 == 0])

def calculate_even_squares_average(numbers):
    """计算偶数的平方平均值"""
    even_numbers = [x for x in numbers if x % 2 == 0] # 筛选偶数
    squared_evens = [x**2 for x in even_numbers] # 计算平方
    return sum(squared_evens) / len(squared_evens) if squared_evens else 0 # 计算平均值

data = [1, 2, 3, 4, 5]
result = calculate_even_squares_average(data)
print(result)  # 输出: (4 + 16) / 2 = 10.0

#默认参数
def create_polynomial(coefficients, variable='x'):
    """
    创建多项式字符串表示
    coefficients: [a0, a1, a2] 对应 a0 + a1*x + a2*x^2
    """
    terms = []
    for i, coef in enumerate(coefficients):
        if coef != 0:
            if i == 0:
                terms.append(f"{coef}")
            elif i == 1:
                terms.append(f"{coef}{variable}")
            else:
                terms.append(f"{coef}{variable}^{i}")
    
    return " + ".join(terms) if terms else "0"

print(create_polynomial([1, 2, 3]))        # 输出: 1 + 2x + 3x^2
print(create_polynomial([0, 1, -1], 't'))  # 输出: 1t + -1t^2
