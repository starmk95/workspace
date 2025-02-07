# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# for line in lines:
#     print(line)

# f.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# for line in lines:
#     for x in range(len(line)):
#         print(line[x])

# f.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# for line in lines:
#     if '2019-10-20' in line:
#         print(line)

# f.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)
# Header = next(lines)

# print(lines)

# f.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# print('%s       %s  %s  %s' % ('일자', '최저기온', '최고기온', '일교차'))
# next(lines)  # 헤더를 건너뜀.

# for line in lines:
#     diff = float(line[4]) - float(line[3])
#     print('%s    %.1f      %.1f     %.1f' % (line[1], float(line[3]), float(line[4]), diff))

# f.close()

# import csv

# file1 = open('month_temp.csv', 'r', encoding='utf-8')
# file2 = open('month_temp3.csv', 'w', encoding='utf-8', newline='')

# lines = csv.reader(file1)
# wr = csv.writer(file2)

# wr.writerow(['일자', '최저기온', '최고기온', '일교차']) # 헤더 추가해주기
# next(lines)

# for line in lines:
#     diff = float(line[4]) - float(line[3])
#     diff = format(diff, '.1f')

#     wr.writerow([line[1], float(line[3]), float(line[4]), diff])

# print('파일쓰기완료!')

# file1.close()
# file2.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# for line in lines:
#     for x in line:
#         print('%s' % x, end='/')    # 각 데이터 끝에 슬래쉬 추가
#     print()

# f.close()

# import csv

# f = open('month_temp.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# next(lines)  # 헤더를 건너뛴다.

# sum = 0
# for line in lines:
#     if (int(line[1][8:]) <= 10):
#         sum += float(line[2])

# avg = sum / 3
# print('10일간 평균 기온 : %.1f' % avg)

# f.close()

# import csv

# f = open('pharm_2019.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)
# header = next(lines)

# for line in lines:
#     if line[1] == '경주시' and line[0] == '신대원약국':
#         print(line[0], line[1], line[2], sep='/')

# f.close()

import csv

f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

for line in lines:
    if ('수지' in line[2]) and ('로얄스포츠' in line[2]):
        print(line[2], line[0], line[3], sep='/')

f.close()
