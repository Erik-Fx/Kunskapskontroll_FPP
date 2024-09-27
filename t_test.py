import os
import sys
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

#Adds the directory of the modules to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from clean_class import DataCleaner
from import_class import DataLoader


#Class to test the functions in the DataLoader class
class TestDataLoader:
    """Test for the function in the DataLoader class."""
    
    #Testing a successful import
    @patch("import_class.pd.read_excel") # Mock pandas read_excel method
    def test_data_loader_success(self, mock_read_excel):
        #Creating a mock dataframe to test on
        mock_df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        mock_read_excel.return_value = mock_df
        
        #Instansiate the DataLoade class and loading data
        data_loader = DataLoader()
        result = data_loader.data_loader()
        
        #Checking that the read_excel only was called once
        mock_read_excel.assert_called_once()
        
        #Checking that the the dataframes match
        pd.testing.assert_frame_equal(result, mock_df)
        
    #Testing a unsuccessful import    
    @patch("import_class.pd.read_excel", side_effect=Exception("Test error")) # Mock path with exeption
    def test_data_loader_faliure(self, mock_read_excel):
        #Instanciating the DataLoader class
        data_loader = DataLoader()
        
        #Checking for exaptions during the data import    
        with pytest.raises(Exception, match="Test error"):
            data_loader.data_loader()
            
#Class to test the functions in the DataCleaner class
class TestDataCleaner:
    """Tests for the functions in DataCleaner."""
    
    @pytest.fixture
    def test_df(self):
        """A sample dataframe of the dataset to run the tests on."""
        
        data = {
            "Date": ["Date", "GEO(Labels)", "European Union", "Belgium", "Bulgaria"],
            "jan-17": ["jan-17", "", "2.8", "2.0", "1.7"],
            "feb-17": ["feb-17", "", "2.1", ":", "3"],
            "mar-17": ["mar-17", "", "7", "2.2", "1.3"]
        }
        df = pd.DataFrame(data)
        return df
    
    def test_replace_name(self, test_df):
        """Test if the name GEO(Labels) has been replaced for Counrty."""
        
        #Instanciating the DataCleaner class
        data_cleaner  = DataCleaner(test_df)
        data_cleaner.replace_name()
        
        #Checking if the name Geo(Labels) has been replaced with Country
        assert data_cleaner.df.iloc[1, 0] == "Country"
        
    def test_date_format(self, test_df):
        """Testing if the date format was changed correctly."""
        
        #Instanciating the DataCleaner class
        data_cleaner = DataCleaner(test_df)
        data_cleaner.replace_name()
        data_cleaner.date_format()
        
        # Checking if the date format was successfully formated
        columns = ["Date", "2017-01", "2017-02", "2017-03"] # What the formated dates should look like
        assert list(data_cleaner.df.columns) == columns
        
    def test_replace_missing_values(self, test_df):
        """Testing if the missing values ":" was replaced successfully."""
        
        #Instanciating the DataCleaner class
        data_cleaner = DataCleaner(test_df)
        data_cleaner.replace_name()
        data_cleaner.date_format()
        data_cleaner.replace_missing_values()
        
        #checking if the missing values ":" was successfully replaced with the row mean
        belgium_mean = (2.2 + 2) / 2
        assert data_cleaner.df.iloc[2, 2] == belgium_mean # 2.1 is the sample row mean    
            
    def test_clean_data(self, test_df):
        """Testing if the cleaned data was returend as a dataframe."""
        
        #Instanciating the DataCleaner class
        data_cleaner  = DataCleaner(test_df)
        cleaned_df = data_cleaner.clean_data()
        
        #Checking if the cleaned data is returned as a dataframe
        assert isinstance(cleaned_df, pd.DataFrame)
            