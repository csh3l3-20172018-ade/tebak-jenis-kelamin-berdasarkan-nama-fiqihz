def cowok(x): #sebuah fungsi untuk mengidentifikasi gender cowok atau bukan
    d = 0
    b = 0
    o = 0
    for i in range(len(x)):
        if i == ' ': break
        if 'b' == x[i]:
            b = b+1
        if 'd' == x[i]:
            d = d+1
        if 'o' == x[i]:
            o = o+1
    return(b,d,o)

def cewek(x):
    q = 0
    a = 0
    u = 0
    e = 0
    t = 0
    l = 0
    for i in range (len(x)):
        if i == ' ': break
        if 'i' == x[i]:
            q = q+1
        if 'a' == x[i]:
            a = a+1
        if 'u' == x[i]:
            u = u+1
        if 'e' == x[i]:
            e = e+1
        if 't' == x[i]:
            t = t+1
        if 'l' == x[i]:
            l = l+1
    return(q,a,u,e,t,l)


x=input('masukkan nama:')

if cewek(x) > cowok(x):
    print('Cewek')
if cowok(x) > cewek(x):
    print('Cowok')
if cowok(x) == cewek(x):
    print('Tidak diketahui')



