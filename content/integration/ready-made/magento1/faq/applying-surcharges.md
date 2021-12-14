---
title: Applying surcharges
weight:
meta_title: "Magento 1 plugin - Applying surcharges - MultiSafepay Docs"

read_more: "."
url: '/magento-1/surcharges/'
aliases: 
    - /integrations/magento1/faq/payment-fee-surcharges/
    - /payments/integrations/ecommerce-platforms/magento1/faq/applying-surcharges/
---

You can apply [surcharges](/glossaries/multisafepay-glossary/#surcharge) (payment fees) of a percentage or a fixed amount to transactions for every payment method.

For how applying surcharges may affect your webshop in relation to PSD2, see [Payment Services Directive 2](/security-and-legal/payment-regulations/about-payment-service-directive-2).

You can also:

- Set the tax class for surcharges.
- Show transaction amounts excluding the surcharge at checkout. Surcharges are always included at checkout.
- Show surcharges with our without VAT at checkout.

To apply a surcharge to a payment method in your [backend](/glossaries/multisafepay-glossary/#backend), follow these steps:

1. Sign in to your Magento 1 backend.
2. Select systems and configuration.
3. In the MultiSafepay module, select the **Option connect** gateway.
4. Select the relevant payment method.
5. Under **Payment fee amount**, enter a surcharge percentage or fixed amount. 
6. Place a test order to verify whether the fee has been correctly processed.