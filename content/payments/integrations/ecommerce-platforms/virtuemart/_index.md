---
title : "MultiSafepay plugin for VirtueMart"
github_url : "https://github.com/MultiSafepay/Virtuemart"
download_url : "https://github.com/MultiSafepay/VirtueMart/releases/download/2.2.2/Plugin_VirtueMart_2.2.2.zip"
changelog_url : "."
faq: "."
meta_title: "VirtueMart plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/VirtueMart.svg"
weight: 18
title_short: "VirtueMart"
layout: 'single'
changelog : "https://github.com/MultiSafepay/VirtueMart/blob/master/CHANGELOG.md"
aliases: [/integrations/virtuemart/]
aliases:
    - /plugins/virtuemart
    - /integrations/plugins/virtuemart
    - /integrations/virtuemart
    - /plugins/virtuemart/manual
    - /integrations/plugins/virtuemart/manual
    - /integrations/virtuemart/manual

---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your VirtueMart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended VirtueMart installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Joomla 2.5 & 3.x + Virtuemart 2.x & 3.x
- Tested on PHP 7.0

{{< /details >}}

## Installation
1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Extension manager**.
3. Install the Plugin_VirtueMart_x.x.x.zip file using **Drag and drop** or **Browse for file**. 
4. Click **Upload & install**.

## Configuration
1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**. 
5. Click **Shop** > **Payment methods**. 
6. To install and configure each payment method separately:  
    - Click **New**.
    - Set the payment method to **VirtueMart – Payment, MultiSafepay**.
    - To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
    - API key
    - Account ID
    - Site ID
    - Site secure code  
    - Gateway ID  
    See [Viewing your API key](/getting-started/set-up-your-account/user-guide/viewing-your-api-key/).


