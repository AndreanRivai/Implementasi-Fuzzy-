
min_hargaMurah = 10000
max_hargaMurah = 15000

min_hargaSedang = 15001
max_hargaSedang = 25000

min_hargaMahal = 25001
max_hargaMahal = 50000

min_porsiSedikit = 150 
max_porsiSedikit = 250

min_porsiBanyak = 251
max_porsiBanyak = 500

min_porsiSangatBanyak = 501
max_porsiSangatBanyak = 1000


def inRange(minimal,maximal,input):
    minimal = min(minimal, maximal)
    maximal = max(minimal, maximal)
 
    if((input> minimal) and (input < maximal)):
        return 1
    else:
        return 0

def fuzzyRules(harga, porsi):
    global nilaiRekomendasiRendah
    global nilaiRekomendasiTinggi

    nilaiRekomendasiRendah = 0
    nilaiRekomendasiTinggi = 0

    hargaMurah = inRange(min_hargaMurah, max_hargaMurah, harga)
    hargaSedang = inRange(min_hargaSedang, max_hargaSedang, harga)
    hargaMahal = inRange(min_hargaMahal, max_hargaMahal, harga)

    porsiSedikit = inRange(min_porsiSedikit, max_porsiBanyak, porsi)
    porsiBanyak = inRange(min_porsiBanyak, max_porsiBanyak, porsi)
    porsiSangatBanyak = inRange(min_porsiSangatBanyak, max_porsiSangatBanyak, porsi)
    
    nrRendah_array = []
    nrTinggi_array = []

    if hargaMurah == 1 and porsiSedikit == 1:
        print("Rule 1 : Harga Murah dan Porsi Sedikit")
        derajatRekomendasiRendah = min(derajathargaMurah, derajatporsiSedikit)
        print("Derajat Rekomendasi Rendah :",derajatRekomendasiRendah)
        nilaiRekomendasiRendah = derajatRekomendasiRendah
        nrRendah = nrRendah_array.append(nilaiRekomendasiRendah)

    if hargaMurah == 1 and porsiBanyak == 1:
        print ("Rule 2 : Harga Murah dan Porsi Banyak")
        derajatRekomendasiTinggi = min(derajathargaMurah, derajatporsiBanyak)
        print( "Derajat Rekomendasi Tinggi :",derajatRekomendasiTinggi)
        nilaiRekomendasiTinggi = min(derajathargaMurah, derajatporsiBanyak)
        nrTinggi = nrTinggi_array.append(nilaiRekomendasiTinggi)

    if hargaMurah == 1 and porsiSangatBanyak == 1:
        print ("Rule 3 : Harga Murah dan Porsi Sangat Banyak")
        derajatRekomendasiTinggi = min(derajathargaMurah, derajatporsiSangatBanyak)
        print ("Derajat Rekomendasi Tinggi :",derajatRekomendasiTinggi) 
        nilaiRekomendasiTinggi = derajatRekomendasiTinggi
        nrTinggi = nrTinggi_array.append(nilaiRekomendasiTinggi)
 
    if hargaSedang == 1 and porsiSedikit == 1:
        print( "Rule 4 : Harga Sedang dan Porsi Sedikit")
        derajatRekomendasiRendah = min(derajathargaSedang, derajatporsiSedikit)
        print ("Derajat Rekomendasi Rendah :",derajatRekomendasiRendah)
        nilaiRekomendasiRendah = derajatRekomendasiRendah #bookmark
        nrRendah = nrRendah_array.append(nilaiRekomendasiRendah)

    if hargaSedang == 1 and porsiBanyak == 1:
        print ("Rule 5 : Harga Sedang dan Porsi Banyak")
        derajatRekomendasiTinggi = min(derajathargaSedang, derajatporsiBanyak)
        print ("Derajat Rekomendasi Tinggi :",derajatRekomendasiTinggi)
        nilaiRekomendasiTinggi = derajatRekomendasiTinggi #bookmark
        nrTinggi = nrTinggi_array.append(nilaiRekomendasiTinggi)

    if hargaSedang == 1 and porsiSangatBanyak == 1:
        print ("Rule 6 : Harga Sedang dan Porsi Sangat Banyak")
        derajatRekomendasiTinggi = min(derajathargaSedang, derajatporsiSangatBanyak)
        print ("Derajat Rekomendasi Tinggi :",derajatRekomendasiTinggi)
        nilaiRekomendasiTinggi = derajatRekomendasiTinggi #bookmark
        nrTinggi = nrTinggi_array.append(nilaiRekomendasiTinggi)

    if hargaMahal == 1 and porsiSedikit == 1:
        print ("Rule 7 : Harga Mahal dan Porsi Sedikit")
        derajatRekomendasiRendah = min(derajathargaMahal, derajatporsiSedikit)
        print ("Derajat Rekomendasi Rendah :",derajatRekomendasiRendah)
        nilaiRekomendasiRendah = derajatRekomendasiRendah #Oke
        nrRendah = nrRendah_array.append(nilaiRekomendasiRendah)

    if hargaMahal == 1 and porsiBanyak == 1:
        print ("Rule 8 : Harga Mahal dan Porsi Banyak")
        derajatRekomendasiRendah = min(derajathargaMahal, derajatporsiBanyak)
        print ("Derajat Rekomendasi Rendah :",derajatRekomendasiRendah)
        nilaiRekomendasiRendah = derajatRekomendasiRendah #oke
        nrRendah = nrRendah_array.append(nilaiRekomendasiRendah)

    if hargaMahal == 1 and porsiSangatBanyak == 1:
        print ("Rule 9 : Harga Mahal dan Porsi Sangat Banyak")
        derajatRekomendasiTinggi = min(derajathargaMahal, derajatporsiSangatBanyak)
        print ("Derajat Rekomendasi Tinggi :",derajatRekomendasiTinggi)
        nilaiRekomendasiTinggi = derajatRekomendasiTinggi #oke
        nrTinggi = nrTinggi_array.append(nilaiRekomendasiTinggi)

 
    if nilaiRekomendasiTinggi == 0:
        nilaiRekomendasiTinggi = 0
    else:
        nilaiRekomendasiTinggi = max(nrTinggi_array)

    if nilaiRekomendasiRendah == 0:
        nilaiRekomendasiRendah = 0
    else:
        nilaiRekomendasiRendah = max(nrRendah_array)
 
    print ()
    print ("Nilai Rekomendasi Rendah : ",nilaiRekomendasiRendah)
    print ("Nilai Rekomendasi Tinggi : ",nilaiRekomendasiTinggi)

