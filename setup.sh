#apt update
add-apt-repository multiverse
dpkg --add-architecture i386
apt update
apt install python3.9 python3-pip steamcmd -y
pip install -r requirements.txt
/usr/games/steamcmd +force_install_dir /etc/SteamGames +quit
echo "SET UP AND READY!"
