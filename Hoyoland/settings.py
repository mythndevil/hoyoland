
import os


MYSQL_HOST = "54.238.75.210"

MYSQL_USER = "root"
MYSQL_PASSWORD = "ghdyfosem!23"

USER_DATABASE = 'hoyoland'
CONTENT_DATABASE = 'content'


USER_TABLE = 'user'


BASE_DIR_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

HOYOLAND_LOGGER_NAME = 'hoyoland'
HOYOLAND_LOGGER_FILE = BASE_DIR_PATH + "/logs/hoyoland.log"

BASE_DIR = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
DATA_DIR = BASE_DIR + '/data'
QR_CODE_DIR = DATA_DIR + '/qr_code/'

HOYOLAND_DOMAIN = 'https://www.hoyoshop.co.kr'
LOGIN_URL = HOYOLAND_DOMAIN + '/login.html?uid=%s'

MARKET_DATE_LIST = ['1009','1010','1011','1012','HY','CMNT','ADMIN']
MARKET_CLIENT_LIST = [7100,7000,9600,8400,600,300,50]