---
title: Payment fee / Surcharges
weight:
meta_title: "Magento 2 plugin surcharge - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---

Adding a payment fee or [surcharge](/security-and-legal/payment-regulations/about-surcharges/) is no longer supported within the plugin in Magento 2.

However, an external package of [Fooman](https://store.fooman.co.nz/extensions/magento2) is available. This allows you to still add a payment fee or surcharge within the desired payment method.

Refunding from the Magento 2 backend is disabled when the order has a Fooman Surcharge. It is still possible to refund those orders through [MultiSafepay account](https://merchant.multisafepay.com)

_Do mind that because an external module has to be installed, our Integration Team's help will be limited_.

Of course, we do our best to support and assist as best as possible, but we investigate or reproduce on the core of a plugin. Therefore, we do not guarantee a perfect compatibility when installing an external package.

Please keep in mind that the Payment Services Directive 2, also called PSD2, is now in place and may have implications on your webshop. PSD2 was first released in 2015 by the European Commission. This directive compelled the Member State to effectively intervene and regulate the payment service industry. See how applying payment fees or surcharges for your customers may affect your webshop on our [PSD2 documentation page](/security-and-legal/payment-regulations/about-payment-service-directive-2)

_It may be the case that unwanted 'Custom Order Totals' will appear on the MultiSafepay payment page.  If you wish for this amount to be excluded, there is an option in the backend of our plugin in Magento 2, which can exclude such 'Totals'. This option will however not be required if the plugin or module removes the custom total from the order when it is not being used._   
