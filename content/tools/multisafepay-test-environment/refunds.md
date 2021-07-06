---
title: "Refunds in Test and Live environments"
weight: 71
meta_title: "Refunds in Test and Live environments - MultiSafepay Docs"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

In both the MultiSafepay [Test](https://testmerchant.multisafepay.com/signup?_ga=2.239314307.1689046699.1579505297-896219683.1574159857) and Live environments, refunds work differently.

__Live environment__: If the refund is done by Bank transfer, the status will go to _Reserved_ and remain that way till midnight. This will automatically change to _Completed_, after midnight has passed.

It must also be noted that in the Live environment, refunds that are carried out via bank transfer such as iDEAL, Bancontact, Belfius, ING Home'Pay and KBC can be withdrawn during the same day before midnight.

Refunds for credit cards, PayPal and Billing Suite payment methods are carried out immediately and cannot be reversed.

__Test environment__: The status will remain _Reserved_ until the refund has been manually approved since there is no settlement with a bank.