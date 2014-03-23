#!/usr/bin/env python

import argparse
import os
import json
import hashlib
import sys
from uuid import uuid4

is_debug = False

## Return a list of long decimal -- thoses are the tickets for this transaction.
## A transaction can have so many ticket: amount / ticket_price.
## Say amount = 10;
## Each ticket is computed alone
## Ticket computation:
##     - Concatenate the transaction hash with the string "_%d" where %d is the N
##       ticket this transaction generates. It starts at 1.
##     - Prepend the server secret to the previously generated string.
##     - Hash the new string using sha256 algorithm.
##     - Convert the hash to a digest hex string. Lets call this ticket_hash
##     - convert ticket_hash to an very long integer.
##     - This new integer is the ticket.
## So you will have txhash_1 ... txhash_2 ....
def get_nums_from_tx(tx, server_secret, ticket_price=1):
    tickets = []
    for n in range(0, tx["amount"] / ticket_price):
        if n == 0:
            continue
        ticket_hash = hashlib.sha256(server_secret + tx["tx_hash"] + '_' + str(n)).hexdigest()
        ticket = int(ticket_hash, base=16)
        tickets.append(ticket)
        if is_debug:
            print "    Ticket: " + str(ticket)
    return tickets

## Generate a list of tickets for every transaction
def generate_tickets_for_tx(data, server_secret):
    for tx in data:
       res = get_nums_from_tx(tx, server_secret)
       tx["tickets"] = res
       print "Transaction " + tx["tx_hash"] + " has " + str(len(res)) + " tickets !"


## Pick the winner. 
## The winner is the one with the lowest ticket's value.
def pick_winner(data):
    winning_tx = [];
    lowest_ticket = False
    for tx in data:
        for t in tx["tickets"]:
            if lowest_ticket == False or t < lowest_ticket:
                lowest_ticket = t
                winning_tx = []
                winning_tx.append(tx["tx_hash"])
            elif t == lowest_ticket:
                winning_tx.append(tx["tx_hash"])

    print "Winning ticket: " + str(lowest_ticket)
    print "Transaction(s) who won:"
    print winning_tx

def main():
    try:
        global is_debug
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', dest='verbose', action='store_true', help="verbose, display all tickets")
        parser.add_argument('-a', '--address', help="lottery bank address (unused yet because it loads transaction from a file)")
        parser.add_argument('-s', '--secret', help="the server_secret")
        args = parser.parse_args()

        if args.verbose == True:
            is_debug = True
        if args.secret == None:
            server_secret = str(uuid4())
        else:
            server_secret = args.secret
    except:
        parser.print_help()
        return
    print "Server Secret: " + server_secret
    print "Server Secret Hash: " + hashlib.sha256(server_secret).hexdigest()

    with open("TXS") as f:
        data = json.loads(f.read())
        generate_tickets_for_tx(data, server_secret)
        pick_winner(data)
    
if __name__ == "__main__":
    main()
