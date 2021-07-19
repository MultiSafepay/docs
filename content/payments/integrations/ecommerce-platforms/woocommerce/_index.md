---
title : "MultiSafepay plugin for WooCommerce"
github_url : "https://github.com/MultiSafepay/WooCommerce"
download_url : "https://github.com/MultiSafepay/WooCommerce/releases/download/4.7.0/Plugin_WooCommerce_4.7.0.zip"
changelog_url : "."
faq: "."
repo_url : "MultiSafepay/WooCommerce"
meta_title: "WooCommerce plugin - MultiSafepay Docs"
meta_description: "Integrate MultiSafepay payment solutions into your Wordpress WooCommerce webshop. MultiSafepay Docs provides information about getting started, building and testing integrations."
logo: "/logo/Plugins/WooCommerce.svg"
weight: 03
title_short: "WooCommerce"
layout: 'single'
changelog : "https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md"
aliases: 
    - /plugins/woocommerce
    - /integrations/plugins/woocommerce
    - /integrations/woocommerce
    - /plugins/woocommerce/manual
    - /integrations/plugins/woocommerce/manual
    - /integrations/woocommerce/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for WooCommerce. WooCommerce is a free, open-source ecommerce platform for Wordpress.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended WooCommerce installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Wordpress 5.0
- PHP 7.2

{{< /details >}}

## Installation

There are two ways to install the plugin:

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce backend.
3. Go to **Plugins** > **Add new**. 
4. Click **Browse file**.
5. Upload the Plugin_WooCommerce_x.x.x.zip file.

**Wordpress installation**

1. Sign in to your WooCommerce backend.
2. Go to **Plugins** > **Add new**.
3. Search for **MultiSafepay**. 
4. For the **MultiSafepay plugin for WooCommerce**, click the **Install now** button.

## Configuration
1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **MultiSafepay Settings**
3. On the **Account** tab, enter your API key. For where to find your API key, see [API key](/tools/multisafepay-control/get-your-api-key).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. On the **WooCommerce** > **Settings** > **Payments**. Enable the relevant payment methods and confirm the settings.


