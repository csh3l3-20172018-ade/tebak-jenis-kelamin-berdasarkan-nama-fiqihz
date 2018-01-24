def cowok(x): #sebuah fungsi untuk mengidentifikasi gender cowok atau bukan
    d = 0
    b = 0
    o = 0
    for i in range(len(x)): #pengulangan yang dilakukan sesuai dengan jumlah karakter yang terdapat pada nama yang di inputkan oleh user
        if i == ' ': break #pengkondisian dimana nama yang akan diperiksa hanya nama depan saja
        if 'b' == x[i]: #pengecekan jika didalam nama terdapat karakter 'b'
            b = b+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'd' == x[i]: #pengecekan jika didalam nama terdapat karakter 'd'
            d = d+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'o' == x[i]: #pengecekan jika didalam nama terdapat karakter 'o'
            o = o+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
    return(b,d,o)

def cewek(x): #sebuah fungsi untuk mengidentifikasi gender cewek atau bukan
    q = 0
    a = 0
    u = 0
    e = 0
    t = 0
    l = 0
    for i in range (len(x)): #pengulangan yang dilakukan sesuai dengan jumlah karakter yang terdapat pada nama yang di inputkan oleh user
        if i == ' ': break #pengkondisian dimana nama yang akan diperiksa hanya nama depan saja
        if 'i' == x[i]: #pengecekan jika didalam nama terdapat karakter 'i'
            q = q+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'a' == x[i]: #pengecekan jika didalam nama terdapat karakter 'a'
            a = a+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'u' == x[i]: #pengecekan jika didalam nama terdapat karakter 'u'
            u = u+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'e' == x[i]: #pengecekan jika didalam nama terdapat karakter 'e'
            e = e+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 't' == x[i]: #pengecekan jika didalam nama terdapat karakter 't'
            t = t+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
        if 'l' == x[i]: #pengecekan jika didalam nama terdapat karakter 'l'
            l = l+1 #penambahan 1 ketika karakter tersebut terdapat pada inputan nama yang dimasukkan oleh user
    return(q,a,u,e,t,l)


x=input('masukkan nama:')

if cewek(x) > cowok(x): #pengecekan jika nilai dari cewek lebih besar maka outputnya Cewek
    print('Cewek')
if cowok(x) > cewek(x): #pengecekan jika nilai dari cowok lebih besar maka outputnya Cowok
    print('Cowok')
if cowok(x) == cewek(x): #pengecekan jika nilai dari cewek dan cowok sama maka outputnya Tidak Diketahui
    print('Tidak diketahui')

  


