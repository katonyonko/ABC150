import io
import sys

_INPUT = """\
6
2 50
6 10
3 100
14 22 40
5 1000000000
6 6 2 6 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  import numpy as np
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  c=1
  test=A[0]
  l=0

  while test%2 == 0:
    test=test//2
    c*=2
    
  for i in np.arange(N-1):
    if A[i+1]%c!=0:
      print(0)
      l=1
      break
    elif A[i+1]%(c*2)==0:
      print(0)
      l=1
      break
    else:
      k=A[i+1]//c
      test=test*k//math.gcd(test,k)
  if l==0:
    k=test*c//2
    print(M//k//2+M//k%2)