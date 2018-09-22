# Numpy

## Slice

### numpy 数组/矩阵如何切片？

一维的numpy和python内置的数组切片方法一样。都 是list[start:end]。

多维的numpy array呢？ 先看numpy array如何indexing.

## Indexing

`x = np.arange(10)`

`x.shape = (2,5)`

`x[1, 3]` 与 `2-d list`的`x[1][3]`等价 

---

知道了numpy array的索引方式，

那么二维的numpy数组如何切片？

```
x[0:,2:] #在逗号两边分别是行和列的索引，分别切片，方法与一维一致。
x[:,:4] #这里前面的':'一定不能少
```

## 关于numpy维度的一些问题

```
data1 = np.array([[[1,2],[1,2],[1,2]],[[3,4],[3,4],[3,4]],[[5,6],[5,6],[5,6]]])
data1.shape		# (n,3,2)

data2 = np.array([[[1,2,3],[1,2,3]],[[4,5,6],[1,2,3]],[[7,8,9],[1,2,3]]])
data2.shape		# (3,2,3)

data3 = np.array([[[1,2,3],'A'],[[4,5,6],'B'],[[7,8,9],'C']])
data3.shape		# (3,2) 
```

这三个对比一下。