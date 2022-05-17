'''
https://www.codechef.com/problems/PRACLIST
'''
x,y = map(int, input().split())
if 1 <= x <= 1000 and 1 <= y <= 1000 and x >= y:
    print(x-y)