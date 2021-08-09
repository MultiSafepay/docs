---
title : "Which order totals appear on the MultiSafepay payment page?"
meta_title: "Which order totals appear on the MultiSafepay payment page? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---

From version 1.9.0 and higher, all the order totals, including custom ones, are automatically read and shown on the MultiSafepay payment page.

Some Magento 2 plugins that provide custom order totals do not completely remove these totals from the order and only remove them from the frontend in order for the user not to see them. This results in our plugin picking up the custom order totals that were not visible in the webshop and showing them on the payment page. 

To prevent this from happening, these custom totals can be excluded in the advanced section of the webshop configuration: _Stores_ > _Configuration_ > _MultiSafepay_ > _MultiSafepay Settings_ > _Advanced Settings_ > _Exclude custom totals_.
