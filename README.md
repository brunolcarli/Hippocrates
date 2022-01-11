<table align="center"><tr><td align="center" width="9999">

<img src="https://cdn.pixabay.com/photo/2020/10/16/22/46/hippocrates-5660772_960_720.png" align="center" width="100" alt="Project icon">

# Hippocrates

*Melanoma detection app*
</td></tr></table>


<div align="center">

> [![Version badge](https://img.shields.io/badge/version-0.0.0-silver.svg)]()

</div>

[Hippocrates](https://en.wikipedia.org/wiki/Hippocrates) é uma aplicação para teste de detecção de Melanoma (câncer de pele) a partir de uma imagem enviada para a aplicação. O serviço é parte integrante e demonstrativo de um trabalho para a disciplina de **Visão Computacional** no curso de Especialização em Inteligência Artificial Aplicada da **Universidade Federal do Paraná **(UFPR) para o Professor Dr. Lucas Ferrari de Oliveira.

O serviço utiliza um modelo de machine learning treinado a partir dos dados fornecidos para o desenvolvimento do trabalho, processar e classificar imagens de melanoma em duas classes:

- Melanoma: Caso positivo para câncer maligno;
- Controle: Caso negativo para câncer maligno;

O princípio do trabalho consiste em elaborar um fluxo de processamento de imagems para a base de dados fornecida (68 amostras) e classificar os dados com machine learning.

O nome do serviço é uma homenagem ao pensador grego de mesmo nome da era de 460 - 370 AC, cujo foi considerado um dos pais da medicina e primeiro homem a descrever e registrar o melanoma.




Uma demo está disponível em: `https://hippocrates.brunolcarli.repl.co/`

Uma API Graphql da aplicação é aberta e disponibilizada no endpoint: `https://hippocrates.brunolcarli.repl.co/graphq/`

</div>

## Executando localmente

> OS Ref: Linux | OSX

Para executar o serviço clone o repositório, inicie um ambiente virtual python (*virtualenv*) e instale as dependências do projeto:

```
$ make install
```

Defina um valor para as variáveis de ambiente do serviço. Isso pode ser feito manualmente pelo *shell* exportando as variáveis:


```
$ export SECRET_KEY=any_kind_of_stuff_you_desire
$ export ENV_REF=common
```

Ou através de um arquivo `.env` definido na raiz do projeto:

```
SECRET_KEY=any_kind_of_stuff_you_desire
ENV_REF=common
```


Execute o serrviço com:

```
$ make run
```

A aplicação estará disponível em `localhost:8787` e a API em `localhost:8787/graphql/`.