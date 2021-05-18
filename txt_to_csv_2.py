import csv 
import glob 
import os 
import jsonlines

input_path = 'summary_data/train.jsonl' 
#검색할 디렉토리, 폴더명 지정(현재위치) 
output_file = 'csv/result_ext.csv'
#결과물 파일명 

with open(input_path, 'rb') as reader:
    mylist = list(jsonlines.Reader(reader))
mylist = mylist[0:5074]
    
l = len(mylist)

with open(output_file, 'a', newline='', encoding='utf-8-sig') as csv_out_file: 
    for idx,items in enumerate(mylist):
        target = items['extractive']
        fwriter= csv.writer(csv_out_file)
        fwriter.writerow([target])