dogeloterry
===========

A provably fair and transparent lottery game for Dogecoin.
This project is an experiment. It currently comes with an very important limitation (see below).
Feel free to read the [wiki](https://github.com/xaqq/dogelottery) for more infos.

CURRENT IMPORTANT LIMITATION ! READ BEFORE BETTING !
====================================================

The whole thing require no subscription and uses
the blockchain to retrieve the Dogecoin address of the winner.

Basically, a Dogecoin Transaction wins the game, not an address. This is
because we use transactions to generate tickets.

In order for the operator to send the money to the winner it needs his/her address.
This can be retrieve from the blockchain -- Its the address on the INPUT side of
the winning transaction. 

Problem? A transaction can have many input from many addresses.
Solutions:
* Carefuly select unspent output that you will use as input for buying ticket. Make sure that they come from a single dogecoin address, and that this address is not change.
* In case you failed this and you are supposed to win, you can still prove you won. This assumes that you are in possession of the private key of one of the address that showed in the INPUT side of the winning transaction. You could sign a message with your key and send it to the pool operator. The pool operator can then verify your claim (I'm pretty of this, but must make sure)