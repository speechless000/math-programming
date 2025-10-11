def smart_grade_calculator():
    """智能成绩计算器"""
    print("=== 智能成绩系统 ===")
    
    # 获取学生信息
    name = input("学生姓名: ")
    math = float(input("数学成绩: "))
    english = float(input("英语成绩: "))
    attendance = float(input("出勤率(0-1): "))
    
    # 计算平均分
    average = (math + english) / 2
    
    print(f"\n{name}的成绩分析")
    print("=" * 30)
    
    # 成绩等级评定
    if average >= 90:
        grade = "A"
        evaluation = "优秀"
    elif average >= 80:
        grade = "B"
        evaluation = "良好"
    elif average >= 70:
        grade = "C" 
        evaluation = "中等"
    elif average >= 60:
        grade = "D"
        evaluation = "及格"
    else:
        grade = "F"
        evaluation = "不及格"

    print(f"平均分: {average:.1f}")
    print(f"成绩等级: {grade} ({evaluation})")
    
    # 特殊资格检查
    print(f"\n🎯 资格检查:")
    
    # 奖学金资格
    if (math >= 85 and english >= 85 and attendance >= 0.9):
        print("  ✅ 符合奖学金申请条件")
    
    # 竞赛资格
    if (math >= 90 or english >= 90) and attendance >= 0.8:
        print("  ✅ 符合学科竞赛条件")
    
    # 预警检查
    if math < 60 or english < 60:
        print("  ⚠️  有科目不及格，需要关注")
    
    if attendance < 0.8:
        print("  ⚠️  出勤率不足，需要注意")
    
    # 个性化建议
    print(f"\n💡 学习建议:")
    if math < english:
        print("  • 数学需要加强练习")
    elif english < math:
        print("  • 英语需要更多练习")
    else:
        print("  • 各科成绩均衡，继续保持")
    
    if average >= 80 and attendance >= 0.9:
        print("  • 表现优秀，继续保持!")
    elif average < 60:
        print("  • 需要制定学习计划，寻求老师帮助")

def subject_specific_feedback():
    学科特定反馈
    print("\n=== 学科详细反馈 ===")
    
    math_score = float(input("数学成绩: "))
    english_score = float(input("英语成绩: "))
    
    print(f"\n📚 学科分析:")
    
    # 数学分析
    if math_score >= 90:
        print("  数学: 非常优秀！逻辑思维能力很强")
    elif math_score >= 80:
        print("  数学: 良好，继续保持练习")
    elif math_score >= 70:
        print("  数学: 中等，需要加强练习")
    else:
        print("  数学: 需要重点提升，建议多做练习题")
    
    # 英语分析
    if english_score >= 90:
        print("  英语: 非常优秀！语言表达能力很强")
    elif english_score >= 80:
        print("  英语: 良好，多读多练")
    elif english_score >= 70:
        print("  英语: 中等，需要加强词汇和阅读")
    else:
        print("  英语: 需要重点提升，建议每天背单词")

if __name__ == "__main__":
    smart_grade_calculator()
    subject_specific_feedback()
    print("\n智能成绩系统完成!")