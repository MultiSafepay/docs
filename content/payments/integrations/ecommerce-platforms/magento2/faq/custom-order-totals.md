---
title : "Order totals on MultiSafepay payment pages"
meta_title: "Order totals on MultiSafepay payment pages - MultiSafepay Docs"

layout: "faqdetail"
read_more: "."
---

From version 1.9.0 and higher, all order totals, including custom ones, are automatically read and displayed on MultiSafepay payment pages.

We read **all **custom totals in the cart. Sometimes this results in unwanted custom totals appearing on payment pages.

To exclude custom totals from payment pages, follow these steps:  
 1. Sign in to your Magento 2 backend.
 2. Go to **Stores** > **Configuration** > **MultiSafepay**.
 3. Select **General settings** > **Advanced settings** > **Exclude custom totals**.

If you have included a custom total and it is **not** being read, make sure that it implements the following methods:

- getCode()
- getTitle() or getLabel()
- getValue() or getAmount() and getBaseAmount()
- getTaxRate() or getBaseTaxRate()
- getTaxAmount() or getBaseTaxAmount()

The base values are required if you have enabled the `use base currency` setting under **MultiSafepay** > **General settings**.