def centroidMethod(nilaiRekomendasiRendah, nilaiRekomendasiTinggi):
 
    global hasil
    hasil =  (((10+20+30+40+50+60)*nilaiRekomendasiRendah)+((70+80+90+100)*nilaiRekomendasiTinggi))/((6*nilaiRekomendasiRendah)+(4*nilaiRekomendasiTinggi))
    print ("Nilai Rekomendasi : ",hasil)
    return hasil

def fungsiKeanggotaanSegitiga(a, b, c, x):

    if ((x>a) and (x<b)):
        derajatKeanggotaan = (x-a)/(b-a)

    elif (x==b):
        derajatKeanggotaan = 1

    elif ((x>b) and (x<c)):
 
        derajatKeanggotaan = -((x-c)/(c-b))
 
    else:
        derajatKeanggotaan = 0
 
    return derajatKeanggotaan



def fungsiKeanggotaanTrapesium(a,b,c,d,x):

    if ((x>a) and (x<b)):
        derajatKeanggotaan = (x-a)/(b-a)
 
    elif ((x>=b) and (x<=c)):
        derajatKeanggotaan = 1
 
    elif ((x>c) and (x<d)):
        derajatKeanggotaan = -((x-d)/(d-c))

    else:
        derajatKeanggotaan = 0
 
    return derajatKeanggotaan

def derajatHarga(harga):

    global derajathargaMurah
    global derajathargaSedang
    global derajathargaMahal

    derajathargaMurah = fungsiKeanggotaanTrapesium(min_hargaMurah,min_hargaMurah,15001,max_hargaMurah, harga)
    derajathargaSedang = fungsiKeanggotaanSegitiga(min_hargaSedang,15000,max_hargaSedang,harga)
    derajathargaMahal = fungsiKeanggotaanTrapesium(min_hargaMahal,25000,max_hargaMahal,max_hargaMahal,harga)

    print ("Kategori Harga Murah  : ",derajathargaMurah)
    print ("Kategori Harga Sedang : ",derajathargaSedang)
    print ("Kategori Harga Mahal  : ",derajathargaMahal)

def derajatPorsi(porsi):

    global derajatporsiSedikit
    global derajatporsiBanyak
    global derajatporsiSangatBanyak


    derajatporsiSedikit = fungsiKeanggotaanTrapesium(min_porsiSedikit,min_porsiSedikit,251,max_porsiSedikit,porsi)
    derajatporsiBanyak = fungsiKeanggotaanTrapesium(min_porsiBanyak,250,501,max_porsiBanyak,porsi)
    derajatporsiSangatBanyak = fungsiKeanggotaanTrapesium(min_porsiSangatBanyak,500,1000,max_porsiSangatBanyak,porsi)
    
    print ("Kategori Porsi Sedikit       : ",derajatporsiSedikit)
    print ("Kategori Porsi Banyak        : ",derajatporsiBanyak)
    print ("Kategori Porsi Sangat Banyak : ",derajatporsiSangatBanyak)
    

def main():
 
    data = []
    n = int(input("Masukkan jumlah data : "))
 
    for i in range(1, n+1):
     
        harga = float(input("Masukkan Harga Makanan : "))
        porsi = float(input("Masukkan Porsi Makanan : "))
     
        print( "\n==========  PROSES FUZZYFICATION   ==========\n")
        print( "\n========== Derajat Keanggotaan Harga ==========\n")
        dHarga = derajatHarga(harga)
     
        print( "\n========== Derajat Keanggotaan Porsi ==========\n")
        dPorsi = derajatPorsi(porsi)
     
        print ("\n========== PROSES INTERFERENCES ==========\n")
        fuzzyRules(harga, porsi)
     
        print ("\n========== PROSES DEFUZZYFICATION ==========\n")
     
        DEFUZZYFICATION = centroidMethod(nilaiRekomendasiRendah,nilaiRekomendasiTinggi)
        print (DEFUZZYFICATION)
        DEFUZZY = data.append(DEFUZZYFICATION)
    
    print()
    print("Himpunan Nilai Rekomendasi: ",data)
    print("Makanan yang direkomendasikan memiliki nilai : ",max(data))
    # print(f"Rekomendasi: Makanan dengan harga Rp {int(harga)} dan porsi {int(porsi)} gram")

main()