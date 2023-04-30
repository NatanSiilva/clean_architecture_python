## Clean Architecture Python

Este repositório contém um exemplo de implementação de uma arquitetura limpa em Python, utilizando o framework Flask. O objetivo é fornecer um exemplo simples e didático de como aplicar os conceitos de arquitetura limpa em um projeto Python.

# Arquitetura

O projeto é estruturado em camadas, seguindo os princípios da arquitetura limpa. A seguir, uma breve descrição de cada camada:

- app: contém as definições de endpoints da API, bem como as configurações do Flask.
- domain: contém as entidades e os casos de uso da aplicação.
- infra: contém as implementações dos repositórios, bem como qualquer outra implementação que se relacione diretamente com infraestrutura (como serviços externos, por exemplo).
- interfaces: contém as interfaces para comunicação entre as camadas (como, por exemplo, as interfaces dos repositórios).

# Dependências

As dependências do projeto estão listadas no arquivo requirements.txt.

# Como rodar o projeto

- Clone o repositório
git clone https://github.com/NatanSiilva/clean_architecture_python.git

- Crie um ambiente virtual e ative-o
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

- Instale as dependências
pip install -r requirements.txt

- Rode o projeto
python app.py


# Endpoints
Os seguintes endpoints estão disponíveis:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /pets | Retorna a lista de pets |
| POST | /pets | Cria um novo pet |
| GET | /pets/{id} | Retorna os detalhes de um pet |
| PUT | /pets/{id} | Atualiza um pet existente |
| DELETE | /pets/{id} | Deleta um pet existente |
| GET | /users | Retorna a lista de usuários |
| POST | /users | Cria um novo usuário |
| GET | /users/{id} | Retorna os detalhes de um usuário |
| PUT | /users/{id} | Atualiza um usuário existente |
| DELETE | /users/{id} | Deleta um usuário existente |

### Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
