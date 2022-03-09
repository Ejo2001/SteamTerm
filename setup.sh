#apt update
add-apt-repository multiverse
dpkg --add-architecture i386
apt update
apt install python3.9 python3-pip steamcmd -y
pip install psycopg2-binary
pip install requests
pip install sqlite3
pip install os
steamcmd +force_install_dir /etc/SteamGames +quit
