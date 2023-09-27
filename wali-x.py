#Github ~ github.com/kunalmannu
#Made By KunalMannu
#If You Copy Give Me Credits
#Thank You
import os

print("""\033[96m

░██╗░░░░░░░██╗░█████╗░██╗░░░░░██╗░░░░░░██╗░░██╗
░██║░░██╗░░██║██╔══██╗██║░░░░░██║░░░░░░╚██╗██╔╝
░╚██╗████╗██╔╝███████║██║░░░░░██║█████╗░╚███╔╝░
░░████╔═████║░██╔══██║██║░░░░░██║╚════╝░██╔██╗░
░░╚██╔╝░╚██╔╝░██║░░██║███████╗██║░░░░░░██╔╝╚██╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚═╝░░╚═╝
                  v1.0
           |---[  By: KunalMannu ]---|       
    """)
    
print("\033[93m IMPORTANT! RENAME YOUR DESIRE IMAGE TO [background] SMALLCAPS WITHOUT BRACKETS AND THE FILE TYPE LIKE png AND jpeg")    

ip = input("\033[96m Enter Path To Image: ")

os.system('sudo rm /usr/share/desktop-base/kali-theme/login/background')

os.system('sudo cp '+ ip +' /usr/share/desktop-base/kali-theme/login/')

print("DONE!")
