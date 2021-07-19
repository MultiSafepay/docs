---
title : "MultiSafepay plugin for Drupal 8 and 9"
github_url : "https://github.com/MultiSafepay/drupal-commerce-2/"
download_url : "https://github.com/MultiSafepay/drupal-commerce-2/releases/download/3.0.0/commerce_multisafepay_payments-3.0.0.zip"
changelog: https://github.com/MultiSafepay/drupal-commerce-2/blob/master/CHANGELOG.md
faq: "."
layout: 'single'
meta_title: "Drupal 8 & 9 plugin integration - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Drupal_8.svg"
weight: 16
title_short: "Drupal 8 & 9"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Drupal 8 webshop"
aliases: 
    - /plugins/drupal8
    - /integrations/plugins/drupal8
    - /integrations/drupal8
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Drupal 8 webshop via Composer.

You can also install the plugin via your Drupal 8 & 9 backend. 

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support phase out" >}}
&nbsp;  
Drupal no longer provides security updates for Drupal 8.9.x, and will only provide bugfix support until early 2021 and security fixes until November 2021. 

For more information about upgrading from Drupal 8 to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).

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
- Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

{{< /details >}}

## Installation
To install the latest stable version of our Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

The latest stable release is downloaded and installed in your Drupal Commerce 2.x webshop.

## Configuration  
1. Sign in to the backend of your webshop.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your account ID, site ID, site code or API key. {{% account_info %}}
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com).

