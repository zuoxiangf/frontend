
'''
采用面向对象编程思想完成如下需求
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
退出购物车

商品	Goods
购物车系统	ShoppingCart
'''

class Goods:
    def __init__(self,g_name,g_price = 0.0,g_num = 1) :
        self.price = g_price
        self.num = g_num
        self.name = g_name
 
    def __str__(self) :
        return f"商品名称：{self.name},价格：{self.price}, 数量：{self.num}"

    
class ShoppingCart:
    def __init__(self) :
        self.car_list = []
    # 添加   
    def add_goods(self):
        name = input("请输入商品名称")
        for goods in self.car_list:
            if goods.name == name :
                print(f"该商品已经存在")
                return
        price = float(input("请输入商品价格"))
        if price < 1 or price > 100:
            print(f"该商品价格在 1-100 之间")
            return

        num= int(input("请输入商品数量"))
        if num < 1 or num > 100:
            print(f"该商品数量在 1-100 之间")
            return
        goods = Goods(name,price,num)
        self.car_list.append(goods)

    def query_goods(self):
        name = input("请输入商品名称")
        for goods in self.car_list:
            if goods.name == name :
                print(goods)
            else:
                print(f"该商品BU存在")

    def query_all_goods(self):
        for goods in self.car_list:
            print(goods)

    def del_goods(self):
        name = input("请输入商品名称")
        for goods in self.car_list:
            if goods.name == name :
                self.car_list.remove(goods)
            else:
                 print(f"该商品BU存在")

    def update_goods(self):
        name = input("请输入商品名称")
        for goods in self.car_list:
            if goods.name == name :
                
                price = float (input("请输入商品价格"))
                if price < 1 or price > 100:
                    print(f"该商品价格在 1-100 之间")
                    return

                num= int(input("请输入商品数量"))
                if num < 1 or num > 100:
                    print(f"该商品数量在 1-100 之间")
                    return
                goods.price =price
                goods.num = num
            else:
                 print(f"该商品BU存在")  

    def run(self):
        print(f"欢迎使用购物车")  
        while True:
            print()
            print(f"1: 添加  2：修改  3：删除 4：查询单个 5：查所有  6：退出")
            print()
            choose = int(input("请输入："))
            match choose:
                case 1 :
                    self.add_goods()
                case 2 :
                    self.update_goods()    
                case 3 :
                    self.del_goods()    
                case 4 :
                    self.query_goods()    
                case 5 :
                    self.query_all_goods()    
                case 6 :
                    break 
                case _ :
                    print(f"输入操作错误：{choose}")               

#测试


if __name__ == "__main__":
    shopping = ShoppingCart()
    shopping.run()