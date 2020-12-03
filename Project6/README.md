# Data Engineering Capstone Project
---

## **Overview**
---
This project is based on the Open Payments program, managed by the Ceneters for Medicare & Medicaid Services. According to their
documentation, the program "promotes transparency and accountability by helping consumers understand the financial relationships between pharmaceutical and medical device industries, and physicians and teaching hospitals". This project is meant to narrow the scope of finding physicians and services or products. The General payment dataset for a single year is more than 10 million lines and more than 70 columns.

## **Project Datasets**
---
The datasets reside in AWS S3. Links for the datasets are as follows:

General Payment Details: ```S3://cms-op-data/OP_DTL_GNRL_PGYR2019_P06302020.csv``` (file is broken up with a suffix of 0 to 10 at the end of the filename and each file contains approx. 1 million lines of data. A manifest file has been added.)

Research Payment Details: ```S3://cms-op-data/OP_DTL_RSRCH_PGYR2019_P06302020.csv```

Physician Ownership Details: ```S3://cms-op-data/OP_DTL_OWNRSHP_PGYR2019_P06302020.csv```

## **General Payment Dataset**
---
Sample record:
```csv
Change_Type, Covered_Recipient_Type, Teaching_Hospital_CCN, Teaching_Hospital_ID, Teaching_Hospital_Name, Physician_Profile_ID, Physician_First_Name, Physician_Middle_Name, Physician_Last_Name, Physician_Name_Suffix, Recipient_Primary_Business_Street_Address_Line1, Recipient_Primary_Business_Street_Address_Line2, Recipient_City, Recipient_State, Recipient_Zip_Code, Recipient_Country, Recipient_Province, Recipient_Postal_Code, Physician_Primary_Type, Physician_Specialty, Physician_License_State_code1, Physician_License_State_code2, Physician_License_State_code3, Physician_License_State_code4, Physician_License_State_code5, Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name, Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID, Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name, Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State, Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country, Total_Amount_of_Payment_USDollars, Date_of_Payment, Number_of_Payments_Included_in_Total_Amount, Form_of_Payment_or_Transfer_of_Value, Nature_of_Payment_or_Transfer_of_Value, City_of_Travel, State_of_Travel, Country_of_Travel, Physician_Ownership_Indicator, Third_Party_Payment_Recipient_Indicator, Name_of_Third_Party_Entity_Receiving_Payment_or_Transfer_of_Value, Charity_Indicator, Third_Party_Equals_Covered_Recipient_Indicator, Contextual_Information, Delay_in_Publication_Indicator, Record_ID, Dispute_Status_for_Publication, Related_Product_Indicator, Covered_or_Noncovered_Indicator_1, Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1, Product_Category_or_Therapeutic_Area_1, Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1, Associated_Drug_or_Biological_NDC_1, Covered_or_Noncovered_Indicator_2, Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2, Product_Category_or_Therapeutic_Area_2, Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2, Associated_Drug_or_Biological_NDC_2, Covered_or_Noncovered_Indicator_3, Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3, Product_Category_or_Therapeutic_Area_3, Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3, Associated_Drug_or_Biological_NDC_3, Covered_or_Noncovered_Indicator_4, Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4, Product_Category_or_Therapeutic_Area_4, Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4, Associated_Drug_or_Biological_NDC_4, Covered_or_Noncovered_Indicator_5, Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5, Product_Category_or_Therapeutic_Area_5, Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5, Associated_Drug_or_Biological_NDC_5, Program_Year, Payment_Publication_Date
'NEW', 'Covered Recipient Physician', '', '', '', '827477', 'STEPHEN', 'W.', 'BOATRIGHT', '', '6 WINDSONG DR', '', 'NORTH LITTLE ROCK', 'AR', '72113-9203', 'United States', '', '', 'Doctor of Dentistry', 'Dental Providers|Dentist|Endodontics', 'AR', '', '', '', '', 'Edge Endo LLC', '100000026244', 'Edge Endo LLC', 'NM', 'United States', '18.88', '05/21/2019', '1', 'In-kind items and services', 'Gift', '', '', '', 'No', 'No Third Party Payment', '', '', '', '', 'No', '618989345', 'No', 'Yes', 'Covered', 'Device', 'General Dental and Oral Health', 'EdgeOne Fire', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2019', '06/30/2020'
```

