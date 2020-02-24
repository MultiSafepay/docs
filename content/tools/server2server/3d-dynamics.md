---
title: "Dynamic 3D Secure"
weight: 71
meta_title: "Server to Server - Dynamic 3D Secure - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

##  Dynamic 3D Secure

Based on a predefined set of rules, an order will be processed with or without [3D Secure](/faq/risk-and-fraud/what-is-3d-secure/).

A request to activate Dynamic 3D Secure is submitted via your account manager by email <sales@multisafepay.com>.

The following information is required:

* The reason why your want to process Dynamic 3D Secure transactions
* A fee can be requested for the use and/or implementation of the Dynamic 3D Secure
* If multiple site are connected within a MultiSafepay Control account, we need to know for which sites the Dynamic 3D Secure should be implemented.

## Minimum requirements to approve the use of Dynamic 3D Secure.

* Current processing performance (especially the chargebacks) needs to be good
* Merchant should be aware of the following:  
_The merchant runs an increased fraud risk on orders processed without 3D Secure, because a layer of security is removed_
* There is no liability shift for orders processed without 3D Secure.  
_The bank does not take liability for fraudulent orders, in other words the merchant runs the chargeback risk_.

## The rule set to Dynamic 3D Secure

We can create rules based on:

* The amount of the transaction
* The country involved (card country, ip country, country user)

Given that by default 3D Secure is enabled for all card orders, we decide with the use of the rules which transactions do not require 3D Secure.
