# [문제5] 사칙연산 관련 패키지와 모듈을 작성하고, 다른 모듈에서 import하여 결과를 확인하시오.
import os, sys

sys.path.append(f'..{os.sep}..{os.sep}')
from chapter06.myCalcPackage import calcModule
from logging import Logger, getLogger, StreamHandler, ERROR
from io import StringIO

logger: Logger = getLogger()
logger.addHandler(StreamHandler())
logger.setLevel(ERROR)

buffer = StringIO()

try:
    x: int = int(input("x="))
    y: int = int(input("y="))
    buffer.write(f"Add={calcModule.add(x, y)}\n")
    buffer.write(f"Sub={calcModule.sub(x, y)}\n")
    buffer.write(f"Mul={calcModule.mul(x, y)}\n")
    buffer.write(f"Div={calcModule.div(x, y)}")
    print(buffer.getvalue())
    buffer.close()
except ValueError:
    logger.error("숫자를 입력하세요.")
    exit(1)
except ZeroDivisionError:
    logger.error("0으로 나눌 수 없습니다.")
    exit(1)