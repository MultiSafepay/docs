---
title : "Processing refunds"
meta_title: "Magento 2 plugin - Processing refunds - MultiSafepay Docs"
layout: "faqdetail"
read_more: "."
url: "/magento-2/refunds/"
aliases: 
    - /integrations/magento2/faq/refunding-magento2/
    - /integrations/ecommerce-integrations/magento2/faq/refunding-magento2/
    - /payments/integrations/ecommerce-platforms/magento2/faq/processing-refunds/
---
## Refund rules

- From your [MultiSafepay dashboard](/refunds/full-partial/): Full and partial refunds 
- From your Magento 2 [backend](/glossaries/multisafepay-glossary/#backend) (see below):  
    - Full and partial refunds, and credit memos 
    - Refunding more than the original transaction is **not** supported
- API:  
    - [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund 
    - `PATCH` requests are **not** supported

To process refunds from your Magento 2 backend, follow these steps:  

1. Sign in to your Magento 2 backend. 
2. On the **Invoices** tab, click the invoice created by MultiSafepay, and then click **Credit memo**. 
3. Click the relevant refund button:  
    - **Offline refund**: Doesn't send a refund request to MultiSafepay.
    - **Refund**: Sends a refund request to MultiSafepay.

## Deprecated plugin

You can refund orders for payment methods from the deprecated plugin in your [MultiSafepay dashboard](https://merchant.multisafepay.com), but not from your Magento 2 backend. 

## Fooman surcharges

You can refund orders with a [Fooman surcharge](/payments/integrations/ecommerce-platforms/magento2/faq/applying-surcharges/) applied in your [MultiSafepay dashboard](https://merchant.multisafepay.com), but not from your Magento 2 backend.

