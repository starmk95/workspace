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

# import csv

# f = open('pharm_2019.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# header = next(lines)

# for line in lines:
#     if ('수지' in line[2]) and ('로얄스포츠' in line[2]):
#         print(line[2], line[0], line[3], sep='/')

# f.close()

# import csv

# # CSV 파일 열기
# f = open('pharm_2019.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)
# header = next(lines)  # 헤더 스킵

# # 분석할 도시 설정
# city = '원주시'
# total = 0
# recent = 0

# # 데이터 분석
# for line in lines:
#     if line[1] == city:
#         total += 1
#         if int(line[3]) > 20140901:
#             recent += 1

# # 결과 출력
# print('%s의 약국 수: %d개' % (city, total))
# print('5년 이내 개설된 약국 수: %d개' % recent)

# import csv

# # CSV 파일 열기
# f = open('jeju_2019.csv', 'r',  )
# lines = csv.reader(f)

# # 헤더 읽기
# header = next(lines)
# print(header[1], header[2], header[3])  # 헤더의 특정 열 출력

# # 데이터 필터링
# for line in lines:
#     if line[1] == '서귀포' and line[2][5:7] == '01':  # 특정 조건 확인
#         print(line[1], line[2], line[3])  # 필터링된 행 출력

# # 파일 닫기
# f.close()

# import csv
# with open('jeju_2019.csv', 'r', encoding='utf-8') as f:
#     lines = csv.reader(f)
#     next(lines)  # 헤더 건너뛰기
#     sum_rain = [0] * 12  # 리스트 컴프리헨션으로 12개월 초기화
#     for line in lines:
#         month = int(line[2][5:7]) - 1  # 월 추출 (0-11 인덱스로 변환)
#         rain = float(line[5] or 0)  # 비 데이터가 없으면 0으로 처리
#         sum_rain[month] += rain
# max_month_rain = max(sum_rain)
# max_month = sum_rain.index(max_month_rain) + 1
# print(f'(1) 최대 강수 월과 강수량: {max_month}월, {max_month_rain:.1f} mm\n')
# print('(2) 월별 강수량')
# for i, rain in enumerate(sum_rain, 1): 
#     print(f'{i}월 : {rain:.1f} mm')

# import csv 
# month = 7  # 기준 월
# with open('jeju_2019.csv', 'r', encoding='utf-8') as f:
#     lines = csv.reader(f)
#     next(lines)  # 헤더 건너뛰기
#     humidities = [float(line[6]) for line in lines
#         if line[1] == '고산' and int(line[2][5:7]) == month]
# min_humidity = min(humidities)
# max_humidity = max(humidities)
# print(f'{month}월 최저 습도: {min_humidity:.1f}')
# print(f'{month}월 최대 습도: {max_humidity:.1f}')

'''
<9-15>
import csv
with open('jeju_2019.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)
    next(lines)  # 헤더 건너뛰기
    sum_rain = [0] * 12
    for line in lines:
        month = int(line[2][5:7]) - 1  # 월 추출 (0-11 인덱스로 변환)
        rain = float(line[5] or 0)  # 비 데이터가 없으면 0 으로 처리
        sum_rain[month] += rain
max_month_rain = max(sum_rain)
max_month = sum_rain.index(max_month_rain) + 1
print(f'(1) 최대 강수 월과 강수량 : {max_month}월, {max_month_rain:.1f} mm\n')
print('(2) 월별 강수량')
for i, rain in enumerate(sum_rain, 1):     print(f'{i}월 : {rain:.1f} mm')

<9-16>
import csv
from statistics import min, max
month = 7  # 기준 월
with open('jeju_2019.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)
    next(lines)  # 헤더 건너뛰기
    humidities = [float(line[6]) for line in lines 
                  if line[1] == '고산' and int(line[2][5:7]) == month]
min_humidity = min(humidities)
max_humidity = max(humidities)
print(f'{month}월 최저 습도 : {min_humidity:.1f}')
print(f'{month}월 최대 습도 : {max_humidity:.1f}')
'''

# import csv

# # 지역 리스트
# areas = ['제주', '고산', '성산', '서귀포']
# total_rain = {area: 0 for area in areas}  # 딕셔너리 사용

# # CSV 파일 읽기
# with open('jeju_2019.csv', 'r', encoding='utf-8') as f:
#     lines = csv.reader(f)
#     next(lines)  # 헤더 건너뛰기

#     # 강수량 계산
#     for line in lines:
#         area, rain = line[1], float(line[5]) if line[5] else 0
#         if area in total_rain:
#             total_rain[area] += rain

# # 최대 강수량 지역 찾기
# max_area = max(total_rain, key=total_rain.get)

# # 결과 출력
# print(f'(1) 연강수 최대 지역: {max_area}\n')
# print('(2) 지역별 강수량')
# for area, rain in total_rain.items():
#     print(f'{area}: {rain:.1f} mm')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title('Scatter Plot')
plt.colorbar()
plt.show()
