#!/usr/bin/python3

cal_list = []
with open('input', 'r')  as f:
  for i in f.readlines():
    cal_list.append(i.replace('\n', ''))
cal_list.append('')

elf_dict = {}
total_cal = []
s = 0
elf_count = 1
for i in range(len(cal_list)):
  if cal_list[i] == '':
    elf_dict[elf_count] = s
    total_cal.append(s)
    elf_count += 1
    s = 0
    continue
  else:
    s += int(cal_list[i])

total_cal = sorted(total_cal, reverse = True)
print(max(elf_dict.values()), sum(total_cal[0 : 3]))