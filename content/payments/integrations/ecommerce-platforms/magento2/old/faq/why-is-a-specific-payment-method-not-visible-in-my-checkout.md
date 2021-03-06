---
title : "Why is a specific payment method not visible in my checkout?"
meta_title: "Magento 2 plugin FAQ - Enable Payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---

When you enabled a payment method, it should always be visible, even when your [API key](/faq/general/multisafepay-glossary/#api-key) is incorrect.

Payment methods may also not be visible in the checkout due to the following:

- When another gateway filter outside of MultiSafepay is activated, for example, the one from [Rico Neitzel Payment Filter](https://github.com/riconeitzel/PaymentFilter)
- Configuration errors in the Magento 2 backend and/or in the database, that prevent changes from being saved.
- The _Enabled in checkout_ is unchecked for the ‘MultiSafepay payment method’. For the MultiSafepay payment method, there is an _Enabled in checkout_ configuration option, which does not show the gateway in the checkout if it is set to _Disabled_.	
