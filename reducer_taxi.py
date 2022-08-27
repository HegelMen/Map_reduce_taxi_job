#!/usr/bin/env python

import sys


def lesson5_reduce():
    list_in = []
    report_group_key = []
    list_uniq_key = set()
    dict_in = []
    list_in_group = []

    for line_in in sys.stdin:
        raw_in = line_in.strip()
        payment_type, month, tips_summ, tips_count = raw_in.split(',')
        raw_in_with_key = ((payment_type + '|' + month), float(tips_summ), int(tips_count))
        list_in.append((raw_in_with_key))
        list_uniq_key.add(raw_in_with_key[0])
        dict_in = [{gr_key: []} for gr_key in list_uniq_key]

    for dic in dict_in:
        for key in dic:
            for i in list_in:
                if i[0] == key:
                    dic[key].append((i[1], i[2]))

    for dict in dict_in:
        for key in dict:
            sum_tips = 0
            sum_cnt_tips = 0
            val_0 = dict.get(key)

            for i in range(len(val_0)):
                sum_tips += val_0[i][0]
                sum_cnt_tips += val_0[i][1]
            dict.update({key: [sum_tips, sum_cnt_tips]})

    for i in dict_in:
        pre_list = list(i.items())
        for x in pre_list:
            payment_type, month = x[0].split('|')
            sum_tips = x[1][0]
            cnt_tips = x[1][1]

            list_in_group.append((payment_type, month, sum_tips, cnt_tips))

    for line in list_in_group:
        if int(line[3]) > 0:
            tips_avg = float(line[2]) / int(line[3])
        else:
            tips_avg = 0
        report_group_key.append((line[1] + '|' + line[0], tips_avg))

    report_group_key.sort()

    print('Payment_type, Month, Tips_average_amount')
    for line in report_group_key:
        month, payment_type = line[0].split('|')
        tips_average_amount = line[1]
        if '2020' in month:
            print('%s,%s,%s' % (payment_type, month, tips_average_amount))


if __name__ == '__main__':
    lesson5_reduce()
