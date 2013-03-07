#!/usr/bin/env python
from googlevoice import Voice
from googlevoice.util import input
import mimic
import sys
import time
import argparse
import random

def troller(args):
    """
    This script is an adaptaion of the script created by Zack Feldstein
    The script uses the credentials provided to it to send TEXT messages 
    via Google Voice to numbers provided.
    From the command line, if a message is not provied one will be 
    generated for you. The generated message is created using a Google 
    Mimic Exercise from their Python Training course.

    Required input :
    ----------------
    All input is provided from argparse. The variables are set as 
    namespace arguments. The following variables are arguments with the 
    "args." prefix

    username 
    password 
    number 
    message 
    total_trolls
    troll_interval
    """
    # Set the creds to login to Google Voice
    voice = Voice()
    voice.login(args.u,args.p)

    # Show us a list of the numbers recieving a message
    num_list = ', '.join(args.n)
    print('People Being Trolled are %s' % num_list)

    # Set our counters 
    counter = 0
    total = tt = args.tt

    for _ in range(tt):
        # Add to counter and subtract from total
        counter += 1
        total = total - 1
        print("Total Trolls Sent %s " % counter)

        try:
            for phoneNumber in args.n:
                # Generate a message if one was not provided
                if not args.m:
                    rm = True
                    args.m = mimic.main()

                # Send the SMS Message
                voice.send_sms(phoneNumber, args.m)

                # If using a large list of numbers sleep for 1 second between messages
                if len(args.n) > 5:
                    time.sleep(1)

                # Reset a random Message if we were using a Random Message
                if rm:
                    args.m = None
        except Exception, e:
            print e
            print 'Google was mad, so we are waiting for a sec'
            time.sleep(2)
            pass

        # If the total amount of trolls left is greater than zero let us know
        if total > 0:
            if args.ti == 0:
                args.ti = 1
            nm = random.randrange(0,args.ti) + 1
            print("next message will be sent in %s seconds" % nm)
            time.sleep(nm)

parser = argparse.ArgumentParser(usage='%(prog)s',
                                 description=('Sends Text Messages to target '
                                              'numbers using %(prog)s'),
                                 epilog=('Based on the original work by Zack Feldstein, '
                                         'Modified by Kevin Carter'))
parser.add_argument('-u', 
                    metavar='[username]',
                    required=True,
                    help='sets username')
parser.add_argument('-p', 
                    metavar='[passwrod]',
                    required=True,
                    help='sets password')
parser.add_argument('-m', 
                    metavar='[message]',
                    help='sets message')
parser.add_argument('-n',
                    type=str,
                    metavar='[number]',
                    default=[],
                    action='append',
                    required=True,
                    help='sets target number, this can be used multiple times')
parser.add_argument('-ti', 
                    metavar='[interval]',
                    type=int,
                    default=1,
                    help='sets the time between trolls, This is a random '
                         'number set between 1 and your provided input')
parser.add_argument('-tt', 
                    metavar='[total]',
                    type=int,
                    default=1,
                    help='sets the total amount of trolls')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit('Give me something to do and I will do it')
else:
    troller(args)

