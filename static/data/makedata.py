import csv
import json

possible_gym = []
f = open('C:\\Users\\sdhky\\Desktop\\nogu.trainer\\nugudjango\\nuguhome\\static\\data\\trainer.csv','r',encoding='euc-kr')
gym_list = csv.reader(f)
for row in gym_list:
    gymdic = {}
    gymdic['gym'] = row[0]
    gymdic['mapurl'] = row[1]
    possible_gym.append(gymdic)
print(possible_gym[0])
with open('C:\\Users\\sdhky\\Desktop\\nogu.trainer\\nugudjango\\nuguhome\\static\\data\\gymJson.json','w',encoding='utf-8') as gymjson:
    json.dump(possible_gym,gymjson,ensure_ascii=False)