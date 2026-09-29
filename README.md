# 🤖 [Aula 1] - Automações de Tarefas e Bots

Este repositório contém um projeto prático de automação construído em Python. O objetivo principal é criar um bot capaz de controlar o mouse e o teclado para realizar tarefas sistêmicas e repetitivas de forma 100% autônoma, desde o login em plataformas até a leitura de bases de dados.

## 🚀 Funcionalidades do Projeto

*   **Automação de Interface (RPA):** O script interage com o sistema operacional para abrir o navegador (Chrome), acessar o link do sistema e realizar o login preenchendo automaticamente e-mail e senha.
*   **Processamento de Dados:** Leitura e extração estruturada de uma base de dados de produtos simulada (`produtos.csv`) para posterior integração no sistema.
*   **Auto-Git (Bônus):** O projeto conta com um script de automação de versionamento (`backup.py`) que detecta alterações locais, cria os commits e faz o envio (push) direto para o GitHub sem necessidade de digitar os comandos manualmente no terminal.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

*   **Python 3**
*   **PyAutoGUI:** Responsável por simular ações humanas (cliques, digitação e atalhos de teclado).
*   **Pandas:** Utilizado para a manipulação e visualização da base de dados.
*   **OpenPyXL:** Motor de suporte para leitura de formatos de planilhas.
*   **Subprocess (Built-in):** Utilizado para integrar comandos do sistema operacional e rodar o Git via Python.

## 📁 Estrutura de Arquivos

*   `codigo.py`: Script principal contendo o passo a passo da automação (abertura do sistema, login e leitura do CSV).
*   `backup.py`: Robô pessoal para automatizar o fluxo do Git (Add, Commit e Push).
*   `auxiliar.py`: Arquivo de suporte para captura de coordenadas da tela.
*   `produtos.csv`: Base de dados utilizada pela automação.

## ⚙️ Como Executar no seu Computador

1. Clone este repositório:
   ```bash
   git clone [https://github.com/DanniSilvaaSiqq/projeto-automacao-python.git](https://github.com/DanniSilvaaSiqq/projeto-automacao-python.git)
