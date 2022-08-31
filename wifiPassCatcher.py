import subprocess
import os
import shutil

os.system('cls')

yellow = '\x1b[33m'
blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
red2 = '\x1b[31m'
cyan = '\x1b[36m'
stop = '\x1b[0m'

print(f"""{green}                           ######                       #                                          
 #    # # ###### #         #     #   ##    ####   ####  #        ####   ####  #    # #    # #####  
 #    # # #      #         #     #  #  #  #      #      #       #    # #    # #   #  #    # #    # 
 #    # # #####  #         ######  #    #  ####   ####  #       #    # #    # ####   #    # #    # 
 # ## # # #      #         #       ######      #      # #       #    # #    # #  #   #    # #####  
 ##  ## # #      #         #       #    # #    # #    # #       #    # #    # #   #  #    # #      
 #    # # #      #         #       #    #  ####   ####  #######  ####   ####  #    #  ####  #      
                   #######                                                                         {stop}""")


def linesel(file, num):
    f = open(file, 'r')
    lines = f.readlines()
    x = lines[int(num)]
    print(x)

while True:
    try:
        subprocess.run('netsh wlan show profile', shell=True)
    except Exception as e:
        print(f'{red}{e}{stop}')
    else:
        wlan0 = input(f'{cyan}name of the wifi :{stop} ')

        purpose = input(f"""{cyan}[1] wifi password
[2] wifi detailed info{stop}

{blue}select [1] or [2] :{stop} """)

        if purpose == '2':
            subprocess.run(f'netsh wlan show profile {wlan0} key=clear', shell=True)
            yes = input(f'{cyan}Do you want to find another password [press any key]{stop} ')
        elif purpose == '1':
            try:
                os.mkdir('c:/temp')
                with open('c:/temp/wlan0.txt', 'w') as wr:
                    subprocess.run(f'netsh wlan show profile {wlan0} key=clear', stdout=wr, shell=True)
                    linesel('c:/temp/wlan0.txt', 32)
                    yes = input(f'{cyan}Do you want to find another password [press any key]{stop} ')
            except:
                shutil.rmtree('c:/temp')
                os.mkdir('c:/temp')
                with open('c:/temp/wlan0.txt', 'w') as wr:
                    subprocess.run(f'netsh wlan show profile {wlan0} key=clear', stdout=wr, shell=True)
                    linesel('c:/temp/wlan0.txt', 32)
                    yes = input(f'{cyan}Do you want to find another password [press any key]{stop} ')
        else:
            print(f'{red}please type in 1 or 2{stop}')
            yes = input(f'{cyan}Do you want to find another password [press any key]{stop} ')
