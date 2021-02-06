-=-=-=-=-=-=LINUX=-=-=-=-=-=-

$ sudo apt update
$ sudo apt install git python3 python3-pip -y
$ cd
$ git clone https://github.com/maldevel/IPGeoLocation
$ cd IPGeoLocation
$ sudo pip3 install -r requirements.txt
$ python3 ipgeolocation.py --target IP

-=-=-=-=-=-=TERMUX=-=-=-=-=-=-

$ pkg update -y
$ pkg install git python
$ cd
$ git clone https://github.com/maldevel/IPGeoLocation
$ cd IPGeoLocation
$ pip3 install -r requirements.txt
$ python3 ipgeolocation.py --target IP
