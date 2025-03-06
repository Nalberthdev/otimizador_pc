# Adicionado script de otimização do PC e arquivo .bat para execução 🚀

## 📌 O que esse commit adiciona?
- Um script em **Python** (`otimizar_pc.py`) para otimizar o desempenho do computador.
- Um arquivo **.bat** (`otimizar.bat`) que executa o script facilmente.

---

## 🔧 Funcionalidades do Script:
### ✅ **Liberação de Memória RAM**
- O script força o **coletor de lixo do Python** a liberar memória.
- Usa uma função do Windows (`SetProcessWorkingSetSize`) para otimizar a RAM.

### ❌ **Fechamento de Processos Não Essenciais**
- O script verifica **todos os processos ativos** e fecha aqueles que não são principais.
- A lista de processos a serem encerrados inclui navegadores, jogos e aplicativos de fundo.

### ⚡ **Evita Suspensão do PC**
- O script impede que o computador entre em modo de descanso ou desligue o monitor automaticamente.

---

## 🛠 Como Usar?
1. **Instale o Python** (caso não tenha instalado).
2. **Execute `otimizar.bat`** para rodar a otimização automaticamente.

---

## 🚀 Melhorias Futuras:
- Criar uma **interface gráfica (GUI)** para facilitar o uso.
- Implementar um **log de processos encerrados**.
