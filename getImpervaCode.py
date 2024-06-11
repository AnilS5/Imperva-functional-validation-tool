import datetime
import re

import modules as md


# noinspection PyGlobalUndefined
def getImpervaCode(*args):

    global mfa
    mfa = str()
    time_mfa_clicked = args[0]
    mfa_click_date = args[0].date().strftime('%d%b%Y')
    mfa_click_time = args[0]
    mfa_actual_time = mfa_click_time.hour * 3600 + mfa_click_time.minute * 60 + mfa_click_time.second


    outlook = md.Dispatch("Outlook.Application").GetNameSpace("MAPI")
    inbox = outlook.GetDefaultFolder(6)

    latest_mails = inbox.Items.Restrict("[Unread]=true")
    latest_mails.Restrict("[SenderEmailAddress]='noreply@okta.com'")
    latest_mails.Sort("[ReceivedTime]", True)

    for email in latest_mails:
        mail_date = email.ReceivedTime.date().strftime('%d%b%Y')
        mail_time = email.ReceivedTime
        mail_received_time = mail_time.hour * 3600 + mail_time.minute * 60 + mail_time.second

        try:
            if (mail_date >= mfa_click_date) and (mail_received_time > mfa_actual_time):
                mfa = re.findall('\d+', email.Body)[0]
                return mfa

        finally:
            if (mail_date >= mfa_click_date) and (mail_received_time > mfa_actual_time):
                pass

    else:
        md.sleep(1)
        getImpervaCode(time_mfa_clicked)

    return mfa

    """            
    mail_date = latest.ReceivedTime.date().strftime('%d%b%Y')
    mail_time = latest.ReceivedTime
    mail_received_time = mail_time.hour * 3600 + mail_time.minute * 60 + mail_time.second

    mfa_click_date = args[0].date().strftime('%d%b%Y')
    mfa_click_time = args[0]
    mfa_actual_time = mfa_click_time.hour * 3600 + mfa_click_time.minute * 60 + mfa_click_time.second
    
    if mail_date == mfa_click_date or mail_date > mfa_click_date:
        print("In first if")
        try:
            if mail_received_time > mfa_actual_time:
                print("In if.")
                mfa = latest_mfa

        finally:
            if mail_received_time >= mfa_actual_time:
                pass

            else:
                md.sleep(1)
                getImpervaCode(time_mfa_clicked)

    
    return mfa
    """