## **Research Payment Dataset**
---
Sample record:
```csv
Change_Type,Covered_Recipient_Type,Noncovered_Recipient_Entity_Name,Teaching_Hospital_CCN,Teaching_Hospital_ID,Teaching_Hospital_Name,Physician_Profile_ID,Physician_First_Name,Physician_Middle_Name,Physician_Last_Name,Physician_Name_Suffix,Recipient_Primary_Business_Street_Address_Line1,Recipient_Primary_Business_Street_Address_Line2,Recipient_City,Recipient_State,Recipient_Zip_Code,Recipient_Country,Recipient_Province,Recipient_Postal_Code,Physician_Primary_Type,Physician_Specialty,Physician_License_State_code1,Physician_License_State_code2,Physician_License_State_code3,Physician_License_State_code4,Physician_License_State_code5,Principal_Investigator_1_Profile_ID,Principal_Investigator_1_First_Name,Principal_Investigator_1_Middle_Name,Principal_Investigator_1_Last_Name,Principal_Investigator_1_Name_Suffix,Principal_Investigator_1_Business_Street_Address_Line1,Principal_Investigator_1_Business_Street_Address_Line2,Principal_Investigator_1_City,Principal_Investigator_1_State,Principal_Investigator_1_Zip_Code,Principal_Investigator_1_Country,Principal_Investigator_1_Province,Principal_Investigator_1_Postal_Code,Principal_Investigator_1_Primary_Type,Principal_Investigator_1_Specialty,Principal_Investigator_1_License_State_code1,Principal_Investigator_1_License_State_code2,Principal_Investigator_1_License_State_code3,Principal_Investigator_1_License_State_code4,Principal_Investigator_1_License_State_code5,Principal_Investigator_2_Profile_ID,Principal_Investigator_2_First_Name,Principal_Investigator_2_Middle_Name,Principal_Investigator_2_Last_Name,Principal_Investigator_2_Name_Suffix,Principal_Investigator_2_Business_Street_Address_Line1,Principal_Investigator_2_Business_Street_Address_Line2,Principal_Investigator_2_City,Principal_Investigator_2_State,Principal_Investigator_2_Zip_Code,Principal_Investigator_2_Country,Principal_Investigator_2_Province,Principal_Investigator_2_Postal_Code,Principal_Investigator_2_Primary_Type,Principal_Investigator_2_Specialty,Principal_Investigator_2_License_State_code1,Principal_Investigator_2_License_State_code2,Principal_Investigator_2_License_State_code3,Principal_Investigator_2_License_State_code4,Principal_Investigator_2_License_State_code5,Principal_Investigator_3_Profile_ID,Principal_Investigator_3_First_Name,Principal_Investigator_3_Middle_Name,Principal_Investigator_3_Last_Name,Principal_Investigator_3_Name_Suffix,Principal_Investigator_3_Business_Street_Address_Line1,Principal_Investigator_3_Business_Street_Address_Line2,Principal_Investigator_3_City,Principal_Investigator_3_State,Principal_Investigator_3_Zip_Code,Principal_Investigator_3_Country,Principal_Investigator_3_Province,Principal_Investigator_3_Postal_Code,Principal_Investigator_3_Primary_Type,Principal_Investigator_3_Specialty,Principal_Investigator_3_License_State_code1,Principal_Investigator_3_License_State_code2,Principal_Investigator_3_License_State_code3,Principal_Investigator_3_License_State_code4,Principal_Investigator_3_License_State_code5,Principal_Investigator_4_Profile_ID,Principal_Investigator_4_First_Name,Principal_Investigator_4_Middle_Name,Principal_Investigator_4_Last_Name,Principal_Investigator_4_Name_Suffix,Principal_Investigator_4_Business_Street_Address_Line1,Principal_Investigator_4_Business_Street_Address_Line2,Principal_Investigator_4_City,Principal_Investigator_4_State,Principal_Investigator_4_Zip_Code,Principal_Investigator_4_Country,Principal_Investigator_4_Province,Principal_Investigator_4_Postal_Code,Principal_Investigator_4_Primary_Type,Principal_Investigator_4_Specialty,Principal_Investigator_4_License_State_code1,Principal_Investigator_4_License_State_code2,Principal_Investigator_4_License_State_code3,Principal_Investigator_4_License_State_code4,Principal_Investigator_4_License_State_code5,Principal_Investigator_5_Profile_ID,Principal_Investigator_5_First_Name,Principal_Investigator_5_Middle_Name,Principal_Investigator_5_Last_Name,Principal_Investigator_5_Name_Suffix,Principal_Investigator_5_Business_Street_Address_Line1,Principal_Investigator_5_Business_Street_Address_Line2,Principal_Investigator_5_City,Principal_Investigator_5_State,Principal_Investigator_5_Zip_Code,Principal_Investigator_5_Country,Principal_Investigator_5_Province,Principal_Investigator_5_Postal_Code,Principal_Investigator_5_Primary_Type,Principal_Investigator_5_Specialty,Principal_Investigator_5_License_State_code1,Principal_Investigator_5_License_State_code2,Principal_Investigator_5_License_State_code3,Principal_Investigator_5_License_State_code4,Principal_Investigator_5_License_State_code5,Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country,Related_Product_Indicator,Covered_or_Noncovered_Indicator_1,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1,Product_Category_or_Therapeutic_Area_1,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1,Associated_Drug_or_Biological_NDC_1,Covered_or_Noncovered_Indicator_2,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2,Product_Category_or_Therapeutic_Area_2,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2,Associated_Drug_or_Biological_NDC_2,Covered_or_Noncovered_Indicator_3,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3,Product_Category_or_Therapeutic_Area_3,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3,Associated_Drug_or_Biological_NDC_3,Covered_or_Noncovered_Indicator_4,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4,Product_Category_or_Therapeutic_Area_4,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4,Associated_Drug_or_Biological_NDC_4,Covered_or_Noncovered_Indicator_5,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5,Product_Category_or_Therapeutic_Area_5,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5,Associated_Drug_or_Biological_NDC_5,Total_Amount_of_Payment_USDollars,Date_of_Payment,Form_of_Payment_or_Transfer_of_Value,Expenditure_Category1,Expenditure_Category2,Expenditure_Category3,Expenditure_Category4,Expenditure_Category5,Expenditure_Category6,Preclinical_Research_Indicator,Delay_in_Publication_Indicator,Name_of_Study,Dispute_Status_for_Publication,Record_ID,Program_Year,Payment_Publication_Date,ClinicalTrials_Gov_Identifier,Research_Information_Link,Context_of_Research
"NEW","Covered Recipient Teaching Hospital",,"103301","8127","MIAMI CHILDRENS HOSPITAL",,,,,,"3100 SW 62ND AVE",,"MIAMI","FL","33155","United States",,,,,,,,,,"127880","IAN","O","MILLER",,"3200 SW 60th Ct Ste 302",,"Miami","FL","33155","United States",,,"Medical Doctor","Allopathic & Osteopathic Physicians|Psychiatry & Neurology|Neurology with Special Qualifications in Child Neurology","FL",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"GW Research Limited","100000486820","GW Research Limited",,"Great Britain (Uk)","Yes","Non-Covered",,,,,,,,,,,,,,,,,,,,,,,,,362.10,"02/08/2019","Cash or cash equivalent",,,,,,,"No","No","EAP","No","701776192","2019","06/30/2020",,,
```

