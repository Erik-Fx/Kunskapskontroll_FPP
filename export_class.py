import pandas as pd
import sqlite3
import logging


class DataExport:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.logger = logging.getLogger(__name__)
          
    def data_exporter(self):
        """Exporting a dataframe to a SQL database."""
        self.logger.info("Starting to export the data to database.")
        try:
            #Creating a connection to the SQL database "inflation_data"
            with sqlite3.connect('inflation_data.db') as con:
                self.df.to_sql('cleaned_data_test', con, if_exists='replace')
                self.logger.info("Data exported successfully.")
                
        except sqlite3.Error as e:
            #Logs errors specific to SQLite and raises them
            self.logger.error(f"SQLite Error: {e} ")
            raise
        
        except Exception as e:
            #Logs unexpected errors and raises them
            self.logger.error(f"A unexpected error occurred: {e}")
            raise
