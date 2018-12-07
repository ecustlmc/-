import requests
from CodeFather import CodeFather
'''
author:ECUST Li Mingchen
qq:63114954
'''
import execjs
def Encry(s:str):
    jm=execjs.compile('''
    var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    function encodeInp(input) {
    var output = "";
    var chr1, chr2, chr3 = "";
    var enc1, enc2, enc3, enc4 = "";
    var i = 0;
    do {
        chr1 = input.charCodeAt(i++);
        chr2 = input.charCodeAt(i++);
        chr3 = input.charCodeAt(i++);
        enc1 = chr1 >> 2;
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
        enc4 = chr3 & 63;
        if (isNaN(chr2)) {
            enc3 = enc4 = 64
        } else if (isNaN(chr3)) {
            enc4 = 64
        }
        output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
        chr1 = chr2 = chr3 = "";
        enc1 = enc2 = enc3 = enc4 = ""
    } while (i < input.length);
    return output
    }
    ''')
    return jm.call('encodeInp',s)
class Spider(requests.sessions.Session):
    __Imgurl = "http://118.25.91.92:6000/ecust"
    __codeUrl = "http://inquiry.ecust.edu.cn/jsxsd/verifycode.servlet"
    __loginUrl = "http://inquiry.ecust.edu.cn/jsxsd/xk/LoginToXk"
    __mainUrl = "http://inquiry.ecust.edu.cn/jsxsd/framework/xsMain.jsp"
    __Headers = {"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "Origin": "http://inquiry.ecust.edu.cn",
                "Referer": "http: // inquiry.ecust.edu.cn/jsxsd/xk/LoginToXk",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    __MAX_LINK = 5#最大测试次数
    def login(self,username:str,passwd:str):
        for i in range(0,self.__MAX_LINK):
            #print("开始获取验证码....%d"%(i+1))
            codeBin = self.get(self.__codeUrl,headers = self.__Headers).content  #获取验证码
            #print("获取成功.....开始解析...%d"%(i+1))
            code = CodeFather.RFromBytes(codeBin).get("value")
            #print(code)
            #
            if len(code) == 0:
                continue
            #
            data = {"encoded":"","RANDOMCODE":code}
            data["encoded"] = Encry(username) + "%%%" + Encry(passwd)
            #print(data)
            #
            self.post(self.__loginUrl,data=data)
            #
            testRes = self.get(self.__mainUrl)
            if testRes.status_code == 200:
                return True
        return False
    def getScoreTermHtml(self,year1,year2,term):
        data = {}
        data["kksj"] = "%d-%d-%d"%(year1,year2,term)
        data["xsfs"] = "all"
        text = self.post("http://inquiry.ecust.edu.cn/jsxsd/kscj/cjcx_list",data=data,headers = self.__Headers).text
        return text
    def getsyllabusUrlHtml(self):
        return self.get("http://inquiry.ecust.edu.cn/jsxsd/xskb/xskb_list.do",headers = self.__Headers).text

if __name__ == "__main__":
    s = Spider()
    if s.login("10162600","!asd112233"):
        #print(s.getsyllabusUrlHtml())
        print(s.getScoreTermHtml(2017,2018,2))