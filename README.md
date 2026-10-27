# CC8550 - Laboratório 9: Testes de Mutação

Implementação dos quatro exercícios do Laboratório 9. Cada exercício é um
projeto independente, com código em `src/`, testes em `tests/` e configuração
própria do pytest/mutmut.

## Execução

```bash
python -m pip install pytest==9.1.1 pytest-cov==7.1.0 mutmut==3.8.0
cd ex1
pytest -q --cov=src --cov-branch --cov-report=term-missing
mutmut run
mutmut results --all true
```

O mesmo procedimento pode ser repetido em `ex2`, `ex3` e `ex4`.
Para executar a mutação sem emojis na saída do terminal, use:

```bash
python scripts/mutmut_clean.py ex1
```

## Resultados finais

| Exercício | Cobertura de ramos | Gerados | Mortos | Equivalentes | Vivos não equivalentes | MS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100% | 36 | 36 | 0 | 0 | 100% |
| 2 | 100% | 16 | 16 | 0 | 0 | 100% |
| 3 | 100% | 22 | 20 | 2 | 0 | 100% |
| 4 | 100% | 27 | 25 | 2 | 0 | 100% |

O escore foi calculado por `MS = mortos / (gerados - equivalentes)`.

## Análise por exercício

### Exercício 1

A suíte inicial de dois testes exercita somente aprovação e reprovação por
média. Não alcança as validações, recuperação nem reprovação por falta. A
melhoria adiciona fronteiras de média/presença, todos os resultados e as duas
mensagens de erro. O uso de `pytest.raises(ValueError, match=msg)` com regex
ancorada também mata mutantes que alteram a mensagem.

Na medição intermediária, antes de ancorar as mensagens e completar as
fronteiras, havia 8 mutantes vivos entre 36. Depois, todos os 36 foram mortos.

### Exercício 2

O assert inicial `total > 0` comprova apenas que o resultado é positivo. O
assert exato e as entradas de quatro itens e de preço fracionário verificam,
respectivamente, o cálculo do desconto, a fronteira do quarto item e o
arredondamento. A suíte final matou os 16 mutantes.

### Exercício 3

Os testes cobrem lista vazia, singleton, máximo no início, no meio, no fim e
empate. Os dois sobreviventes finais são equivalentes:

- `>` por `>=` em `maior`: o valor máximo devolvido não muda em caso de empate;
- `range(1, len(temps))` por `range(len(temps))` em `dia_do_maior`: comparar o
	primeiro elemento consigo mesmo não altera a posição.

Assim, `MS = 20 / (22 - 2) = 100%`.

### Exercício 4

A suíte usa valor-limite para `n = 0, 1, 3, 4, 12, 13`, além de um caso que
revela o arredondamento da parcela. Os dois sobreviventes são equivalentes:
`n <= 3` por `n < 3` produz os mesmos juros quando `n = 3`, e a alteração da
mensagem não é observável porque a especificação exige apenas `ValueError`.

Para a análise de segunda ordem, combinei manualmente o mutante que altera
`n > 12` e o mutante que altera a fórmula do juros, ambos mortos
individualmente pela suíte. A suíte também mata a combinação, pois os efeitos
continuam observáveis nos casos `n = 13` e `n = 4/12`. Isso é compatível com o
efeito de acoplamento discutido por Offutt (1992): mutantes de ordem superior
podem mascarar efeitos, mas não necessariamente sobrevivem quando os testes
exercitam as fronteiras e os resultados afetados.