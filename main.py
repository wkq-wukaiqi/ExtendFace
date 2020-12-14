import os
import re
import bs4
from bs4 import BeautifulSoup
import requests
import time
import random



def get_baike_url(keyword,proxy_http):
    url = 'http://www.baidu.com/s'
    params = {'wd': keyword}
    try:
        print('查找百科url')
        r = requests.get(url=url, params=params,
                         headers={'User-agent':get_ua(),
                                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                  'Cookie':'BAIDUID=E108DCCE3C73F68E5CA3EBDCE06244F7:FG=1; BIDUPSID=E108DCCE3C73F68E5CA3EBDCE06244F7; PSTM=1568558569; BDUSS=0VDYXRUOTg5RUVtQ0hiQnRKS3c2aXVoUEdtc0ZpTjFYU1NSc3J6Q0xhZ0tvSXBmRVFBQUFBJCQAAAAAAAAAAAEAAAAZG-s6TWljaGFlac7eu9oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoTY18KE2NfN; BDUSS_BFESS=0VDYXRUOTg5RUVtQ0hiQnRKS3c2aXVoUEdtc0ZpTjFYU1NSc3J6Q0xhZ0tvSXBmRVFBQUFBJCQAAAAAAAAAAAEAAAAZG-s6TWljaGFlac7eu9oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoTY18KE2NfN; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=cV4OJeC62wcmSD7rc0oxudVYsgKWCRoTH6aos4OFCR74_OF0XSABEG0PoU8g0KubIktFogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbCtoC82tD-3fP36q4jHhR_tbfrjetJyaR3lMhOvWJ5TMCoGy4CBybDX-N3GanQbQH5e0hv60MooShPC-tPMjqvDKfAJ0JJe2bvxLIbv3l02VMQ9e-t2ynLVQnbq--RMW23v0h7mWP02sxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKejj0jGtqtTnQbCj0WJj2266jjbTk-DTDMJTMDG7mWMT-0bFHhDQgKMQxqR8xyP6hbhK4KUJiB-PLaan7_JjOK4DhOxAC0PAM2tIRMhQ8KMQxtNRd-CnjtpvhHxJkj-QobUPUWMJ9LUvftgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtKtWMDIlD5035n-WqlOKaRcKaDv3LPbMHJOoDDvYjxOcy4LdjGKfhTcwQjcH3KJcQt5fSxTRbURRLpDe3-Aq544Dt2AqL454KbDbshLRyR5RQfbQ0a7hqP-jW5TaVR-53b7JOpvybUnxybbQQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6IetRIDoK--JIvbfP0kb4Q_KtF8Mq0X5-RLfaTOLl7F5l8-h45_M6r1KRDSDMnp-43py67MaM3nLJ7xOKQphT8hWKuLMaOlbbJWJ2vJ_p7N3KJmS4P9bT3v5tD10pjf2-biWabM2MbdbKJP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6KWD6j0jH-8qbbfb-o33RTs2Rj_enTxq4bohjPS3GO9BtQmJJrf3b6R3I3KHIJv2bof3lFybPRU3hjyQg-q3R7bJp7PEU_6jhncQ68R0PQG0x-jLIOPVn0MW-5DOJvmQ4nJyUPRbPnnBn-j3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XhI_mj6JP; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=1; BAIDUID_BFESS=E108DCCE3C73F68E5CA3EBDCE06244F7:FG=1; COOKIE_SESSION=399_0_6_8_3_7_0_0_6_3_68_1_21310_0_72_0_1607774936_0_1607774864%7C9%231106_67_1607764416%7C9; H_PS_645EC=474aG0Q63hqabQC9PHaogE9rknOHluMNDDyq%2BAyrVjUBzP1gxoNZi2ILvMS0cpfz1lVs; H_PS_PSSID=1462_33222_33060_31253_33098_33100_32957_33198; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=2lah840h800k2lalh91ft9l8e0r; BDSVRTM=0'},
                         proxies=proxy_http,
                         timeout=(3,7))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(r.text)
        # 获取搜索结果的标签
        for tag in soup.find_all('div'):
            # a标签下含有结果中文内容和跳转链接
            a_tag=tag.find('a')
            if a_tag:
                for child in a_tag.contents:
                    # 检查标签的字符串内容
                    if isinstance(child, bs4.element.NavigableString):
                        match = re.match(r'.*百度百科.*', child)
                        if match:
                            return a_tag.attrs['href']
        #没找到
        return ''
    except:
        print('请求出错')
        return ''

# def get_players(players):
#     try:
#         r=requests.get(url='http://cbadata.sports.sohu.com/players/')
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         soup=BeautifulSoup(r.text,'html.parser')
#         #每个div对应从a-z的某个字符打头的球员名
#         for div_tag in soup.find_all('div','right'):
#             # print(div_tag)
#             for a_tag in div_tag.ul.find_all('a'):
#                 players.append(a_tag.string)
#     except:
#         print('请求出错')

