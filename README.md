[![Build Status](https://travis-ci.org/riquellopes/small-gateway.svg?branch=master)](https://travis-ci.org/riquellopes/small-gateway)
[![Coverage Status](https://coveralls.io/repos/github/riquellopes/small-gateway/badge.svg?branch=master)](https://coveralls.io/github/riquellopes/small-gateway?branch=master)

Small Gateway
=============

O small gateway é uma proposta simples ao grande universo de como realmente funciona o fluxo de captura de valores de um cartão ou geração de boleto.

#### Montando a aplicação:
Para utilizar a aplicação é necessario possuir [docker](https://docs.docker.com/install/) e [docker-compose](https://docs.docker.com/compose/install/) na máquina. Para montar a aplicação siga os passos a baixo:

```sh
 $ make install # Para buildar o container e instalar todas as dependências.
 $ make up # levanta a aplicação na porta 5000. Para acessar - http://localhost:5000/

 $ make test # executa todos os testes na aplicação
 or
 $ make test path=INFORME_O_CAMINHO_DE_UM_TESTE_ESPECIFICO
```

#### Como processar um pagamento:
A aplicação possui [swagger](https://swagger.io/) com todos os endpoint mapeados e a forma de utilizar.
