# 简单使用一下
from xpinyin import Pinyin

p = Pinyin()
# result = p.get_pinyin('小琳爱分享')  # 此处结果：xiao-lin-ai-fen-xiang
# result = p.get_pinyin('小琳爱分享', '')  # 此处结果：xiaolinaifenxiang
result = p.get_pinyin('小琳爱分享', ' ')  # 此处结果：xiao lin ai fen xiang
print(result)  # 结果：xiao-lin-ai-fen-xiang
