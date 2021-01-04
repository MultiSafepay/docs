---
title: "Dynamic 3D Secure"
weight: 71
meta_title: "Server to Server - Dynamic 3D Secure - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

##  Dynamic 3D Secure

Based on a predefined set of rules, an order will be processed with or without [3D Secure](/faq/general/what-is-3d-secure)


{{< alert-notice >}}
__Please note__: Since January 1st 2021, we no longer support Flexible 3D with merchants based in Europe due to PSD2 regulations. If your business handles many transactions with customers outside of Europe and you are interested in a more flexible setup, please contact your account manager by email <sales@multisafepay.com>
{{< /alert-notice >}}

The following information is required:

* The reason why your want to process Dynamic 3D Secure transactions.
* A fee can be requested for the use and/or implementation of the Dynamic 3D Secure.
* If multiple site are connected within a MultiSafepay Control account, we need to know for which sites the Dynamic 3D Secure should be implemented.

## Minimum requirements to approve the use of Dynamic 3D Secure.

* A significant amount of transactions are based outside of Europe.
* Current processing performance (especially the chargebacks) needs to be good
* Merchant should be aware of the following:  
_The merchant runs an increased fraud risk on orders processed without 3D Secure, because a layer of security is removed._
* There is no liability shift for orders processed without 3D Secure.  
_The bank does not take liability for fraudulent orders, in other words the merchant runs the chargeback risk_.

## The rule set to Dynamic 3D Secure

We can create rules based on:

* The amount of the transaction
* The country involved (card country, ip country, country user)

Given that by default 3D Secure is enabled for all card orders, we decide with the use of the rules which transactions do not require 3D Secure.
