import logging
import pandas as pd


class DataLoader:
    """Class to load data from Excel file."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def data_loader(self):
        """Loads data from a Excel file and returns a dataframe."""
        self.logger.info("Started to load the Excel data.")
        try:
            #Reading a Excel file into a dataframe using the file path
            df = pd.read_excel(
                r"C:\Users\erikf\ec\Fordjupad Pythonprogrammering\Kunskapskontroll_fodjupad_pytomprogrammering\Inflation_data_excel.xlsx"
            )
            self.logger.info("The data was succesfully loaded from Excel.")
            
            #Returning the Excel file as a dataframe
            return df
        
        except Exception as e:
            #Raises unexpected exceptions and logs them
            self.logger.error(f"Error in loading the data: {e}")
            raise

        
    
