# 📚 for循环基本语法
def for_loop_demo():
    # 示例：遍历一个列表
    sample_list = [10, 20, 30]
    for item in sample_list:
        print(f"列表项: {item}")


print("=== for循环基础 ===")

# 1. 遍历列表
numbers = [1, 2, 3, 4, 5] # 示例列表
print("遍历列表:") # 示例输出
for num in numbers: # 遍历列表
    print(f"数字: {num}, 平方: {num**2}") # 输出数字及其平方

# 2. 遍历字符串
word = "Math"
print("\n遍历字符串:") # 示例输出
for char in word: # 遍历字符串中的每个字符
    print(f"字符: {char}, ASCII: {ord(char)}") # 输出字符及其ASCII值

# 3. 使用range()函数
print("\n使用range():")
for i in range(5):  # 0到4
    print(f"i = {i}")

for i in range(2, 6):  # 2到5
    print(f"i = {i}")

for i in range(1, 10, 2):  # 1到9，步长为2
    print(f"奇数: {i}")    

#数学分析中的应用
print("\n数学分析中的应用:")
def analyze_function_on_interval(func, start, end, num_points):
    """在区间上分析函数 - 使用for循环"""
    print(f"\n🔍 分析函数在 [{start}, {end}] 上的行为")
    print("x\t\tf(x)")
    print("-" * 20)
    
    step = (end - start) / (num_points - 1)
    
    for i in range(num_points):
        x = start + i * step
        try:
            y = func(x)
            print(f"{x:.2f}\t\t{y:.4f}")
        except (ValueError, ZeroDivisionError):
            print(f"{x:.2f}\t\tundefined")

# 测试函数
def quadratic(x):
    return x**2 - 4*x + 3

# 使用for循环分析
analyze_function_on_interval(quadratic, 0, 5, 6)

# 嵌套for循环
def generate_multiplication_table(n):
    """生成乘法表 - 嵌套for循环"""
    print(f"\n📊 {n}×{n}乘法表")
    
    # 表头
    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n   " + "----" * n)
    
    # 表格内容
    for i in range(1, n + 1):
        print(f"{i:2}|", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

# 生成乘法表
generate_multiplication_table(5)