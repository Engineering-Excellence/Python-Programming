# 6.5 패키지와 모듈

# 6.5.1 라이브러리 import

# 1. 모듈 추가 (방법1)
# 형식) import 패키지명.모듈명
import os, sys

sys.path.append(f'..{os.sep}..{os.sep}')
import chapter06.myPackage.scattering

# 데이터셋
data: list[float] = [1, 3, 1.5, 2, 1, 3.2]

# 산술평균 함수 호출
print(f'평균: {chapter06.myPackage.scattering.average(data)}')

# 분산과 표준편차 함수 호출
var, sd = chapter06.myPackage.scattering.var_sd(data)
print(f'분산: {var}')
print(f'표준편차: {sd}')

print()

# 2. 모듈 추가 (방법2)
# 형식) from 패키지명.모듈명 import 함수명
from chapter06.myPackage.scattering import average, var_sd

print(f'평균: {average(data)}')

var, sd = var_sd(data)
print(f'분산: {var}')
print(f'표준편차: {sd}')
