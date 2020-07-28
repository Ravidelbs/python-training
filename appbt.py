from classfis import BesaranTurunan

# membuat instance pada class besaran turunan
obj = BesaranTurunan()

print('-'*50)
print('Aplikasi Besaran Turunan Fisika'.center(50))
print('-'*50)

# daftar besaran turunan
dbt = ['Luas', 'Volume', 'Massa Jenis', 'Kecepatan', 'Percepatan',
    'Gaya', 'Usaha', 'Daya', 'Tekanan', 'Momentum']

# daftar paremeter input
dpi = ['panjang, lebar', 'panjang, lebar, tinggi', 'massa, volume',
    'perpindahan, waktu', 'kecepatan, waktu', 'massa, percepatan',
    'gaya, perpindahan', 'usaha, waktu', 'gaya, luas', 'massa, kecepatan']

# menampilkan daftar list besaran turunan dan parameter inputnya
print('No.  ' + 'Besaran Turunan'.ljust(17) + 'Parameter Input'.ljust(29))
print('-'*50)

for i in range(len(dbt)):
    print('['+ str(i+1) +']  ' + dbt[i].ljust(17) + ':' + dpi[i].ljust(28))

print('-'*50)
print('Peraturan: ')
print('- Parameter yang akan dimasukkan berupa angka')
print('- Sebelum masuk besaran turuna lihat terlebih dahulu parameter input')
print('  yang diperlukan, jika parameternya belum terdefinisi maka pakailah')
print('  besaran turunan yang sesuai terlebih dahulu untuk mendapatkan parameternya')
print('- Untuk keluar dari program tekan 0 pada input daftar list')
print('\n')

while i != 0:
    i = int(input('Masukkan nomor daftar list: '))
    if i == 1:
        panjang = float(input('- Masukkan nilai panjang (m): '))
        lebar = float(input('- Masukkan nilai lebar (m): '))
        print(f'- Luas object tersebut adalah: {obj.Luas(panjang, lebar)} m^2')
        print('\n')
    elif i == 2:
        panjang = float(input('- Masukkan nilai panjang (m): '))
        lebar = float(input('- Masukkan nilai lebar (m): '))
        tinggi = float(input('- Masukkan nilai tinggi (m): '))
        print(f'- Volume object tersebut adalah: {obj.Volume(panjang, lebar, tinggi)} m^3')
        print('\n')
    elif i == 3:
        massa = float(input('- Masukkan nilai massa (kg): '))
        volume = float(input('- Masukkan nilai volume (m^3): '))
        print(f'- Massa Jenis object tersebut adalah: {obj.MassaJenis(massa, volume)} kg/m^3')
        print('\n')
    elif i == 4:
        perpindahan = float(input('- Masukkan nilai perpindahan (m): '))
        tinggi = float(input('- Masukkan nilai waktu (s): '))
        print(f'- Kecepatan object tersebut adalah: {obj.Kecepatan(perpindahan, tinggi)} m^2')
        print('\n')
    elif i == 5:
        kecepatan = float(input('- Masukkan nilai kecepatan (m/s): '))
        waktu = float(input('- Masukkan nilai waktu (s): '))
        print(f'- Percepatan object tersebut adalah: {obj.Percepatan(kecepatan, waktu)} m/s^2')
        print('\n')
    elif i == 6:
        massa = float(input('- Masukkan nilai massa (kg): '))
        percepatan = float(input('- Masukkan nilai percepatan (m/s^2): '))
        print(f'- Gaya object tersebut adalah: {obj.Gaya(massa, percepatan)} (kg m)/s^2')
        print('\n')
    elif i == 7:
        gaya = float(input('- Masukkan nilai gaya ((kg m)/s^2): '))
        perpindahan = float(input('- Masukkan nilai perpindahan (m): '))
        print(f'- Usaha object tersebut adalah: {obj.Usaha(gaya, perpindahan)} (kg m^2)/s^2')
        print('\n')
    elif i == 8:
        usaha = float(input('- Masukkan nilai usaha ((kg m^2)/s^2): '))
        waktu = float(input('- Masukkan nilai waktu (s): '))
        print(f'- Daya object tersebut adalah: {obj.Daya(usaha, waktu)} (kg m^2)/s^3')
        print('\n')
    elif i == 9:
        gaya = float(input('- Masukkan nilai gaya ((kg m)/s^2): '))
        luas = float(input('- Masukkan nilai luas (m^2): '))
        print(f'- Tekanan object tersebut adalah: {obj.Tekanan(gaya, luas)} N/m^2')
        print('\n')
    elif i == 10:
        massa = float(input('- Masukkan nilai massa (kg): '))
        kecepatan = float(input('- Masukkan nilai kecepatan (m/s): '))
        print(f'- Momentum object tersebut adalah: {obj.Momentum(massa, kecepatan)} (kg m)/s^2')
        print('\n')
    elif i == 0:
        print('Anda sudah keluar dari Program\nSilahkan run program kembali')
        exit()
    else:
        print('Silahkan masukkan nomor yang tertera pada daftar list diatas!')
        print('\n')
