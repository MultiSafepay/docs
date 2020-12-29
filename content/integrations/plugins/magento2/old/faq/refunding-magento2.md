---
title : "Can I refund orders?"
meta_title: "Magento 2 plugin FAQ - Refund - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---
Yes, it is possible to refund orders or credit memo from within the Magento 2 backend. The refunds can either be full or partial refunds.

A full refund with the shopping cart can be issued. Partial refunding with shopping cart is available only for certain items. Please note that adjustment refunding for the shopping cart is not supported.

In the Magento backoffice, go to the Invoices tab, click on the invoice that was created by MultiSafepay and then click Credit Memo. Now you see 2 refund buttons:
* Offline refund: refund request will not be sent to MultiSafepay
* Refund: a refund request will be sent to MultiSafepay.

You can also refund from your [MultiSafepay Control](https://merchant.multisafepay.com)

_Note: Refunding from the Magento 2 backend is disabled when the order has a Fooman Surcharge. It is still possible to refund those orders through [MultiSafepay Control](https://merchant.multisafepay.com)_
