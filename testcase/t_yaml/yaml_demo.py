"""
#1、创建yaml格式文件
#2、读取这个文件
#3、输出这个文件
"""
import yaml
#读取单个文档
# with open("./data.yml","r",encoding="utf-8")as f:
#     r =yaml.safe_load(f)
# print(r)

#读取多个文档
# with open("./data.yml","r",encoding="utf-8")as f:
# #     r = yaml.safe_load_all(f)
# #     for i in r:
# #         print(i)

from utils.Yamlutil import YamlReader

#res = YamlReader("./data.yml").data()
res = YamlReader("./data.yml").data_all()
print(res)
