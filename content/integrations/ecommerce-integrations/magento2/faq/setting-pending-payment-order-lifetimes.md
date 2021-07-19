---
title: "Setting pending payment order lifetimes"
weight:
meta_title: "Magento 2 plugin - Setting pending payment order lifetimes - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
aliases: 
    - /integrations/magento2/faq/pending-payment-order-lifetime/
---

The lifetime of orders marked as **Pending payments** in Magento 2 is determined by the **Order Cron settings** configuration. The default value is 480 minutes (8 hours).

For payment methods with a validation period longer than 8 hours, the status of orders in Magento 2 automatically changes to **Canceled** due to the default value. To fix this, increase the **Order Cron settings** value to longer than the validation period. 

## Setting pending payment order lifetimes
To set the lifetime of pending payments orders, see Magento - [Pending payment order lifetime](https://docs.magento.com/m2/ee/user_guide/sales/order-pending-payment-lifetime.html).

## ERP systems
For ERP systems, if the order status is **Declined**, successful payments often fail to process for orders with **Canceled** status.

The lifetime of [bank transfers](/payment-methods/banks/bank-transfer/#how-does-it-work) is 86400 minutes (60 days).

The order status changes to **Cancelled** in Magento 2 before the payment can be linked.


