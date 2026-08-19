library(tidyverse)

df <- tibble(
  nome = c('yasmin', 'íris', 'lucas', 'guilherme', 'vitor', 'ana', 'carol'),
  idade = c(20, 21, 22, 23, 24, 25, 26),
  nota = c(9.5, 8.0, 7.5, 6.0, 5.5, 4.0, 3.5)
)

summarise(df, media = mean(nota))

df |>
  filter(nota > 7) |>
  select(nome, nota)

'''
Saída:

A tibble: 1 × 1
media
<dbl>
6.285714

A tibble: 3 × 2
nome	nota
<chr>	<dbl>
yasmin	9.5
íris	8.0
lucas	7.5

O comando em pandas seria:
df[df.nota > 7][["nome", "nota"]] ou usando o método .loc, como feito no exercício anterior.
'''