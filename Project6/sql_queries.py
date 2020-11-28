import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
IAM_ROLE = config['IAM_ROLE']['ARN']
PMT_DATA = config['S3']['PMT_DATA']
RSH_DATA = config['S3']['RSH_DATA']
PHY_DATA = config['S3']['PHY_DATA']

# DROP TABLES

physicians_table_drop = "DROP TABLE IF EXISTS physicians"
payments_table_drop = "DROP TABLE IF EXISTS payments"
research_table_drop = "DROP TABLE IF EXISTS research"

# CREATE TABLES

physicians_table_create = ("""
                        CREATE TABLE IF NOT EXISTS physicians (
                        change_type         VARCHAR(20),
                        phys_id             NUMERIC(38,0),
                        phys_fname          VARCHAR(20),
                        phys_lname          VARCHAR(35),
                        phys_addr1          VARCHAR(55),
                        phys_addr2          VARCHAR(55),
                        phys_city           VARCHAR(40),
                        phys_st             CHAR(2),
                        phys_zip            VARCHAR(10),
                        phys_type           VARCHAR(50),
                        phys_spec           VARCHAR(300),
                        record_id           NUMERIC(38,0),
                        prog_yr             CHAR(4),
                        tot_amt_inv         NUMERIC(12,2),
                        int_val             NUMERIC(12,2),
                        int_term            VARCHAR(500),
                        sub_mfg_name        VARCHAR(100),
                        sub_mfg_id          NUMERIC(38,0),
                        sub_mfg_st          CHAR(2),
                        disputed            CHAR(3))
""")

payments_table_create = ("""
                        CREATE TABLE IF NOT EXISTS payments (
                        change_type         VARCHAR(20),
                        rcp_type            VARCHAR(50),
                        teach_hosp_ccn      VARCHAR(6),
                        teach_hosp_id       NUMERIC(38,0),
                        teach_hosp_name     VARCHAR(100),
                        phys_id             NUMERIC(38,0),
                        phys_fname          VARCHAR(20),
                        phys_lname          VARCHAR(35),
                        phys_city           VARCHAR(40),
                        phys_st             CHAR(2),
                        phys_type           VARCHAR(100),
                        phys_spec           VARCHAR(300),
                        sub_mfg_name        VARCHAR(100),
                        sub_mfg_id          VARCHAR(12),
                        sub_mfg_st          CHAR(2),
                        tot_pmt             NUMERIC(12,2),
                        pmt_date            DATE,
                        num_pmts            NUMERIC(3,0),
                        pmt_type            VARCHAR(100),
                        pmt_nature          VARCHAR(200),
                        third_party_ind     VARCHAR(50),
                        third_party_name    VARCHAR(50),
                        charity_ind         CHAR(3),
                        context_info        VARCHAR(500),
                        record_id           NUMERIC(38,0),
                        cov_noncov_ind1     VARCHAR(100),
                        product_type1       VARCHAR(100),
                        product_cat1        VARCHAR(100),
                        product_name1       VARCHAR(500),
                        product_ndc1        VARCHAR(100),
                        cov_noncov_ind2     VARCHAR(100),
                        product_type2       VARCHAR(100),
                        product_cat2        VARCHAR(100),
                        product_name2       VARCHAR(500),
                        product_ndc2        VARCHAR(100),
                        cov_noncov_ind3     VARCHAR(100),
                        product_type3       VARCHAR(100),
                        product_cat3        VARCHAR(100),
                        product_name3       VARCHAR(500),
                        product_ndc3        VARCHAR(100),
                        cov_noncov_ind4     VARCHAR(100),
                        product_type4       VARCHAR(100),
                        product_cat4        VARCHAR(100),
                        product_name4       VARCHAR(500),
                        product_ndc4        VARCHAR(100),
                        cov_noncov_ind5     VARCHAR(100),
                        product_type5       VARCHAR(100),
                        product_cat5        VARCHAR(100),
                        product_name5       VARCHAR(500),
                        product_ndc5        VARCHAR(100),
                        pmt_pub_date        DATE)
""")

