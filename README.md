# interface-framework
* 不想搞路径。。。
---
```python

#os.path.abspath(__file__)取本文件绝对路径
#os.path.dirname()去掉路径里最末一个文件or文件夹
import os
import sys
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取当前项目路径并添加到path中
sys.path.append(base_path)


# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
# from common.utils import *
from commons.getResponse import HttpRequestResponse
#添加本文件所在文件夹的隔壁文件夹的文件


```