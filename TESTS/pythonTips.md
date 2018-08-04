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



## String join() method

### Example

The following example shows the usage of join() method.

```
#!/usr/bin/python3

s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))
```

### Result

When we run above program, it produces the following result −

```
a-b-c
```



## String format() method

### Example

另一种格式化字符串的方法是使用字符串的`format()`方法，它会用传入的参数依次替换字符串内的占位符`{0}`、`{1}`……，不过这种方式写起来比%要麻烦得多：

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

`{1:.1f}%` 这种写法表示精度



```python
cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

```

`{: ^5}`表示中间对齐，宽度为5



## set

set查找复杂度为O(1)。