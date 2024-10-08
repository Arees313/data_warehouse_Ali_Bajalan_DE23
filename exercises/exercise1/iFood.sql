CREATE DATABASE IFOOD;

CREATE SCHEMA IF NOT EXISTS ifood.staging;

CREATE ROLE EXTRACT_LOADER;

USE ROLE ACCOUNTADMIN;

ALTER USER extract_loader
    SET PASSWORD = 'Extract123!',       -- Replace with a secure password
    DEFAULT_ROLE = extract_loader,      -- Assign the role that has appropriate privileges
    DEFAULT_WAREHOUSE = marketing_wh,   -- Replace with your warehouse name
    DEFAULT_NAMESPACE = ifood.staging,  -- Sets default database and schema
    MUST_CHANGE_PASSWORD = TRUE;        -- Force the user to change the password upon first login

ALTER USER EXTRACT_LOADER
    SET PASSWORD = 'Ali12345';

SHOW USERS LIKE 'extract_loader';
SHOW USERS;
SHOW DATABASES;
DESCRIBE USER extract_loader;


CREATE ROLE marketing_dlt_role;

GRANT USAGE ON DATABASE IFOOD TO ROLE MARKETING_DLT_ROLE;
GRANT USAGE ON SCHEMA IFOOD.STAGING TO ROLE MARKETING_DLT_ROLE;

GRANT SELECT ON ALL TABLES IN SCHEMA IFOOD.STAGING TO ROLE MARKETING_DLT_ROLE;

GRANT INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA IFOOD.STAGING TO ROLE MARKETING_DLT_ROLE;
GRANT INSERT, DELETE, UPDATE ON FUTURE TABLES IN SCHEMA IFOOD.STAGING TO ROLE MARKETING_DLT_ROLE;

GRANT ROLE MARKETING_DLT_ROLE TO USER EXTRACT_LOADER;

USE ROLE ORGADMIN;

USE WAREHOUSE MARKETING_WH;
SHOW ACCOUNTS;

SHOW USERS;



USE DATABASE IFOOD;
USE WAREHOUSE MARKETING_WH;

USE WAREHOUSE COMPUTE_WH;
