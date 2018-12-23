#判断字符串中是否包含越南语
import re
# import chardet



def getUnicode(source):
    # charList  = []
    source_2 = source.encode('unicode_escape').decode()
    # print(source,source_2)
    charList = re.findall('\\\\u\w{4}|\\\\x\w{2}',source_2)
    return charList


def getVietnamese(source):
    try:
        # 正常中文
        source = source.encode('gb2312')
        print('正常1：', source.decode('gb2312'))
    except:
        try:
            # 繁体字
            source = source.encode('big5')
            print('正常2：', source.decode('big5'))
        except:
            try:
                res = langid.classify(source)
                if res[0] == 'vi':
                    print('越南语：', source)
            except:
                #     source = source.encode('unicode_escape').decode().encode('windows-1258')
                pass
                #     print('异常：', source.decode('windows-1258'))
import langid
import time
if __name__ == '__main__':
    # yn = 'Thời tiết hâôm nay thế nào'
    # res = yn.encode('unicode_escape').decode('utf-16').encode('windows-1258')
    # print(res)
    f = open('data/vietnamese',encoding='utf-8')
    start = time.time()
    for i in range(1000):
        source = 'Thời tiết hâôm nay thế nào'
        res = getUnicode(source)
        for each in res:
            for j in range(50):
                if each == 1:break


        # print(res[0],source)
    # for source in f.readlines()[:3]:
    #     source = source.strip()
    #     getVietnamese(source)
    end = time.time()
    print('1000条',end-start)


        # res = getUnicode(source)
        #

        #'gb2312'


