---
title : "MultiSafepay plugin for Drupal 7"
github_url : "https://github.com/MultiSafepay/Drupal-Commerce"
download_url : "https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip"
changelog: https://docs.multisafepay.com/payments/integrations/ecommerce-platforms/drupal7/changelog/
faq: "."
meta_title: "Drupal 7 plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Drupal_7.svg"
weight: 15
title_short: "Drupal 7"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Drupal 7 webshop"
layout: 'single'
aliases: 
    - /plugins/drupal7
    - /integrations/plugins/drupal7
    - /integrations/drupal7
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Drupal 7 webshop.

{{< details title="Test environment" >}}
&nbsp;  

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp; 
- MultiSafepay account – See [Getting started](/getting-started/).
- Drupal 7.x
- Tested on PHP 7.0

{{< /details >}}

## Installation and configuration
1. Unpack the content of the .ZIP file in the root of your Drupal 7 webshop.
2. Sign in to your Drupal 7 backend.
3. Go to **Site settings** > **Modules**. 
4. Enable the Commerce MultiSafepay JSON module, and your selected payment method modules. 
5. Click **Save configuration**.
6. Go to **Store settings** > **Advanced store settings** > **Payment methods**.
7. **Enable** the `multisafepay` core module.
8. **Enable** the modules for each payment method.
9. To configure each payment method, under **Actions**, click the **Edit** button.
10. When the main module is installed, two rules are created but disabled by default:  
    * MultiSafepay order paid in full: Order state to `processing`  
This rule sets the order to `processing` when the order is paid in full.  

    * MultiSafepay order complete: Shipped at MultiSafepay  
This rule updates the transaction status to **Shipped** at MultiSafepay. For Pay After Delivery, Klarna, and E-invoicing, this triggers the invoicing process.
