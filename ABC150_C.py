import io
import sys

_INPUT = """\
6
3
1 3 2
3 1 2
8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1
3
1 2 3
1 2 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  N=int(input())
  P=list(map(int,input().split()))
  Q=list(map(int,input().split()))
  p=0
  q=0

  for i in range(N-1):
    p+=sum(list(1 if P[i]>P[k] else 0 for k in range(i,N)))*math.factorial(N-i-1)
    q+=sum(list(1 if Q[i]>Q[k] else 0 for k in range(i,N)))*math.factorial(N-i-1)
  print(abs(p-q))