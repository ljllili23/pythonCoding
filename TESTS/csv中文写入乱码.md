## [python3-csv写入中文乱码](https://www.cnblogs.com/adampei-bobo/p/8615978.html)

2018-03-21 11:25 by 菜鸟Alex, 996 阅读, 0 评论, [收藏](https://www.cnblogs.com/adampei-bobo/p/8615978.html#),  [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=8615978)

- 代码如下

```
import csv
data = [['American','美国人'],
        ['Chinese','中国人']]

with open('results.csv','w',newline='',) as f:
    w = csv.writer(f)
    w.writerows(data)
```

- 结果如下
   ![img](https://images2018.cnblogs.com/blog/831196/201803/831196-20180321112255972-776701631.png)
- 正确打开方式应该加上`encoding='utf-8-sig'`
- 代码

```
import csv

data = [['American','美国人'],
        ['Chinese','中国人']]
with open('results.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerows(data)
```

- 结果
   ![img](https://images2018.cnblogs.com/blog/831196/201803/831196-20180321112425500-456104519.png)