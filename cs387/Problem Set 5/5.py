# cs387 ; Problem Set 5 ; 5
# HW5 Challenge Problem 5 

# For this problem, we've attempted to make a
# simplified example demonstrating the beast
# attack.  We've created a simple site
# that has a secret message, `m`.

# You have the ability to send a message, attack, to 
# the server.  The server will prepend
# `attack` to `m` and then encrypt the resulting
# message using CBC mode with a block size
# of 128 bits.  

# The initialization vector, iv, is used from
# the the last block of the last encryption.
# Dave outlined how to deal with and use 
# this in lecture.  He also discussed a paper
# by Thai Duong and Juliano Rizzo that might
# have more useful information

# Specifically, the code below POSTs two values
# `attack` and `token`.  `attack` is the string
# prepended to the message and `token` is used
# internally to maintain a session and keep track
# of the last `iv.`  We highly recommend you don't
# mess with it.
# If `token` is empty or invalid - the server generates a
# random iv value and uses that for the encryption

# Rarely, similar to how a user might close and start
# a new TLS session, the server will start over, pick a new random
# IV and use that for encryption.

# The send function takes in a string as an argument and returns
# a string as an argument.  This is different from previous
# assignments where most functions took in arrays of bits.
# Just remember that each character represents a byte (8 bits)

# More information available: http://forums.udacity.com/cs387-april2012/questions/3506/hw5-5-challenge-question-discussion

###################
# This code is provided as an example of how to send and recieve
# information from the server.
# 
# You should only need to use the `send` function

import urllib
import json
import base64

BLOCK_SIZE = 128
site = "http://cs387.udacity-extras.appspot.com/beast"

def unencode_json(txt):
    d = json.loads(txt)
    return dict((str(k),
                 base64.urlsafe_b64decode(str(v)))
                for k,v in d.iteritems())

def _send(attack=None, token=None):
    data = {}
    if attack is not None:
        data["attack"] = base64.urlsafe_b64encode(attack)
    if token is not None:
        data["token"] = base64.urlsafe_b64encode(token)

    # here we make a post request to the server, sending
    # the attack and token data
    json = urllib.urlopen(site, urllib.urlencode(data)).read()
    json = unencode_json(json)
    return json
    
_TOKEN = None
def send(attack=None):
    """send takes a string (representing bytes) as an argument 
    and returns a string (also, representing bytes)"""
    global _TOKEN
    json = _send(attack, _TOKEN)
    _TOKEN = json["token"]
    return json["message"]

# End of example code
##################

##################
# Change secret_message to be the decrypted value
# from the server
secret_message = ""
