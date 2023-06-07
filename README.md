# APP_Gerenciador
Projeto - Tecnologias Emergentes
 
Este projeto consiste em uma aplicação para o gerenciamento de funcionários e suas informações pessoais. A aplicação é composta por uma API desenvolvida com Django Rest Framework, que permite realizar operações de criação, leitura, atualização e exclusão (CRUD) dos registros de funcionários. Além disso, também é desenvolvido um frontend utilizando Vue.js, que se comunica com a API e apresenta os dados de forma amigável aos usuários.

#  ⚙️ Tecnologias Utilizadas

Django: framework web em Python que facilita o desenvolvimento rápido e eficiente de aplicações web.

Django Rest Framework: uma extensão do Django que fornece ferramentas e funcionalidades adicionais para a construção de APIs RESTful.

MongoDB: um banco de dados NoSQL que oferece flexibilidade e escalabilidade para armazenar os dados da aplicação.

MongoDB Atlas: plataforma de hospedagem de bancos de dados MongoDB gerenciada pela MongoDB.

Vue.js: framework JavaScript progressivo para a construção de interfaces de usuário interativas.

#  📋 Objetivo da Aplicação

Permitir o gerenciamento eficiente dos funcionários de uma empresa. Através da API, é possível realizar as seguintes operações:

Adicionar um novo funcionário, fornecendo as informações necessárias como nome, departamento e data de registro.

Recuperar as informações de um funcionário específico, incluindo seus detalhes pessoais.

Atualizar as informações de um funcionário, como seu departamento ou data de registro.

Excluir um funcionário do sistema.


💻 Ambiente de Desenvolvimento

Para desenvolver e executar a aplicação, é necessário ter o seguinte ambiente configurado:

Python 3.9 ou superior
Django 3.2 ou superior
Django Rest Framework 3.12 ou superior
Vue.js 2.6 ou superior

🔧 Instalação e Execução
Siga as instruções abaixo para instalar e executar a aplicação:

Clone o repositório do projeto do GitHub: [URL do repositório]
Acesse o diretório raiz do projeto.
Configuração do Backend (API):
Crie um ambiente virtual para isolar as dependências do projeto (opcional, mas recomendado).
Ative o ambiente virtual.
Instale as dependências do projeto usando o comando pip install -r requirements.txt.
Execute as migrações do banco de dados usando o comando python manage.py migrate.
Inicie o servidor do backend usando o comando python manage.py runserver.
Configuração do Frontend:
Acesse o diretório frontend dentro do diretório raiz do projeto.
Instale as dependências do frontend usando o comando npm install.
Inicie o servidor do frontend usando o comando npm run serve.
Acesse a aplicação no navegador através do seguinte endereço: http://localhost:8080.

📝 Práticas de Código Limpo

Durante o desenvolvimento da aplicação, foram aplicadas as seguintes práticas de código limpo:

Nomes significativos de variáveis, funções e classes.
Organização e estruturação adequada do código.
Divisão do código em módulos reutilizáveis e de fácil manutenção.

✅ Testes Automatizados
A aplicação possui testes automatizados para garantir a qualidade e o funcionamento correto das funcionalidades. Os testes abrangem as principais operações da API, como criação, leitura, atualização e exclusão de funcionários.

🤝 Contribuição para o Projeto
Caso deseje contribuir para o projeto, siga os passos abaixo:

Faça um fork do repositório do projeto.
Crie um branch para a sua nova feature ou correção.
Faça as modificações necessárias.
Realize os testes unitários para garantir o funcionamento correto.
Faça um push das suas alterações para o seu repositório fork.
Abra um Pull Request no repositório original, descrevendo as alterações realizadas.
📌 Padrão de Projeto de Software
Para este projeto, foi aplicado o padrão de projeto MVC (Model-View-Controller) para separação das responsabilidades. O Django facilita a implementação desse padrão, onde os modelos (model) são responsáveis pela definição dos dados e regras de negócio, as views (controller) tratam das requisições e respostas da API, e os templates (view) cuidam da apresentação dos dados para o usuário.


Desenvolvido por [Marcos Manfré](https://www.linkedin.com/in/marcosmanfre/) 
