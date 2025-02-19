def LPS(string):

    def expand_center(string, right, left):
        while( 0<=left and right<len(string) and string[right] == string[left]):
            left-=1
            right+=1
        
        return left+1, right-1
    
    start=0
    end=0
    for i in range(len(string)):

        l1, r1 = expand_center(string, i, i)
        l2, r2 = expand_center(string,i, i+1)

        if (r1-l1) > (end-start):
            start, end = l1, r1

        if (r2-l2) > (end-start):
            start, end = l2, r2

    return string[start:end+1]

string = "forgeeksskeegfor"

print(LPS(string))