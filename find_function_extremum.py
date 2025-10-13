import math

def find_function_extremum(func, search_range, step=0.01):
    """
    寻找函数极值 - 综合循环应用
    """
    start, end = search_range
    x = start
    max_point = (start, func(start))
    min_point = (start, func(start))
    
    print(f"\n🔍 在 [{start}, {end}] 搜索极值")
    print("x\t\tf(x)\t\t状态")
    print("-" * 40)
    
    iteration = 0
    while x <= end:
        try:
            y = func(x)
            iteration += 1
            
            # 更新最大值
            if y > max_point[1]:
                max_point = (x, y)
                status = "新最大值"
            # 更新最小值
            elif y < min_point[1]:
                min_point = (x, y)
                status = "新最小值"
            else:
                status = "扫描中"
            
            if iteration % 50 == 0:  # 每50次显示一次进度
                print(f"{x:.3f}\t\t{y:.4f}\t\t{status}")
            
            x += step
            
        except (ValueError, ZeroDivisionError):
            x += step
            continue
    
    print(f"\n🎯 极值搜索结果:")
    print(f"最大值: f({max_point[0]:.3f}) = {max_point[1]:.4f}")
    print(f"最小值: f({min_point[0]:.3f}) = {min_point[1]:.4f}")
    
    return max_point, min_point

class FunctionExtremumAnalyzer:
    """函数极值分析器 - 面向对象版本"""
    
    def __init__(self, precision=1e-6):
        self.precision = precision
        self.analysis_history = []
    
    def find_extremum(self, func, interval, method='auto'):
        """
        寻找函数极值点
        
        参数:
            func: 目标函数
            interval: 搜索区间 (start, end)
            method: 搜索方法 ['auto', 'gradient', 'grid', 'newton', 'all']
        """
        if method == 'auto':
            # 自动选择方法
            results = self._auto_method_search(func, interval)
        elif method == 'all':
            # 使用所有方法并合并结果
            results = self._combined_method_search(func, interval)
        else:
            results = find_function_extremum(func, interval, method, 
                                           tolerance=self.precision)
        
        # 记录分析历史
        analysis_record = {
            'function': getattr(func, '__name__', '匿名函数'),
            'interval': interval,
            'method': method,
            'results': results,
            'timestamp': self._get_timestamp()
        }
        self.analysis_history.append(analysis_record)
        
        return results
    
    def _auto_method_search(self, func, interval):
        """自动选择搜索方法"""
        # 根据区间大小选择方法
        start, end = interval
        interval_size = end - start
        
        if interval_size > 10:
            # 大区间使用网格搜索快速定位
            coarse_results = find_function_extremum(func, interval, 'grid', step=0.1)
            # 然后在极值点附近使用精确方法
            refined_results = []
            for point in coarse_results:
                refined_interval = (point['position'] - 0.5, point['position'] + 0.5)
                refined = find_function_extremum(func, refined_interval, 'newton', 
                                               tolerance=self.precision)
                refined_results.extend(refined)
            return refined_results
        else:
            # 小区间直接使用牛顿法
            return find_function_extremum(func, interval, 'newton', 
                                        tolerance=self.precision)
    
    def _combined_method_search(self, func, interval):
        """组合多种方法搜索"""
        all_results = []
        
        methods = ['grid', 'gradient', 'newton']
        for method in methods:
            try:
                results = find_function_extremum(func, interval, method, 
                                               tolerance=self.precision)
                all_results.extend(results)
            except Exception as e:
                print(f"方法 {method} 失败: {e}")
        
                return _remove_duplicates(all_results)
        
        def _remove_duplicates(points, tol=1e-6):
            """去除极值点列表中的重复项（按位置和函数值）"""
            unique = []
            for p in points:
                if not any(abs(p['position'] - q['position']) < tol and abs(p['value'] - q['value']) < tol for q in unique):
                    unique.append(p)
            return unique
    
    def analyze_function_behavior(self, func, interval):
        """综合分析函数行为"""
        extremum_points = self.find_extremum(func, interval, 'all')
        
        # 计算函数在区间的统计信息
        start, end = interval
        num_samples = 100
        step = (end - start) / num_samples
        
        values = []
        for i in range(num_samples + 1):
            x = start + i * step
            try:
                values.append(func(x))
            except:
                values.append(float('nan'))
        
        valid_values = [v for v in values if not math.isnan(v)]
        
        analysis = {
            'extremum_points': extremum_points,
            'global_min': min(valid_values) if valid_values else None,
            'global_max': max(valid_values) if valid_values else None,
            'average': sum(valid_values) / len(valid_values) if valid_values else None,
            'monotonicity': self._analyze_monotonicity(func, interval),
            'convexity': self._analyze_convexity(func, interval)
        }
        
        return analysis
    
    def _analyze_monotonicity(self, func, interval):
        """分析函数单调性"""
        start, end = interval
        test_points = [start + i * (end - start) / 10 for i in range(11)]
        
        increasing = 0
        decreasing = 0
        
        for i in range(1, len(test_points)):
            try:
                delta = func(test_points[i]) - func(test_points[i-1])
                if delta > 0:
                    increasing += 1
                elif delta < 0:
                    decreasing += 1
            except:
                continue
        
        if increasing > decreasing * 2:
            return "递增"
        elif decreasing > increasing * 2:
            return "递减"
        else:
            return "波动"
    
    def _analyze_convexity(self, func, interval):
        """分析函数凸凹性"""
        def second_derivative(x, h=1e-5):
            return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
        
        start, end = interval
        test_points = [start + i * (end - start) / 10 for i in range(11)]
        
        convex = 0
        concave = 0
        
        for x in test_points:
            try:
                f_double_prime = second_derivative(x)
                if f_double_prime > 0:
                    convex += 1
                elif f_double_prime < 0:
                    concave += 1
            except:
                continue
        
        if convex > concave:
            return "凸函数"
        elif concave > convex:
            return "凹函数"
        else:
            return "混合"
    
    def _get_timestamp(self):
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def generate_report(self, analysis):
        """生成分析报告"""
        report = f"""
函数极值分析报告
================

函数行为分析:
--------------
单调性: {analysis['monotonicity']}
凸凹性: {analysis['convexity']}
全局最小值: {analysis['global_min']:.4f}
全局最大值: {analysis['global_max']:.4f}
平均值: {analysis['average']:.4f}

极值点分析:
------------
找到 {len(analysis['extremum_points'])} 个极值点:
"""
        
        for i, point in enumerate(analysis['extremum_points'], 1):
            report += f"""
{i}. 位置: x = {point['position']:.6f}
   函数值: f(x) = {point['value']:.6f}
   类型: {point['type']}
   方法: {point.get('method', '未知')}
   迭代次数: {point.get('iterations', 'N/A')}
"""
        
        return report
    
