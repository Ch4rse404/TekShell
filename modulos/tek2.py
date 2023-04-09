import os

from colorama import init, Fore, Back, Style

init(autoreset=True)

os.system('cls|clear')

print("""

            \033[94m [ \033[0m \033[1;37;41mTekShell generator reverse shell \033[0m \033[94m ] \033[0m

\033[1;49;35m████████╗███████╗██╗  ██╗\033[4;49;96m███████╗██╗  ██╗███████╗██╗     ██╗\033[0m

\033[1;49;35m╚══██╔══╝██╔════╝██║ ██╔╝\033[4;49;96m██╔════╝██║  ██║██╔════╝██║     ██║\033[0m

\033[1;49;35m   ██║   █████╗  █████╔╝ \033[4;49;96m███████╗███████║█████╗  ██║     ██║\033[0m

\033[1;49;35m   ██║   ██╔══╝  ██╔═██╗ \033[4;49;96m╚════██║██╔══██║██╔══╝  ██║     ██║\033[0m

\033[1;49;35m   ██║   ███████╗██║  ██╗\033[4;49;96m███████║██║  ██║███████╗███████╗███████╗\033[0m

\033[1;49;35m   ╚═╝   ╚══════╝╚═╝  ╚═╝\033[4;49;96m╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\033[0m

            \033[1;37;41mCodded By: CharseSec\033[0m - \033[1;37;41mLybeSec Group\033[0m""")

print("\033[97m╔══════════════════════════════════════════════╗")

print("")

print(""" \033[1;49;35m[ 1 ] \033[4;49;96mBASH\033[0m

 \033[1;49;35m[ 2 ] \033[4;49;96mJAVA\033[0m

 \033[1;49;35m[ 3 ] \033[4;49;96mPERL\033[0m

 \033[1;49;35m[ 4 ] \033[4;49;96mPYTHON\033[0m

 \033[1;49;35m[ 5 ] \033[4;49;96mPHP\033[0m

 \033[1;49;35m[ 6 ] \033[4;49;96mNC-PLAIN\033[0m

 \033[1;49;35m[ 7 ] \033[4;49;96mNC-MKFIFO\033[0m

 \033[1;49;35m[ 8 ] \033[4;49;96mRUBY\033[0m

 \033[1;49;35m[ 9 ] \033[4;49;96mTELNET\033[0m

 \033[1;49;35m[ 10 ] \033[4;49;96mWIN-POWERSHELL\033[0m""")

print("")

print("\033[97m╚══════════════════════════════════════════════╝ ")

opt = input("\033[1;37;41mESCOLHA SUA SHELL >>\033[0m")

if opt == '1':
  import bash
    
elif opt == '2':
  import Java
  
elif opt == '4':
  import perl
  
elif opt == '5':
  import python

elif opt == '6':
  import plein

elif opt == '7':
  import mkfifo

elif opt == '8':
  import ruby
  
elif opt == '9':
  import telnet
  
elif opt == '10':
  import powershell
  
else:
  print("opção invalida")
  
