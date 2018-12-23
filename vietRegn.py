#判断字符串中是否包含越南语
import re
# import chardet



def getUnicode(source):
    # charList  = []
    source_2 = source.encode('unicode_escape').decode()
    print(source,source_2)
    charList = re.findall('\\\\u\w{4}|\\\\x\w{2}',source_2)
    return charList


def getVietnamese(source):
    try:
        # 正常中文
        source = source.encode('gb2312')
        print('正常1：', source.decode('gb2312'))
    except:
        try:
            # 排除画像中有繁体字
            source = source.encode('big5')
            print('正常2：', source.decode('big5'))
        except:
            try:
                source = source.encode('unicode')
                print('异常：', source)
            except:
                #     source = source.encode('unicode_escape').decode().encode('windows-1258')
                #     # source.encode('unicode_escape').encode('windows-1258')
                print(123, source)
                print()
                #     print('异常：', source.decode('windows-1258'))
import langid
if __name__ == '__main__':
    # yn = 'Thời tiết hâôm nay thế nào'
    # res = yn.encode('unicode_escape').decode('utf-16').encode('windows-1258')
    # print(res)
    f = open('data/vietnamese',encoding='utf-8')
    for source in f.readlines():
        source = source.strip()
        source = 'Thời tiết hâôm nay thế nào'
        # res = getUnicode(source)
        # res = langid.classify(source)
    print(res)
        #'gb2312'


