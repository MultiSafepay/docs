---
title : "Can I refund orders?"
meta_title: "Magento 2 plugin FAQ - Refund - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---
Yes, it is possible to refund orders or credit memo from within the Magento 2 backend.  

In the Magento backoffice, go to the Invoices tab, click on the invoice that was created by MultiSafepay and then click Credit Memo. Now you see 2 refund buttons:
* Offline refund: refund request will not be sent to MultiSafepay
* Refund: a refund request will be sent to MultiSafepay.

You can also refund from your [MultiSafepay account](https://merchant.multisafepay.com)

_Note: Refunding from the Magento 2 backend is disabled when the order has a Fooman Surcharge. It is still possible to refund those orders through [MultiSafepay account](https://merchant.multisafepay.com)_
