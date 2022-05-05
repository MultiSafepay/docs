---
title : "Deprecated app"
meta_title: "Shopify - Deprecated app - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
url: 'shopify/deprecated'
---

This technical manual is for installing and configuring the deprecated version of our  app for integrating MultiSafepay payment solutions into your Shopify webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the app in a test environment following the recommended Shopify installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
New merchants will need a MultiSafepay account.  See [Getting started](/getting-started/).

{{< /details >}}

{{< details title="Availability" >}}

Our Shopify app is unavailable in Norway and Finland. 

For more information, email <integration@multisafepay.com>

{{< /details >}}

{{< details title="Supported payment methods" >}}

Credit cards:

- [American Express](/payment-methods/amex/)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa/), including [Cartes Bancaires](/payment-methods/cartes-bancaires/) and [Dankort](/payment-methods/dankort/)

Banking methods:

- [Bancontact](/payment-methods/bancontact/)
- [Bank transfer](/payment-methods/bank-transfer/)
- [Belfius](/payment-methods/belfius/)
- [Dotpay](/payment-methods/dotpay/)
- [EPS](/payment-methods/eps/)
- [Giropay](/payment-methods/giropay/)
- [iDEAL and iDEAL QR](/payment-methods/ideal/)
- [ING Home'Pay](/payment-methods/ing-home-pay/)
- [KBC](/payment-methods/cbc-kbc/)
- [Maestro](/payment-methods/maestro/)
- [Request to Pay](/payment-methods/request-to-pay/)
- [Sofort](/payment-methods/sofort/)
- [Trustly](/payment-methods/trustly/)

Wallets:

- [Alipay](/payment-methods/alipay/)
- [PayPal](/payment-methods/paypal/)

Prepaid cards:

[Paysafecard](/payment-methods/paysafecard/)

{{< /details >}}

## Installation and configuration

1. To install payment methods, use the relevant links. For each, click the **Install** button on the bottom right:
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
  * [Sofort](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052866)
  * [Trustly](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1053945)
  * [Visa (including Cartes Bancaires & Dankort)](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1030328)

{{< /details >}}

2. Sign in to your Shopify [backend](/glossaries/multisafepay-glossary/#backend).
3. Go to **Settings** > **Payment providers** > **Alternative payments**.
4. Search for and click on the payment methods you have installed.
5. Enter your [site ID and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
6. Activate the payment method.

**Note**: To bundle all payment methods under a single MultiSafepay payment gateway at checkout, under **Alternative payments**, activate the **MultiSafepay** payment method.
