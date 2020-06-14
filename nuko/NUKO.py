import subprocess as sp
import os
import time

ip=list(range(1, 50)) # 아이피 리스트

ID=list(range(1, 50)) # 아이디 리스트

for i in range(49): # 아이피 리스트 0으로 초기화
    ip[i]=0

for i in range(49): # 아이디 리스트 0으로 초기화
    ID[i]=0

LIVE_IP = 0 # 확인 된 아이피 개수
LIVE_ID = 0 # 확인 된 아이디 개수






print('NUKO v5.0 : E-mail ▶ dnwn306@naver.com\n\n')
def CONNECT_SSH():
    while True:
    
        IP_READER() # ip 리스트를 읽는 역할


        print('[SSH] 연결할 아이피를 선택 / 뒤로(B)\n')

        choice = input('INPUT$> ')
    


        if len(choice)==0: # 아무것도 입력을 안함
            choice = 999
            choice = int(choice)




        else:
            try:
                choice = int(choice)
            except:
                if choice == 'b' or choice == 'B':
                    return
                
                choice = 999
                choice = int(choice)

        
        

        if choice >= 0 and choice <= LIVE_IP-1:

            ACCOUNT_READER()
            
            print("[",ip[choice],"의 사용자 계정 선택 / 뒤로(B) ]\n")
            account = input('INPUT$> ')

            if len(account)==0: # 아무것도 입력을 안함
                account = 999
                account = int(account)

            else:
                try:
                    account = int(account)
                except:
                    if account == 'b' or account == 'B':
                        return
                
                    account = 999
                    account = int(account)


            if account >= 0 and account <= LIVE_ID-1:

                print("\n")
                print(ip[choice],"으로 연결중..")
                cmd = "ssh "+ID[account]+"@"+ip[choice]
                os.system(cmd)

            else:
                print('[-] 리스트에 없는 번호입니다.')



        else:
            print('[-] 리스트에 없는 번호입니다.')



def CONNECT_FTP():
    while True:
    
        IP_READER() # ip 리스트를 읽는 역할


        print('[FTP] 연결할 아이피를 선택 / 뒤로(B)\n')

        choice = input('INPUT$> ')
    


        if len(choice)==0: # 아무것도 입력을 안함
            choice = 999
            choice = int(choice)




        else:
            try:
                choice = int(choice)
            except:
                if choice == 'b' or choice == 'B':
                    return
                
                choice = 999
                choice = int(choice)

        
        

        if choice >= 0 and choice <= LIVE_IP-1:

            print("\n")
            print(ip[choice],"으로 연결중..")
            cmd = "ftp "+ip[choice]
            os.system(cmd)



        else:
            print('[-] 리스트에 없는 번호입니다.')




def MOD_SSH(): # SSH 모드

    while True:

        print("\n")
        print("█SSH████████████████████████[X]█")
        print("║                              ║")
        print("║        [1] SSH Connect       ║")
        print("║                              ║")
        print("║        [2] ICMP Check        ║")
        print("║                              ║")
        print("║        [3] Back              ║")
        print("║                              ║")
        print("════════════════════════════════")
        print("\n")
        
        cmd = input("INPUT$> ")

        if cmd == 'x' or cmd == 'X': # 종료
            exit()

        elif cmd == '1':
            CONNECT_SSH()
            

        elif cmd == '2':

            IP_CHECK() # IP 리스트를 기반으로 ICMP 확인

        elif cmd == 'back' or cmd == '3':
            return
            
        else:
            print('[-] \''+cmd+'\' is Unknown command.')


