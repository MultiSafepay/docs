---
title : "MultiSafepay app for Shopify"
meta_title: "Shopify app - MultiSafepay Docs"
faq: "."
logo: "/logo/Integrations/Shopify.svg"
weight: 05
title_short: "Shopify"
type: 'App'
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

{{< alert-notice >}} **Urgent action required:** [Migrate to our updated app](#installation) before March 31, 2022.  {{< /alert-notice>}}

This technical manual is for installing/migrating to our free app for integrating MultiSafepay payment solutions into your Shopify webshop.

This new app leverages a single, powerful gateway for a faster, safer connection between your Shopify store and MultiSafepay.

{{< details title="Support" >}}

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
New merchants will need a MultiSafepay account. See [Getting started](/getting-started/).

{{< /details >}}

{{< details title="Currencies" >}}
&nbsp;  
Payments are processed in the webshop's default currency only.

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

- [American Express](/payment-methods/amex)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payment-methods/request-to-pay)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

[Paysafecard](/payment-methods/paysafecard)

{{< /details >}}

{{< details title="Availability" >}}

Our Shopify app is unavailable in Norway and Finland. 

For more information, email <integration@multisafepay.com>

{{< /details >}} 

## Installation

To install or migrate, follow these steps:

1. For increased security and stability, wait for off-peak hours and temporarily enable password protection for your webshop.
2. From the [Shopify app store](https://apps.shopify.com/), install the [MultiSafepay Payments app](https://apps.shopify.com/multisafepay-payments).  
3. Check that the app is successfully added under **Admin** > **Settings** > **Payments** > **Alternative payment methods**.
4. In your Shopify checkout, test the **MultiSafepay Payments** gateway.  
  **Note:** If using a test [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code), make sure you also enable **Test mode**. 
5. For existing merchants, you must disable the deprecated individual MultiSafepay payment method gateways under **Admin** > **Settings** > **Payments** > **Third-party payment providers**.
6. Once testing is complete, disable password protection again.

