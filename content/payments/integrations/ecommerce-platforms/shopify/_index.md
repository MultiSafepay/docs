---
title : "MultiSafepay app for Shopify"
meta_title: "Shopify plugin - MultiSafepay Docs"
faq: "."
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Integrations/Shopify.svg"
weight: 05
title_short: "Shopify"
layout: 'single'
aliases: 
    - /hosted/shopify
    - /integrations/hosted/shopify
    - /integrations/shopify
    - /integrations/shopify/faq/how-can-i-update-the-plugin-for-shopify/
    - /integrations/shopify/manual
    - /hosted/shopify/manual
    - /integrations/hosted/shopify/manual
    - /integrations/shopify/manual
---

This technical manual is for installing and configuring our free app for integrating MultiSafepay payment solutions into your Shopify webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the app in a test environment following the recommended Shopify installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
You will need a MultiSafepay account. See [Getting started](/getting-started/).

{{< /details >}}

{{< details title="Availability" >}}

Our Shopify app is unavailable in Norway and Finland. 

For more information, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}

{{< details title="Payment method links" >}}

  * [Alipay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052872)
  * [American Express](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052852)
  * [Bancontact](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052848)
  * [Bank transfer](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052868)
  * [Belfius](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052846)
  * [Dotpay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052874)
  * [EPS](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052876)
  * [Giropay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052864)
  * [iDEAL QR](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052850)
  * [iDEAL](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052844)
  * [ING Home'Pay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052860)
  * [KBC](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052862)
  * [Maestro](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052870)
  * [Mastercard](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052842)
  * [PayPal](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052854)
  * [PaySafecard](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052856)
  * [Request to Pay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1055441)
  * [SEPA Direct Debit](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052858)
  * [SOFORT Banking](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052866)
  * [Trustly](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1053945)
  * [Visa (including Cartes Bancaires & Dankort)](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1030328)

{{< /details >}}

## Installation and configuration

1. To install payment methods, use the relevant links above. For each, click the **Install** button on the bottom right.
2. Sign in to your Shopify backend.
3. Go to **Settings** > **Payment providers** > **Alternative payments**.
4. Search for and click on the payment methods you have installed.
5. Fill in your API key, site ID, and site secure code. For where to find them, see [API key](/tools/multisafepay-control/get-your-api-key).
6. Activate the payment method.

**Note**: To bundle all payment methods under a single MultiSafepay payment gateway at checkout, under **Alternative payments**, activate the **MultiSafepay** payment method.

