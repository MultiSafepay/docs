---
title : "Processing refunds"
meta_title: "Magento 2 plugin - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
aliases: 
    - /integrations/magento2/faq/refunding-magento2/
    - /integrations/ecommerce-integrations/magento2/faq/refunding-magento2/
---
Refund rules:

- From your [MultiSafepay account](/account/multisafepay-account/processing-refunds/): Full and partial refunds 
- From your Magento 2 [backend](/getting-started/glossary/#backend) (see below):  
    - Full and partial refunds, and credit memos 
    - Refunding more than the original transaction is **not** supported
- API:  
    - [Refund with shopping cart](/api/#refund-with-shopping-cart) 
    - PATCH requests are **not** supported

To process refunds from your Magento 2 backend, follow these steps:  

1. Sign in to your Magento 2 backend. 
2. On the **Invoices** tab, click the invoice created by MultiSafepay, and then click **Credit memo**. 
3. Click the relevant refund button:  
    - **Offline refund**: Doesn't send a refund request to MultiSafepay.
    - **Refund**: Sends a refund request to MultiSafepay.

**Deprecated plugin**
You can refund orders for payment methods from the deprecated plugin in your [MultiSafepay account](https://merchant.multisafepay.com), but not from your Magento 2 backend. 

**Fooman surcharges**
You can refund orders with a [Fooman surcharge](/payments/integrations/ecommerce-platforms/magento2/faq/applying-surcharges/) applied in your [MultiSafepay account](https://merchant.multisafepay.com), but not from your Magento 2 backend.

