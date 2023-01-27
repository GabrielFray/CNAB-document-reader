# CNAB Document Reader

## Tabela de Conteúdos

1. [Sobre](#sobre)
2. [Techs](#techs)
3. [Instalação](#install)
4. [Como usar](#comousar)
5. [Desenvolvido por](#dev)
6. [Termos de uso](#terms)


---

<a name="sobre"></a>

## 1. Sobre

- O programa foi desenvolvido com o objetivo de processar arquivos CNAB, que contêm dados sobre movimentações financeiras de várias lojas. Ele armazena esses dados de forma organizada e de fácil leitura em um banco de dados relacional. 
- Para facilitar o uso do programa, foi criada uma interface web que permite o upload do arquivo CNAB. O arquivo é processado, os dados são normalizados e armazenados no banco de dados. As informações processadas podem ser visualizadas na tela.

<a name="techs"></a>

## 3. Techs

Visão Geral das tecnologias usadas no projeto.

- [Python](https://docs.python.org/3/)
- [Django](https://www.djangoproject.com/)
- [django rest_framework](https://www.django-rest-framework.org/)


---
<a align="left" name="techs"></a>

<a name="install"></a>

## 3. Instalação e uso

### 3.1 Requisitos

- Python a partir da versão 3.11.1
- Gerenciador de pacotes pip

### 3.2 Instalação

3.2.1 - Clone o repositório crie um ambiente de desenvolvimento:
 ```
 python -m venv venv
 ```
 
 3.2.2 - Após a criação do ambiente virtual voce terá que ativa-lo com o seguinte comando
 
 para linux:
 ```
 source venv/bin/activate
 ```
 
 para windows:
 ```
 source venv/Scripts/activate
 ```
 
 3.2.3 - Agora que ja ativou o ambiênte de desenvolvimento voce terá que instalar as dependências do projeto
```
pip install -r requirements.txt
```

3.2.4 - Após instalar as dependências vamos persistir as migrations no banco de dados
```
python manage.py migrate
```

3.2.5 Para rodar projeto utilize o comando 
```
python manage.py runserver
``` 

3.2.6 - Caso de tudo certo receberá uma mensagem parecida com essa:

```
System check identified no issues (0 silenced).
January 04, 2023 - 13:53:34
Django version 4.1.5, using settings 'djangoAnimes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

<a align="left" name="comousar"></a>

<a name="comousar"></a>

## 4. Como usar

- Para usar essa aplicação é bem simples, após o processo de instalação, siga os seguintes passos.

4.1 Se não estiver com o projeto rodando, rode o projeto com o comando no terminal 

```
python manage.py runserver
```

4.2 Logo após isso clique ou copie o url que aparecerá no console 

```
Starting development server at http://127.0.0.1:8000/
```

4.3 Adicione um ```api/``` no final da url

```
http://127.0.0.1:8000/api/
```

4.4 Na página estará um botão de ```Escolher arquivo``` clique nele 

<a href="https://imgur.com/4kYVeGA"><img src="https://i.imgur.com/4kYVeGA.png" title="source: imgur.com" /></a>


4.5 Selecione um arquivo CNAB com o final .txt

<a href="https://imgur.com/ro8Nafv"><img src="https://i.imgur.com/ro8Nafv.png" title="source: imgur.com" /></a>

4.6 Logo após, clique no botão ```POST``` assim ele irá normalizar o arquivo 

<a href="https://imgur.com/S7zmKNe"><img src="https://i.imgur.com/S7zmKNe.png" title="source: imgur.com" /></a>

4.7 E por fim, para retornar os dados normalizados e organizados, basta clicar no botão de ```GET``` 

<a href="https://imgur.com/s8Sgzlf"><img src="https://i.imgur.com/s8Sgzlf.png" title="source: imgur.com" /></a>

### Dados retornados após clicar no botão de ```GET```

<a href="https://imgur.com/FpbWs7g"><img src="https://i.imgur.com/FpbWs7g.png" title="source: imgur.com" /></a>


<a name="devs"></a>

## 5. Desenvolvido por

[Voltar para o topo](#tabela-de-conteúdos)

- <a name="Gabriel-fray" href="https://www.linkedin.com/in/gabrielfray/" target="_blank">Gabriel Fray</a>

<a name="terms"></a>

## 6. Termos de uso

Este é um projeto Open Source para fins educacionais e não comerciais, **Tipo de licença** - <a name="mit" href="https://opensource.org/licenses/MIT" target="_blank">MIT</a>
