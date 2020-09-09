---
title: "Pending payment order lifetime"
weight:
meta_title: "Magento 2 plugin FAQ - Order Lifetime - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

The lifetime of orders marked as pending payments in Magento 2 is determined by the _Order Cron Settings configuration_. The default value is set to 480 minutes (8 hours)

When you offer payment methods whose validation period is more than 8 hours, the order in Magento 2 will automatically be marked as _cancelled_ due to the default setting in Magento 2.

In use with an ERP system, for example, where an order is marked as declined, a successful payment will often not be processed to an order that is marked as cancelled.

The lifetime of a [bank transfer](/payment-methods/bank-transfer/how-does-bank-transfer-work) is 86400 minutes (60 days)

The order will set to _cancelled_ in Magento 2 before a payment can be linked.

To set pending payments order lifetime, see the [Magento Documentation page](https://docs.magento.com/m2/ee/user_guide/sales/order-pending-payment-lifetime.html)
