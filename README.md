# API Teorema de Pitágoras (Case Cromai)

Projeto desenvolvido em um processo seletivo da [Cromai](https://www.cromai.com), o qual consiste em uma API para cálculo do Teorema de Pitágoras. A API foi desenvolvida utilizando Python 3, aplicando o framework Flask.

## 🚀 Tecnologias utilizadas

- Python 3
- Flask

## 🔧 Instalação

Clone o repositório e execute o comando para instalar todas as dependências do projeto

```bash
pip install -r requirements.txt
```

Para iniciar o servidor

```bash
flask run
```

## 🛠️ Funcionamento

Com o servidor em execução, basta enviar uma requisição para a rota /pitagoras, enviando os parâmetros "oposto" e "adjacente" no URL. O servidor está sendo executado em sua configuração default, logo utiliza a porta padrão (5000).

Exemplo: GET http://localhost:5000/pitagoras?adjacente=5&oposto=12

![Exemplo de retorno da API](https://i.imgur.com/8ZFueBF.png)

O retorno fornecido pela API será o valor da hipotenusa, calculado através do Teorema de Pitágoras.

O projeto também está hospedado no Heroku, então é possível acessar a API através do endpoint abaixo, utilizando os parâmetros supracitados.

https://pitagoras-backend.herokuapp.com/pitagoras
