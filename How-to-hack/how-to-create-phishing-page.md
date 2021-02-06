-=-=-=-=-=-=LINUX=-=-=-=-=-=-

$ apt update
$ apt install git python3 zip unzip openssh-server php wget curl -y
$ cd
$ git clone https://github.com/htr-tech/zphisher
$ cd zphisher
$ bash zphisher.sh

-=-=-=-=-=-=TERMUX=-=-=-=-=-=-

$ pkg update -y
$ pkg install git python zip unzip openssh php wget curl -y
$ cd
$ git clone https://github.com/htr-tech/zphisher
$ git clone https://github.com/Marcel0Sousa/termux-ngrok
$ cd termux-ngrok
$ bash termux-ngrok.sh -y
$ cd ../zphisher
$ bash zphisher.sh