## **Physician Ownership Dataset**
---
Sample record:
```csv
Change_Type,Physician_Profile_ID,Physician_First_Name,Physician_Middle_Name,Physician_Last_Name,Physician_Name_Suffix,Recipient_Primary_Business_Street_Address_Line1,Recipient_Primary_Business_Street_Address_Line2,Recipient_City,Recipient_State,Recipient_Zip_Code,Recipient_Country,Recipient_Province,Recipient_Postal_Code,Physician_Primary_Type,Physician_Specialty,Record_ID,Program_Year,Total_Amount_Invested_USDollars,Value_of_Interest,Terms_of_Interest,Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country,Dispute_Status_for_Publication,Interest_Held_by_Physician_or_an_Immediate_Family_Member,Payment_Publication_Date
"NEW","122203","MATTHEW","ROSS","ALBERT",,"661 E ALTAMONTE DR","SUITE 220","ALTAMONTE SPRINGS","FL","32701","United States",,,"Medical Doctor","Allopathic & Osteopathic Physicians|Colon & Rectal Surgery","623627959","2019",0.00,32500.00,"CLASS B COMMON STOCK","Applied Medical Corporation","100000005730","Applied Medical Corporation","CA","United States","No","Physician Covered Recipient","06/30/2020"

```

## **Schema**
---
### Fact Table
**physicians** - description
```
change_type, phys_id, phys_fname, phys_lname, phys_addr1, phys_addr2, phys_city, phys_st, phys_zip, phys_type, phys_spec, record_id, prog_yr, tot_amt_inv, int_val, int_term, sub_mfg_name, sub_mfg_id, sub_mfg_st, disputed
```

