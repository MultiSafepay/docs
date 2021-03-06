---
title: "Can I adjust the payment methods based on the billing address?"
meta_title: "Can I adjust the payment methods based on the billing address MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---
Yes, it is possible to adjust the payment methods when changing the billing address on the checkout page. By default, the payment selection is not adjusted per country unless you change the settings in the backend of Magento 2:

1. Go to _Stores_ > _Sales_ > _Checkout_ > _Checkout Options_
2. Locate _Display Billing Address On (store view)_
3. Select _Payment Page_
4. Save settings.

_Please note that this only applies for Magento 2.3.4 Community - Plugin 1.14.0_