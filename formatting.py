name = "李华"
scores = [85, 92, 78]
average = sum(scores) / len(scores)
print(f"{name}的平均分: {average:.2f}")
# 基本用法
name = "李华"
age = 18
score = 92.5

print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")

# 数学格式化
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}") #保留小数
print(f"{a} // {b} = {a // b}") #取整
print(f"{a} % {b} = {a % b}") #取余
print(f"{a} ** {b} = {a ** b}") #幂运算

pi = 3.1415926
print(f"默认: {pi}")
print(f"2位小数: {pi:.2f}")
print(f"4位小数: {pi:.4f}")

scores = [85, 92, 78, 96]
average = sum(scores) / len(scores)
print(f"平均分: {average}")
print(f"平均分: {average:.1f}")

number = 123
print(f"右对齐: {number:>10}")
print(f"左对齐: {number:<10}")
print(f"居中对齐: {number:^10}")
print(f"零填充: {number:08}")

completion = 0.856
print(f"完成度: {completion:.1%}")
print(f"完成度: {completion:.2%}")


# 字符串对齐
name = "张三"
course = "数学分析"

print(f"姓名: {name:<8} | 课程: {course}")    # 姓名: 张三      | 课程: 数学分析
print(f"姓名: {name:^8} | 课程: {course}")    # 姓名:    张三   | 课程: 数学分析  
print(f"姓名: {name:>8} | 课程: {course}")    # 姓名:       张三 | 课程: 数学分析

# 自定义填充字符
title = "成绩单"
print(f"{title:-^30}")    # ------------成绩单------------
print(f"{title:*^30}")    # ************成绩单************
print(f"{title:>30}")     #                         成绩单