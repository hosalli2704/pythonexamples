import pandas as pd
L1 = [[10,20,30],[40,50,60]]
L2 = list([[10,20,30],[40,50,60]])
df1 = pd.DataFrame([[10,20,30],[40,50,60]], index=['r1','r2'],columns=['c1','c2','c3'])
print(L1, L2, df1, sep='\n')

import matplotlib.pyplot as plt
df1.plot()
#plt.show()
df1.plot.bar()
plt.savefig('graph.png')

writer = pd.ExcelWriter('myreport.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='DATA')
wb = writer.book
ws = wb.add_worksheet('GRAPH')
ws.insert_image('B2','graph.png')
writer.close()

