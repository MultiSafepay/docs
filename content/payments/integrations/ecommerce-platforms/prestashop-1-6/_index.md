---
title : "MultiSafepay plugin for PrestaShop 1.6"
download_url : "/payments/integrations/ecommerce-platforms/prestashop-1-6/releases/Plugin_PrestaShop1.6_3.6.0.zip"
changelog_url : "."
changelog: https://docs.multisafepay.com/payments/integrations/ecommerce-platforms/prestashop-1-6/changelog/
faq: "."
meta_title: "PrestaShop 1.6 plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.6"
layout: 'single'
aliases: 
    - /plugins/prestashop-1-6
    - /integrations/plugins/prestashop-1-6
    - /integrations/prestashop-1-6
    - /plugins/prestashop-1-6/manual
    - /integrations/plugins/prestashop-1-6/manual
    - /integrations/prestashop-1-6/manual
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Prestashop 1.6 webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended PrestaShop 1.6 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- PrestaShop 1.6
- Tested on PHP 7.0

{{< /details >}}

## Installation and configuration
1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directoy, merging the two folders.
2. Sign in to your PrestaShop 1.6 backend.
3. Go to **Modules and services** > **Payments and gateways**.  
    **Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your [API key](/faq/general/multisafepay-glossary/#api-key), and then click **Save**. {{% account_info %}}
6. On the **Payments** tab, enable the relevant payment methods.

**Note:** Payment links generated manually in your MultiSafepay account don't automatically create or update orders in your PrestaShop 1.6 backend.

