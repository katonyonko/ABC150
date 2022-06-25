import io
import sys

_INPUT = """\
6
2 900
1 501
4 2000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  K,X=map(int,input().split())
  if K*500>=X:
    print("Yes")
  else:
    print("No")