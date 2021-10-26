---
title : "MultiSafepay app for Shopify"
meta_title: "Shopify plugin - MultiSafepay Docs"
faq: "."

logo: "/logo/Integrations/Shopify.svg"
weight: 05
title_short: "Shopify"
url: '/shopify/'
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
    - /integrations/ecommerce-integrations/shopify
    - /ecommerce-platforms/shopify/
    - /payments/integrations/ecommerce-platforms/shopify/
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

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) and [Dankort](/payments/methods/credit-and-debit-cards/dankort)

**Banking methods**

- [Bancontact](/payments/methods/banks/bancontact)
- [Bank transfer](/payments/methods/banks/bank-transfer)
- [Belfius](/payments/methods/banks/belfius)
- [Dotpay](/payments/methods/banks/dotpay)
- [EPS](/payments/methods/banks/eps)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)

**Wallets**

- [Alipay](/payments/methods/wallet/alipay)
- [PayPal](/payments/methods/wallet/paypal)

**Prepaid cards**

[Paysafecard](/payments/methods/prepaid-cards/paysafecard)

{{< /details >}}

{{< details title="Availability" >}}

Our Shopify app is unavailable in Norway and Finland. 

For more information, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}

{{< details title="Currencies" >}}
&nbsp;  
Payments are processed in the webshop's default currency only.

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
  * [Sofort](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052866)
  * [Trustly](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1053945)
  * [Visa (including Cartes Bancaires & Dankort)](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1030328)

{{< /details >}}

## Installation and configuration

1. To install payment methods, use the relevant links above. For each, click the **Install** button on the bottom right.
2. Sign in to your Shopify [backend](/getting-started/glossary/#backend).
3. Go to **Settings** > **Payment providers** > **Alternative payments**.
4. Search for and click on the payment methods you have installed.
5. Enter your [site ID and secure code](/set-up-your-account/site-id-api-key-secure-code).
6. Activate the payment method.

**Note**: To bundle all payment methods under a single MultiSafepay payment gateway at checkout, under **Alternative payments**, activate the **MultiSafepay** payment method.

