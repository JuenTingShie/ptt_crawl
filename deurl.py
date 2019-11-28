table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
# M之後為10進位，轉成64進位共6碼
# A之後為16進位，轉成64進位共2碼
# 文章代碼總長度為8碼
# https://www.ptt.cc/bbs/PttNewhand/M.1449878551.A.895.html


def url_to_code(long_url):
    url = long_url[:-5].split('/')[-1]

    def hex_to_base64():
        hex_code = url[15:]

        bins = bin(int(hex_code, 16))[2:]  # 16進位轉2進位
        while(len(bins) % 6 != 0):  # 前面不足項補0
            bins = '0'+bins
        bins_list = [bins[i:i+6]
                     for i in range(0, len(bins), 6)]  # 每6個為一組，預備轉成64進位
        hex_list = [int(i, 2) for i in bins_list]  # 轉成10進位
        base64_list = [table[int(i)]
                       for i in hex_list]  # 去table找各10進位數字所代表的64進位值

        return ''.join(base64_list)

    def dec_to_base64():
        dec_code = url[2:12]

        bins = (bin(int(dec_code))[2:])  # 10進位轉2進位
        while(len(bins) % 6 != 0):  # 前面不足項補0
            bins = '0'+bins
        bins_list = [bins[i:i+6]
                     for i in range(0, len(bins), 6)]  # 每6個為一組，預備轉成64進位
        hex_list = [int(i, 2) for i in bins_list]  # 轉成10進位
        base64_list = [table[int(i)]
                       for i in hex_list]  # 去table找各10進位數字所代表的64進位值

        return ''.join(base64_list)

    return '#'+''.join(dec_to_base64()+hex_to_base64())
