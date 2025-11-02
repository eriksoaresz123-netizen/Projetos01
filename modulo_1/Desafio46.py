from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'\033[31;40m{"Estourando fogos":=^20}\033[m')