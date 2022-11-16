import os,sys
os.system('clear')
print('''\33[1;32m                    
██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
''')
print('''\033[1;32m

                         
                            [  NAYZK  ]
Telegram : @NAYZK17                           
                           [  WELCOME  ]

                                                    

''')
print('\033[1;32m[1] >> install pkg [Termux ~ kali]')

print('\033[1;32m~~~')
print('\033[1;33m[2] >> install nethunter')

print('\033[1;33m~~~')

print('\33[1;34m[3] >> install  BackBox ')

print('\033[1;34m~~~')
print('\033[1;31m[4] >> install metasploit [ 1 ]')

print('\033[1;31m~~~')
print('\033[1;33m[5] >> install metasploit [ 2 ] ')

print('\033[1;33m~~~')
print('\033[1;34m[6] >> install xersploit')

print('\033[1;34m~~~')
print('\033[1;31m[7] >> install nikto')

print('\033[1;31m~~~')
print('\033[1;32m[8] >> install nmap')

print('\033[1;32m~~~')
print('\033[1;34m[9] >> install FREE-PROXY [ proxy ]')

print('\033[134m~~~')
print('\033[1;35m[10] >> install AndroRAT')

print('\033[;135m~~~')
print('\033[1;36m[11] >> install ROOT [ ubuntu ]')

print('\033[1;36m~~~')
print('\033[1;31m[12] >> install ROOT [ fish ]')

print('\033[1;31m~~~')
print('\033[1;32m[13] >> install sqlmap')

print('\033[1;32m~~~')
print('\033[1;36m[14] >> install botnet')

print('\033[1;36m~~~')
print('\033[1;33m[15] >> install Evil-Droid')
print('\033[1;33m~~~')
print('\033[1;36m[16] >> install Tmvenom ')
print('\033[1;36m~~~')
print('\033[1;34m[17] >> install tor')
print('\033[1;34m~~~')

print('\033[1;33m[00] >> exit')
print('\033[1;33m~~~')
print('\033[1;31m_'*20)
print('''''')
n = input('\033[1;36m ○~~> :  ')
if n == '1':
	os.system('clear')
	print('\033[1;33m                plase wait        ')
	os.system('termux-setup-storage;cd;dpkg --configure -a;pkg update -y;pkg upgrade -y;pkg install python -y;pkg install python2 -y;pkg install python2-dev -y;pkg install python3 -y;pkg install pip -y;pkg install pip2;pip2 install requests;pkg install fish -y;pkg install ruby -y;pkg install git -y;pkg install dnsutils -y;pkg install php -y;pkg install perl -y;pkg install nmap -y;pkg install bash -y;pkg install clang -y;pkg install nano -y;pkg install w3m -y;pkg install figlet -y;pkg install cowsay -y;gem install lolcat;pkg install curl -y;pkg install tar -y;pkg install zip -y;pkg install unzip -y;pkg install tor -y;pkg install wget -y;pkg install wgetrc -y;pkg install wcalc -y;pkg install bmon -y;pkg install unrar -y;pkg install toilet -y;pkg install proot -y;pkg install golang -y;pkg install chroot -y;termux-chroot -y;pkg install openssl -y;pkg install cmatrix -y;pkg install openssh -y;apt update && apt upgrade -y')
	os.system('python3 install.py')
elif n == '2':
	os.system('clear')
	os.system('pkg install wget -y')
	os.system('wget -O install-nethunter-termux https://offs.ec/2MceZWr')
	os.system('chmod +x install-nethunter-termux')
	os.system('./install-nethunter-termux')
	os.system('clear')
	print('\033[1;34mDo you want run nethunter')
	nt = input('\033[1;33m[ n / y ] :  ')
	if nt == 'y':
		os.system('clear')
		print('''\033[1;33m
[1] VNC
		
[2] Termux
		''')
		nh = input('\033[1;31mEnter number :  ')
		if nh == '1':
			os.system('nh kex passwd')
		else:
			os.system('nh')
	if nt == 'n':
		os.system('python3 install.py')
