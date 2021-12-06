import logging
import pandas as pd

path = '/home/smadden7/OneDrive/'
# path =  '/home/tloken/inputs/'
v2020_base_count = '101010'
v2021_base_count = '099993'
build_nadac = "nadac file built successfully"
append_nadac_2020 = "2020 nadac file built successfully"
append_nadac_2021 = "2021 nadac file built successfully"
append_pgte_2020 = "2020 pgte file built successfully"
append_pgte_2021 = "2021 pgte file built successfully"
append_finance_2020 = "2020 finance file built successfully"
append_finance_2021 = "2021 finance file built successfully"
append_admin_2020 = "2020 admin file built successfully" 
append_admin_2021 = "2021 admin file built successfully" 
append_txn_2020 = "2020 txn file built successfully"      
append_txn_2021 = "2021 txn file built successfully"
build_pos = "pos built successfully"
build_generics = "generics built successfully"
semifill_2020 =  "2020 semifill file built successfully"      
semifill_2021 =  "2021 semifill file built successfully"

try:
    logfile = path + 'inr_reporting_file_'+ str(pd.to_datetime('today').date()) + '.log'
    logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)    
    logging.info('=============================================================================================')
    logging.info('======================== INR Reporting Reporting Build  - Daily Run =========================')
    logging.info('=============================================================================================')
    logging.info('append_nadac_2020 =' + append_nadac_2020)
    logging.info('append_nadac_2021 = ' + append_nadac_2021)
    logging.info('append_pgte_2020 = ' + append_pgte_2020)
    logging.info('append_pgte_2021 = ' + append_pgte_2021)
    logging.info('append_finance_2020 = ' + append_finance_2020)
    logging.info('append_finance_2021 = ' + append_finance_2021)
    logging.info('admin_2020 = ' + append_admin_2020)
    logging.info('append_admin_2021 = ' + append_admin_2021)
    logging.info('admin_2020 = ' + append_admin_2020)
    logging.info('append_txn_2020 = ' + append_txn_2020)
    logging.info('append_txn_2021 = ' + append_txn_2021)
    logging.info('build_pos = ' + build_pos)
    logging.info('build_generics = ' + build_generics)
    logging.info('semifill_2020 = ' + semifill_2020)
    logging.info('semifill_2021 = ' + semifill_2021)
    email_to = 'todd.loken@Optum.com','shawn_madden@Optum.com'


except Exception as e: 
        logging.info(traceback.print_exc())
        logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        logging.info('Failed...')
        logging.info(sys.exc_info()[0])
        logging.info(e)