research_table_create = ("""
                        CREATE TABLE IF NOT EXISTS research (
                        change_type         VARCHAR(20),
                        rcp_type            VARCHAR(50),
                        noncov_rcp_name     VARCHAR(50),
                        teach_hosp_ccn      VARCHAR(6),
                        teach_hosp_id       NUMERIC(38,0),
                        teach_hosp_name     VARCHAR(100),
                        phys_id             NUMERIC(38,0),
                        phys_fname          VARCHAR(20),
                        phys_lname          VARCHAR(35),
                        phys_addr1          VARCHAR(55),
                        phys_addr2          VARCHAR(55),
                        phys_city           VARCHAR(40),
                        phys_st             CHAR(2),
                        phys_zip            VARCHAR(10),
                        phys_type           VARCHAR(50),
                        phys_spec           VARCHAR(300),
                        phys_lic_st1        CHAR(2),
                        phys_lic_st2        CHAR(2),
                        phys_lic_st3        CHAR(2),
                        phys_lic_st4        CHAR(2),
                        phys_lic_st5        CHAR(2),
                        sub_mfg_name        VARCHAR(100),
                        sub_mfg_id          NUMERIC(38,0),
                        sub_mfg_st          CHAR(2),
                        prod_ind            VARCHAR(100),
                        prod1               VARCHAR(100),
                        prod2               VARCHAR(100),
                        prod3               VARCHAR(100),
                        prod4               VARCHAR(100),
                        prod5               VARCHAR(100),
                        ndc1                VARCHAR(100),
                        ndc2                VARCHAR(100),
                        ndc3                VARCHAR(100),
                        ndc4                VARCHAR(100),
                        ndc5                VARCHAR(100),
                        tot_pmt             NUMERIC(12,2),
                        pmt_date            DATE,
                        pmt_type            VARCHAR(100),
                        pmt_cat1            VARCHAR(50),
                        pmt_cat2            VARCHAR(50),
                        pmt_cat3            VARCHAR(50),
                        pmt_cat4            VARCHAR(50),
                        pmt_cat5            VARCHAR(50),
                        pmt_cat6            VARCHAR(50),
                        name_of_study       VARCHAR(500),
                        record_id           NUMERIC(38,0),
                        prg_year            CHAR(4),
                        research_context    VARCHAR(500))
                        """)

# FINAL TABLES

physician_table_insert = ("""
                            INSERT INTO physicians (
                            change_type,
                            phys_id,
                            phys_fname,
                            phys_lname,
                            phys_addr1,
                            phys_addr2,
                            phys_city,
                            phys_st,
                            phys_zip,
                            phys_type,
                            phys_spec,
                            record_id,
                            prog_yr,
                            tot_amt_inv,
                            int_val,
                            int_term,
                            sub_mfg_name,
                            sub_mfg_id,
                            sub_mfg_st,
                            disputed
                        )
                        SELECT
                            Change_Type,
                            Physician_Profile_ID,
                            Physician_First_Name,
                            Physician_Last_Name,
                            Recipient_Primary_Business_Street_Address_Line1,
                            Recipient_Primary_Business_Street_Address_Line2,
                            Recipient_City,
                            Recipient_State,
                            Recipient_Zip_Code,
                            Physician_Primary_Type,
                            Physician_Specialty,
                            Record_ID,
                            Program_Year,
                            Total_Amount_Invested_USDollars,
                            Value_of_Interest,
                            Terms_of_Interest,
                            Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,
                            Dispute_Status_for_Publication
                        FROM
                            staging_physicians
                        """)

payments_table_insert = ("""
                            INSERT INTO payments (
                            change_type,
                            rcp_type,
                            teach_hosp_ccn,
                            teach_hosp_id,
                            teach_hosp_name,
                            phys_id,
                            phys_fname,
                            phys_lname,
                            phys_city,
                            phys_st,
                            phys_type,
                            phys_spec,
                            sub_mfg_name,
                            sub_mfg_id,
                            sub_mfg_st,
                            tot_pmt,
                            pmt_date,
                            num_pmts,
                            pmt_type,
                            pmt_nature,
                            third_party_ind,
                            third_party_name,
                            charity_ind,
                            context_info,
                            record_id,
                            cov_noncov_ind1,
                            product_type1,
                            product_cat1,
                            product_name1,
                            product_ndc1,
                            cov_noncov_ind2,
                            product_type2,
                            product_cat2,
                            product_name2,
                            product_ndc2,
                            cov_noncov_ind3,
                            product_type3,
                            product_cat3,
                            product_name3,
                            product_ndc3,
                            cov_noncov_ind4,
                            product_type4,
                            product_cat4,
                            product_name4,
                            product_ndc4,
                            cov_noncov_ind5,
                            product_type5,
                            product_cat5,
                            product_name5,
                            product_ndc5,
                            pmt_pub_date
                        )
                        SELECT
                            Change_Type,
                            Covered_Recipient_Type,
                            Teaching_Hospital_CCN,
                            Teaching_Hospital_ID,
                            Teaching_Hospital_Name,
                            Physician_Profile_ID,
                            Physician_First_Name,
                            Physician_Last_Name,
                            Recipient_City,
                            Recipient_State,
                            Primary_Physician_Type,
                            Physician_Specialty,
                            Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,
                            Total_Amount_of_Payment_USDollars,
                            Date_of_Payment,
                            Number_of_Payments_Included_in_Total_Amount,
                            Form_of_Payment_or_Transfer_of_Value,
                            Nature_of_Payment_or_Transfer_of_Value,
                            Third_Party_Payment_Recipient_Indicator,
                            Name_of_Third_Party_Entity_Receiving_Payment_or_Transfer_of_Value,
                            Charity_Indicator,
                            Contextual_Information,
                            Record_ID,
                            Covered_or_Noncovered_Indicator_1,
                            Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1,
                            Product_Category_or_Therapeutic_Area_1,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1,
                            Associated_Drug_or_Biological_NDC_1,
                            Covered_or_Noncovered_Indicator_2,
                            Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2,
                            Product_Category_or_Therapeutic_Area_2,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2,
                            Associated_Drug_or_Biological_NDC_2,
                            Covered_or_Noncovered_Indicator_3,
                            Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3,
                            Product_Category_or_Therapeutic_Area_3,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3,
                            Associated_Drug_or_Biological_NDC_3,
                            Covered_or_Noncovered_Indicator_4,
                            Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4,
                            Product_Category_or_Therapeutic_Area_4,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4,
                            Associated_Drug_or_Biological_NDC_4,
                            Covered_or_Noncovered_Indicator_5,
                            Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5,
                            Product_Category_or_Therapeutic_Area_5,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4,
                            Associated_Drug_or_Biological_NDC_5,
                            Payment_Publication_Date
                        FROM
                            staging_payments
                            """)

