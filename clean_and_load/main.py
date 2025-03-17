from typing import Set
from facts.indicatori_econ_161_268 import clean_161_268
from facts.pernottamenti_68_357 import clean_68_357
from facts.dati_strutture_122_54 import clean_122_54
from dimensions.download_dimensions import download_dimensions
from download_structures import get_structure
from db_operations.db_operations import *

# Selected datastructures to get dimensions
structures = ["DCSC_TUR", "DCCV_TURNOT_CAPI", "DCSP_SBSREG"]

# enum for fact table names
fact_tables = {
    "turismo": "facts_turismo",
    "pernottamenti": "facts_pernottamenti",
    "indicatori_econ": "facts_indicatori_economici",
}

# set to group dimension without repetitions
dimensions: Set[str] = set()

# download all of the structures and add them to the dimension set
for structure in structures:
    struct = get_structure(structure)
    dimensions.update(struct)

print("----------------------------------------------------------------------")
print("Downloading Dimensions: \n")
df_dimensions = download_dimensions(dimensions)

print("----------------------------------------------------------------------")
print("Downloading Dataflows: \n")
df_161_268 = clean_161_268()
df_68_357 = clean_68_357()
df_122_54 = clean_122_54()
print("----------------------------------------------------------------------")

print("Uploading dimensions: \n")
for dim_name, dim_df in zip(dimensions, df_dimensions):
    print(f"- Uploading {dim_name}...")
    upsert_dataframe(f"dim_{dim_name.lower()}", dim_df)
print("----------------------------------------------------------------------")

print("Truncating Fact Tables:\n")
for table in fact_tables.values():
    print(f"- Truncating {table}...")
    truncate_table(table)
print("----------------------------------------------------------------------")


print("Uploading Dataflows:\n")
bulk_insert(fact_tables["turismo"], df_122_54)
bulk_insert(fact_tables["pernottamenti"], df_68_357)
bulk_insert(fact_tables["indicatori_econ"], df_161_268)

print("----------------------------------------------------------------------")
