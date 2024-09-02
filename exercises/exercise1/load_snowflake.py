import dlt
import pandas as pd
from pathlib import Path
import os

# Used for extracting data from source, in this case a local CSV file
@dlt.resource(write_disposition="append")
def load_csv_resource(file_path: str, **kwargs):
    df = pd.read_csv(file_path, **kwargs)  # Adjust to read_excel if using Excel
    yield df.to_dict(orient="records")

if __name__ == "__main__":
    # Define the path to the file
    working_directory = Path("C:/Users/Ali/Desktop/Gitbash/data_warehouse_Ali_Bajalan_DE23/exercises/exercise1")
    file_path = working_directory / "iFood_df.csv"  # Adjust if the file is a CSV or Excel

    # Print out the file path to debug
    print("Checking file path:", file_path)
    print("Absolute path:", os.path.abspath(file_path))
    
    # Check if the file exists
    if not file_path.is_file():
        print(f"Error: The file {file_path} does not exist or is not a file.")
    else:
        # Pipeline setup and execution
        pipeline = dlt.pipeline(
            pipeline_name="load_snowflake_ifood",
            destination="snowflake",
            dataset_name="staging"  # This is the schema
        )

        data = list(
            load_csv_resource(
                file_path, encoding="latin1"  # Adjust encoding if necessary
            )
        )

        # Print the data yielded from resource
        print(data)

        # Run the pipeline with the correct parameters
        load_info = pipeline.run(data, table_name="marketing_data")  # Adjust the table name

        # Pretty print the information on data that was loaded
        print(load_info)