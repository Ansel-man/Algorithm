
# 倒序输出
# 递归输出
# 栈 先见后出的性质


'''递归方法'''

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []
