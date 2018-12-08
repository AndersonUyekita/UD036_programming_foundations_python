##############################################################################################
#                                                                               VERSION: 1.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Course:   Programming Foundations with Python                                             #
#  COD:      nd036                                                                           #
#  Project:  Send SMS Message                                                                #
#  Lesson:   04                                                                              #
#  Date:     07/12/2018                                                                      #
#  Tags:     Udacity, Python                                                                 #
#                                                                                            #
##############################################################################################

# Accessing the https://www.twilio.com/docs/sms/send-messages you can copy this code bellow, this
# is a generic code provided by Twilio.

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'X'
auth_token = 'X'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+X',  # Twilio number
                              body='Hello World!',    # Message
                              to='+X'     # My number
                          )
print(message.sid)
