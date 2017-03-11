# 1 Berarti Loop, Selain itu tidak akan Loop
loop = 1

satu = 1;
dua = 2;
tiga = 3;
empat = 4;
lima = 5;

import time
start_time = time.time()
while loop == 1:
    print "Hello Rizki, Selamat datang di Program Kalkulator."
    choice = 1;
    if choice == 1:
        jum1 = input("Jumlahkan Ini: ")
        jum2 = input("Dengan ini: ")
        kal3 = input("Kalikan dengan: ")
        bag4 = input("Bagikan dengan: ")
        print jum1, "+", jum2, "*", kal3, "/", bag4, "=", jum1 + jum2 * kal3 / bag4

        loop = 0;
    totalTime = format((time.time() - start_time), '.5f')
    print("Delta t = ", totalTime)