elif n == '3':
	os.system('clear')
	os.system('pkg install wget openssl-tool proot -y')
	os.system('hash -r')
	os.system('wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh')
	os.system('bash backbox.sh')
	os.system('wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh')
	os.system('bash de-apt-xfce4.sh')
	os.system('python3 install.py')
elif n == '4':
	os.system('clear')
	os.system('pkg install wget')
	os.system('pkg install perl')
	os.system('pkg install ruby')
	os.system('pkg install proot')
	os.system('pkg install pip')
	os.system('clear')
	os.system('gem install resolved')
	os.system('wget clone https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh')
	os.system('chmod +x metasploit.sh')
	os.system('./metasploit.sh ')
	os.system('clear')
	print('Do you want run metasploit')
	ow = input('[ n / y ]》:  ')
	if ow == 'y':
		os.system('clear')
		print('\033[1;33mplase wait')
		os.system('msfconsole')
	if ow == 'n':
		os.system('python3 install.py')
elif n == '5':
	os.system('clear')
	os.system('curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
	os.system('chmod +x metasploit.sh')
	os.system('bash metasploit.sh')
	os.system('cd metaaploit-framework')
	os.system('bundle install rake-12.3.1')
	os.system('bundle config')
	os.system('build.nokogiri--use-system--libraries')
	os.system('gem install nokogiri')
	os.system('gem install pkg-config -v rake-12.3.1')
	os.system('bundle install rake-12.3.1')
	os.system('clear')
	print('Do you want run metasploit')
	ob = input('\033[1;31m[ n / y ]》》 :  ')
	if ob == 'y':
		os.system('clear')
		print('\033[1;36mplase wait')
		os.system('msfconsole')
	if ob == 'n':
		os.system('python3 install.py')
elif n == '6':
	os.system('clear')
	os.system('pkg install git')
	os.system('git clone https://github.com/LionSec/xerosploit')
	os.system('cd xerosploit')
	os.system('sudo python install.py')
	os.system('clear')
	print('\033[1;34mDo you want run  xerosploit')
	ak = input('\033[1;36m[ n / y ]》:  ')
	if ak == 'y':
		os.system('sudo xerosploit')
	if ak == 'n':
		os.system('python3 install.py')
elif n == '7':
	os.system('clear')
	os.system('pkg install git')
	os.system('pkg install wget')
	os.system('pkg install perl')
	os.system('git clone https://github.com/sullo/nikto')
	os.system('cd program')
	os.system('perl nikto.pl')
	os.system('clear')
	print('\033[1;32mDo you want to check a site')
	sb = input('\033[1;35m[ n / y ]》 :  ')
	if sb == 'y':
		os.system('clear')
		iv = input('Enter web :  ')
		os.system('perl nikto.pl -h '+iv)
	if sb == 'n':
		os.system('python3 install.py')
elif n == '8':
	os.system('clear')
	os.system('pkg install nmap')
	os.system('clear')
	print('\033[1;31mDo you want scan')
	ox = input('\033[1;34m[ n / y ]>》:  ')
	if ox == 'y':
		os.system('clear')
		print('''\033[1;36m
[1] nmap <Target>
		
[2] nmap -V <Target>
		
[3] nmap -sV <Target>
		
[4] nmap -sS -sV <Target>

[5] nmap -sS <Target>
		
		''')
		up = input('\033[1;35m○~~> @  ')
		if up == '1':
			os.system('clear')
			ib = input('\033[1;32mEnter Target @  ')
			os.system('nmap '+ib)
		if up == '2':
			os.system('clear')
			mc = input('\033[1;33mEnter Target @  ')
			os.system('nmap -V '+mc)
		if up == '3':
			os.system('clear')
			jg = input('\033[1;31mEnter Target @  ')
			os.system('nmap -sV '+jg)
		if up == '4':
			os.system('clear')
			ad = input('\033[1;36mEnter Target @  ')
			os.system('nmap -sS -sV '+ad)
		if up == '5':
			os.system('clear')
			iz = input('\033[1;34mEnter Target @  ')
			os.system('nmap -sS '+iz)
elif n == '9':
	os.system('clear')
	os.system('pkg install git')
	os.system('git clone https://github.com/mishakorzik/Free-Proxy')
	os.system('cd Free-Proxy')
	os.system('bash Setup.sh')
	os.system('clear')
	print('\033[1;35mDo you want run Free-Proxy')
	kt = input('[ n / y ]>~》@  ')
	if kt == 'y':
		os.system('clear')
		os.system('bash Free-Proxy.sh')
	if kt == 'n':
		os.system('python3 install.py')
if n == '10':
	os.system('clear')
	os.system('pkg install git')
	os.system('pkg install pip')
	os.system('git clone https://github.com/karma9874/AndroRAT.git')
	os.system('cd AndroRAT')
	os.system('apt install openjdk-17')
	os.system('pip install -r requirements.txt')
	os.system('clear')
	print('\033[1;33mDo you want run AndroRAT')
	ox = input('\033[1;36m[ n / y ] >》¤  ')
	if ox == 'y':
		os.system('python3 androRAT.py')
	if ox == 'n':
		os.system('python3 install.py')
elif n == '11':
	os.system('clear')
	os.system('pkg instsll proot')
	os.system('proot-distro install ubuntu')
	os.system('clear')
	print('\033[1;33mDo you want run root')
	tt = input('\033[1;33m[ n / y ]>》¤  ')
	if tt == 'y':
		os.system('clear')
		os.system('proot-distro login ubuntu')
	if tt == 'n':
		os.system('python3 install.py')
if n == '12':
	os.system('clear')
	os.system('git clone https://github.com/adarshaddee/root.git')
	os.system('cd root')
	os.system('chmod +x main')	
	os.system('./main')
	os.system('clear')
	print('\033[1;31mDo want you run root')
	vz = input('[ n / y ]>》☆  ')
	if vz == 'y':
		os.system('clear')
		os.system('fakeroot')
		os.system('fish')
	if vz == 'n':
		os.system('python3 install.py')
elif n == '13':
	os.system('clear')
	os.system('pkg install git')
	os.system('git clone https://github.com/sqlmapproject/sqlmap.git')
	os.system('clear')
	print('\033[1;33mDo you want run sqlmap')
	gob = input('\033[1;34m[ n / y ] >》@  ')
	if gob == 'y':
		os.system('clear')
		kom = input('\033[1;32mEnter web @  ')
		os.system('cd sqlmap')
		os.system('python2 sqlmap.py -h')
		os.system('python2 sqlmap.py -u '+kom+' --dbs')
	if gob == 'n':
		os.system('python3 install.py')
if n == '14':
	os.system('clear')
	os.system('git clone https://github.com/epsylon/ufonet.git')
	os.system('python3 install.py')
if n == '15':
	os.system('clear')
	os.system('pkg install git')
	os.system('clear')
	os.system('git clone https://github.com/M4sc3r4n0/Evil-Droid.git')
	os.system('clear')
	print('\033[1;32mDo you want run Evil-Droid')
	name = input('\033[1;33m[ n / y ]>》@  ')
	if name == 'y':
		os.system('clear')
		os.system('cd Evil-Droid')
		os.system('chmod +x evil-droid')
		os.system('clear')
		os.system('sudo ./evil-droid')
	if name == 'n':
		os.system('python3 install.py')
elif n == '16':
	os.system('clear')
	os.system('pkg isntall git')
	os.system('clear')
	os.system('pkg install git')
	os.system('pkg install python2')
	os.system('git clone https://github.com/TechnicalMujeeb/tmvenom.git')
	os.system('cd tmvenom')
	os.system('chmod +x *')
	os.system('sh install.sh')
	os.system('clear')
	print('\033[1;32mDo you want run Tmvenom')
	sbo = input('\033[1;34m[ n / y ]>》@  ')
	if sbo == 'y':
		os.system('clear')
		os.system('python2 tmvenom.py')
	if sbo == 'n':
		os.system('python3 install.py')
if n == '17':
	os.system('clear')
	os.system('pkg install tor')
	os.system('clear')
	print('\033}1;36mDo you want run tor')
	qov = input('\033[1;31m[ n / y ]>》@  ')
	if qov == 'y':
		os.system('clear')
		os.system('tor')
	if qov == 'n':
		os.system('python3 install.py')
if n == '00':
	os.system('clear')
	os.system('cd')