### Dimension Tables
**payments** - description
```
change_type, rcp_type, hosp_ccn, teach_hosp_id, teach_hosp_name, phys_id, phys_fname, phys_lname, phys_city, phys_st, phys_type, phys_spec, sub_mfg_name, sub_mfg_id, sub_mfg_st, tot_pmt, pmt_date, num_pmts, pmt_type, pmt_nature, third_party_ind, third_party_name, charity_ind, context_info, record_id, cov_noncov_ind1, product_type1, product_cat1, product_name1, product_ndc1, cov_noncov_ind2, product_type2, product_cat2, product_name2, product_ndc2, cov_noncov_ind3, product_type3, product_cat3, product_name3, product_ndc3, cov_noncov_ind4, product_type4, product_cat4, product_name4, product_ndc4, cov_noncov_ind5, product_type5, product_cat5, product_name5, product_ndc5, pmt_pub_date
```

**research** - description
```
change_type, rcp_type, hosp_ccn, noncov_rcp_name, teach_hosp_id, teach_hosp_name, phys_id, phys_fname, phys_lname, phys_addr1, phys_addr2, phys_city, phys_st, phys_zip, phys_type, phys_spec, phys_lic_st1, phys_lic_st2, phys_lic_st3, phys_lic_st4, phys_lic_st5, sub_mfg_name, sub_mfg_id, sub_mfg_st, prod_ind, prod1, prod2, prod3, prod4, ndc1, ndc2, ndc3, ndc4, ndc5, tot_pmt, pmt_date, pmt_type, pmt_cat1, pmt_cat2, pmt_cat3, pmt_cat4, pmt_cat5, pmt_cat6, name_of_study, record_id, prg_year, research_context
```

## **Project Files**
---
```dwh.cfg``` -> configuration file for AWS

```create_staging_tables.py``` -> used for creating data structure for staging tables in Redshift

```staging_sql_queries``` -> used to define SQL statements used by the ```create_staging_tables.py``` file

```create_tables.py``` -> used for creating the final data structure in Redshift

```sql_queries.py``` -> used to define SQL statements used by the ```create_tables.py``` file and the ```etl.py``` file

```etl.py``` -> used to process data into analytic tables in Redshift

```RedshiftQueries.ipynb``` -> Jupyter Notebook for summary queries

```ValidateDataRedshift.ipynb``` -> Jupyter Notebook for data validations

## **Environment**
---
Python 3.8 or above

AWS Redshift

AWS S3

psycopg2 2.8.6 - PostgresSQL database adapter for Python

sqlalchemy 1.3.20 - Python SQL toolkit for Object Realtional Mapping

JupyterLab 2.2.9

## **Setup for analytics**
---
### **Prep environment**
Create ```cms-op-data``` bucket in S3

Copy project dataset files to bucket

Create Redshift cluster

Run the ```create_staging_tables.py``` file as follows:
```
python create_staging_tables.py
```

### **Use SQL queries to copy csv data to staging tables**
Copy payments data to staging table:
```
COPY staging_payments
FROM 's3://cms-op-data/cmsop.manifest'
iam_role 'arn:aws:iam::626256558589:role/dwhRole'
dateformat 'auto'
csv
manifest;
```

Copy research data to staging table:
```
COPY staging_research
FROM 's3://cms-op-data/OP_DTL_RSRCH_PGYR2019_P06302020.csv'
iam_role 'arn:aws:iam::626256558589:role/dwhRole'
dateformat 'auto'
ignoreheader 1
csv;
```

Copy physician data to staging table:
```
COPY staging_physicians
FROM 's3://cms-op-data/OP_DTL_OWNRSHP_PGYR2019_P06302020.csv'
iam_role 'arn:aws:iam::626256558589:role/dwhRole'
dateformat 'auto'
ignoreheader 1
csv;
```

### **Load data to fact and dimension tables**
Run the ```create_tables.py``` and ```etl.py``` files as follows:
```
python create_tables.py
python etl.py
```


## **Data Quality Checks**
---
- Integrity constraints on the relational db (data types)
    - Data types were defined in the code to create all tables in Redshift. If a field failed during execution, adjustments were made to the data types, tables dropped and code re-run.
- Source/Count checks to ensure completeness
    - See ```ValidateDataRedshift.ipynb``` Jupyter notebook for data checks.


