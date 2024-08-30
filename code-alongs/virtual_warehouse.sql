SHOW WAREHOUSES;

CREATE WAREHOUSE marketing_wh
WITH
WAREHOUSE_SIZE = 'X-Small'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE
INITIALLY_SUSPENDED = TRUE
COMMENT = 'No comment';


ALTER WAREHOUSE COMPUTE_WH
SET AUTO_SUSPEND = 60;

ALTER WAREHOUSE DEMO_WAREHOUSE
SET MAX_CLUSTER_COUNT = 3;