# 一个简单的感知器逻辑实现
def perceptron(inputs, weights, bias):
    """
    一个简单的感知器函数。
    - inputs: 输入信号列表，例如 [1, 0]
    - weights: 对应每个输入的权重列表，例如 [0.7, 0.5]
    - bias: 偏置项，一个浮点数
    """
    # 1. 计算加权和
    weighted_sum = 0
    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]
    
    # 2. 加上偏置
    total = weighted_sum + bias
    
    # 3. 通过激活函数（阶跃函数）
    # 如果总和大于0，就“激活”，输出1；否则输出0
    if total > 0:
        return 1
    else:
        return 0

# 模拟“是否带伞”的决策
# 输入: [天气预报说下雨(1), 天色阴沉(1)]
inputs = [1, 1]
# 权重: [天气预报的重要性(0.6), 天色阴沉的重要性(0.3)]
weights = [0.6, 0.3]
# 偏置: 决定了激活的难易度，负值越大越难激活
bias = -0.5

# 获取决策结果
decision = perceptron(inputs, weights, bias)
print(f"决策结果: {'带伞' if decision == 1 else '不带伞'}") # 输出: 决策结果: 带伞
