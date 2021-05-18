import csv 
import glob 
import os 
# 형태소 분석한 것 csv로 만드는 코드
input_path = './news_dir' 
#검색할 디렉토리, 폴더명 지정(현재위치) 
output_file = 'csv/result_art.csv'
#결과물 파일명 
is_first_file = True 
for i in range(0, 5074):
    for input_file in glob.glob(os.path.join(input_path, 'output'+str(i))): #검색할 파일명 
        print(os.path.basename(input_file))
        with open(input_file, 'r', newline='', encoding='utf-8-sig') as txt_file: 
            with open(output_file, 'a', newline='', encoding='utf-8-sig') as csv_out_file: 
                freader = txt_file.read()
                fwriter = csv.writer(csv_out_file)
                if is_first_file: 
                    fwriter.writerow([freader])
                    is_first_file = False 
                else: 
                    #header = next(freader) 
                    # #헤더를 건너뛰는 옵션 
                    fwriter.writerow([freader])
                
                    