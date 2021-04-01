import pandas as pd
csv       = pd.read_csv('/Users/premagrawal/Desktop/Profit_Loss_Report_BN2248_2021.csv')
net_pnl   = []
for i in range(5,32):
    if i < 10 :
        date  = '0'+str(i)+'-03-2021'
    else :
        date  = str(i)+'-03-2021'
    buy_data  = pd.DataFrame(csv[(csv['Buy Date']  == date)])
    sell_data = pd.DataFrame(csv[(csv['Sell Date'] == date)])
    data = pd.concat([buy_data,sell_data],ignore_index=True)
    gross_pnl = ((data['Gross PL']).to_list())
    total_pnl = []
    for gross in gross_pnl:
        gross = float(gross.replace(',',''))
        total_pnl.append(gross)
    total = sum(total_pnl)
    if total == 0 : 
        pass
    else :
        print(date,' ',total)
        net_pnl.append(total)
    #data.to_csv('Data.csv')
print('Total :',sum(net_pnl))
