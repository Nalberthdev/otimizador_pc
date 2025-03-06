import os
import psutil
import ctypes
import gc
import subprocess

# Lista de processos que podem ser finalizados (adicione mais se quiser)
PROCESSOS_BLOQUEADOS = [
    "notepad.exe", "chrome.exe", "spotify.exe", "discord.exe", "teams.exe",
    "zoom.exe", "epicgameslauncher.exe", "steam.exe", "battle.net.exe"
]

def liberar_memoria():
    """Força a liberação de memória RAM"""
    gc.collect()
    ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)

def matar_processos():
    """Fecha processos não essenciais"""
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            if proc.info["name"].lower() in PROCESSOS_BLOQUEADOS:
                os.kill(proc.info["pid"], 9)  # Força o encerramento
                print(f"Encerrado: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def manter_pc_ativo():
    """Evita que o PC entre em suspensão"""
    subprocess.run("powercfg -change -standby-timeout-ac 0", shell=True)
    subprocess.run("powercfg -change -monitor-timeout-ac 0", shell=True)
    subprocess.run("powercfg -change -disk-timeout-ac 0", shell=True)

if __name__ == "__main__":
    print("Otimizando o PC...")
    liberar_memoria()
    matar_processos()
    manter_pc_ativo()
    print("PC otimizado com sucesso!")
