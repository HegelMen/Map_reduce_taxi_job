#!/usr/bin/env python

import sys
import datetime as dt


def lesson5_map():
    list_in = []
    list_uniq_key = set()
    dict_in = []

    for line in sys.stdin:
        line = line.strip()
        raw_in = line.split(',')
        if raw_in[0].isdigit():
            raw_in[1] = dt.datetime.strptime(raw_in[1], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
            raw_in[13] = float(raw_in[13])
            raw_in_with_key = ((raw_in[9] + '|' + raw_in[1]), raw_in[13])
            list_in.append(raw_in_with_key)

            list_uniq_key.add(raw_in_with_key[0])

            dict_in = [{gr_key: []} for gr_key in list_uniq_key]

    for dic in dict_in:
        for key in dic:
            for i in list_in:
                if i[0] == key:
                    dic[key].append(i[1])

    for dic in dict_in:
        for key in dic:
            sum_tips = sum(dic.get(key))
            cnt_tips = len(dic.get(key))
            dic.update({key: [sum_tips, cnt_tips]})

    for item in dict_in:
        pre_list = list(item.items())
        for i in pre_list:
            payment_type, month = i[0].split('|')
            sum_tips = i[1][0]
            cnt_tips = i[1][1]
            print('%s,%s,%s,%s' % (payment_type, month, sum_tips, cnt_tips))


if __name__ == '__main__':
    lesson5_map()