def get_cba_players(players_list):
    try:
        r=requests.get('http://cba.sports.163.com/player/')
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,'html.parser')
        for player_tag in soup.find_all('td','playername'):
            players_list.append(player_tag.a.string)
    except:
        print('请求出错')

def get_csl_players(player_list):
    link_list=[]
    try:
        r=requests.get('https://m.hupu.com/soccer/csl/tables',
                       headers={'User-agent':get_ua()},
                       timeout=(3,7))
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,'html.parser')
        for tr_tag in soup.tbody.find_all('tr'):
            link_list.append('https:'+tr_tag.attrs['data-href'])
        for url in link_list:
            r1=requests.get(url,
                            headers={'User-agent':get_ua()},
                            timeout=(3,7))
            r1.raise_for_status()
            r1.encoding=r1.apparent_encoding
            soup1=BeautifulSoup(r1.text,'html.parser')
            for li_tag in soup1.find_all('li'):
                if li_tag.attrs.get('data-href'):
                    name=li_tag.find('span').string
                    #有的名字后面有"(U23)"，去除
                    player_list.append(re.sub(r'\u0028|\u0029|(U23)','',name))
    except:
        print('请求出错')


def get_baike_summery_img(keyword,proxy_http):
    url=get_baike_url(keyword,proxy_http)
    if url=='':
        #没有找到百科信息
        return ''
    try:
        print('查找百科概述图url')
        r=requests.get(url=url,
                       headers={'User-agent': get_ua(),
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'Cookie': 'BAIDUID=E108DCCE3C73F68E5CA3EBDCE06244F7:FG=1; BIDUPSID=E108DCCE3C73F68E5CA3EBDCE06244F7; PSTM=1568558569; BDUSS=0VDYXRUOTg5RUVtQ0hiQnRKS3c2aXVoUEdtc0ZpTjFYU1NSc3J6Q0xhZ0tvSXBmRVFBQUFBJCQAAAAAAAAAAAEAAAAZG-s6TWljaGFlac7eu9oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoTY18KE2NfN; BDUSS_BFESS=0VDYXRUOTg5RUVtQ0hiQnRKS3c2aXVoUEdtc0ZpTjFYU1NSc3J6Q0xhZ0tvSXBmRVFBQUFBJCQAAAAAAAAAAAEAAAAZG-s6TWljaGFlac7eu9oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoTY18KE2NfN; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=cV4OJeC62wcmSD7rc0oxudVYsgKWCRoTH6aos4OFCR74_OF0XSABEG0PoU8g0KubIktFogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbCtoC82tD-3fP36q4jHhR_tbfrjetJyaR3lMhOvWJ5TMCoGy4CBybDX-N3GanQbQH5e0hv60MooShPC-tPMjqvDKfAJ0JJe2bvxLIbv3l02VMQ9e-t2ynLVQnbq--RMW23v0h7mWP02sxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKejj0jGtqtTnQbCj0WJj2266jjbTk-DTDMJTMDG7mWMT-0bFHhDQgKMQxqR8xyP6hbhK4KUJiB-PLaan7_JjOK4DhOxAC0PAM2tIRMhQ8KMQxtNRd-CnjtpvhHxJkj-QobUPUWMJ9LUvftgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtKtWMDIlD5035n-WqlOKaRcKaDv3LPbMHJOoDDvYjxOcy4LdjGKfhTcwQjcH3KJcQt5fSxTRbURRLpDe3-Aq544Dt2AqL454KbDbshLRyR5RQfbQ0a7hqP-jW5TaVR-53b7JOpvybUnxybbQQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6IetRIDoK--JIvbfP0kb4Q_KtF8Mq0X5-RLfaTOLl7F5l8-h45_M6r1KRDSDMnp-43py67MaM3nLJ7xOKQphT8hWKuLMaOlbbJWJ2vJ_p7N3KJmS4P9bT3v5tD10pjf2-biWabM2MbdbKJP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6KWD6j0jH-8qbbfb-o33RTs2Rj_enTxq4bohjPS3GO9BtQmJJrf3b6R3I3KHIJv2bof3lFybPRU3hjyQg-q3R7bJp7PEU_6jhncQ68R0PQG0x-jLIOPVn0MW-5DOJvmQ4nJyUPRbPnnBn-j3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XhI_mj6JP; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=1; BAIDUID_BFESS=E108DCCE3C73F68E5CA3EBDCE06244F7:FG=1; COOKIE_SESSION=399_0_6_8_3_7_0_0_6_3_68_1_21310_0_72_0_1607774936_0_1607774864%7C9%231106_67_1607764416%7C9; H_PS_645EC=474aG0Q63hqabQC9PHaogE9rknOHluMNDDyq%2BAyrVjUBzP1gxoNZi2ILvMS0cpfz1lVs; H_PS_PSSID=1462_33222_33060_31253_33098_33100_32957_33198; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=2lah840h800k2lalh91ft9l8e0r; BDSVRTM=0'},
                       proxies=proxy_http,
                       timeout=(3,7))
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,'html.parser')
        #查找百度百科侧边栏内容
        side_content_tag=soup.find('div','side-content')
        if side_content_tag:
            #查找侧边栏中的概述图
            summary_pic_tag=side_content_tag.find('div','summary-pic')
            if summary_pic_tag:
                #查找概述图链接
                # pic_url=summary_pic_tag.img.attrs['src']
                #这个链接可以查看原图
                pic_url='https://baike.baidu.com'+summary_pic_tag.a.attrs['href']
                # print(pic_url)
                print('获取概述图原图')
                r1=requests.get(pic_url,
                                headers={'User-agent': get_ua()},
                                proxies=proxy_http,
                                timeout=(3, 7)
                                )
                r1.raise_for_status()
                r1.encoding=r1.apparent_encoding
                soup1=BeautifulSoup(r1.text,'html.parser')
                #含有原图链接的标签
                ori_tag=soup1.find('a','tool-button origin')
                pic_url=ori_tag.attrs['href']
                return pic_url
        return ''
    except:
        print('请求出错')
        return ''

