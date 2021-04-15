---
title : "Which order totals appear on the MultiSafepay payment page?"
meta_title: "Which order totals appear on the MultiSafepay payment page? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

From version 1.9.0 and higher, all the order totals, including custom ones, are automatically read and shown on the MultiSafepay payment page.

Some Magento 2 plugins also add custom totals that are not necessarily for adding or subtracting something from the cart. These totals will however still appear on our MultiSafepay payment page. 

To prevent this from happening, these custom totals can be excluded in the advanced section of the webshop configuration: _Stores_ > _Configuration_ > _MultiSafepay_ > _General Settings_ > _Advanced Settings_ > _Exclude custom totals_.
