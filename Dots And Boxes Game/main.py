"""import sys
sys.stdin = open('3e4.txt','r',encoding='utf-8')"""

sutun = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

hatali_giris = True
while hatali_giris == True:
    try:
        yatay_cizgi_say = int(input('Yatay çizgi sayısını gir [3-7]: \n'))
        if 3 <= yatay_cizgi_say <= 7:
            hatali_giris = False
        else:
            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
    except ValueError:
        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

tas_sayisi = int(yatay_cizgi_say * (yatay_cizgi_say + 1))
beyaz_tas_sayisi, siyah_tas_sayisi = int(tas_sayisi/2), int(tas_sayisi/2)

def tablo_ciz(cizgi_say,sutun,liste={}):

    for i in range(cizgi_say):
        print(f"  {sutun[i]} ",end='')
    print(f"  {sutun[cizgi_say]}")

    if len(liste) == 0:
        for i in range(1,cizgi_say):
            print(f"{i}  ",end='')
            print('--- '*(cizgi_say),end='')
            print(f" {i}")
            print('  | '*cizgi_say,end='')
            print('  |')

        print(f"{cizgi_say} ", end='')
        print(' ---'*(cizgi_say),end='')
        print(f"  {cizgi_say}")

    else:
        for i in range(1,cizgi_say):
            print(f"{i} ",end='')
            print(("{}---"*(cizgi_say)).format(tas_konumlari[str(i) + sutun[0]], tas_konumlari[str(i) + sutun[1]], tas_konumlari[str(i) + sutun[2]], tas_konumlari[str(i) + sutun[3]], tas_konumlari[str(i) + sutun[4]], tas_konumlari[str(i) + sutun[5]], tas_konumlari[str(i) + sutun[6]]), end='')
            print("{} {}".format(tas_konumlari[str(i) + sutun[cizgi_say]], i))
            print('  | ' * cizgi_say, end='')
            print('  |')

        print(f"{cizgi_say} ",end='')
        print(("{}---"*(cizgi_say)).format(tas_konumlari[str(cizgi_say) + sutun[0]], tas_konumlari[str(cizgi_say) + sutun[1]], tas_konumlari[str(cizgi_say) + sutun[2]], tas_konumlari[str(cizgi_say) + sutun[3]], tas_konumlari[str(cizgi_say) + sutun[4]], tas_konumlari[str(cizgi_say) + sutun[5]], tas_konumlari[str(cizgi_say) + sutun[6]]), end='')
        print("{} {}".format(tas_konumlari[str(cizgi_say) + sutun[cizgi_say]], cizgi_say))

    for i in range(cizgi_say):
        print(f"  {sutun[i]} ",end='')
    print(f"  {sutun[cizgi_say]}")


def kare_sayisi_bul(cizgi_say,sutun,liste):
    beyaz_kare_sayisi = 0
    siyah_kare_sayisi = 0
    silinemeyecek_taslar = []

    for i in range(1,cizgi_say):
        ic_liste = []
        for j in range(cizgi_say):
            ic_liste.append(liste[str(i)+sutun[j]])
            ic_liste.append(liste[str(i)+sutun[j+1]])
            ic_liste.append(liste[str(i+1)+sutun[j]])
            ic_liste.append(liste[str(i+1)+sutun[j+1]])

            if ic_liste.count('B') == 4:
                beyaz_kare_sayisi += 1
                silinemeyecek_taslar.append(str(i)+sutun[j])
                silinemeyecek_taslar.append(str(i)+sutun[j+1])
                silinemeyecek_taslar.append(str(i+1)+sutun[j])
                silinemeyecek_taslar.append(str(i+1)+sutun[j+1])
            elif ic_liste.count('S') == 4:
                siyah_kare_sayisi += 1
                silinemeyecek_taslar.append(str(i) + sutun[j])
                silinemeyecek_taslar.append(str(i) + sutun[j + 1])
                silinemeyecek_taslar.append(str(i + 1) + sutun[j])
                silinemeyecek_taslar.append(str(i + 1) + sutun[j + 1])

            ic_liste.clear()

    return beyaz_kare_sayisi,siyah_kare_sayisi,silinemeyecek_taslar

tablo_ciz(yatay_cizgi_say,sutun)
print('-'*50)

