<p align="center">
    <img width="300px" src=".github/assets/logo_2.png">
</p>

<p align="center">
<a href="https://dio.me/"><img src="https://img.shields.io/badge/DIO-Project-FED564?logo=youtube" alt="DIO - Project"></a>
<a href="https://python.org/" title="Made with Python"><img src="https://img.shields.io/badge/Made%20with-Python-FED564?logo=python&logoColor=white" alt="Made with Python"></a>
<a href="https://nmap.org/" title="Powered by Nmap">
  <img src="https://img.shields.io/badge/Powered%20by-Nmap-FED564?logo=apache&logoColor=white" alt="Powered by Nmap">
</a>
</p>

<p align="center">
  <h3 align="center">🔍 Scanner de Portas TCP</h3>
Este projeto ensina a desenvolver um scanner de portas TCP utilizando Python e a biblioteca Nmap. Exploramos três métodos de varredura: **SYN**, **UDP** e **Comprehensive**, fundamentais para detectar portas abertas e coletar informações de rede.
</p>

## 📋 Índice

- [📋 Índice](#-índice)
- [📝 Introdução](#-introdução)
- [🔍 Métodos de Varredura](#-métodos-de-varredura)
- [🚀 Como Executar](#-como-executar)
- [🧑‍🏫 Autor](#-autor)

---

## 📝 Introdução

Este laboratório foi desenvolvido para ensinar como implementar um scanner de portas TCP em Python, utilizando a biblioteca `nmap` e `colorama`. A ideia principal é explorar como a detecção de portas abertas e serviços pode ser feita através de três métodos de varredura.

---

## 🔍 Métodos de Varredura

Este projeto implementa três métodos principais de varredura:

- **SYN Scan**: Método rápido e furtivo, onde apenas um pacote SYN é enviado ao alvo. Se a porta estiver aberta, um pacote SYN-ACK será retornado.
- **UDP Scan**: Utilizado para descobrir serviços que utilizam o protocolo UDP. Este tipo de varredura não é tão confiável quanto a SYN, mas é crucial para a descoberta de portas UDP.
- **Comprehensive Scan**: Combina várias técnicas, incluindo SYN, ACK e UDP, para proporcionar uma varredura completa e profunda.

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/dio-portscanner.git



2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .\.venv\Scripts\activate  # Windows


3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Execute o script principal:
    ```bash
    python PortScanner2.0.py

🧑‍🏫 Autor
- Bruno Dias, Expert Instructor, DIO