research_table_insert = ("""
                            INSERT INTO research (
                            change_type,
                            rcp_type,
                            noncov_rcp_name,
                            teach_hosp_ccn,
                            teach_hosp_id,
                            teach_hosp_name,
                            phys_id,
                            phys_fname,
                            phys_lname,
                            phys_addr1,
                            phys_addr2,
                            phys_city,
                            phys_st,
                            phys_zip,
                            phys_type,
                            phys_spec,
                            phys_lic_st1,
                            phys_lic_st2,
                            phys_lic_st3,
                            phys_lic_st4,
                            phys_lic_st5,
                            sub_mfg_name,
                            sub_mfg_id,
                            sub_mfg_st,
                            prod_ind,
                            prod1,
                            prod2,
                            prod3,
                            prod4,
                            prod5,
                            ndc1,
                            ndc2,
                            ndc3,
                            ndc4,
                            ndc5,
                            tot_pmt,
                            pmt_date,
                            pmt_type,
                            pmt_cat1,
                            pmt_cat2,
                            pmt_cat3,
                            pmt_cat4,
                            pmt_cat5,
                            pmt_cat6,
                            name_of_study,
                            record_id,
                            prg_year,
                            research_context
                        )
                        SELECT
                            Change_Type,
                            Covered_Recipient_Type,
                            Noncovered_Recipient_Entity_Name,
                            Teaching_Hospital_CCN,
                            Teaching_Hospital_ID,
                            Teaching_Hospital_Name,
                            Physician_Profile_ID,
                            Physician_First_Name,
                            Physician_Last_Name,
                            Recipient_Primary_Business_Address_Line1,
                            Recipient_Primary_Business_Address_Line2,
                            Recipient_City,
                            Recipient_State,
                            Recipient_Zip_Code,
                            Physician_Primary_Type,
                            Physician_Specialty,
                            Physician_License_State_code1,
                            Physician_License_State_code2,
                            Physician_License_State_code3,
                            Physician_License_State_code4,
                            Physician_License_State_code5,
                            Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,
                            Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,
                            Related_Product_Indicator,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4,
                            Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5,
                            Associated_Drug_or_Biological_NDC_1,
                            Associated_Drug_or_Biological_NDC_2,
                            Associated_Drug_or_Biological_NDC_3,
                            Associated_Drug_or_Biological_NDC_4,
                            Associated_Drug_or_Biological_NDC_5,
                            Total_Amount_of_Payment_USDollars,
                            Date_of_Payment,
                            Form_of_Payment_or_Transfer_of_Value,
                            Expenditure_Category1,
                            Expenditure_Category2,
                            Expenditure_Category3,
                            Expenditure_Category4,
                            Expenditure_Category5,
                            Expenditure_Category6,
                            Name_of_Study,
                            Record_ID,
                            Program_Year,
                            Context_of_Research
                        FROM
                            staging_research
                            """)

# QUERY LISTS

create_table_queries = [physicians_table_create, payments_table_create, research_table_create]
drop_table_queries = [physicians_table_drop, payments_table_drop, research_table_drop]
insert_table_queries = [physician_table_insert, payments_table_insert, research_table_insert]
