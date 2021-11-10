---
title : "Which order totals appear on the MultiSafepay payment page?"
meta_title: "Which order totals appear on the MultiSafepay payment page? - MultiSafepay Docs"

layout: "faqdetail"
read_more: "."
---

From version 1.9.0 and higher, all the order totals, including custom ones, are automatically read and shown on the MultiSafepay payment page.

We pick up all the custom totals in the cart. Sometimes this can result in the MultiSafepay payment page showing unwanted custom totals.

To prevent this from happening, these custom totals can be excluded in the advanced section of the webshop configuration: _Stores_ > _Configuration_ > _MultiSafepay_ > _General Settings_ > _Advanced Settings_ > _Exclude custom totals_.

If you have created a custom total and it is not being picked up by our plugin, please make sure that your custom total implements the following methods:

- getCode()
- getTitle() or getLabel()
- getValue() or getAmount() and getBaseAmount()
- getTaxRate() or getBaseTaxRate()
- getTaxAmount() or getBaseTaxAmount()

The base values are needed if you are using the 'use base currency' setting inside the MultiSafepay general settings.
