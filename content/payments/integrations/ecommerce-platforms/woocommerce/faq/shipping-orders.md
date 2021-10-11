---
title : "Shipping orders"
meta_title: "WooCommerce plugin - Shipping orders - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
url: '/woo-commerce/shipping/'
aliases:
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/changing-order-status-to-shipped/
---

For [pay later](/payments/methods/billing-suite/) payment methods, after you ship the order to the customer, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring and informs the payment method that they can invoice the customer and transfer the funds to MultiSafepay. 

If you change the order status to **Shipped** in your [backend](/getting-started/glossary/#backend), the updated status is passed to your MultiSafepay account automatically.