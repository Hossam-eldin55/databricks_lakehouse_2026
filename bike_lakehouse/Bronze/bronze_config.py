Base_path = '/Volumes/workspace/bronze/source_systems'

INGESTION_CONFIG = [
{
    "source": "crm",
    "path": f"{Base_path}/source_crm/cust_info.csv",
    "target": "crm_cust_info"
},
{
    "source": "crm",
    "path": f"{Base_path}/source_crm/prd_info.csv",
    "target": "crm_prd_info"
},
{
    "source": "crm",
    "path": f"{Base_path}/source_crm/sales_details.csv",
    "target": "crm_sales_details"
},
{
    "source": "erp",
    "path": f"{Base_path}/source_erp/CUST_AZ12.csv",
    "target": "erp_CUST_AZ12"
},
{
    "source": "erp",
    "path": f"{Base_path}/source_erp/LOC_A101.csv",
    "target": "erp_LOC_A101"
},
{
    "source": "erp",
    "path": f"{Base_path}/source_erp/PX_CAT_G1V2.csv",
    "target": "PX_CAT_G1V2"
}
]