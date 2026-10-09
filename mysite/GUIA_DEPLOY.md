🚀 Guia de Configuração e Deploy (Linux & Windows)
----------------------------------------------------------------------------
Este guia serve como um passo a passo definitivo para clonar, configurar e executar o seu projeto Django 5 Blog em diferentes sistemas operacionais (Linux e Windows), garantindo compatibilidade total com o PostgreSQL (via Docker) e o VS Code.
----------------------------------------------------------------------------
1. Clonar o Projeto do GitHub

Abra o seu terminal (ou Git Bash) na pasta onde deseja armazenar o código e execute:

git clone https://github.com/henriquej-blip/CriandoBlog.git
cd CriandoBlog

----------------------------------------------------------------------------
2. Abrir o Projeto no VS Code

Para abrir a pasta diretamente no editor Visual Studio Code pela linha de comando:

code .

----------------------------------------------------------------------------
3. Configuração no Linux (Ubuntu / Debian / Fedora)

Siga os passos abaixo no terminal integrado do VS Code ou no terminal do sistema:

Criar o ambiente virtual:

python3 -m venv venv


Ativar o ambiente virtual:

source venv/bin/activate


Atualizar o gerenciador de pacotes e instalar as dependências:

pip install --upgrade pip
pip install -r requirements.txt


Banco de Dados e Execução:

Certifique-se de que o Docker está rodando na sua máquina e que o container do PostgreSQL está ativo.

Execute as migrações e inicie o servidor de desenvolvimento:

python manage.py migrate
python manage.py runserver

----------------------------------------------------------------------------
4. Configuração no Windows (CMD ou PowerShell)

Siga os passos abaixo no Prompt de Comando (cmd) ou no PowerShell dentro da pasta do projeto:

Criar o ambiente virtual:

python -m venv venv


Ativar o ambiente virtual:

Se estiver usando o Prompt de Comando (CMD):

venv\Scripts\activate.bat


Se estiver usando o PowerShell:

.\venv\Scripts\Activate.ps1


Atualizar o pip e instalar as dependências:

python -m pip install --upgrade pip
pip install -r requirements.txt


Banco de Dados e Execução:

Certifique-se de que o Docker Desktop está rodando no Windows.

Execute as migrações do banco e inicie o servidor:

python manage.py migrate
python manage.py runserver

----------------------------------------------------------------------------
💡 Dicas Úteis

Desativar o ambiente virtual: Quando terminar de programar, basta digitar deactivate no terminal.

Atualizar o repositório: Sempre que fizer alterações em outro computador, lembre-se de rodar git pull origin main antes de começar a codar.