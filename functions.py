import subprocess
import re
import json

def bytes_to_gigabytes(bytes:int):
    return str(bytes/1024**3)

# --------------- LAPS: ---------------------------------
def getpassword(pcname):
    command = f'Get-LapsADPassword -Identity {pcname} -AsPlainText' #comando para pegar a local admin password
    #comando sendo executado para pegar a saída do mesmo:
    result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)   
    
    if result.returncode == 0:  #returncode == 0 isto é não houve erros na hora de executar o comando no shell
        text = result.stdout #atribuindo a saída ao text
        pattern = re.compile('Password            : (.+)')    #criando o padrão para extrair somente a senha do text
        match = re.search(pattern, text)   #extraindo a senha
        return match.group(1)  #retorna a senha
    
    else: #houve erros ao executar o comando, entao ele retorna uma mensagem que vai ser colocada na line:
        return 'Senha não encontrada'   #estou retornando isso ao invés do st.derr pois a line é pequena.
        
        
        
# --------------------- PING ----------------

def icmpv4(pa):

    with open('Support-APP\\ip_address.json', 'r') as file:
        iplist : dict = json.loads(file.read())
    
    ip = iplist[pa]
            
    result = subprocess.run(f'ping {ip} -n 1', capture_output=True, shell=True)
    if result.returncode == 0:
        return 1
    else:
        return 0 
    

def icmpv4_(pcname, ip):
    
    result = subprocess.run(f'psexec \\\\{pcname} cmd /c ping {ip} -n 1', capture_output=True, shell=True)
    if result.returncode == 0:
        return 1
    else:
        return 0 



########### CLEAN  ##############


def funccleaner(pcname):
    subprocess.run(f'xcopy "C:\\Users\\Administrador\\Documents\\limpeza.bat" "\\\\{pcname}\\c$\\Users\\Administrador\\Documents\\limpeza.bat" -F -Y')
    subprocess.run(f'psexec \\\\{pcname} "C:\\Users\\Administrador\\Documents\\limpeza.bat"')

    
    
    
############################## INFO ##################


def getusername(pcname):
    
    pattern = r'UNICOOB\\(.+)'  
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c wmic computersystem get username', capture_output=True, text=True)
    match = re.search(pattern, output.stdout)
    
    
    if output.returncode != 0:
        match = f'Erro: {output.stderr}'
        return match
        
    
        
    return match.group(1)




def getcpuname(pcname):
    
    
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c wmic cpu get name', capture_output=True, text=True)
    
    if output.returncode != 0:
        match = f'Erro: {output.stderr}'
        return match
    
    try:
        pattern = r'(i\d(.+))'
        match = re.search(pattern,output.stdout)
    except:
        pattern = '\n(.+)'
        match = re.search(pattern,output.stdout)
    

    return match.group(1)


    
def getdiskspace(pcname):
    
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c fsutil volume diskfree c:',
                            capture_output=True, text=True)
    
    pattern = r'\((.+)\)'
    
    if output.returncode != 0:
        match = f'Erro: {output.stderr}'
        return match
    
    try:    
        match = re.findall(pattern,output.stdout)  
    except:
        return 'Ñ foi possível acessar'
    
    return match[1], match[2]   #1° free; 2° totla
    
    

def getmac(pcname):
    
    pattern = r'..-..-..-..-..-..'
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c getmac /v /fo list', capture_output=True, text=True)
    
    if output.returncode != 0:
        
        match = f'Erro: {output.stderr}'
        return match
    
    match = re.search(pattern, output.stdout)
    return match.group(0)
    

def getmodel(pcname):
    
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c wmic computersystem get model',
                            capture_output=True, text=True)
    
    
    if output.returncode != 0:
        match = f'Erro: {output.stderr}'
        return match

        # pattern = r'\n\nModel    \n\n(.+)'  
    pattern = r'\n\n(.+)'  
    match = re.findall(pattern,output.stdout)
    
    return match[1]



def getram(pcname):
    
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c wmic memorychip get capacity', 
                            capture_output=True, text=True)
    
    pattern = r'\n(\d.+)'
    
    match = re.findall(pattern,output.stdout)
    
    if match[1]:     #caso tenha uma segunda memoria ram
        slot1 = int(match[0])
        slot2 = int(match[1])
        slotgiga = bytes_to_gigabytes(slot1)
        slotgiga2 = bytes_to_gigabytes(slot2)
        return f'{slotgiga} GB + {slotgiga2} GB'
    
        #bytes to gigabytes ele converte o valor que a wmic memorychip retorna que é bytes pra gb
        
    return bytes_to_gigabytes(match[0])  + 'GB'


def getip(pcname):
    
    output = subprocess.run(f'psexec \\\\{pcname} cmd /c ipconfig', 
                            capture_output=True, text=True)
    
    
    pattern = r'\d\d\.\d\d\d\.\d\d\d\.\d\d'
    match = re.search(pattern,output.stdout)
    
    if match == None:
        
        pattern = r'\d\d\.\d\d\d\.\d\d\.\d\d'
        match = re.search(pattern,output.stdout)
        return match.group(1)

        

    return match.group(0)
    
    
    
        
        