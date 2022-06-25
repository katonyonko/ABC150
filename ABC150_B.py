import io
import sys

_INPUT = """\
6
10
ZABCDBABCQ
19
THREEONEFOURONEFIVE
33
ABCCABCBABCCABACBCBBABCBCBCBCABCB
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  c=0

  for i in range(N-2):
    if S[i:i+3]=="ABC":
      c+=1

  print(c)