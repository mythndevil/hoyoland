# -*- coding:utf-8 -*-

import sys
import qrcode

import pymysql.cursors

import settings
import log_util
import sql_query


def generate_qrcode_option(id, value):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=2
    )
    qr.add_data(value)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # img.save(f"{settings.QR_CODE_DIR}{str(idx).zfill(5)}.jpg")
    img.save(f"{settings.QR_CODE_DIR}{str(id)[:-4]}/{str(id)[-4:]}.jpg")


# def create_qr_code_with_size(data, idx, size_mm, box_size=None):
#     """
#     지정된 크기의 QR 코드를 생성하고 저장합니다.
#
#     Args:
#         data: QR 코드로 인코딩할 데이터 (문자열).
#         filename: 저장할 파일 이름 (예: 'qr_code.png').
#         size_mm: QR 코드의 예상 크기 (mm).  정확한 크기를 보장하지 않으며, box_size와 버전에 따라 조정됩니다.
#         box_size: 각 모듈의 픽셀 크기. None이면 자동 계산 (권장).
#     """
#
#     # QR 코드 버전과 에러 보정 레벨 설정 (필요에 따라 조정)
#     version = 1  # 최소 버전. 데이터 양에 따라 자동으로 증가합니다.
#     error_correction = qrcode.constants.ERROR_CORRECT_L  # 에러 보정 레벨 (L, M, Q, H)
#
#     # 필요한 경우 box_size 계산
#     if box_size is None:
#         # 데이터 양과 에러 보정 레벨에 따라 적절한 버전과 모듈 수를 계산합니다.
#         # 17mm 크기를 기준으로 box_size를 대략적으로 추정합니다.
#         # 실제 계산은 QR 코드 버전과 모듈 수에 따라 달라집니다.
#         # 이 예제에서는 17mm를 대략 67px로 가정하고, 버전을 먼저 결정합니다.
#         qr = qrcode.QRCode(
#             version=version,
#             error_correction=error_correction,
#             box_size=1,  # 우선 1로 설정하고, 실제 크기에 맞춰 조정
#             border=4,
#         )
#         qr.add_data(data)
#         qr.make(fit=True)
#
#         # QR 코드 버전과 모듈 수 확인
#         version = qr.version
#         modules_per_side = qr.modules_count
#         # 버전에 따른 모듈 수:  version 1은 21, 2는 25, 3은 29, ...
#         # 최소 17mm 크기를 위한 box_size 추정
#         # (추정 값:  17mm * 10px/mm / modules_per_side)
#         estimated_pixels_per_module = (size_mm * 10) / modules_per_side
#         box_size = int(estimated_pixels_per_module)
#
#         # QR 코드 다시 생성
#         qr = qrcode.QRCode(
#             version=version,
#             error_correction=error_correction,
#             box_size=box_size,
#             border=4,
#         )
#         qr.add_data(data)
#         qr.make(fit=True)
#
#
#     # 이미지 생성
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(f"{settings.QR_CODE_DIR}{str(idx).zfill(5)}.jpg")


if __name__ == '__main__':
    logger = log_util.getLogHandler(settings.HOYOLAND_LOGGER_NAME, settings.HOYOLAND_LOGGER_FILE)
    logger.info("========= " + sys.argv[0] + " Start =========")


    user_info_db = pymysql.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                   passwd=settings.MYSQL_PASSWORD, db=settings.USER_DATABASE,
                                   cursorclass=pymysql.cursors.DictCursor)
    user_info_cursor = user_info_db.cursor()

    date_list = settings.MARKET_DATE_LIST

    for idx in range(0, 5):
        target_date = date_list[idx] + '%'

        query = sql_query.make_select_query(target_date)
        print(query)
        user_info_cursor.execute(query)
        records = user_info_cursor.fetchall()
        for record in records:
            user_id = record['user_id']
            record_id = record['id']
            url = settings.LOGIN_URL % str(user_id)
            # print(url)

            generate_qrcode_option(record_id, url)

