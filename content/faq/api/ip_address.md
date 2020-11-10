---
title: "Why request the IP address of the customer?"
weight:
meta_title: "FAQ API - Customer ip_address - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

#### ip_address
Post-payment and credit card payment methods require the customer <i>ip_address</i> to be validated and thus, we need the actual IP address of the end user within the <i>ip_address</i> field. This means that the optional parameter <i>"ip_address (optional)</i> within the JSON request is now a <i>"required"</i> field when processing post-payment and/or credit card transactions.

Please note! When validating the localhost <i>ip_address</i> instead of the end user's <i>ip_address</i>, it may result in transactions being marked with the status _uncleared_ or even be rejected/declined.


```shell
   "customer": {
        "ip_address": "31.148.195.10",
        "forwarded_ip": "" 
```

#### forwarded_ip

The X-FORWARDED-FOR header of the customer request when using a proxy.

<i>forwarded_ip</i> is to be used when there is a proxy. In all other cases they need to use the <i>ip_address</i> to retrieve the IP address of the customer.


#### Uncleared status or Declined 
Due to the validation on the IP address of the end user (customer) a transaction can unnecessarily be marked with the status _uncleared_ or even be declined. 

Before a payment is accepted, a fraud check will take place on the transaction. The required ip_address field is one of the checks processed in the validation of the payment. When provided with an empty or incorrect IP address (by providing the ip_address of the webshop instead of the customer), the chances that the transaction will be marked with the status _uncleared_ are very high. 

Credit cards and post-payment methods represent a high risk for fraud. Therefore, the validation of each transaction will automatically take place to protect the merchants processing with MultiSafepay. 

