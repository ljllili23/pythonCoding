# Python Tips

## zip()的用法

### 第三个用法：

#### `zip(*zippedList)`

> 作用：Unzipping the Value Using zip()

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

