# interface-framework
* 再也不搞路径！
---
```python
import os
import sys
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取当前项目路径并添加到path中
sys.path.append(base_path)

```