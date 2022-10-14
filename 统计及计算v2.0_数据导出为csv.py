import csv

f_right = open("answer.txt", 'r')
f_test = open("answer_wrong.txt", 'r')

result_right = f_right.readlines()
result_test = f_test.readlines()

N = 200
N_block = 40
N_c = [0] * N_block
N_u = [0] * N_block
N_cf = [0] * N_block
N_uf = [0] * N_block
N_cs = [0] * N_block
N_us = [0] * N_block
N_s = 0
N_f = 0

f_export = open("export.csv", 'wt', encoding='utf-8', newline='')
writer = csv.writer(f_export, delimiter=",")

header = ["Tarantula", "result_0", "Goodman", "result_1", "Michael", "result_2"]
csvrow1 = []
csvrow2 = []
csvrow3 = []
csvrow4 = []
csvrow5 = []
csvrow6 = []


for i in range(N):
    result_right[i] = result_right[i][:-2]
    result_test[i] = result_test[i][:-2]
    right = result_right[i].split('  ')
    test = result_test[i].split('  ')
    if right[0] == test[0]:
        n = test[1].replace('block:', '').split(',')
        N_s += 1
        for j in n:
            N_c[eval(j)] += 1
            N_cs[eval(j)] += 1
    else:
        n = test[1].replace('block:', '').split(',')
        N_f += 1
        for j in n:
            N_c[eval(j)] += 1
            N_cf[eval(j)] += 1
f_right.close()
f_test.close()


for i in range(N_block):
    N_u[i] = N - N_c[i]
    N_uf[i] = N_f - N_cf[i]
    N_us[i] = N_s - N_cs[i]

Tarantula = {}
Goodman = {}
Michael = {}
for i in range(N_block):
    if N_c[i] == 0:
        Tarantula["block{}".format(i+1)] = 0
        Goodman["block{}".format(i+1)] = 0
        Michael["block{}".format(i+1)] = 0
    else:
        Tarantula["block{}".format(i+1)] = (N_cf[i]/N_f)/(N_cf[i]/N_f+N_cs[i]/N_s)
        Goodman["block{}".format(i+1)] = (2*N_cf[i]-N_uf[i]-N_cs[i])/(2*N_cf[i]+N_uf[i]+N_cs[i])
        Michael["block{}".format(i+1)] = (4*(N_cf[i]*N_us[i]-N_cs[i]*N_uf[i]))/(pow(N_cf[i]+N_us[i],2)+pow(N_cs[i]+N_uf[i],2))

x = ''
T = Tarantula
print("Tarantula:")
while 1:
    y = 0
    for j in T.keys():
        if abs(T[j]) >= y:
            x = j
            y = abs(T[x])
    print("{}: {}".format(x, y))
    csvrow1.append(x)
    csvrow2.append(y)
    del T[x]
    if T == {}:
        break
print("")

G = Goodman
print("Goodman:")
while 1:
    y = 0
    for j in G.keys():
        if abs(G[j]) >= y:
            x = j
            y = abs(G[x])
    print("{}:{}".format(x, y))
    csvrow3.append(x)
    csvrow4.append(y)
    del G[x]
    if G == {}:
        break
print("")

M = Michael
print("Michael:")
while 1:
    y = 0
    for j in M.keys():
        if abs(M[j]) >= y:
            x = j
            y = abs(M[x])
    print("{}:{}".format(x, y))
    csvrow5.append(x)
    csvrow6.append(y)
    del M[x]
    if M == {}:
        break
print("")

writer.writerow(header)
writer.writerows(zip(csvrow1, csvrow2, csvrow3, csvrow4, csvrow5, csvrow6))

f_export.close()