def MOD_FTP(): # FTP 모드

    while True:

        print("\n")
        print("█FTP████████████████████████[X]█")
        print("║                              ║")
        print("║        [1] FTP Connect       ║")
        print("║                              ║")
        print("║        [2] ICMP Check        ║")
        print("║                              ║")
        print("║        [3] Back              ║")
        print("║                              ║")
        print("════════════════════════════════")
        print("\n")
        
        cmd = input("INPUT$> ")

        if cmd == 'x' or cmd == 'X': # 종료
            exit()

        elif cmd == '1':
            CONNECT_FTP()

        elif cmd == '2':

            IP_CHECK() # IP 리스트를 기반으로 ICMP 확인

        elif cmd == 'back' or cmd == '3':
            return
            
        else:
            print('[-] \''+cmd+'\' is Unknown command.')



def IP_CHECK(): # IP 리스트를 기반으로 ICMP 확인
    print("\n")
    print("===========IP_CHECK===========")

    i = 0

    print('\n확인 된 아이피 개수:',LIVE_IP,'개\n')
    
    while i != LIVE_IP:
        
        pop = ip[i]
        
        status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
        if status == 0:
            print("[온라인✓]", str(pop),end='\n\n')
        else:
            print("[오프라인✗]", str(pop),end='\n\n')

        i=i+1

    print("==============================\n")
    print("\n")



def IP_LOADER(): # ip.txt를 읽어들이는 역할   
    f = open("ip.txt", 'r')

    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        ip[i]=line

        if ip[i][len(ip[i])-1] == '\n':
            ip[i]=ip[i].replace('\n', '')

        
        i=i+1
    f.close()


def IP_READER(): # ip 리스트를 읽는 역할
    global LIVE_IP
    print("\n")
    print("===========IP_LIST===========")
    i = 0
    while ip[i] != 0: # 0으로 차있는 리스트행은 무시
        print('\n[',i,'] ',ip[i],end='\n\n',sep='')
        i=i+1

    print("\n등록된 아이피 개수:",i)
    LIVE_IP = i

    print("=============================\n")
    print("\n")



def ACCOUNT_LOADER(): # account.txt를 읽어들이는 역할   
    f = open("account.txt", 'r')

    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        ID[i]=line

        if ID[i][len(ID[i])-1] == '\n':
            ID[i]=ID[i].replace('\n', '')

        
        i=i+1
    f.close()


def ACCOUNT_READER(): # account 리스트를 읽는 역할
    global LIVE_ID
    print("\n")
    print("===========ID_LIST===========")
    i = 0
    while ID[i] != 0: # 0으로 차있는 리스트행은 무시
        print('\n[',i,'] ',ID[i],end='\n\n',sep='')
        i=i+1

    print("\n등록된 아이디 개수:",i)
    LIVE_ID = i

    print("=============================\n")
    print("\n")


    
def USER_INPUT(): # 사용자 입력
    MAIN_TITLE() # 메인 타이틀
    while True:
        CMD_LIST()
        
        cmd = input("INPUT$> ")

        if cmd == 'x' or cmd == 'X' or cmd == '3' or cmd == 'exit' or cmd == 'EXIT': # 종료
            exit()

        elif cmd == 'ssh' or cmd == 'SSH' or cmd == '1': # SSH 서비스 선택
            MOD_SSH()

        elif cmd == 'ftp' or cmd == 'ftp' or cmd == '2': # FTP 서비스 선택
            MOD_FTP()
            
        else:
            print('[-] \''+cmd+'\' is Unknown command.')

''' sys 파기 but 이를 활용
        elif cmd[0] == 'sys': # SYS 커맨드
            print('SYS 커맨드>'+cmd[1]+cmd[2])
            os.system(cmd[1])
'''            


def DONE_FISH():
    print("      ▄██║║║║   ▄█")
    print("     ██▄█╬╬╬╬╬╬███ Done.")
    print("      ▀██║║║║   ▀█")

def WAITING_FISH():
    print("      ▄██║║║║   ▄█")
    print("     ██▄█╬╬╬╬╬╬███ Waiting...")
    print("      ▀██║║║║   ▀█")



