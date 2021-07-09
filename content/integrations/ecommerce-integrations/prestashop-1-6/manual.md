---
title : "MultiSafepay PrestaShop 1.6 installation & configuration manual"
weight:
meta_title: "PrestaShop 1.6 plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /plugins/prestashop-1-6/manual
    - /integrations/plugins/prestashop-1-6/manual
    - /integrations/prestashop-1-6/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for PrestaShop 1.6.

We recommend first installing the plugin in a test environment following the recommended PrestaShop 1.6 installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/getting-started/).
- PrestaShop 1.6
- Tested on PHP 7.0

### Installation and configuration
1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directoy, merging the two folders.
2. Sign in to your PrestaShop 1.6 backend.
3. Go to **Modules and services** > **Payments and gateways**.  
    **Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your [API key](/faq/general/multisafepay-glossary/#api-key), and then click **Save**. {{% account_info %}}
6. On the **Payments** tab, enable the relevant payment methods.

**Note:** Payment links generated manually in your MultiSafepay account don't automatically create or update orders in your PrestaShop 1.6 backend.

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>