# 测试函数
import math

def test_extremum_finder():
    """测试极值点查找器"""
    print("=== 函数极值点查找测试 ===\n")
    
    # 创建分析器
    analyzer = FunctionExtremumAnalyzer()
    
    # 测试函数 1: 二次函数 f(x) = x^2 - 4x + 3
    def quadratic(x):
        return x**2 - 4*x + 3
    
    print("1. 二次函数 f(x) = x² - 4x + 3")
    results = analyzer.find_extremum(quadratic, (-1, 5), 'all')
    analysis = analyzer.analyze_function_behavior(quadratic, (-1, 5))
    print(analyzer.generate_report(analysis))
    
    # 测试函数 2: 三次函数 f(x) = x^3 - 3x
    def cubic(x):
        return x**3 - 3*x
    
    print("\n2. 三次函数 f(x) = x³ - 3x")
    results = analyzer.find_extremum(cubic, (-2, 2), 'all')
    analysis = analyzer.analyze_function_behavior(cubic, (-2, 2))
    print(analyzer.generate_report(analysis))
    
    # 测试函数 3: 三角函数 f(x) = sin(x) + 0.5*cos(2x)
    def trigonometric(x):
        return math.sin(x) + 0.5 * math.cos(2*x)
    
    print("\n3. 三角函数 f(x) = sin(x) + 0.5*cos(2x)")
    results = analyzer.find_extremum(trigonometric, (0, 2*math.pi), 'all')
    analysis = analyzer.analyze_function_behavior(trigonometric, (0, 2*math.pi))
    print(analyzer.generate_report(analysis))
    
    # 测试函数 4: 复杂函数 f(x) = x^4 - 4x^2 + x
    def complex_func(x):
        return x**4 - 4*x**2 + x
    
    print("\n4. 复杂函数 f(x) = x⁴ - 4x² + x")
    results = analyzer.find_extremum(complex_func, (-2, 2), 'all')
    analysis = analyzer.analyze_function_behavior(complex_func, (-2, 2))
    print(analyzer.generate_report(analysis))

# 运行测试
test_extremum_finder()

# 可视化极值点
import matplotlib.pyplot as plt

def visualize_extremum(func, interval, extremum_points, title="函数极值点可视化"):
    """可视化函数和极值点"""
    start, end = interval # 获取区间
    x_values = [start + i * (end - start) / 200 for i in range(201)] # 生成x值
    y_values = [func(x) for x in x_values] # 计算对应的y值
    
    plt.figure(figsize=(12, 6)) # 创建图形
    
    # 绘制函数曲线
    plt.plot(x_values, y_values, 'b-', linewidth=2, label='函数曲线') # 绘制函数曲线
    
    # 标记极值点
    for point in extremum_points: # 遍历极值点
        x, y = point['position'], point['value'] # 获取极值点位置和值
        if point['type'] == '极大值': # 极大值
            plt.plot(x, y, 'ro', markersize=8, label='极大值')
            plt.annotate(f'极大值\n({x:.3f}, {y:.3f})', # 标注极大值
                        xy=(x, y), xytext=(10, 20),
                        textcoords='offset points',
                        arrowprops=dict(arrowstyle='->', color='red'))
        else:  # 极小值
            plt.plot(x, y, 'go', markersize=8, label='极小值')
            plt.annotate(f'极小值\n({x:.3f}, {y:.3f})', 
                        xy=(x, y), xytext=(10, -30),
                        textcoords='offset points',
                        arrowprops=dict(arrowstyle='->', color='green'))
    
    plt.title(title, fontsize=14) # 设置标题
    plt.xlabel('x', fontsize=12) # 设置x轴标签
    plt.ylabel('f(x)', fontsize=12) # 设置y轴标签
    plt.grid(True, alpha=0.3) # 添加网格
    plt.legend() # 显示图例
    plt.tight_layout() # 自动调整布局
    plt.show() # 显示图形

# 可视化示例
def demo_visualization():
    """演示极值点可视化"""
    def sample_func(x):
        return x**3 - 3*x + math.sin(5*x) # 复杂函数
    
    analyzer = FunctionExtremumAnalyzer() # 创建分析器
    extremum_points = analyzer.find_extremum(sample_func, (-2, 2), 'all') # 查找极值点
    
    print("找到的极值点:")
    for point in extremum_points:
        print(f"x = {point['position']:.4f}, f(x) = {point['value']:.4f}, {point['type']}")
    
    visualize_extremum(sample_func, (-2, 2), extremum_points, 
                      "f(x) = x³ - 3x + sin(5x) 的极值点")

# 运行可视化演示
demo_visualization()