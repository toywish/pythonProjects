# 假设我要新建10个txt文件,这里我用一个for循环
# for i in range(10):
#     # 这里的./指代的是当前文件夹, %i表示文件的名称,a表示没有该文件就新建.
#     f = open('./%s' % i + '.txt', "a")
#     f.write("")  # 写入文件，空
#     f.close()  # 执行完结束

# 批量创建文件夹
import os  # 导入模块

path = './test/'  # 设置创建后文件夹存放的位置
number = 10  # 文件夹数量
folder_name_prefix = "css"  # 指定文件夹名前缀
for i in range(1, number):
    # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
    folder_name = folder_name_prefix + str(i).zfill(2)  # 指定文件夹名,zfill(n)在字符串前补0，使其占n个字符的位置
    isExists = os.path.exists(path + folder_name)
    if not isExists:  # 判断如果文件夹不存在,则创建
        os.makedirs(path + folder_name)
        print(folder_name, "目录创建成功")
    else:
        print(folder_name, "目录已经存在")
        continue  # 如果文件夹不存在,则继续上述操作,直到循环结束
