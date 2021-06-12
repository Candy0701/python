'''
顯示今天的日期，
零食的保存期限為2/21/2022，
請顯示還有多久會到保存期限。
'''

import datetime
now = datetime.date.today()
期限=int(input('輸入保存期限:')
next = datetime.datetime.strptime(期限, '%m/%d/%Y').date()
diff = (next-now)
print(diff)