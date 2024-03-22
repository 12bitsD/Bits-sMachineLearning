# Numpy 速成手册

```python
import numpy as np	
```

>   numpy实例化数组（矩阵）
>
>   Numpy进行向量运算



数组实例化

`直接 myarr = np.arrray([1,2,3])`

`numpy.array.shape #会返回数据的维度`

exmple：

```python
myarr = np.array([1,2,3])
print(myarr.shape)

#result: (3,)
```

访问数据可以直接用下标访问。



向量运算

```python
myarr =np.array([[1,2,3],[4,5,6]]) #2x3 
myarr2 = np.array([[7,8,9],[10,11,12]])

print(myarr+myarr2)
print(myarr*myarr2)
#RESULT
[[ 8 10 12]
 [14 16 18]]

[[ 7 16 27]
 [40 55 72]]


```

