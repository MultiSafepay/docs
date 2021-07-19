---
title : "MultiSafepay plugin for Craft Commerce"
title_short: "Craft Commerce"
meta_title: "Craft Commerce plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
github_url : "https://github.com/MultiSafepay/craft-commerce"
changelog_url : "."
logo: "/logo/Integrations/Craft_Commerce.svg"
weight: 21
title_short: "Craft Commerce"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Craft Commerce webshop"
changelog: https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md
layout: 'single'
faq: "."
aliases: 
    - /plugins/craftcommerce
    - /integrations/plugins/craftcommerce
    - /integrations/craftcommerce
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Craft Commerce 3 webshop via Composer.

You can also install the plugin via the [Craft Plugin Store](https://plugins.craftcms.com/multisafepay).

{{< details title=Features >}}
&nbsp;  
- Support for separate payment methods, billing suites, and gift cards
- Partial and full refunds for non-billing suite payment methods
- Customizable order statuses
- Shipment notifications for billing suite payment methods

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

## Configuration
1. Sign in to the backend of your Craft Commerce webshop.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure gateways, go to **Commerce** > **System settings** > **Gateways**.  