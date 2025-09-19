# -*- coding:utf-8 -*-

import os

import settings

from openpyxl import Workbook
from openpyxl.drawing.image import Image

# 1만 개씩 분할 저장하도록 chunk 함수
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


if __name__ == '__main__':
    for idx in range(0, len(settings.MARKET_DATE_LIST)):
        target_date = settings.MARKET_DATE_LIST[idx]
        target_count = settings.MARKET_CLIENT_LIST[idx]
        target_dir = settings.QR_CODE_DIR + target_date + '/'
        # 이미지 파일 경로 리스트
        all_imgs = sorted(os.listdir(target_dir))
        batches = list(chunks(all_imgs, target_count))
        # batches = list(chunks(all_imgs, 5))

        for batch_idx, batch in enumerate(batches, start=1):
            wb = Workbook()
            ws = wb.active
            ws.title = target_date

            for row_idx, fname in enumerate(batch, start=1):
                img_path = os.path.join(target_dir, fname)
                img = Image(img_path)
                # 셀 크기 조정(필요하면)
                ws.row_dimensions[row_idx].height = 100
                ws.column_dimensions['A'].width = 20
                ws.add_image(img, f'A{row_idx}')

            out_fname = f'{settings.DATA_DIR}/Hoyoland_QR_Code_{target_date}.xlsx'
            wb.save(out_fname)
            print(f'{out_fname} 저장 완료')