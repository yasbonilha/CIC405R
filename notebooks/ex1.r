library(tidyverse)
library(palmerpenguins)

R.version.string
packageVersion("dplyr")
packageVersion("ggplot2")
dim(penguins)
head(penguins)

'''
Saída:

R version 4.6.1 (2026-06-24)
[1] ‘1.2.1’
[1] ‘4.0.3’
3448
                            A tibble: 6 × 8
species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	    sex	    year
<fct>	<fct>	        <dbl>	    <dbl>	        <int>	            <int>	    <fct>	<int>
Adelie	Torgersen	     39.1	    18.7	         181	            3750	    male	2007
Adelie	Torgersen	     39.5	    17.4	         186	            3800	    female	2007
Adelie	Torgersen	     40.3	    18.0	         195	            3250	    female	2007
Adelie	Torgersen	     NA 	    NA	             NA	                NA	        NA	    2007
Adelie	Torgersen	     36.7	    19.3	         193	            3450	    female	2007
Adelie	Torgersen	     39.3	    20.6	         190	            3650	    male	2007

'''