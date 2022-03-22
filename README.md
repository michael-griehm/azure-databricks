# azure-data-bricks

## Get Databricks API Permission Ids

    $> az ad sp show --id 2ff814a6-3304-4ab8-85cb-cd0e6f879c1d >azure_dbx_permission_list.json

## Get DBx Service Principal Token of behalf of User

- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/app-aad-token>

## Azure Data Bricks Pricing

- <https://databricks.com/product/azure-pricing>

## Databricks CLI

- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/cli/>

## Setup Key Vault Secret Scope

- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets>
- <https://docs.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes#create-an-azure-key-vault-backed-secret-scope-using-the-databricks-cli>
- <https://docs.microsoft.com/en-us/azure/databricks/security/secrets/secrets>

## Set Secret

- <https://docs.microsoft.com/en-us/azure/databricks/security/secrets/secrets>

## Access Azure Data Lake Gen 2 from Azure Databricks

- <https://docs.databricks.com/data/data-sources/azure/adls-gen2/azure-datalake-gen2-get-started.html>

## Convert Binary to String with DataFrame and Python

- <https://stackoverflow.com/questions/57186799/how-to-extract-columns-from-binarytype-using-pyspark-databricks>

## Avro Guide

- <https://spark.apache.org/docs/latest/sql-data-sources-avro.html#supported-types-for-spark-sql---avro-conversion>
- <https://docs.microsoft.com/en-us/azure/databricks/data/data-sources/read-avro>
- <https://docs.databricks.com/data/data-sources/read-avro.html>

## Pandas and Pythons

- <https://www.geeksforgeeks.org/python-pandas-dataframe/>

## Sort a Data Frame

- <https://sparkbyexamples.com/spark/spark-how-to-sort-dataframe-column-explained/>

## Mount Databricks to ADLS Gen 2

- <https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-use-databricks-spark>

## References

- <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/databricks_workspace>
- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/terraform/azure-workspace>
- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/terraform/>
- <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet>
- <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/databricks_workspace#vnet_address_prefix>
- <https://techcommunity.microsoft.com/t5/azure-data-factory-blog/azure-databricks-activities-now-support-managed-identity/ba-p/1922818>
- <https://docs.microsoft.com/en-us/azure/databricks/dev-tools/terraform/workspace-management>
- <https://www.azenix.com.au/blog/databricks-on-azure-with-terraform>
