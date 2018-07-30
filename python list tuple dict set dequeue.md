# python list/tuple/dict/set/deque的简单比较、优化和时间复杂度（表格）

2018年01月19日 17:06:23

 				阅读数：711 											

**参考：（以下很多地方有参考的链接我统一放在这里）**

1. 基于python2.7，不是完全完整，基于目前所学分析，后面有其他会补充，主要也是为了可观性；
2. 关于时间复杂度，参考： 
        · 英文：<https://wiki.python.org/moin/TimeComplexity> 
        · 中文：<http://www.orangecube.net/python-time-complexity> 
3. 前四种算是基本数据结构，最后一种是from collections这个内置库，是双向队列。它相当于队列和列表的结合，并且支持两端增删。它其实更常用于和多线程，redis使用，之所以放在这里，是因为它和list的相似性；
4. 关于tuple的优点，知乎有很好的答案：<https://www.zhihu.com/question/60574107>
5. 关于dict的删除： 
        1). <http://www.runoob.com/python/python-dictionary.html> 
        2). <http://www.iplaypy.com/jinjie/jj116.html> 
6. 关于dict的插入：<https://www.zhihu.com/question/62050494>
7. 关于set的删除： <http://blog.csdn.net/jcjc918/article/details/9359503>
8. 性能比较：<https://www.cnblogs.com/cfang90/p/6220956.html>
9. 优化建议：<http://www.jb51.net/article/56699.htm>
10. 算法时间复杂度：<https://www.ibm.com/developerworks/cn/linux/l-cn-python-optim/>

------

#### 一、关于增删改查

| 序列         | list | tuple | dict | set  | deque |
| ------------ | ---- | ----- | ---- | ---- | ----- |
| 能否增加元素 | √    | ×     | √    | √    | √     |
| 是否有序     | √    | √     | ×    | ×    | √     |
| 能否删除     | √    | ×     | √    | √    | √     |
| 可否哈希     | ×    | √     | √    | √    | ×     |

------

| 序列             | list                                  | tuple                                                    | dict                                                    | set                        | deque                                                        |
| ---------------- | ------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------- | -------------------------- | ------------------------------------------------------------ |
| 增加方法         | append、extend、insert                | ×                                                        | update                                                  | add、update                | append/appendleft、extend/extendleft                         |
| 删除方法         | pop、remove                           | × (tuple只有count和index两个方法)                        | pop、clear(这两个是方法)/del（函数） del dict/dict[key] | pop、remove                | 和list类似，但多一个popleft（它和其他的区别在于双端，append/extend/pop都多一个left） |
| 优点（只是部分） | 功能相对比较齐全                      | 可以生成器，占内存小，安全，遍历速度比list快，可一赋多值 | 查找和插入速度快                                        | 不用判断重复的元素         | 插入速度快                                                   |
| 缺点             | 相对tuple占内存，查找和insert时间较慢 | 不能添加和更改元素                                       | 占内存大                                                | 不能存储可变对象，例如list | remove和获取索引的时候比较慢                                 |

------

#### 二、关于时间复杂度

**这里简单说一下相对序列关于时间复杂度的意思：**

· 

> ·  *O(1)：*常数级别，意思即时间保持在一个固定的范围内，不会随序列的长度和大小而增长。* 
>    ·  *O(n)：*线性级别，时间与序列的大小成正比，即序列元素越多，越长，所花时间越多* 
>    ·  *O(k)：*官网上说，“n”是容器中当前的元素的数量。’k’是参数的值或参数中元素的数量。但是目前我还不太清楚它是什么意思，我看到第一个例子用在了pop上，所以猜测是随它变化，具体求哪位大神能给解释一下* 
>        · 还有一些类似O(n log n)和O(n^2) ，你画个图就知道了，具体日后有时间补

**注意：**

1. 因为tuple不能增删改，所以这里不做比较。

2. 因为deque只是和list样子相似，但作用和queue相似，看名字就知道了，所以它只能从两端增删，不能从中间增删，它也就没有insert或者update这样的方法。