tas_konumlari = {'1A':' ','1B':' ','1C':' ','1D':' ','1E':' ','1F':' ','1G':' ','1H':' ',
                 '2A':' ','2B':' ','2C':' ','2D':' ','2E':' ','2F':' ','2G':' ','2H':' ',
                 '3A':' ','3B':' ','3C':' ','3D':' ','3E':' ','3F':' ','3G':' ','3H':' ',
                 '4A':' ','4B':' ','4C':' ','4D':' ','4E':' ','4F':' ','4G':' ','4H':' ',
                 '5A':' ','5B':' ','5C':' ','5D':' ','5E':' ','5F':' ','5G':' ','5H':' ',
                 '6A':' ','6B':' ','6C':' ','6D':' ','6E':' ','6F':' ','6G':' ','6H':' ',
                 '7A':' ','7B':' ','7C':' ','7D':' ','7E':' ','7F':' ','7G':' ','7H':' ',}

while tas_sayisi != 0:
    if tas_sayisi %2 == 0:
        renk = 'Beyaz'
    else:
        renk = 'Siyah'

    sutun_kontrol = []
    for i in range(yatay_cizgi_say+1):
        sutun_kontrol.append(sutun[i])

    hata = True
    while hata:
        try:
            tas_dizme = input(f'Oyuncu {renk} taşınızı hangi konuma koymak istersiniz: \n')

            if len(tas_dizme) < 2:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            elif (1 <= int(tas_dizme[0]) <= yatay_cizgi_say) and (tas_dizme[1] in sutun_kontrol) and (len(tas_dizme) == 2):
                hata = False
            else:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        except ValueError:
            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

    tas_konumlari[tas_dizme] = renk[0]
    tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
    tas_sayisi -= 1

beyaz_kare_sayisi, siyah_kare_sayisi, silinemeyecek_tas_konumlari = kare_sayisi_bul(yatay_cizgi_say, sutun, tas_konumlari)

if (beyaz_kare_sayisi + siyah_kare_sayisi) == 0:
    hata = True
    while hata:
        try:
            silinecek_rakip_tas = input('2 oyuncuda kare oluşturamadağı için beyaz oyuncu bir rakip taş silecek: \n')

            if len(silinecek_rakip_tas) < 2:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            elif (1 <= int(silinecek_rakip_tas[0]) <= yatay_cizgi_say) and (
                    silinecek_rakip_tas[1] in sutun_kontrol) and (len(silinecek_rakip_tas) == 2):
                hata = False
            else:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        except ValueError:
            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

    while tas_konumlari[silinecek_rakip_tas] == 'B':
        try:
            silinecek_rakip_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

            if len(silinecek_rakip_tas) < 2:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            elif (1 <= int(silinecek_rakip_tas[0]) <= yatay_cizgi_say) and (
                    silinecek_rakip_tas[1] in sutun_kontrol) and (len(silinecek_rakip_tas) == 2):
                hata = False
            else:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        except ValueError:
            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
    else:
        tas_konumlari[silinecek_rakip_tas] = ' '
        tablo_ciz(yatay_cizgi_say, tas_konumlari)
        siyah_tas_sayisi -= 1

else:
    toplam_silinecek_tas_say = beyaz_kare_sayisi + siyah_kare_sayisi
    for i in [beyaz_kare_sayisi, siyah_kare_sayisi]:
        for j in range(i):
            if 0 < toplam_silinecek_tas_say <= siyah_kare_sayisi:
                oyuncu = 'Siyah'
            else:
                oyuncu = 'Beyaz'

            hata = True
            while hata:
                try:
                    silinecek_rakip_tas = input('Silinecek rakip taş konumunu gir: \n')

                    if len(silinecek_rakip_tas) < 2:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    elif (1 <= int(silinecek_rakip_tas[0]) <= yatay_cizgi_say) and (
                            silinecek_rakip_tas[1] in sutun_kontrol) and (len(silinecek_rakip_tas) == 2):
                        hata = False
                    else:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                except ValueError:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

            while tas_konumlari[silinecek_rakip_tas] == oyuncu[0]:
                try:
                    silinecek_rakip_tas = input('Kendi taşınızı silemezsiniz. Lütfen geçerli bir konum giriniz: \n')

                    if len(silinecek_rakip_tas) < 2:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    elif (1 <= int(silinecek_rakip_tas[0]) <= yatay_cizgi_say) and (
                            silinecek_rakip_tas[1] in sutun_kontrol) and (len(silinecek_rakip_tas) == 2):
                        hata = False
                    else:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                except ValueError:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

            while silinecek_rakip_tas in silinemeyecek_tas_konumlari:
                try:
                    silinecek_rakip_tas = input(
                        'UYARI !!! Kare oluşturan bir taşı alamazsınız. Silinecek rakip taş konumunu gir: \n')

                    if len(silinecek_rakip_tas) < 2:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    elif (1 <= int(silinecek_rakip_tas[0]) <= yatay_cizgi_say) and (
                            silinecek_rakip_tas[1] in sutun_kontrol) and (len(silinecek_rakip_tas) == 2):
                        hata = False
                    else:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                except ValueError:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

            else:
                if tas_konumlari[silinecek_rakip_tas] == 'S':
                    siyah_tas_sayisi -= 1
                    toplam_silinecek_tas_say -= 1
                elif tas_konumlari[silinecek_rakip_tas] == 'B':
                    beyaz_tas_sayisi -= 1
                    toplam_silinecek_tas_say -= 1

                tas_konumlari[silinecek_rakip_tas] = ' '

            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)

