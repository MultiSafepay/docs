---
title: "Pending payment order lifetime"
weight:
meta_title: "Magento 2 plugin FAQ - Order Lifetime - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
layout: "faqdetail"
---

The lifetime of orders marked as pending payments in Magento 2 is determined by the Order Cron Settings configuration. The default value is set to 480 minutes (8 hours)

When you offer payment methods whose validation period is more than 8 hours, the order in Magento 2 will automatically be marked as cancelled due to the default setting of 8 hours in Magento 2.

In use with an ERP system, for example, where an order is marked as declined, a successful payment will often not be processed to an order that is marked as cancelled.

The lifetime of a bank transfer is 86400 minutes (60 days) [Bank Transfer](/payment-methods/bank-transfer/how-does-bank-transfer-work/)

The order will set to cancelled in Magento 2 before a payment can be linked.

To set [pending payments order lifetime](https://docs.magento.com/m2/ee/user_guide/sales/order-pending-payment-lifetime.html)
