no = 1
daftar_pilih = ['SHOW', 'INSERT', 'EDIT', 'DELATE']

print('-' * 25 + '\n  MENU DATA GEMERS  \n' + '-' * 25)

for daftar in daftar_pilih:
    print(f'{no}. {daftar} DATA')
    if no == 4:
        print('5. KELUAR PROGRAM')
    no += 1

list_nama = []
list_role = []
list_team = []

data = {'nama': list_nama,
        'role': list_role,
        'team': list_team}

# fungsi show data
def show_data():
    if len(data['nama']) == 0:
        print('Data masih kosong')
    else:
        for i in range(len(data['nama'])):
            print(str(i+1) + '. ' + data['nama'][i].ljust(15) + 'as: ' + data['role'][i].ljust(10) + 'team: ' + data['team'][i])

# fungsi insert data
def insert_data():
    nama = input('Masukkan nama anda: ')
    role = input('Masukkan role anda: ')
    team = input('Masukkan team anda: ')
    list_nama.append(nama)
    list_role.append(role)
    list_team.append(team)

# fungsi edit data
def edit_data():
    indeks = int(input('Masukkan nomor indeks yang diedit: '))
    if indeks < 0 or indeks > len(data['nama']):
        print('ID tidak ditemukan')
    else:
        nama_baru = input('Nama baru: ')
        role_baru = input('Role baru: ')
        team_baru = input('Team baru: ')
        list_nama[indeks-1] = nama_baru
        list_role[indeks-1] = role_baru
        list_team[indeks-1] = team_baru

# fungsi hapus data
def delete_data():
    indeks = int(input('Masukkan nomor indeks yang dihapus: '))
    if indeks < 0 or indeks > len(data['nama']):
        print('ID tidak ditemukan')
    else:
        del list_nama[indeks-1]
        del list_role[indeks-1]
        del list_team[indeks-1]

i = 0

while i == 0:
    menu = int(input('\nPILIH MENU> '))
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        print('Anda sudah keluar dari program\nSilahkan masuk kembali')
        exit()
    else:
        print('Masukkan angka yang ada pada list')
