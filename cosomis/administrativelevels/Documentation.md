# Administrative Level documentation

Before a provided user interface to load the administrative levels, a simple way to do it, is by using the shell.

Given a file `adminlevels.xlsx` structured like this:

| DÉPARTEMENT | COMMUNE   | ARRONDISSEMENT | VILLAGE |
| ----------- | --------- | -------------- | ------- |
| ALIBORI     | BANIKOARA | SOROKO         | Mékrou  |
| ATACORA     | KOUANDE   | OROUKAYO       | Pélima  |

Run this in the shell to save the datas to the MIS database:

```
import pandas as pd
from administrativelevels.functions import save_adm_lvl_csv_datas_to_db
df = pd.read_excel("adminlevels.xlsx")
adminlevels = df.to_dict()
save_adm_lvl_csv_datas_to_db(adminlevels)
```