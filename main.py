#https://ec.europa.eu/eurostat/databrowser/view/PRC_HICP_MANR__custom_12887636/default/table?lang=en
import logging
from import_class import DataLoader
from clean_class import DataCleaner
from export_class import DataExport

#Configure the setting for logging
logging.basicConfig(
    filename="data_logfile.log",
    format="[%(asctime)s][%(levelname)s] %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M",
    filemode="w"
)

#Loading the data using the DataLoader class
data_loader = DataLoader()
df = data_loader.data_loader()

#Cleaning the data using the DataCleaner class
cleaner = DataCleaner(df)
cleaner.date_format()
cleaner.replace_name()
cleaner.replace_missing_values()
cleaned_data = cleaner.clean_data()

#Exporting the data using the DataExporter class
exporter = DataExport(cleaned_data)
exporter.data_exporter()