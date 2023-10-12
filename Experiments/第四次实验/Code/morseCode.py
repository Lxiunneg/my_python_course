MORSE_CODE = {
    '·-': 'A', '–···': 'B', '–·–·': 'C', '–··': 'D', '·': 'E', '··–·': 'F', '––·': 'G', '····': 'H',
    '··': 'I', '·–––': 'J', '–·–': 'K', '·–··': 'L', '––': 'M', '–·': 'N', '–––': 'O', '·––·': 'P',
    '––·–': 'Q', '·–·': 'R', '···': 'S', '–': 'T', '··–': 'U', '···–': 'V', '·––': 'W', '–··–': 'X',
    '–·––': 'Y', '––··': 'Z', '–––––': '0', '·––––': '1', '··–––': '2', '···––': '3', '····–': '4',
    '·····': '5', '–····': '6', '––···': '7', '–––··': '8', '––––·': '9', '·–·–·–': '.', '––··––': ',',
    '··––··': '?', '·––––·': "'", '–·–·––': '!', '–··–·': '/', '–·––·': '(', '–·––·–': ')', '·–···': '&',
    '–––···': ':', '–·–·–·': ';', '–···–': '=', '·–·–·': '+', '–····–': '-', '··––·–': '_', '·–··–·': '"',
    '···––··–': '$', '·––·–·': '@'
}



def decodeBits(bits):
    bits = bits.strip('0')
    # 寻找最小单位时间
    bits_temp = bits.split('1')
    bits_temp_0 = [x for x in bits_temp if x != '']
    bits_temp = bits.split('0')
    bits_temp_1 = [x for x in bits_temp if x != '']
    print(bits_temp_0)
    print(bits_temp_1)
    if bits_temp_0:
        min_len_0 = len(min(bits_temp_0))
    else:
        min_len_0 = 0
    if bits_temp_1:
        min_len_1 = len(min(bits_temp_1))
    else:
        min_len_1 = 0
    if min_len_0 == 0:
        unit_time = min_len_1
    elif min_len_1 == 0:
        unit_time = min_len_0
    else:
        unit_time = min(min_len_1,min_len_0) # 通过比较bits中最短的有意义段确定单位时间
    
    print(min_len_0)
    print(min_len_1)
    print(unit_time)
    
    bits = bits[::unit_time] # 按照单位时间对原字符串进行切片，还原至最简形式
    print(bits)
    decoded_Bits = bits.replace('111','-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','') # 字符转义
    print(decoded_Bits)
    return decoded_Bits
    
def decodeMorse(morseCode):
    words = morseCode.split('   ')
    
    message = ''
    
    for word in words:
        chars = word.split()
        for char in chars:
           message = message + MORSE_CODE[char]
        message = message + ' '
    
    return message.strip()

bits = '1110111'
print(decodeMorse((decodeBits(bits))))