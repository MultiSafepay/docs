---
title : "Transaction and order numbers"
meta_title: "Shopware 5 plugin - Transaction and order numbers - MultiSafepay Docs"

layout: "faqdetail"
read_more: "."
weight: 7
url: "/shopware-5/transaction-order-numbers/"
aliases:
    - /payments/integrations/ecommerce-platforms/shopware5/faq/transaction-number-order-number/
---
Shopware 5 generates an order number and a transaction number.

The order number is generated **after** the payment is completed (unlike most ecommerce integrations where it is generated at the beginning of the order). 

The transaction number is generated when the transaction is initialized. MultiSafepay uses this number as the **order ID** in transactions.
