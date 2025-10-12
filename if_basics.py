# 条件判断基础
# 1. 简单的if语句
temperature = 28

if temperature > 30:
    print("天气很热，建议穿短袖")
if temperature <= 30:
    print("天气舒适，可以穿长袖")

# 2. if-else 结构
score = 75

if score >= 60:
    print("✅ 考试及格！")
else:
    print("❌ 考试不及格")

# 3. if-elif-else 多条件
grade = 85

if grade >= 90:
    print("优秀！")
elif grade >= 80:
    print("良好")
elif grade >= 70:
    print("中等")
elif grade >= 60:
    print("及格")
else:
    print("需要加油")
# 4. 嵌套的if语句
age = 20
if age < 18:
    print("未成年")
else:
    if age < 65:
        print("成年人")
    else:
        print("老年人") 