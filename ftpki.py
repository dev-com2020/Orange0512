import ftplib

# ftp = ftplib.FTP('test.rebex.net')
# logowanie = ftp.login('demo', 'password')
# print(logowanie)
# katalogi = ftp.nlst("/pub/example")
# print(katalogi)
# # x = ftp.retrbinary('RETR readme.txt', open('README2.TXT', 'wb').write)
# x = ftp.retrbinary('RETR /pub/example/imap-console-client.png', open('OBRAZEK.png', 'wb').write)

import requests
odp = requests.get('https://cdn.gamesnostalgia.com/files/l/c/lcq683594501v29204703183/harpoon_manual_amiga.7z')
with open("manual.7z","wb") as f:
    f.write(odp)
