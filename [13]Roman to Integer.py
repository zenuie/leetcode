def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    # 判斷是否是空值 以及剩餘一個字母時
    while s != '' and s not in roman_dict:
        # 判斷是否後面數字大於前面 and 兩字母不相等
        if roman_dict[s[0]] < roman_dict[s[1]] and roman_dict[s[0]] != roman_dict[s[1]]:
            result += abs(roman_dict[s[0]] - roman_dict[s[1]])
            s = s.replace(s[0], '', 1).replace(s[1], '', 1)
        else:
            result += roman_dict[s[0]]
            s = s.replace(s[0], '', 1)
    if s != '':
        result += roman_dict[s[0]]
    return result


romanToInt('MCMXCIV')
