nomer = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
tingkat = [["", "satu"], ["puluh", "sepuluh"], ["ratus", "seratus"], ["ribu", "seribu"], ["juta", "sejuta"]]
belasan = [[11, 12, 13, 14, 15, 16, 17, 18, 19], ["sebelas", "belas Dua", "belas tiga", "belas empat", "belas lima", "belas enam", "belas tujuh", "belas delapan", "belas sembilan"]]
angka = input().strip()
hasil = ""
patokanAkhir = len(angka) - 1
ribuan = True
while patokanAkhir >= 0 :
    patokanAwal = 0
    if int(angka[patokanAkhir - 1] + angka[patokanAkhir]) in belasan[0] and len(angka) > 1:
        hasil = hasil + " " + belasan[1][belasan[0].index(int(angka[patokanAkhir - 1] + angka[patokanAkhir]))]
        patokanAkhir -= 2
    pembatas = 3 if len(angka) % 3 == 1 else 2
    while patokanAkhir >= 0 and pembatas >= 0 :
        if angka[patokanAkhir] != "0" :
            kondisi_1 = " " + nomer[int(angka[patokanAkhir]) - 1] + " " if angka[patokanAkhir] != "1" else ""
            kondisi_2 = 0 if angka[patokanAkhir] != "1" else 1
            hasil += " " + tingkat[patokanAwal][kondisi_2] + kondisi_1
        patokanAkhir -= 1
        patokanAwal += 1
        pembatas -= 1
    if ribuan == True and patokanAwal > 2  and "se" not in hasil and "ribu" not in hasil:
        hasil = hasil + " ribu"
        ribuan == False
#print("=" * 15 + " Selesai " + 15 * "=")
hasilList = hasil.split()
hasil = ""
jarak = len(hasilList) - 1
while jarak >= 0 :
    hasil += hasilList[jarak] + " "
    jarak -= 1
print(hasil)