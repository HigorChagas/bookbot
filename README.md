
# BookBot

BookBot é uma ferramenta simples em Python que analisa o conteúdo de um livro em formato texto (.txt), exibindo a contagem total de palavras e a frequência de cada letra no texto.

## Funcionalidades

- Conta o número total de palavras no livro.
- Conta a frequência de cada letra (ignorando caracteres não alfabéticos).
- Ordena e exibe as letras pela frequência, da mais frequente para a menos frequente.

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/HigorChagas/bookbot.git
cd bookbot
```

2. Execute o script passando o caminho para o arquivo .txt do livro que deseja analisar:

```bash
python3 main.py caminho/para/o/livro.txt
```

Exemplo:

```bash
python3 main.py livros/meulivro.txt
```

## Estrutura do projeto

- `main.py`: Script principal que lê o arquivo e chama as funções para análise.
- `stats.py`: Contém funções para contagem de palavras e caracteres.

## Requisitos

- Python 3.x

## Requisitos adicionais

- Nenhuma biblioteca externa é necessária além do Python padrão.

## Exemplo de saída

```
============ BOOKBOT ============
Analyzing book found at livros/meulivro.txt...
----------- Word Count ----------
Found 12345 total words
--------- Character Count -------
a: 1234
b: 567
c: 890
...
============= END ===============
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---

Feito por Higor Chagas
