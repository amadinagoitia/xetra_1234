"""Running the Xetra ETL application"""

import logging
import logging.config
import yaml


def main():
    """
        entry point to run the xetra ETL job.
    """
    # Parsing YAML file
    config_path = 'E:/Sources/xetra_project/xetra_1234/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    print (config)
    
    # configure logging (for all the app)
    log_config = config['logging']
    logging.config.dictConfig(log_config)   #convert logger to dictionary format
    logger = logging.getLogger(__name__)    #creates a logger using the name of the file
    logger.info("This is a test.")
    
if __name__ == '__main__':
    main()

