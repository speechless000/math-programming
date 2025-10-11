score_str = str(input("请输入你的成绩: "))
score_float = float(score_str)
score_int = int(score_float)

print("你的成绩是: ", score_int)
print("整数是: ", type(score_int))
print("浮点数是: ", type(score_float))
print("字符串是: ", type(score_str))

score_test = "成绩是: " + str(score_int)
print(score_test)

data_list = [
    "25",      # 年龄字符串
    "175.5",   # 身高字符串  
    "88.5",    # 成绩字符串
    "100",     # 满分字符串
    "3.14159"  # PI字符串
]

print("原始数据:")
for i, item in enumerate(data_list, 1):
    print(f"  数据{i}: '{item}' (类型: {type(item).__name__})")

print("\n转换结果:") # 打印一个换行符，相当于空一行
# 转换为整数（如果可以）
age_int = int(data_list[0])
print(f"  '{data_list[0]}' → 整数: {age_int}")

# 转换为浮点数
height_float = float(data_list[1])
score_float = float(data_list[2])
pi_float = float(data_list[4])
print(f"  '{data_list[1]}' → 浮点数: {height_float}")
print(f"  '{data_list[2]}' → 浮点数: {score_float}")
print(f"  '{data_list[4]}' → 浮点数: {pi_float}")

# 练习1：实际计算应用
print("\n=== 练习2: 实际计算应用 ===")

# 学生信息处理
student_name = "李华"
birth_year = "2005"
current_year = 2024
height_cm = "175.5"
weight_kg = "65.2"

# 类型转换
birth_year_int = int(birth_year)
height_float = float(height_cm)
weight_float = float(weight_kg)

# 计算年龄
age = current_year - birth_year_int

# 计算BMI（体重kg / 身高m²）
height_m = height_float / 100
bmi = weight_float / (height_m ** 2)

print(f"学生: {student_name}")
print(f"出生年份: {birth_year_int} → 年龄: {age}岁")
print(f"身高: {height_float} cm → {height_m:.2f} m")
print(f"体重: {weight_float} kg")
print(f"BMI指数: {bmi:.2f}")

# 练习2：错误处理演示
print("\n=== 练习2: 错误处理 ===")

# 安全的类型转换函数
def safe_int_conversion(value, default=0):
    """安全地将值转换为整数"""
    try:
        return int(value)
    except ValueError:
        print(f"⚠️  警告: 无法将 '{value}' 转换为整数，使用默认值 {default}")
        return default

def safe_float_conversion(value, default=0.0):
    """安全地将值转换为浮点数"""
    try:
        return float(value)
    except ValueError:
        print(f"⚠️  警告: 无法将 '{value}' 转换为浮点数，使用默认值 {default}")
        return default

# 测试安全转换
test_data = ["100", "95.5", "abc", "75.5", "123abc"]

print("安全类型转换测试:")
for data in test_data: #for循环语句 遍历test_data列表中的每个元素，并将当前元素赋值给变量data
    int_result = safe_int_conversion(data)
    float_result = safe_float_conversion(data)
    print(f"  '{data}' → 整数: {int_result}, 浮点数: {float_result}")