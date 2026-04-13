# [Introdução](https://github.com/ficayzx/Checker-satellite-android-adb)
- Objetivo do algoritmo:
     é automatizar á verificação de Contas de usuários, caso esteje disponiveis ou não

    - A solução é sistematica:
    Usa-se uma comunicação de **Android Debug Bridge (ADB)** o framework utilizado:
    > uiautomator2
    
    proporciona funções que contém a capacidade de chamar o comando de entrada e enviar a instrução para o evento de toque/clique do smartphone, simulando um comportamento voluntario

# Arquitetura
A arquitetura é composta pelos seguintes componentes:
```mermaid
sequenceDiagram
participant PY as Script Python
participant ADB as ADB Server
participant ANB as Dispositivo Android
participant APP as Aplicativo

PY->>ADB: Envia comando
ADB->>ANB: Transmite via TCP
ANB->>APP: Simula toque/input
APP-->>PY: Retorno (sucesso/falha)
```
# Requisitos
- Python 3.10+
- Termux
- Depuração Wi-Fi habilitada com permissão

```bash
git clone https://github.com/ficayzx/Checker-satellite-android-adb

cd Checker-satellite-android-adb

python main.py
```

> [!WARNING]
> Não se responsabilizo por qualquer dano usando o codigo.

![Android Studio](https://img.shields.io/badge/android%20studio-346ac1?style=for-the-badge&logo=android%20studio&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) [![MvnRepository](https://badges.mvnrepository.com/badge/com.google.android.uiautomator/uiautomator/badge.svg?label=MvnRepository)](https://mvnrepository.com/artifact/com.google.android.uiautomator/uiautomator)

# Contribuições
[walker](https://github.com/ficayzx/)
