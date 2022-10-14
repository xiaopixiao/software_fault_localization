import csv
import matplotlib.pyplot as plt
# from pandas.io.excel import ExcelWriter
# import pandas as pd

# with ExcelWriter('export.xlsx') as ew:
# 	#将csv文件转换为excel文件
# 	pd.read_csv("export.csv").to_excel(ew, sheet_name="sheet_1", index=False)

data_x = []
data_y = []
data_x_new = []
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_x = [row[0] for row in reader]
data_x.remove('Tarantula')
for i in data_x:
    data_x_new.append(i[5:])
print(data_x_new)


f_csv.close()
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_y = [row[1] for row in reader]
data_y.remove('result_0')
data_y = [float(x) for x in data_y]
print(data_y)

    
x = [0] * 40
for i in range(40):
    x[i] += i

fig = plt.figure(figsize=(16, 5))
plt.bar(x, data_y, width=0.5, tick_label=data_x_new)
plt.ylim(0, 1)
plt.title("Tarantula")
plt.xlabel("block[i]")
plt.ylabel("value")
plt.savefig('Tarantula.jpg')
plt.show()



data_x = []
data_y = []
data_x_new = []
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_x = [row[2] for row in reader]
data_x.remove('Goodman')
for i in data_x:
    data_x_new.append(i[5:])
print(data_x_new)


f_csv.close()
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_y = [row[3] for row in reader]
data_y.remove('result_1')
data_y = [float(x) for x in data_y]
print(data_y)

    
x = [0] * 40
for i in range(40):
    x[i] += i

fig = plt.figure(figsize=(16, 5))
plt.bar(x, data_y, width=0.5, tick_label=data_x_new)
plt.ylim(0, 1)
plt.title("Goodman")
plt.xlabel("block[i]")
plt.ylabel("value")
plt.savefig('Goodman.jpg')
plt.show()



data_x = []
data_y = []
data_x_new = []
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_x = [row[4] for row in reader]
data_x.remove('Michael')
for i in data_x:
    data_x_new.append(i[5:])
print(data_x_new)


f_csv.close()
f_csv = open("export.csv", "r")
reader = csv.reader(f_csv)
data_y = [row[5] for row in reader]
data_y.remove('result_2')
data_y = [float(x) for x in data_y]
print(data_y)

    
x = [0] * 40
for i in range(40):
    x[i] += i

fig = plt.figure(figsize=(16, 5))
plt.bar(x, data_y, width=0.5, tick_label=data_x_new)
plt.ylim(0, 1)
plt.title("Michael")
plt.xlabel("block[i]")
plt.ylabel("value")
plt.savefig('Michael.jpg')
plt.show()


