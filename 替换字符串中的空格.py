

# python 和 java 的语言中,字符串为不可变的类型,必须通过新建一个字符串实现

# c++ 语言中 string 类型可变,

class Solution:
    def replaceSpace(self,s:str) -> str :
        res = []
        for c in s:
            if c == " ":
                c = "%20"
            res.append(c)