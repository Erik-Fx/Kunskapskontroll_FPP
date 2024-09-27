import logging
import pandas as pd
import numpy as np


class DataCleaner:
    """A class to clean the Inflation dataset."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.logger = logging.getLogger(__name__)
        
    def replace_name(self):
        """Replacing the name GEO(Labels) with Country."""
        self.logger.info("Replacing the name GEO(Labels) with Country.")
        
        try:
            #Converting the data to string type.
            self.df = self.df.astype(str)
            
            #Replacing the desierd name.
            self.df.replace({"GEO(Labels)": "Country"}, inplace=True)
            
            self.logger.info("Name replaced successfully.")
            
        except Exception as e:
            #Logs unexpected exceptions and raises them
            self.logger.error(f"An unexpected error occured: {e}")
            raise
    
    
    def date_format(self):
        """Changing the date format"""
        self.logger.info("Changing the date format.")
        
        #Initializing an empty list. 
        new_columns = []
        
        for col in self.df.columns:
            try:
                #Attempting to change the date format to "YYYY-MM"
                new_col = pd.to_datetime(col, format="%b-%y").strftime("%Y-%m")
            except ValueError:
                self.logger.warning(f"column {col} could not be converted.")
                new_col = col
                
            #Retaning the original column if the conversion failes    
            new_columns.append(new_col)
            
        #Uppdating the columns with the new date format    
        self.df.columns = new_columns
        self.logger.info("Date format changed successfully.")
        
    
    def replace_missing_values(self):
        """Replacing ":" with the row mean in all data except the first two rows and the first column."""
        self.logger.info("Replacing missing values.")
        
        try:
            #Selecting all data execpt for the first column and first row
            data_range = self.df.iloc[1:, 1:]
    
            #Replaceing ":" with NaN
            data_range.replace(":", np.nan, inplace=True)
    
            #Converting the numeric columns to floats
            data_range = data_range.apply(
                lambda x: pd.to_numeric(x.replace(",", "."), errors="coerce")
            )
    
            #Calculate the row means
            row_means = data_range.apply(lambda row: row.mean(), axis=1)
            
            #Filling the NaNs with the row mean
            data_range = data_range.apply(lambda row: row.fillna(row_means[row.name]), axis=1)
            
            #Assigning the new data to the original dataframe
            self.df.iloc[1:, 1:] = data_range
            self.logger.info("Replaced missing values successfully.")
            
        except KeyError as e:
            #Logs and raises KeyError if there is a problem with accessing a row or column
            self.logger.error(f"KeyError: Problem with accessing the data rang: {e}")
            raise
            
        except ValueError as e:
            #Logs and raises ValueError if there is a error with a value converssion
            self.logger.error(f"ValueError: Problem when converting the data to numeric: {e}")
            raise
            
        except Exception as e:
            #Logs unexpected exceptions and raises them
            self.logger.error(f"A Unecpexted error occurred while replacing missing values: {e}")
            raise


    def clean_data(self) -> pd.DataFrame:
        """Returning the cleaned data as a dataframe."""
        try:
            #Checking if the self.df is a dataframe and not empty
            if self.df is None or not isinstance(self.df, pd.DataFrame):
                raise ValueError("The data is not a dataframe or is empty")
            
            #Returning the cleaned dataframe
            return self.df
        
        except Exception as e:
            #Logs unexpected exceptions and raises them
            self.logger.error(f"A unexpected error occurred when returning the cleaned dataframe: {e}")
            raise



