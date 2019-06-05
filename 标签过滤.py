import traceback

def main():
    print('输入标签时，请使用空格分隔多个标签，标签只需要输入前两个字，比如"费用回复",只需要输入"费用"')
    while True:
        try:

            input_tags = input('请输入标签:').strip().split()
            if len(input_tags) == 0:
                input_tags.append('')
            if len(input_tags) == 1:
                input_tags.append('')
            if len(input_tags) == 2:
                input_tags.append('')
            best = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            best_tags = ['', '', '', '']
            for i in range(0, len(input_tags) - 2):
                for j in range(i + 1, len(input_tags) - 1):
                    for k in range(j + 1, len(input_tags)):
                        sum = [0, 0, 0]
                        search_tags = []
                        search_tags.append(input_tags[i][:2])
                        search_tags.append(input_tags[j][:2])
                        search_tags.append(input_tags[k][:2])
                        for employee in employee_list:
                            for tag in employee:
                                if tag in search_tags and employee[0] != '6':
                                    sum[2] += 1
                                    if employee[0] == '5':
                                        sum[0] = sum[0] + 1
                                    if employee[0] == '4':
                                        sum[1] = sum[1] + 1
                                    break

                        message = search_tags[0] + ' ' + search_tags[1] + ' ' + search_tags[2]
                        is_change = False
                        if sum[0] >= best[0][0]:
                            is_change = True
                            best[0] = sum
                            best_tags[0] = message
                        if sum[1] > best[1][1] or (is_change and sum[1] >= best[1][1]):
                            best[1] = sum
                            best_tags[1] = message
                        if sum[2] >= best[2][2]:
                            best[2] = sum
                            best_tags[2] = message
                        if sum[0] + sum[1] > best[3][0] + best[3][1]:
                            best[3] = sum
                            best_tags[3] = message
            # print('{:<19}\t{:<9}\t其中包含的5星、4星、全部干员数分别为：{}'.format('覆盖5星干员最多的标签组合：',      best_tags[0],str(best[0][0])+' '+str(best[0][1])+' '+str(best[0][2])))
            # print('{:<19}\t{:<9}\t其中包含的5星、4星、全部干员数分别为：{}'.format('覆盖4星干员最多的标签组合：',      best_tags[1],str(best[1][0])+' '+str(best[1][1])+' '+str(best[1][2])))
            # print('{:<19}\t{:<9}\t其中包含的5星、4星、全部干员数分别为：{}'.format('覆盖5星和4星干员最多的标签组合：',  best_tags[2],str(best[2][0])+' '+str(best[2][1])+' '+str(best[2][2])))
            # print('{:<19}\t{:<9}\t其中包含的5星、4星、全部干员数分别为：{}'.format('覆盖全部干员最多的标签组合：',      best_tags[3],str(best[3][0])+' '+str(best[3][1])+' '+str(best[3][2])))
            print('{:<19}\t{:<9}'.format('覆盖5星干员最多的标签组合：',      best_tags[0]))
            print('{:<19}\t{:<9}'.format('覆盖4星干员最多的标签组合：',      best_tags[1]))
            print('{:<19}\t{:<9}'.format('覆盖5星和4星干员最多的标签组合：',  best_tags[2]))
            print('{:<19}\t{:<9}'.format('覆盖全部干员最多的标签组合：',      best_tags[3]))
        except:
            traceback.print_exc()


