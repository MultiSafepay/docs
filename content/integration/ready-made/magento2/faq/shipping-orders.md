---
title : "Shipping orders"
meta_title: "Magento 2 plugin - Shipping orders  - MultiSafepay Docs"
layout: "faqdetail"
read_more: "."
url: '/magento-2/shipping-orders/'
aliases:
    - /payments/integrations/ecommerce-platforms/magento2/faq/changing-order-status-to-shipped/
---

For [pay later](/payments/methods/pay-later/) payment methods, after you ship the order to the customer, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets the payment method initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance. 

If you change the order status to **Shipped** in your [backend](/glossaries/multisafepay-glossary/#backend), the updated status is passed to your MultiSafepay dashboard automatically.