# Python Tips



## zip()的用法

### 第三个用法：

#### `zip(*zippedList)`

==作用：Unzipping the Value Using zip()==

#### eg:

```python
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)
```

#### result:

```python
[('x', 3), ('y', 4), ('z', 5)]
c = ('x', 'y', 'z')
v = (3, 4, 5)
```



## List Comprehensions

==List Comprehensions 提供了一种简化的方法创建lists==

```python
squares = list(map(lambda x: x**2, range(10))) #lambda 隐函数的方法
```

or, equivalently:

```python
squares = [x**2 for x in range(10)]
```



## List/tuple/string 切片

```python
L = list(range(100))
L[:3] 		#[0,1,2]
L[1:3] 		#[1,2]
L[-3:]		#[97,98,99]

#第2个元素取一个
list[::5]		#[0, 5, 10, 15,..., 90, 95]
list[::-1]		# 倒着取 [99,98,...,0]
```



## defaultdict

在Python中如果访问字典中不存在的键，会引发KeyError异常 

```python
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts[kw] += 1
```

该例子统计strings中某个单词出现的次数，并在counts字典中作记录。单词每出现一次，在counts相对应的键所存的值数字加1。但是事实上，运行这段代码会抛出KeyError异常，出现的时机是每个单词第一次统计的时候，因为Python的dict中不存在默认值的说法，可以在Python命令行中验证：

```python
>>> counts = dict()
>>> counts
{}
>>> counts['puppy'] += 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'puppy'
```

