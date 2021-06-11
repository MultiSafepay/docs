---
title : "Configuring tax settings"
meta_title: "Magento 2 - Configuring tax settings - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/magento2/faq/which-tax-settings-should-i-use/
---

## Configuring Magento tax settings
To configure tax settings in Magento, go to **Stores** > **Configuration** > **Sales** > **Tax** > **Calculation settings**.

## Recommended tax settings
To avoid discrepancies between item amounts in MultiSafepay transactions and Magento orders, we recommend using the following tax settings in Magento.

To show prices **excluding tax**, use the following settings:

+ **Tax calculation method based on**: Row total
+ **Catalog prices**: Excluding tax
+ **Apply customer tax**: After discount
+ **Apply discount on prices**: Excluding tax

To show prices **including tax**, use the following settings:

+ **Tax calculation method based on**: Row total
+ **Catalog prices**: Including tax
+ **Apply customer tax**: After discount
+ **Apply discount on prices**: Including tax

These recommended settings are based on Magento's standards. For more information, see Magento - [Warning messages](https://docs.magento.com/user-guide/tax/warning-messages.html).
