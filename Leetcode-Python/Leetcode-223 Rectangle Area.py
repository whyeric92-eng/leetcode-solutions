class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left_wid=max(ax1,bx1)
        right_wid=min(ax2,bx2)
        top_height=min(ay2,by2)
        bottom_height=max(ay1,by1)
        def area(x1,x2,y1,y2):
            return (x2-x1)*(y2-y1) if (x2-x1)*(y2-y1)>0 else 0
        if bx1>=ax2 or by1>=ay2 or ax1>=bx2 or ay1>=by2:
            covered=0
        else:
            covered=area(left_wid,right_wid,bottom_height,top_height)
        return area(ax1,ax2,ay1,ay2)+area(bx1,bx2,by1,by2)-covered

#可改进
class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        overlap_w = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_h = max(0, min(ay2, by2) - max(ay1, by1))
        overlap = overlap_w * overlap_h
        
        return area_a + area_b - overlap