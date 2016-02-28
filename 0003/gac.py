
# coding: utf-8

# ## 0001 使用 Python 如何生成 200 个激活码（或者优惠券）
# 
# 激活码是一个12位或16位的由26个大写英文字母以及10个数字组成
# 
# 使用每位数字随机生成的形式，采用12位的激活码 0-25对应A-Z，26-35对应0-9

# In[6]:

import numpy as np
import string
map_char = string.uppercase+string.digits
def gen_active_code():
    total_l = {}    
    while len(total_l)<200:
        mapped_l = []
        l = np.random.randint(0,36,12)
        for j in l:
            mapped_l.append(map_char[j])
        total_l.setdefault(''.join(mapped_l))
    return total_l.keys() 

