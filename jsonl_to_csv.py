import json
import csv
# music.json 파일을 읽어서 melon.csv 파일에 저장
with open('summary_data/train.json', 'r', encoding = 'utf-8') as input_file, open('train_to_csv.csv', 'w', newline = '') as output_file :
    data = json.load(input_file)
    '''
    data[0] 은 json 파일의 한 줄을 보관 {"title:"Super Duper", "songId": ...}
    data[0]['컬럼명'] 은 첫 번째 줄의 해당 컬럼 element 보관
    '''
    f = csv.writer(output_file)
    # csv 파일에 header 추가
    f.writerow(["media", "id", "article_original", "abstractive", "extractive"])
    
    # write each row of a json file
    for datum in data:
    # exclude instrument versions
        f.writerow([datum["media"], datum["id"], datum["article_original"], datum["abstractive"], datum["extractive"]])

