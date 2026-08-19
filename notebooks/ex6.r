library(palmerpenguins)
library(tidyverse)

count(penguins, species)

count(penguins, island)

'''
Saída:

A tibble: 3 × 2
species	    n
<fct>	    <int>
Adelie	    152
Chinstrap	68
Gentoo	    124

A tibble: 3 × 2
island	    n
<fct>	    <int>
Biscoe	    168
Dream	    124
Torgersen	52
'''