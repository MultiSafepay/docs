---
title: Payment fee / Surcharges
weight:
meta_title: "Magento 1 plugin surcharge - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: [/integrations/magento1/faq/payment-fee-surcharges/]
---

Magento 1 allows you to add a payment fee. The payment fee can be a [Surcharge](/faq/general/multisafepay-glossary/#surcharge) by percentage or a fixed amount. Each payment method has the option to set a fee.

Other options available are settings like tax class for payment fee and show payment fee inclusive or exclusive during a checkout procedure.

The payment fee will always be shown to the customer during the checkout procedure.

Follow the steps below to set a surcharge per payment method in the backend of Magento 1:

1. Select systems and configuration
2. In the module from MultiSafepay choose the option connect gateway
3. Select the desired payment method
4. Add a surcharge percentage or fixed amount to set-up a fee within the section > payment fee amount
5. It is optional to show the added fee with or without VAT in the checkout.

See how applying payment fees or surcharges for your customers may affect your webshop on our [PSD2 documentation](/faq/payment-regulations/payment-service-directive-2) page.

Place a test order to verify whether the fee has been correctly processed.
