# Python 数据科学快速手册

## Numpy 速成指南

### 导入库
```python
import numpy as np
```

### 数组实例化
- **创建数组**：`myarr = np.array([1,2,3])`
- **查看维度**：`numpy.array.shape` - 返回数据的维度
- **访问数据**：直接用下标访问

**示例**：
```python
myarr = np.array([1,2,3])
print(myarr.shape)  # 输出: (3,)
```

### 向量运算
```python
# 创建二维数组
myarr = np.array([[1,2,3],[4,5,6]])    # 2x3矩阵
myarr2 = np.array([[7,8,9],[10,11,12]])

# 数组加法
print(myarr + myarr2)
# 结果: [[ 8 10 12]
#        [14 16 18]]

# 数组乘法（逐元素相乘）
print(myarr * myarr2)
# 结果: [[ 7 16 27]
#        [40 55 72]]
```

---

## Matplotlib 可视化指南

### 导入库
```python
import matplotlib.pyplot as plt
```

### 线型图
```python
# 准备数据
data = np.array([[1,2,3],[2,3,4]])

# 绘制线型图
plt.plot(data)
plt.xlabel("X axis")  # X轴标签
plt.ylabel("Y axis")  # Y轴标签
plt.show()           # 显示图形
```

### 散点图
```python
# 准备数据
data1 = np.array([1,2,3])
data2 = np.array([4,5,6])

# 绘制散点图
plt.scatter(data1, data2)
# 创建三个坐标点：(1,4), (2,5), (3,6)
plt.show()
```

---

## 快速参考

| 功能 | Numpy | Matplotlib |
|------|-------|------------|
| 导入 | `import numpy as np` | `import matplotlib.pyplot as plt` |
| 创建数据 | `np.array([1,2,3])` | 使用numpy数组作为数据源 |
| 基本操作 | 数组运算：`+`, `*`, `shape` | 绘图：`plot()`, `scatter()` |
| 显示结果 | `print()` | `plt.show()` |

这份手册涵盖了Numpy数组操作和Matplotlib基础绘图的核心功能，适合快速查阅和参考。
        