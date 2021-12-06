import smtplib
from datetime import date
from datetime import datetime
from datetime import timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# All assignments in code INR inital count
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
email_to = 'todd.loken@optum.com, shawn_madden@optum.com'




def INR_reporting_email(email_to, v2020_base_count, v2021_base_count, build_nadac, append_nadac_2020,
                        append_nadac_2021, append_pgte_2020, append_pgte_2021,
                        append_finance_2020, append_finance_2021, append_admin_2020,
                        append_admin_2021, append_txn_2020, append_txn_2021,
                        build_pos, build_generics, semifill_2020, semifill_2021):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'Industry and Network Relations Business Review - Data Generation' 
1
        msg['From'] = 'INR_do_not_reply_@Optum.com'
        msg['To'] = email_to

        ms = """
        <html>
        <head></head>
        <body>
        <p>INR Reporting EMAIL</p>
        <p></p>
        <p>==============================================================================</p>
        <p><strong>Industry and Network Relations Business Review - Data Generation</strong></p>
        <p>==============================================================================</p>
        <p>last_year_base_data_table_count = {0}</strong></p>
        <p>current_year_base_data_table_count = {1}</strong></p>
        <p>build_nadac = {2}</strong></p>
        <p>append_nadac_2020 = {3}</strong></p>
        <p>append_nadac_2021 = {4}</strong></p>
        <p>append_pgte_2020 = {5}</strong></p>
        <p>append_pgte_2021 = {6}</strong></p>
        <p>append_finance_2020 = {7}</strong></p>
        <p>append_finance_2021 = {8}</strong></p>
        <p>append_admin_2020 = {9}</strong></p>
        <p>append_admin_2021 = {10}</strong></p>
        <p>append_txn_2020 = {11}</strong></p>
        <p>append_txn_2021 = {12}</strong></p>
       <p>build_pos = {13}</strong></p>
        <p>build_generics = {14}</strong></p>
        <p>semifill_2020 = {15}</strong></p>
        <p>semifill_2021 = {16}</strong></p>
        <p>&nbsp;</p>
        </body>
        </html>""".format(v2020_base_count, v2021_base_count, build_nadac, append_nadac_2020,
                            append_nadac_2021, append_pgte_2020, append_pgte_2021,
                            append_finance_2020, append_finance_2021, append_admin_2020,
                            append_admin_2021, append_txn_2020, append_txn_2021,
                            build_pos, build_generics, semifill_2020, semifill_2021)



        chunk = MIMEText(ms, 'html')
        msg.attach(chunk)



        s = smtplib.SMTP('localhost')
        s.send_message(msg)

        return_message = 'done'

        return msg

    except: 
2
        raise
        return_message = 'broke'
        return return_message

msg = INR_reporting_email(email_to, v2020_base_count, v2021_base_count, build_nadac,
append_nadac_2020,append_nadac_2021, append_pgte_2020, append_pgte_2021,append_finance_2020,
append_finance_2021, append_admin_2020,append_admin_2021, append_txn_2020, append_txn_2021,build_pos,
build_generics, semifill_2020, semifill_2021)
# msg = "todd"
print(msg)
