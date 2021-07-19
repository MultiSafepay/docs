---
title : "MultiSafepay plugin for Zen Cart"
github_url : "https://github.com/MultiSafepay/Zencart"
download_url : "https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip"
changelog_url : "."
faq: "."
meta_title: "ZenCart plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Zen_Cart.svg"
weight: 20
title_short: "Zen Cart"
layout: 'single'
changelog : "https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md"
aliases: 
    - /plugins/zencart
    - /integrations/plugins/zencart
    - /integrations/zencart
    - /plugins/zencart/manual
    - /integrations/plugins/zencart/manual
    - /integrations/zencart/manual
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Zen Cart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended Zen Cart installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- ZenCart 1.5.5
- Tested on PHP 7.0

{{< /details >}}

## Installation and configuration
1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart backend.
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/tools/multisafepay-control/get-your-api-key).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.



