import io
import sys

_INPUT = """\
6
1
1000000000
2
5 8
5
52 67 72 25 79
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  N=int(input())
  C=list(map(int,input().split()))
  C.sort()
  ans=0
  for i in range(N):
    ans=(ans+pow(2,2*N-2,mod)*(N-i+1)*C[i])%mod
  print(ans)