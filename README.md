# Inflation Data Processing Project

## Overview
This project is designed to create a pipline that load, clean, and export data from an Excel file to a SQL database.
The workflow consists of 5 python scripts that handel the diffrent tasks, like data loading, cleaning, exporting, and testing.
Each script has there own class for better organization and reusability.

## Project Structure
import_class.py: Contains the DataLoader class, which loads the data from an Excel file.

clean_class.py: Contains the DataCleaner class, which cleans the data with diffrent functions like changing formats and replacing missing values.

export_class.py: Contains the DataExport class, which exports the data to a SQL database.

main.py: The main script which does the import, cleaning, and exporting.

t_test.py: Contains tests for some of the scripts.


## Dependencies
pandas: For data manipulation.

numpy: For numerical operations.

sqlite3: For interacting with the SQL database.

pytest: For testing classes and their methods.

logging: For logging the process and error messages.
