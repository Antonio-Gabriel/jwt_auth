# Autenticação com JWT em python

Aplicação bem simples, onde criaremos uma atenticação simples usando a linguagem
python e como framework trabalharemos com o flask.

Mas antes precisaremos aprender um pouco sobre JWT

## O que é JWT

O significado da sigla JWT é (Json web token) que minimamente é um padrão que define token
no formato json para troca de informações de forma leve, seguda e autocontinua.

A otura questão que poderá surgir é, o que é `token?`.
De forma símples token refere-se minimamente a uma chave electrônica.

Proceguindo.

Com o jwt conseguimos adicionar a um token tudo que nós precisamos passar em uma aplicação
tirando assim o proveito da segurança que o token já ofecere.

Diminuindo o tamanho de dados ao contrário de arquivos como **XML** entre outros.

## Suas características (JWT).

- O Jwt é leve, pós adota o json como base.
De uma forma mais descritiva o `Json`, facilita a interoperabilidade entre sistemas, ou seja partilha de dados entre sistemas de **n** tipos.
- AutoContido, traz consigo todas as informações necessárias para o seu processamento.
- Segura pós utiliza um algoritimo de hashing para validação da integridade do token.

## Casos em que podemos utilizar o Jwt

Existem várias razões para utilizar um jwt dentre elas as mais comuns são.

- Para troca de informação entre aplicações tirando proveito das caracteristicas a cima.
- Em mecanismos de autenticação também onde encontramos de forma mais comum.

**OBS:** JWT não representa o mecanismo de autenticação mas sim o meio utilizado para
viabilizar esse mecanismo em nossas aplicações.

Com o jwt os dados são consumidos com base na validade do token.

### Gerando uma chave secreta para o token.

```python

import os
from uuid import uuid4
from secrets import token_urlsafe

urandom_delimiter = os.urandom(12)
secret_key_generate_oub = uuid4().hex
urlsafe_token = token_urlsafe(12)

print(
    urandom_delimiter,
    secret_key_generate_oub,
    urlsafe_token
)

```