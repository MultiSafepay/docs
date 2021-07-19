---
title : "MultiSafepay plugin for X-Cart"
github_url : "https://github.com/MultiSafepay/X-Cart"
download_url : "https://github.com/MultiSafepay/X-Cart/releases/download/2.3.0/Plugin_X-Cart_2.3.0.zip"
changelog_url : "."
faq: "."
meta_title: "X-Cart plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/X-Cart.svg"
weight: 14
title_short: "X-Cart"
layout: 'single'
changelog : "https://github.com/MultiSafepay/X-Cart/blob/master/CHANGELOG.md"
aliases: 
    - /integrations/x-cart/
aliases:
    - /plugins/x-cart
    - /integrations/plugins/x-cart
    - /integrations/x-cart
    - /plugins/x-cart/manual
    - /integrations/plugins/x-cart/manual
    - /integrations/x-cart/manual
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your X-Cart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended X-Cart installation procedure. Make sure you have made a backup.

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
- X-Cart 5.x        
- Tested on PHP 7.0

{{< /details >}}

## Installation
1. In the root of your webshop, unzip the content of the .ZIP file.
2. Sign in to your X-Cart backend.
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

## Configuration
1. Sign in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your [API key](/faq/general/multisafepay-glossary/#api-key) in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
    - Enter your account ID, site ID, site secure code, and your API key.
    - Make sure you enter the correct API key for the account type you want to use. 
    - For where to find your account ID, site ID, site secure code, see [API key](/tools/multisafepay-control/get-your-api-key).
9. Click **Save changes**.  