def CMD_LIST(): # 명령어 목록
    print("\n")
    print("█MAIN███████████████████████[X]█")
    print("║                              ║")
    print("║           [1] SSH            ║")
    print("║                              ║")
    print("║           [2] FTP            ║")
    print("║                              ║")
    print("║           [3] EXIT           ║")
    print("║                              ║")
    print("════════════════════════════════")
    print("\n")

def MAIN_TITLE(): # 메인 타이틀
    
    print("\n")

    '''
      █████
     █     █
    █ █   █ █                                     
    █   █   █
    █  █ █  ███████████████
    █                      █
    █                       █
    █                       █
    █ █████  ███████████    █
    █  █  █  █        █ ██  █
     ██    ██          ██ ██
    '''


    print("███╗   ██╗██╗   ██╗██╗  ██╗ ██████╗ ")
    print("████╗  ██║██║   ██║██║ ██╔╝██╔═══██╗")
    print("██╔██╗ ██║██║   ██║█████╔╝ ██║   ██║")
    print("██║╚██╗██║██║   ██║██╔═██╗ ██║   ██║")
    print("██║ ╚████║╚██████╔╝██║  ██╗╚██████╔╝")
    print("╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ")

    print("\n")

    print("  █████")
    print(" █     █  The")
    print("█ █   █ █ SSH & FTP Connect Assistor")
    print("█   ^   █")
    print("█       ██████████████████████")
    print("█                             █")
    print("█                              █")
    print("█                              █")
    print("█ █████  ██████████████████    █")
    print("█  █  █  █               █ ██  █")
    print(" ██    ██                 ██ ██")

    
    time.sleep(0.5)


    '''
    print("▪▄██████▄ ▪ ▄█    █▄·  ▄████████ .  ▄████████")
    print("███    ███ ███  ·███   ███    ███· ███    ███")
    print("███    ███ ███    ███   ███  . █▀    ███    ███·")
    print("███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀")
    print("███  . ███ ███    ███ ▀▀███▀▀▀  ▪  ▀▀███▀▀▀▀▀  ")
    print("███    ███ ███    ███•  ███    █▄  ▀███████████")
    print("███    ███ ███    ███   ███    ███   ███    ███")
    print("▀██████▀▪. ▀██████▀    ██████████    ███ •  ███ ")
    print("                                   . ███    ███ ")  

    print("  ▄█        ▄██████▄     ▄████████ ████████▄     ▄████████  . ▄████████")
    print(" ███ •   ▪ ███    ███   ███    ███ ███▪  ▀███   ███    ███ ·███    ███·")
    print(" ███       ███    ███   ███    ███ ███    ███   ███  . █▀    ███    ███")
    print(" ███ ▪     ███ .  ███   ███    ███ ███·  ███  ▄███▄▄▄      ▄███▄▄▄▄██▀")
    print(" ███       ███    ███ ▀███████████ ███    ███ ▀▀███▀▀▀▪    ▀▀███▀▀▀▀▀")
    print(" ███       ███    ███   ███    ███ ███    ███   ███    █▄  ▀███████████")
    print(" ███▌    ▄ ███    ███   ███  ▪ ███ ███.  ▄███   ███    ███   ███    ███")
    print("█████▄▄██  ▀██████▀ ▪  ███     █▀  ████████▀•   ██████████   ███ •  ███")
    print("▀                                                          . ███    ███")
    '''



if __name__ == "__main__": # 메인 영역


    WAITING_FISH()


    ACCOUNT_LOADER() # ip.txt를 읽어들이는 역할

    ACCOUNT_READER() # ip 리스트를 읽는 역할
    
    
    IP_LOADER() # ip.txt를 읽어들이는 역할

    IP_READER() # ip 리스트를 읽는 역할

    IP_CHECK() # IP 리스트를 기반으로 ICMP 확인


    time.sleep(0.5)


    DONE_FISH()


    print("\n\n\n")


    USER_INPUT() # 사용자 입력