employee_list = [
    ['6', '远程', '女性', '医疗', '支援', '治疗'],
    ['6', '远程', '女性', '医疗', '支援', '治疗'],
    ['6', '远程', '女性', '术师', '群攻', '削弱'],
    ['6', '远程', '女性', '狙击', '输出', '高资'],
    ['6', '近战', '女性', '重装', '防护', '支援', '治疗'],
    ['6', '近战', '女性', '重装', '防护', '输出'],
    ['6', '近战', '女性', '先锋', '费用', '输出'],
    ['6', '近战', '男性', '近卫', '输出', '支援'],
    ['5', '远程', '女性 ', '狙击', '输出'],
    ['5', '远程', '女性', '医疗', '支援', '治疗'],
    ['5', '远程', '女性', '医疗', '支援', '治疗'],
    ['5', '远程', '女性', '医疗', '治疗'],
    ['5', '远程', '女性', '特种', '控场', '快速'],
    ['5', '远程', '女性', '狙击', '群攻', '削弱'],
    ['5', '远程', '女性', '狙击', '输出'],
    ['5', '远程', '女性', '狙击', '输出', '爆发'],
    ['5', '远程', '女性', '狙击', '输出'],
    ['5', '远程', '女性', '辅助', '减速', '输出'],
    ['5', '远程', '女性', '辅助', '削弱'],
    ['5', '远程', '女性', '辅助', '召唤', '控场'],
    ['5', '近战', '女性', '重装', '防护', '位移'],
    ['5', '近战', '女性', '重装', '防护', '治疗'],
    ['5', '近战', '女性', '重装', '防护', '输出'],
    ['5', '近战', '女性', '重装', '防护', '输出', '生存'],
    ['5', '近战', '女性', '先锋', '费用', '支援'],
    ['5', '近战', '女性', '先锋', '费用', '控场'],
    ['5', '近战', '女性', '特种', '位移', '减速'],
    ['5', '近战', '女性', '特种', '输出', '生存'],
    ['5', '近战', '女性', '特种', '位移', '输出'],
    ['5', '近战', '女性', '近卫', '输出', '生存'],
    ['5', '近战', '女性', '近卫', '群攻', '生存'],
    ['4', '远程', '女性', '医疗', '治疗'],
    ['4', '远程', '女性', '医疗', '治疗'],
    ['4', '远程', '女性', '术师', '群攻'],
    ['4', '远程', '女性', '术师', '输出', '削弱'],
    ['4', '远程', '女性', '狙击', '输出', '削弱'],
    ['4', '远程', '女性', '狙击', '群攻', '减速'],
    ['4', '远程', '女性', '狙击', '输出', '生存'],
    ['4', '远程', '女性', '辅助', '减速'],
    ['4', '近战', '女性', '重装', '防护'],
    ['4', '近战', '女性', '重装', '防护', '治疗'],
    ['4', '近战', '女性', '先锋', '费用', '输出'],
    ['4', '近战', '女性', '先锋', '费用', '输出'],
    ['4', '近战', '女性', '特种', '位移'],
    ['4', '近战', '女性', '特种', '位移'],
    ['4', '近战', '女性', '特种', '快速', '防护'],
    ['4', '近战', '女性', '近卫', '输出', '生存'],
    ['4', '近战', '女性', '近卫', '输出', '减速'],
    ['4', '近战', '女性', '近卫', '群攻', '生存'],
    ['4', '近战', '女性', '近卫', '输出'],
    ['4', '近战', '女性', '近卫', '输出', '支援'],
    ['4', '近战', '男性', '重装', '防护'],
    ['3', '远程', '女性', '医疗', '治疗'],
    ['3', '远程', '女性', '术师', '群攻'],
    ['3', '远程', '女性', '狙击', '输出'],
    ['3', '远程', '女性', '辅助', '减速'],
    ['3', '远程', '男性', '医疗', '治疗'],
    ['3', '远程', '男性', '术师', '输出'],
    ['3', '远程', '男性', '狙击', '输出'],
    ['3', '近战', '女性', '重装', '防护'],
    ['3', '近战', '女性', '先锋', '费用', '输出'],
    ['3', '近战', '女性', '先锋', '费用'],
    ['3', '近战', '女性', '先锋', '费用'],
    ['3', '近战', '女性', '近卫', '输出', '生存'],
    ['2', '远程', '女性', '术师'],
    ['2', '远程', '男性', '术师'],
    ['2', '远程', '男性', '狙击'],
    ['2', '近战', '女性', '先锋'],
    ['2', '近战', '男性', '重装'],
    ['1', '远程', '女性', '医疗', '治疗'],
    ['1', '近战', '男性', '近卫', '支援']
]
tag_dic = ['近战', '远程', '男性', '女性', '先锋', '狙击', '医疗', '术师', '近卫', '重装', '辅助', '特种', '输出', '防护', '生存', '治疗', '支援', '费用',
           '快速', '群攻', '召唤', '削弱', '减速', '控场', '位移', '爆发']
main()