def get_proxies(proxies):
    api_url='https://proxyapi.horocn.com/api/v2/proxies?order_id=CTSN1685981415804376&num=10&format=text&line_separator=unix&can_repeat=no&user_token=e591fc36b991d3e5b3c86329a7bf7f35'
    while True:
        try:
            r = requests.get(api_url,timeout=(3,7))
            r.raise_for_status()
            #提取频繁，等待后重新提取
            if re.search(r'.+(调用频率过快).+',r.text):
                print('提取代理频繁，等待中')
                time.sleep(10)
            else:
                proxies_list = r.text.split('\n')
                # print(proxies_list)
                for proxy in proxies_list:
                     if len(proxy) > 0:
                        proxies.append({'https': proxy,'http':proxy})
                        return proxies
        except:
            print('请求代理出错')
            return []

# def get_proxies():
#     proxies = []
#     import hashlib
#     import sys
#     input_name = hashlib.md5()  # 要加密的字符串
#     input_name.update('46412484'.encode("utf-8"))
#     print(input_name.hexdigest())
#     params={'api':'202012122319327010','akey':'46412484','timespan':'2','type':'2'}
#     r = requests.get('http://www.zdopen.com/ShortProxy/GetIP/',params=params)
#     print(r.text)
#     # proxies_list = r.text.split(' ')
#     #     for proxy in proxies_list:
#     #         if len(proxy) > 0:
#     #             proxies.append({'https': proxy})
#     #             return proxies

def test_proxy(proxy):
    try:
        r=requests.get('https://www.baidu.com',proxies=proxy,timeout=(3,7))
        r.raise_for_status()
        return True
    except:
        return False

def get_ua():
    keys = [
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
    ]
    return keys[random.randint(0, len(keys) - 1)]


if __name__ == '__main__':

    root_path='./web_face_img/'
    if not os.path.exists(root_path):
        os.mkdir(root_path)
    # #获取球员名单
    players=[]
    get_cba_players(players)
    get_csl_players(players)
    # print(players)
    count=0
    round=0
    #去重
    for player_name in set(players):
        #加运动员是防止百科找不到
        player_keyword=player_name+' 运动员'
        print('正在搜索：'+player_name+'，获取代理中...')
        #每搜索5次更换代理
        if round%5==0:
            http={}
            flag=False
            while(not flag):
                proxies=[]
                get_proxies(proxies)
                for proxy in proxies:
                    http=proxy
                    #测试代理
                    flag=test_proxy(http)
        print('使用代理：' + str(http))
        pic_url=get_baike_summery_img(player_keyword,http)
        if pic_url=='':
            print('没有找到：'+player_name+'的相关百科图片，原因：没有搜索到百科链接或没有概述图')
            round+=1
            continue
        try:
            print('下载图片')
            r=requests.get(pic_url,
                           headers={'User-agent':get_ua()},
                           proxies=http,
                           timeout=(3, 7)
                           )
            r.raise_for_status()
            with open(root_path+str(count)+'.jpg','wb') as f:
                f.write(r.content)
                f.close()
                print('第'+str(count+1)+'个球员：'+player_name+'的图片信息保存成功！')
                count+=1
                round+=1
        except:
            print('没有找到：' + player_name + '的相关百科图片，原因：请求错误')
            round += 1
            continue