sayac = 0

while (beyaz_tas_sayisi > 3) and (siyah_tas_sayisi > 3):
    if sayac %2 == 0:
        oyuncu = 'Beyaz'
    else:
        oyuncu = 'Siyah'
    sayac += 1

    hata = True
    while hata:
        try:
            tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Lütfen hareket ettirmek istediğiniz taşın mevcut konumu ve gitmesini istediğiniz konumu girin: \n')

            if len(tasinacak_tasin_konumlari) < 5:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                hata = False
            else:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        except ValueError:
            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
    a = tasinacak_tasin_konumlari.split()
    eski_konum = a[0]
    yeni_konum = a[1]

    while tas_konumlari[eski_konum] == ' ':
        hata = True
        while hata:
            try:
                tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Seçtiğiniz konumda taş yok. Lütfen geçerli konum giriniz: \n')
                if len(tasinacak_tasin_konumlari) < 5:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                    hata = False
                else:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            except ValueError:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        a = tasinacak_tasin_konumlari.split()
        eski_konum = a[0]
        yeni_konum = a[1]

    while tas_konumlari[eski_konum] != oyuncu[0]:
        hata = True
        while hata:
            try:
                tasinacak_tasin_konumlari = input('Girdiğiniz konumda rakip taşı bulunmaktadır. Lütfen kendi taşınızın konumunu giriniz: \n')
                if len(tasinacak_tasin_konumlari) < 5:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                    hata = False
                else:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            except ValueError:
                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
        a = tasinacak_tasin_konumlari.split()
        eski_konum = a[0]
        yeni_konum = a[1]

    gidebilir_mi = False

    while gidebilir_mi == False:
        if eski_konum[0] == yeni_konum[0]:
            aradaki_nokta_say = sutun.index(yeni_konum[1]) - sutun.index(eski_konum[1])

            if aradaki_nokta_say < 0:
                aradaki_nokta_say = -aradaki_nokta_say

            gidebilir_mi = True
            for i in range(aradaki_nokta_say):
                if sutun.index(yeni_konum[1]) - sutun.index(eski_konum[1]) > 0:
                    i = -i

                if tas_konumlari[yeni_konum[0] + sutun[(sutun.index(yeni_konum[1]) + i)]] != ' ':
                    gidebilir_mi = False

            if gidebilir_mi:
                tas_konumlari[yeni_konum] = tas_konumlari[eski_konum]

                if eski_konum in silinemeyecek_tas_konumlari:
                    tas_konumlari[eski_konum] = ' '
                    tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                    yeni_beyaz_kare_sayisi, yeni_siyah_kare_sayisi, silinemeyecek_tas_konumlari = kare_sayisi_bul(yatay_cizgi_say, sutun, tas_konumlari)

                    if (yeni_beyaz_kare_sayisi >= beyaz_kare_sayisi) and (tas_konumlari[yeni_konum] == 'B'):
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'B':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            siyah_tas_sayisi -= 1

                    elif yeni_beyaz_kare_sayisi < beyaz_kare_sayisi:
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi

                    if (yeni_siyah_kare_sayisi >= siyah_kare_sayisi) and (tas_konumlari[yeni_konum] == 'S'):
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'S':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            siyah_tas_sayisi -= 1

                    elif yeni_siyah_kare_sayisi < siyah_kare_sayisi:
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi

                else:
                    tas_konumlari[eski_konum] = ' '
                    tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                    yeni_beyaz_kare_sayisi, yeni_siyah_kare_sayisi, silinemeyecek_tas_konumlari = kare_sayisi_bul(yatay_cizgi_say, sutun, tas_konumlari)

                    if yeni_beyaz_kare_sayisi > beyaz_kare_sayisi:
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'B':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            siyah_tas_sayisi -= 1

                    elif yeni_beyaz_kare_sayisi <= beyaz_kare_sayisi:
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi

                    if yeni_siyah_kare_sayisi > siyah_kare_sayisi:
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi

                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'S':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            beyaz_tas_sayisi -= 1

                    elif yeni_siyah_kare_sayisi <= siyah_kare_sayisi:
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi

            else:
                hata = True
                while hata:
                    try:
                        tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Lütfen hareket ettirmek istediğiniz taşın mevcut konumu ve gitmesini istediğiniz konumu girin: \n')

                        if len(tasinacak_tasin_konumlari) < 5:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                            hata = False
                        else:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    except ValueError:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                a = tasinacak_tasin_konumlari.split()
                eski_konum = a[0]
                yeni_konum = a[1]

                while tas_konumlari[eski_konum] == ' ':
                    hata = True
                    while hata:
                        try:
                            tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Seçtiğiniz konumda taş yok. Lütfen geçerli konum giriniz: \n')
                            if len(tasinacak_tasin_konumlari) < 5:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                                hata = False
                            else:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        except ValueError:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    a = tasinacak_tasin_konumlari.split()
                    eski_konum = a[0]
                    yeni_konum = a[1]

                while tas_konumlari[eski_konum] != oyuncu[0]:
                    hata = True
                    while hata:
                        try:
                            tasinacak_tasin_konumlari = input('Girdiğiniz konumda rakip taşı bulunmaktadır. Lütfen kendi taşınızın konumunu giriniz: \n')
                            if len(tasinacak_tasin_konumlari) < 5:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                                hata = False
                            else:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        except ValueError:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    a = tasinacak_tasin_konumlari.split()
                    eski_konum = a[0]
                    yeni_konum = a[1]

        elif eski_konum[1] == yeni_konum[1]:
            aradaki_nokta_say = int(yeni_konum[0]) - int(eski_konum[0])

            if aradaki_nokta_say < 0:
                aradaki_nokta_say = -aradaki_nokta_say

            gidebilir_mi = True
            for i in range(aradaki_nokta_say):
                if (int(yeni_konum[0]) - int(eski_konum[0])) > 0:
                    i = -i

                if tas_konumlari[str(int(yeni_konum[0]) + i) + yeni_konum[1]] != ' ':
                    gidebilir_mi = False

            if gidebilir_mi:
                tas_konumlari[yeni_konum] = tas_konumlari[eski_konum]

                if eski_konum in silinemeyecek_tas_konumlari:
                    tas_konumlari[eski_konum] = ' '
                    tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                    yeni_beyaz_kare_sayisi, yeni_siyah_kare_sayisi, silinemeyecek_tas_konumlari = kare_sayisi_bul(yatay_cizgi_say, sutun, tas_konumlari)

                    if (yeni_beyaz_kare_sayisi >= beyaz_kare_sayisi) and (tas_konumlari[yeni_konum] == 'B'):
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'B':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            siyah_tas_sayisi -= 1

                    elif yeni_beyaz_kare_sayisi < beyaz_kare_sayisi:
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi

                    if (yeni_siyah_kare_sayisi >= siyah_kare_sayisi) and (tas_konumlari[yeni_konum] == 'S'):
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'S':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            beyaz_tas_sayisi -= 1

                    elif yeni_siyah_kare_sayisi < siyah_kare_sayisi:
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi

                else:
                    tas_konumlari[eski_konum] = ' '
                    tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                    yeni_beyaz_kare_sayisi, yeni_siyah_kare_sayisi, silinemeyecek_tas_konumlari = kare_sayisi_bul(yatay_cizgi_say, sutun, tas_konumlari)

                    if (yeni_beyaz_kare_sayisi > beyaz_kare_sayisi) and (tas_konumlari[yeni_konum] == 'B'):
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'B':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            siyah_tas_sayisi -= 1

                    elif yeni_beyaz_kare_sayisi <= beyaz_kare_sayisi:
                        beyaz_kare_sayisi = yeni_beyaz_kare_sayisi

                    if (yeni_siyah_kare_sayisi > siyah_kare_sayisi) and (tas_konumlari[yeni_konum] == 'S'):
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi
                        hata = True
                        while hata:
                            try:
                                silinecek_tas = input('Tebrikler kare oluşturdunuz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                if len(silinecek_tas) < 2:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                    hata = False
                                else:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            except ValueError:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == ' ':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz konumda taş bulunmamaktadır. Lütfen geçerli bir konum giriniz: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while tas_konumlari[silinecek_tas] == 'S':
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Kendi taşınızı silemezsiniz. Lütfen silmek istediğiniz rakip taşını gir: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')

                        while silinecek_tas in silinemeyecek_tas_konumlari:
                            hata = True
                            while hata:
                                try:
                                    silinecek_tas = input('Seçtiğiniz taş rakip karesi oluşturuyor. Lütfen geçerli bir taş girin: \n')

                                    if len(silinecek_tas) < 2:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                    elif (1 <= int(silinecek_tas[0]) <= yatay_cizgi_say) and (silinecek_tas[1] in sutun_kontrol) and (len(silinecek_tas) == 2):
                                        hata = False
                                    else:
                                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                                except ValueError:
                                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        else:
                            tas_konumlari[silinecek_tas] = ' '
                            tablo_ciz(yatay_cizgi_say, sutun, tas_konumlari)
                            beyaz_tas_sayisi -= 1

                    elif yeni_siyah_kare_sayisi <= siyah_kare_sayisi:
                        siyah_kare_sayisi = yeni_siyah_kare_sayisi

            else:
                hata = True
                while hata:
                    try:
                        tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Lütfen hareket ettirmek istediğiniz taşın mevcut konumu ve gitmesini istediğiniz konumu girin: \n')

                        if len(tasinacak_tasin_konumlari) < 5:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                            hata = False
                        else:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    except ValueError:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                a = tasinacak_tasin_konumlari.split()
                eski_konum = a[0]
                yeni_konum = a[1]

                while tas_konumlari[eski_konum] == ' ':
                    hata = True
                    while hata:
                        try:
                            tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Seçtiğiniz konumda taş yok. Lütfen geçerli konum giriniz: \n')
                            if len(tasinacak_tasin_konumlari) < 5:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                                hata = False
                            else:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        except ValueError:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    a = tasinacak_tasin_konumlari.split()
                    eski_konum = a[0]
                    yeni_konum = a[1]

                while tas_konumlari[eski_konum] != oyuncu[0]:
                    hata = True
                    while hata:
                        try:
                            tasinacak_tasin_konumlari = input('Girdiğiniz konumda rakip taşı bulunmaktadır. Lütfen kendi taşınızın konumunu giriniz: \n')
                            if len(tasinacak_tasin_konumlari) < 5:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                            elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                                hata = False
                            else:
                                print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        except ValueError:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    a = tasinacak_tasin_konumlari.split()
                    eski_konum = a[0]
                    yeni_konum = a[1]

        else:
            hata = True
            while hata:
                try:
                    tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Lütfen hareket ettirmek istediğiniz taşın mevcut konumu ve gitmesini istediğiniz konumu girin: \n')

                    if len(tasinacak_tasin_konumlari) < 5:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                        hata = False
                    else:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                except ValueError:
                    print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
            a = tasinacak_tasin_konumlari.split()
            eski_konum = a[0]
            yeni_konum = a[1]

            while tas_konumlari[eski_konum] == ' ':
                hata = True
                while hata:
                    try:
                        tasinacak_tasin_konumlari = input(f'Oyuncu: {oyuncu}. Seçtiğiniz konumda taş yok. Lütfen geçerli konum giriniz: \n')
                        if len(tasinacak_tasin_konumlari) < 5:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                            hata = False
                        else:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    except ValueError:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                a = tasinacak_tasin_konumlari.split()
                eski_konum = a[0]
                yeni_konum = a[1]

            while tas_konumlari[eski_konum] != oyuncu[0]:
                hata = True
                while hata:
                    try:
                        tasinacak_tasin_konumlari = input('Girdiğiniz konumda rakip taşı bulunmaktadır. Lütfen kendi taşınızın konumunu giriniz: \n')
                        if len(tasinacak_tasin_konumlari) < 5:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                        elif (1 <= int(tasinacak_tasin_konumlari[0]) <= yatay_cizgi_say) and (tasinacak_tasin_konumlari[1] in sutun_kontrol) and (len(tasinacak_tasin_konumlari) == 5):
                            hata = False
                        else:
                            print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                    except ValueError:
                        print('Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.')
                a = tasinacak_tasin_konumlari.split()
                eski_konum = a[0]
                yeni_konum = a[1]


if beyaz_tas_sayisi == 3:
    print(f'Tebrikler oyuncu: {oyuncu} kazandı')
elif siyah_tas_sayisi == 3:
    print(f'Tebrikler oyuncu: {oyuncu} kazandı')