3. pop各种方法有些不一样，另外我们知道pop的时候它会返回被删掉的数据。因此，pop我们会分为pop last、pop(index[list]/key[dict])，但实际上他们的命令都是pop：

       deque：popleft是其独有，但它的pop不能从指定的位置删
       list：list/dict都可以从指定位置删，list简单直接给pop(index)即可
       set：set其实有pop，但它既不能指定，且没有所谓最后一个，也是随机，其他得用remove或者discard（区别在于如果元素不存在，前者会报错而后者不会）
       dict： 根据官网来看，dict的复杂度平均是O(1)，最坏的结果才是O(n)。只是占内存一些，dict的pop比较特殊：
           - popitem()：这个尤其特别，它随机返回并删除字典中的一对键和值。为什么随机呢，因为dict是无序的，没有所谓最后一个
           - pop(key[,default])：删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

4. 由于无序序列的存在，设置了中括号标注下哪个方法是对应哪个序列的，这里的中括号不代表索引，这里索引直接用index代替 

平均情况下：

| 序列                         | list    | deque  | dict    | set    |
| ---------------------------- | ------- | ------ | ------- | ------ |
| insert                       | √ O(n)  | ×      | ×       | ×      |
| append                       | √ O(1)  | √ O(1) | ×       | ×      |
| appendleft                   | ×       | √ O(1) | ×       | ×      |
| extend                       | √ O(k)  | √ O(1) | ×       | ×      |
| extendleft                   | ×       | √ O(1) | ×       | ×      |
| add                          | ×       | ×      | ×       | √ O(1) |
| update                       | ×       | ×      | √  O(1) | √O(1)  |
| remove                       | √       | √O(n)  | ×       | √      |
| clear                        | ×       | √      | √       | √      |
| del                          | √  O(n) | √      | √ O(1)  | √      |
| popleft                      | ×       | √ O(1) | ×       | ×      |
| pop last（pop()[list]）      | √ O(1)  | √ O(1) | ×       | ×      |
| pop（index[list]/key[dict]） | √ O(k)  | √ O(1) | √ O(1)  | ×      |
| popitem()                    | ×       | ×      | √ O(1)  | ×      |
| Iteration(迭代)              | √ O(n)  | √      | √  O(n) | √ O(n) |
| x in s （查找）              | √ O(n)  | √ O(n) | √  O(1) | √ O(1) |

------

**特点：**

1. tuple：
   1. tuple可哈希，所以它可转换成dict和set，它做dict——{():value}
   2. tuple的优点： 
       2.1. 函数返回多个值， 
       2.2. 字符串里有多个元素，如果刚好这些元素处于一个列表或tuple内，可以直接用，但是列表需转换， 
       2.3. 可以快速调换赋值，如a,b = b,a
   3. 定义只有一个元素的tuple时候，必须写成这种格式，即加个逗号， 如a = (1,)，否则默认为进行()的运算。
2. dict：
   1. dict的最好和平均时间是O(1)，最差是O(n)，set大多和dict差不多
3. set：
   1. set存储的元素和dict的key类似，必须是不变对象，所以set不支持list/dict，它可以通过update的方式将list的元素一个个添加到set里，但不支持整个list，set 和dict转换只会用到它的key而不是value）
   2. 你在最初set([1,2,3])时，它会转换为{1,2,3}。
   3. 不过它转换成list很方便，只需要list(set())即可，而不用遍历set中的元素
   4. set(i for i in range(n))比set([i for i in range(n)])要快一些，因为前者用到了生成器，来源于，但是如果要遍历，后者可能更快（参考链接9）
4. 查找（即x in s）：dict，set是常数查找时间（O(1)），list、tuple是线性查找时间（O(n)）

**优化：**

1. list因为占用的内存会随着元素的增大而增大，所以最好不要用 List 来保存中间结果，而是通过 iterable 对象来迭代。（参考链接）
2. 由表3可知，在判断某个元素是否在某个序列中的时候，dict是O(1)，list需要遍历，所以是O(n)，这时候尽量不要用list，能够用字典进行存储，尽量不要用list。如果觉得list和dict转换麻烦，可以用set，set和list的转换比较方便，总之可以避开直接用list。存储的时候似情况而定用list还是set，这样可以省去转换。