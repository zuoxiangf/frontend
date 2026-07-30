# 打印99 乘法表

for i in range(1,10): # 行数
    for j in range(1,10): # 列数
        print(f"{j} * {i} ={i * j}",end="  ")
        if j == i :
            break
    print()