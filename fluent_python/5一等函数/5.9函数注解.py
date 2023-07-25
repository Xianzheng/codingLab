'''
Python 对注解所做的唯一的事情是，把它们存储在函数的
__annotations__ 属性里。仅此而已，Python 不做检查、不做强制、
不做验证，什么操作都不做。换句话说，注解对 Python 解释器没有任何
意义。注解只是元数据，
'''
def clip(text:str, max_len:'int > 0'=80) -> str: 
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
    if space_after >= 0:
        end = space_after
    if end is None: # 没找到空格
        end = len(text)
    return text[:end].rstrip()

print(clip.__annotations__)

str1 = 'hello world'
#find找第一次出现
#r.find 找第二次出现
print(str1.find('l',0, 2))

str1 = 'a b c d'
print(str1.rsplit())