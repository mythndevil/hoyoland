# -*- coding:utf-8 -*-

import sys
import random
import string
import time

import pymysql.cursors

import settings
import log_util
import sql_query


logger = log_util.getLogHandler(settings.HOYOLAND_LOGGER_NAME, settings.HOYOLAND_LOGGER_FILE)
logger.info("========= " + sys.argv[0] + " Start =========")


def generate_random_string(length):
    """주어진 길이의 랜덤 문자열을 생성합니다."""
    characters = string.ascii_letters + string.digits  # 대문자, 소문자, 숫자 조합
    return ''.join(random.choice(characters) for idx in range(length))


def set_user_info(target_id):
    user_info_dict = dict()
    user_info_dict['id'] = target_id
    user_info_dict['user_id'] = generate_random_string(16)

    return user_info_dict


if __name__ == '__main__':
    user_info_db = pymysql.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                                   passwd=settings.MYSQL_PASSWORD, db=settings.USER_DATABASE,
                                   cursorclass=pymysql.cursors.DictCursor)
    user_info_cursor = user_info_db.cursor()

    count = 1
    market_date_list = settings.MARKET_DATE_LIST
    market_client_list = settings.MARKET_CLIENT_LIST
    market_date_idx = 0

    for num in range(0, 31600):
        id = market_date_list[market_date_idx] + str(count).zfill(4)
        user_info = set_user_info(id)
        insert_query = sql_query.make_insert_query(settings.USER_TABLE, user_info)
        # print(insert_query)

        user_info_cursor.execute(insert_query)

        if num % 100 == 0:
            print(num)
            time.sleep(1)

        if count % market_client_list[market_date_idx] == 0:
            market_date_idx += 1
            count = 1
        else:
            count += 1

    user_info_cursor.execute("commit;")

    user_info_cursor.close()



logger.info("========= " + sys.argv[0] + " End =========")