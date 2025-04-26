import os
import platform
import subprocess

VENV_NAME = "venv"  # Nome do ambiente virtual

def activate_venv():
    """Ativa o ambiente virtual dependendo do sistema operacional."""
    system = platform.system()
    
    if system == "Windows":
        activate_script = os.path.join(VENV_NAME, "Scripts", "activate.bat")
        subprocess.run(f'cmd /k "{activate_script}"', shell=True)
    else:
        activate_script = os.path.join(VENV_NAME, "bin", "activate")
        subprocess.run(f"source {activate_script}", shell=True, executable="/bin/bash")

    print(f"Ambiente virtual '{VENV_NAME}' ativado.")

def deactivate_venv():
    """Instrui o usuário a desativar manualmente no Windows."""
    system = platform.system()
    
    if system == "Windows":
        print("Para desativar o ambiente virtual, digite 'deactivate' manualmente no terminal.")
    else:
        subprocess.run("deactivate", shell=True)

if __name__ == "__main__":
    choice = input("Digite '1' para ativar ou '2' para desativar o ambiente virtual: ")

    if choice == "1":
        activate_venv()
    elif choice == "2":
        deactivate_venv()
    else:
        print("Opção inválida. Escolha '1' ou '2'.")
