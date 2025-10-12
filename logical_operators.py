# 逻辑运算符练习

# 学生资格检查
math_score = 85
english_score = 92
attendance = 0.95  # 出勤率95%

print("=== 学生资格检查 ===")
print(f"数学: {math_score}, 英语: {english_score}, 出勤: {attendance*100}%")

# 逻辑运算
print("\n=== 逻辑运算结果 ===")

# and: 所有条件都要满足
can_get_scholarship = (math_score >= 80) and (english_score >= 80) and (attendance >= 0.9)
print(f"可以获得奖学金: {can_get_scholarship}")

# or: 至少一个条件满足
can_join_competition = (math_score >= 90) or (english_score >= 90)
print(f"可以参加竞赛: {can_join_competition}")

# not: 条件取反
is_failing = not (math_score >= 60)
print(f"数学不及格: {is_failing}")

# 复杂条件组合
print("\n=== 复杂条件 ===")
has_good_grades = (math_score >= 85) and (english_score >= 85)
has_good_attendance = attendance >= 0.9

if has_good_grades and has_good_attendance:
    print("🎉 优秀学生！可以获得奖励")
elif has_good_grades or has_good_attendance:
    print("👍 表现良好，继续努力")
else:
    print("💪 需要更加努力")