## **Logical Approach**
---
- Should the data increase by 100x, Redshift would be able to handle the storage with minor configuration modifications. In it's current configuration, the cluster is a dc2.large node type which has a max storage of 160GB and 1 node, but can handle up to 2 Petabytes, if needed, with modification to the cluster.

- CMS does not publish its data in intervals smaller than yearly, so it this particular case, daily, weekly or monthly pipelines would not be run, as this would cause unnecessary traffic on this cluster. However, if, theoretically, there was a need to run pipelines on a daily basis by 7am every day, Airflow could be used to schedule DAGs to pull in new data. Because reporting does not happen on a daily basis, if a DAG were to fail to run, a dashboard could continue showing last day data.

- Should the database need to be accessed by more than 100 people, Redshift is perfectly capable of handling the traffic with some minor configuration tweaks. It can handle 500 maximum connections, which it could handle without issue.


## **Choice of tools, technologies and data model**
---
1. Description of data model
    - There are three tables which focus on the CMS data, physician information data, payment information data and payment research data.
2. Why chose data model
    - This is the most straightforward and simplest way to present the data for running the analytics needed. There is much information from the original data file but, as stated in the summary, the scope of the data for this project was narrowed to eliminate unnecessary data fields.
3. What kind of queries do we want to explore?
    1. Top 10 providers receiving payments
    2. Top 10 Manufacturers making payments or investments to providers
    3. Top 10 NDC codes associated with provider payments/investments
4. Use cases the data is being prepared for
    - The scope of this data is narrowed and its use would be for public and private entities that want to know if a provider or hospital is receiving compensation from a device or pharmaceutical manufacturer and how much they are receiving.
    - It would also show how much money or other investment a manufacturer has paid out for the reporting year.


## **Findings**
---
Using Jupyter Notebook and Redshift queries (to verify totals) I found the following:
Top 10 providers receiving payments

| phys_id | phys_lname | phys_fname | phys_st | tot_amt_inv  |
| ------- | ---------- | ---------- | ------- | ------------ |
| 1315076 | Lopez      | George     | CA      | 276759911.11 |
| 286115  | MOLL       | FREDERIC   | CA      | 84460265.67  |
| 355094  | Steinmann  | John       | CA      | 6718139.00   |
| 40822   | Chao       | Michael    | CA      | 6000000.00   |
| 52496   | Jackson    | Frank      | PA      | 4750000.00   |
| 342101  | FREEMAN    | JOHN       | TN      | 4186000.00   |
| 221546  | FREEMAN    | JAMES      | TN      | 4186000.00   |
| 411850  | Cirksena   | William    | MD      | 3300000.00   |
| 245560  | Scheker    | Luis       | KY      | 2577614.00   |
| 164611  | Chaitoff   | Jeffrey    | OH      | 2294231.00   |


Top 10 Manufacturers Making payments or investments to providers

| sub_mfg_id   | sub_mfg_name                        | tot_amt_inv  |
| ------------ | ----------------------------------- | ------------ |
| 100000010657 | ICU Medical Inc                     | 276759911.11 |
| 100000226828 | Auris Health, Inc.                  | 84460265.67  |
| 100000005426 | Renovis Surgical Technologies, Inc. | 6718139.00   |
| 100000010807 | Parsolex GMP Center, Inc.           | 6000000.00   |
| 100000076364 | GI Supply, Inc.                     | 4750000.00   |
| 100000041242 | Grace Medical, Inc.                 | 4186000.00   |
| 100000071358 | Vapotherm Inc                       | 3300000.00   |
| 100000010554 | Aptis Medical, LLC                  | 2577614.00   |
| 100000151627 | SPR Therapeutics, Inc               | 2294231.00   |
| 100000196812 | AxioMed LLC                         | 2000000.00   |


Top 10 NDC codes associated with provider payments/investments

| ndc1         | count |
| ------------ | ----- |
| 0006-3029-02 | 34332 |
| 64678-211-01 | 25070 |
| 0597-0152-30 | 11730 |
| 62856-710-30 | 8525  |
| 0074-0038-28 | 6271  |
| 0069-0187-21 | 4974  |
| 0051-8462-33 | 4936  |
| 0024-5914-01 | 4850  |
| 0093-3607-82 | 4188  |
| 65597-406-01 | 4139  |

#### References:
[2019 Program Year Open Payments Dataset](https://www.cms.gov/OpenPayments/Explore-the-Data/Dataset-Downloads)

[Open Payments Methodology & Data Dictionary](https://www.cms.gov/OpenPayments/Downloads/OpenPaymentsDataDictionary.pdf)

