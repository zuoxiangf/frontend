''' 


age = 30             # int
price = 19.99        # float
z = 3 + 4j           # complex

生产开发场景：
int：计数器、分页参数、状态码、数据库 ID（注意：处理金融金额时绝对不要用 float，应使用 Decimal 类型）。
float：经纬度坐标、非精确计算的物理量。
complex：信号处理、量子计算等科研领域


2、字符串 Str
Python 的字符串是不可变序列，原生支持 Unicode（类似 Java 的 String，但更强大）。支持极其丰富的切片（Slicing）和格式化（f-string）操作。

name = "Alice"
greeting = f"Hello, {name}!"  # f-string 格式化（类似 Java 的 String.format）
sub = name[0:2]               # 切片获取 "Al"

生产开发场景：
接口返回的 JSON 字符串解析与构建。
日志格式化、SQL 语句拼接（注意防注入，推荐用 ORM 的参数化查询）。
数据清洗（正则表达式 re 模块配合使用）。


3、列表 list
有序、可变的序列。可以存储任意类型的数据。底层是动态数组。

users = ["Alice", "Bob", "Charlie"]
users.append("David")      # 添加元素
users[0] = "Alicia"        # 修改元素
evens = [i for i in range(10) if i % 2 == 0] # 列表推导式

生产开发场景：
存储数据库查询返回的多条记录（如 List<User>）。
作为 API 接口的入参或出参（JSON 数组）。
临时数据缓冲池、消息队列的内存实现。


4、字典 dict
键值对（Key-Value）集合。Python 3.7+ 保证插入顺序。底层是哈希表。

user = {"name": "Alice", "age": 25}
user["email"] = "a@b.com"  # 新增/修改
name = user.get("name", "Unknown") # 安全获取，不存在返回默认值

生产开发场景：
JSON 数据的内存表示：前后端交互的核心数据结构。
缓存结构：结合 Redis 或内存缓存，存储配置信息、用户 Session。
数据聚合：将列表按某个字段分组（类似 Java 的 Collectors.groupingBy）。

5、元组 tuple
有序、不可变的序列。一旦创建，不能增删改。因为不可变，所以可以作为字典的 Key 或放入 Set 中。

point = (10, 20)
x, y = point          # 解包
# point[0] = 100      # 报错！不可修改

生产开发场景：
函数多返回值：Python 函数返回多个值时，本质是返回一个元组。
数据库查询结果：ORM 或原生 SQL 查询返回的一行数据通常是元组。
常量集合：定义不需要修改的配置项，如 HTTP_STATUS_CODES = (200, 404, 500)。
字典的复合键：如 (year, month) 作为字典的 Key。

6、集合 set
无序、不重复的元素集合。底层是哈希表。

tags = {"python", "java", "python"}  # 自动去重，结果为 {"python", "java"}
tags.add("go")
tags.discard("java")  # 安全删除，不存在不报错

生产开发场景：
数据去重：从列表中提取唯一值 unique_list = list(set(my_list))。
权限/标签管理：存储用户的角色列表、文章的标签集合。
集合运算：求交集（&）、并集（|）、差集（-），例如“找出两个部门共同拥有的员工”。


| 需求场景 | 选择类型 | 为什么？ |
| :--- | :--- | :--- |
| 存储多条同构记录 | `list` | 类似 `ArrayList`，支持索引和遍历 |
| 存储配置/JSON对象 | `dict` | 键值对查找 O(1)，类似 `HashMap` |
| 函数返回多个值 | `tuple` | 轻量级，不可变，安全 |
| 数据去重/权限集合 | `set` | 自动去重，支持集合运算 |
| 存储金额/精确计算 | `Decimal` | 千万别用 float，会有精度丢失 |
| 需要作为字典的 Key | `tuple` / `str` / `int` | list 和 set 不能作为 Key（因为可变） |





'''
