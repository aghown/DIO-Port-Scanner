import nmap
import time
from colorama import Fore, Style, init

# Inicializa o colorama
init()

def print_separator():
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

def print_title(title):
    print(Fore.GREEN + title + Style.RESET_ALL)
    print_separator()

def print_progress_bar(iteration, total, length=50):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = Fore.YELLOW + '█' * filled_length + '-' * (length - filled_length)
    progress_message = f'[{bar}] {percent:.2f}% Completo'
    print(f'\r{progress_message}', end=Style.RESET_ALL)

scanner = nmap.PortScanner()

print_title("Seja Bem Vindo ao DIOScanner")

ip = input(Fore.GREEN + "Digite o IP ou domínio a ser varrido: " + Style.RESET_ALL)
print(Fore.GREEN + "O IP ou domínio digitado foi:", ip + Style.RESET_ALL)

menu = input(Fore.BLUE + """\nEscolha o tipo de varredura a ser realizada
                1 -> Varredura SYN
                2 -> Varredura UDP
                3 -> Varredura Intensa
                Digite a opção escolhida: """ + Style.RESET_ALL)
print(Fore.GREEN + "A opção escolhida foi:", menu + Style.RESET_ALL)

try:
    print_title("Iniciando a Varredura")

    # Adiciona uma pausa inicial para simular a configuração da varredura
    time.sleep(1)

    # Marca o início do tempo da varredura
    start_time = time.time()

    total_steps = 10  # Número de etapas para a barra de progresso
    for step in range(total_steps):
        print_progress_bar(step, total_steps)
        time.sleep(0.5)  # Simula o progresso

    # Limpa a linha de progresso após a conclusão
    print()

    # Executa a varredura
    try:
        if menu == "1":
            scan_args = '-v -sS'
            print(Fore.MAGENTA + "Varredura SYN em andamento..." + Style.RESET_ALL)
            result = scanner.scan(ip, '1-1024', arguments=scan_args)
        elif menu == "2":
            scan_args = '-v -sU'
            print(Fore.MAGENTA + "Varredura UDP em andamento..." + Style.RESET_ALL)
            result = scanner.scan(ip, '1-1024', arguments=scan_args)
        elif menu == "3":
            scan_args = '-v -sC'
            print(Fore.MAGENTA + "Varredura Intensa em andamento..." + Style.RESET_ALL)
            result = scanner.scan(ip, '1-1024', arguments=scan_args)
        else:
            print(Fore.RED + "Escolha uma opção correta!!!" + Style.RESET_ALL)
            exit()

    except Exception as e:
        print(Fore.RED + f"Erro durante a varredura: {e}" + Style.RESET_ALL)
        exit()

    # Marca o final do tempo da varredura
    elapsed_time = time.time() - start_time

    print("\n" + Fore.GREEN + "Resultado da varredura:" + Style.RESET_ALL)
    print(Fore.GREEN + "Resultado completo do scan:" + Style.RESET_ALL)
    print(result)  # Adiciona um print do resultado para debug

    # Encontrar o IP real do domínio
    found_ip = None
    for host in scanner.all_hosts():
        if ip in host or ip == scanner[host].hostname():
            found_ip = host
            break

    if found_ip:
        print(Fore.GREEN + f"Status do IP: {scanner[found_ip].state()}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Protocolos encontrados: {scanner[found_ip].all_protocols()}" + Style.RESET_ALL)

        if menu == "1":
            ports = scanner[found_ip].get('tcp', {})
            if ports:
                for port, port_info in ports.items():
                    state = port_info['state']
                    if state == 'open':
                        print(Fore.GREEN + f"Porta {port} está ABERTA (resposta SYN/ACK)" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + f"Porta {port} está FECHADA (resposta RST)" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nenhuma porta aberta encontrada." + Style.RESET_ALL)

        elif menu == "2":
            ports = scanner[found_ip].get('udp', {})
            if ports:
                for port, port_info in ports.items():
                    state = port_info.get('state', 'Desconhecido')
                    print(Fore.GREEN + f"Porta UDP {port} detectada (Estado: {state})" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nenhuma porta UDP detectada." + Style.RESET_ALL)

    else:
        print(Fore.RED + f"O IP ou domínio {ip} não foi encontrado nos resultados da varredura." + Style.RESET_ALL)

    print(Fore.GREEN + f"\nVarredura concluída em {elapsed_time:.2f} segundos." + Style.RESET_ALL)

except Exception as e:
    print(Fore.RED + f"Erro geral: {e}" + Style.RESET_ALL)
