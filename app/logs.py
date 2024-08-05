import datetime
import logging
import sys

# 현재 로컬 타임존 정보 가져오기
local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

# 타임존 오프셋 계산
tz_offset = datetime.datetime.now(local_timezone).strftime("%z")

# 로거 설정
_logger = logging.getLogger("nemo-worker")
_logger.setLevel(logging.DEBUG)

# 포맷 설정
formatter = logging.Formatter("[%(asctime)s: %(levelname)s/%(processName)s] %(message)s")

# 핸들러 생성 및 포맷 설정
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 로거에 핸들러 추가
_logger.addHandler(console_handler)
_logger.propagate = False


def get_logger(name=None):
    if name:
        logger = logging.getLogger(name)
    else:
        logger = _logger
    return logger
