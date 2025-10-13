print("=== while循环基础 ===")

# 1. 计数器循环
print("计数器循环:")
count = 1
while count <= 5:
    print(f"计数: {count}")
    count += 1  # 重要：更新循环变量

# 2. 条件控制循环
print("\n条件控制循环:") 
import random # 导入随机数模块
target = random.randint(1, 10) # 生成1到10之间的随机整数
guess = 0 # 初始化猜测值
attempts = 0 # 初始化尝试次数

print("猜数字游戏 (1-10)")
while guess != target:
    guess = int(input("你的猜测: "))
    attempts += 1
    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")

print(f"恭喜！你在 {attempts} 次尝试后猜对了！")

# 3. 无限循环与break
print("\n无限循环示例:")
while True:
    user_input = input("输入 'quit' 退出: ") # 获取用户输入
    if user_input.lower() == 'quit': # 检查是否为退出命令
        print("退出循环")
        break
    print(f"你输入了: {user_input}") # 回显输入

# 4. 使用continue跳过迭代
print("\n使用continue跳过偶数:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0: # 如果是偶数，跳过本次循环
        continue
    print(f"奇数: {num}")

# 5. 嵌套循环
print("\n嵌套循环打印乘法表:")
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i*j:2}", end=' ') # 打印乘积，格式化输出
        j += 1
    print() # 换行
    i += 1

# 6. 使用while循环实现二分法求根（在数学分析中的应用）
print("\n使用while循环实现二分法求根:")
def find_root_bisection(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    使用二分法求函数根 - while循环应用
    在区间[a, b]上寻找f(x)=0的解
    """
    # 检查区间端点
    fa, fb = func(a), func(b) # 计算端点函数值

    if fa * fb > 0: # 退出条件
        return None, "区间端点函数值同号，无法保证有根"

    print(f"\n二分法求根: 区间[{a}, {b}]")
    iteration = 0
    
    while (b - a) > tolerance and iteration < max_iterations: # 继续迭代直到满足精度或达到最大迭代次数
        iteration += 1
        c = (a + b) / 2  # 中点
        fc = func(c)
        
        print(f"迭代 {iteration}: x = {c:.6f}, f(x) = {fc:.6f}")
        
        if abs(fc) < tolerance:
            print(f"✅ 找到根: x = {c:.6f} (精确解)")
            return c, "成功"
        
        if fa * fc < 0:
            b, fb = c, fc  # 根在左半区间
        else:
            a, fa = c, fc  # 根在右半区间
    
    root = (a + b) / 2
    if abs(func(root)) < tolerance:
        print(f"✅ 找到根: x = {root:.6f} (达到精度)")
        return root, "成功"
    else:
        print(f"❌ 未在最大迭代次数内收敛")
        return root, "未完全收敛"

# 测试二分法
def test_function(x):
    return x**2 - 4  # 根为 x=2 和 x=-2

root, status = find_root_bisection(test_function, 0, 3)
print(f"结果: {root}, 状态: {status}")

# 7. 收敛性分析的while循环应用
print("\n收敛性分析示例:")
def analyze_sequence_convergence(sequence_func, tolerance=1e-6, max_terms=1000):
    """
    分析数列收敛性 - while循环应用
    """
    print(f"\n数列收敛性分析")
    print("项数\t值\t\t差值")
    print("-" * 35)
    
    n = 1
    previous = sequence_func(1)
    converged = False
    
    while n <= max_terms and not converged: # 继续直到达到最大项数或收敛
        current = sequence_func(n) # 计算当前项
        difference = abs(current - previous) # 计算与前一项的差值
        
        print(f"{n}\t{current:.8f}\t{difference:.2e}") # 打印当前项和差值
        
        if difference < tolerance and n > 1: # 收敛条件
            converged = True
            print(f"\n🎯 数列在 {n} 项后收敛")
            print(f"极限值: {current:.8f}")
        elif n == max_terms: # 达到最大项数
            print(f"\n⚠️  达到最大项数，可能不收敛")
        
        previous = current
        n += 1 # 更新项数
    
    return converged, current, n # 返回是否收敛，极限值，项数

# 测试数列收敛性
def harmonic_sequence(n):
    """调和数列: 1 + 1/2 + 1/3 + ... + 1/n"""
    return sum(1/i for i in range(1, n+1))

# 调和数列发散
converged, limit, terms = analyze_sequence_convergence(harmonic_sequence)

def geometric_sequence(n):
    """几何数列: 1/2 + 1/4 + 1/8 + ..."""
    return sum(0.5**i for i in range(1, n+1))

# 几何数列收敛
print("\n" + "="*50)
converged, limit, terms = analyze_sequence_convergence(geometric_sequence)