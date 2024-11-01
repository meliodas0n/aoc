#!/usr/bin/python3


A_score1 = {'X' : 4, 'Y' : 8, 'Z' : 3}
B_score1 = {'X' : 1, 'Y' : 5, 'Z' : 9}
C_score1 = {'X' : 7, 'Y' : 2, 'Z' : 6}

A_score2 = {'X' : 3, 'Y' : 4, 'Z' : 8}
B_score2 = {'X' : 1, 'Y' : 5, 'Z' : 9}
C_score2 = {'X' : 2, 'Y' : 6, 'Z' : 7}

moves = []
with open('input', 'r') as f:
  for i in f.readlines():
    j = i.replace('\n', '')
    moves.append(j)

score1 = 0
score2 = 0
for i in moves:
  o, u = i.split(' ')
  if o == 'A':
    score1 += A_score1[u]
    score2 += A_score2[u]
  elif o == 'B':
    score1 += B_score1[u]
    score2 += B_score2[u]
  else:
    score1 += C_score1[u]
    score2 += C_score2[u]

print(score1, score2)