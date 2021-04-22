---
title : "Which tax settings should i use?"
meta_title: "Magento 2 payment link - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

To prevent discrepancies between item amounts inside the MultiSafepay transactions and Magento orders, we recommend to use certain tax settings inside Magento.

Tax settings in Magento can be found under _Stores_ > _Configuration_ > _Sales_ > _Tax_ > _Calculation Settings_

If you want to show prices **excluding tax**, we recommend the following settings:

+ _Tax Calculation Method Based On_: Row Total
+ _Catalog Prices_: Excluding Tax
+ _Apply Customer Tax_: After Discount
+ _Apply Discount On Prices_: Excluding Tax

For stores that want to show prices **including tax**, we recommend the following settings:

+ _Tax Calculation Method Based On_: Row Total
+ _Catalog Prices_: Including Tax
+ _Apply Customer Tax_: After Discount
+ _Apply Discount On Prices_: Including Tax

We also recommend to look at the recommendations from Magento, as our settings should be in line with the [Magento recommendations](https://docs.magento.com/user-guide/tax/warning-messages.html).