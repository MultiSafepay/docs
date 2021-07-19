---
title : "MultiSafepay plugin for CS-Cart"
github_url : "https://github.com/MultiSafepay/CS-Cart"
download_url : "https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip"
faq: "."
changelog: "https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md"
meta_title: "CS-Cart plugin integration - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/CS-Cart.svg"
weight: 13
title_short: "CS-Cart"
layout: 'single'
description_short: "Free plugin to integrate MultiSafepay payment solutions into your CS-Cart webshop"
aliases: 
    - /plugins/cs-cart
    - /integrations/plugins/cs-cart
    - /integrations/cs-cart
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your CS-Cart webshop.

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
- CS-Cart 4.x
- Tested on PHP 7.0

{{< /details >}}

## Installation
 1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
 2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
 3. Delete the `msp_installer.php` file.
 4. In your [MultiSafepay account](https://merchant.multisafepay.com), provide your [notification URL](/tools/multisafepay-control/set-your-notification-url).

## Configuration
1. Sign in to your CS-Cart backend.
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required.
7. Click **Create**.
8. In the **Configure** tab, enter your account ID, site ID, and site code. {{% account_info %}}
Your account ID appears in the top right corner of your MultiSafepay account.

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.
