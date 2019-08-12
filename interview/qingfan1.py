class rectangle:
    def __init__(self,p1x,p1y,p2x,p2y):
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
class Solution:
    def judge_overlap(self,rec1,rec2):
        def not_overlap(): #判断是否不重叠
            if rec1.p2x <= rec2.p1x:
                return True
            if rec1.p1x >= rec2.p2x:
                return True
            if rec1.p2y >= rec2.p1y:
                return True
            if rec1.p1y <= rec2.p2y:
                return True
            return False
        if not rec1 or not rec2:
            raise KeyError("rectangle must not be None")
        if not_overlap():
            return False
        return True