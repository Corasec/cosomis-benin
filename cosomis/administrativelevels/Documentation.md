# Administrative Level documentation

Administrative levels can be created by loading csv or excel file
on the "Niveaux administratifs" page on the dashboard.

Make sure you created first a `administrative_levels` database for the couch db.

For example, a file named `adminlevels.xlsx` will be structured like this:

| DÉPARTEMENT | COMMUNE   | ARRONDISSEMENT | VILLAGE |
| ----------- | --------- | -------------- | ------- |
| ALIBORI     | BANIKOARA | SOROKO         | Mékrou  |
| ATACORA     | KOUANDE   | OROUKAYO       | Pélima  |

You can also run this in the shell to save the datas to the MIS database:

```
import pandas as pd
from administrativelevels.functions import save_adm_lvl_csv_datas_to_db
df = pd.read_excel("adminlevels.xlsx")
adminlevels = df.to_dict()
save_adm_lvl_csv_datas_to_db(adminlevels)
```

Depending on your setup you may also want to create an 
administrative level corresponding to the Country following this
model in the couch db

{
  "administrative_id": "447",
  "name": "BENIN",
  "administrative_level": null,
  "type": "administrative_level",
  "parent_id": null,
  "latitude": null,
  "longitude": null
}
and update the highest administratives level `parent_id`, with this 
new object `administrative_id`. In our previous example we will update all "département" i.e Alibori and Atacora