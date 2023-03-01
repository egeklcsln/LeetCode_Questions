class Solution(object):
    def checkStraightLine(self, coordinates):
        x1 = coordinates[0][0] 
        x2 = coordinates[1][0]
        y1 = coordinates[0][1] 
        y2 = coordinates[1][1]

        #(y2-y1)/(x2-x1)==(y3-y2)/(x3-x2)   -->   (y2-y1)*(x3-x2)==(y3-y2)(x2-x1)

        ydiff=y2-y1
        xdiff=x2-x1

        for i in range(2,len(coordinates)):
            diff_x=coordinates[i][0] - coordinates[i-1][0]
            diff_y=coordinates[i][1] - coordinates[i-1][1]
            if(ydiff * diff_x)  != (xdiff * diff_y):
                return False
        return True

