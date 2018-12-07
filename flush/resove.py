import Spider
import datetime
import random
from pyquery import PyQuery as pq
#import datetim
n = datetime.datetime.now()
y = n.year
class Resove:
    @staticmethod
    def getExam(s_id,s_name,jwc_pwd):
        s = Spider.Spider()
        res = []
        if s.login(s_id,jwc_pwd):
            try:
                html = pq(s.get(url = "http://inquiry.ecust.edu.cn/jsxsd/xsks/xsksap_list").text)
                l1 = []
                table = pq(html("#dataList")[0])
                trs = pq(table("tr"))
                for i in range(1, len(trs)):
                    l1.append(pq(trs[i]).text().split())
                for eac in l1:
                    if eac[0] == "未查询到数据":
                        return []
                res.append((s_id, s_name,each[1],each[2],datetime.datetime(2018,1,1,1,1),each[5]))
            except:
                res = []
        return res
    @staticmethod
    def getScore(s_id,s_name,jwc_pwd):
        s = Spider.Spider()
        res = []
        if s.login(s_id, jwc_pwd):
            kksjL = ['%d-%d-1' % (y - 1, y),
                     '%d-%d-2' % (y - 1, y),
                     '%d-%d-1' % (y, y + 1),
                     '%d-%d-2' % (y, y + 1)]
            for each in kksjL:
                data = {
                    'kksj': each,
                    'kcxz': '',
                    'kcmc': '',
                    'xsfs': 'all'}
                try:
                    html = pq(s.post(url='http://inquiry.ecust.edu.cn/jsxsd/kscj/cjcx_list', data=data).text)
                    l1 = []
                    table = pq(html("#dataList")[0])
                    trs = pq(table("tr"))
                    for i in range(1, len(trs)):
                        l1.append(pq(trs[i]).text().split())
                    for eac in l1:
                        res.append((s_id,s_name,eac[1],eac[2],float(eac[-3]),str(eac[-3])))
                except:
                    pass
        return res

if __name__ == "__main__":
    for each in Resove.getExam('10162600','李明辰','!asd112233'):
        print(each)