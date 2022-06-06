money = float(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(money/100*per_cent['ТКБ'])
deposit.append(money/100*per_cent['СКБ'])
deposit.append(money/100*per_cent['ВТБ'])
deposit.append(money/100*per_cent['СБЕР'])
deposit.sort(reverse = True)
print('Максимальная сумма, которую вы можете заработать — ', deposit[0])