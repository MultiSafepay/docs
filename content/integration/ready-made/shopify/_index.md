---
title : "Shopify app"
meta_title: "Shopify app - MultiSafepay Docs"
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
    - /shopify/deprecated
    - /integrations/shopify/faq/refunding-shopify/
    - /payments/integrations/ecommerce-platforms/shopify/faq/processing-refunds/
    - /shopify/refunds/
    - shopify/reconciliation
    - /shopify/abandoned-checkouts/
---

{{< alert-notice >}} **Urgent action required!** Migrate to our [updated app](#installation).  {{< /alert-notice>}}

This technical manual is for installing/migrating to MultiSafepay's free app for integrating with Shopify. This new app leverages a single, powerful gateway for a faster, safer integration.

{{< details title="Requirements" >}}
&nbsp;  
You will need a [MultiSafepay account](/getting-started/).

{{< /details >}}

{{< details title="Support" >}}

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>

{{< /details >}}

## Installation

To install or migrate, follow these steps:

1. For increased security and stability, wait for off-peak hours and temporarily enable password protection for your webshop.
2. From the Shopify app store, install the [MultiSafepay Payments app](https://apps.shopify.com/multisafepay-payments).  
3. Enter your [site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code), and specify whether it is live or test.
4. Click **Save and continue** (this might take a few seconds).
  A pop up or new tab opens.
5. Scroll down and click **Activate MultiSafepay payments**. 
6. Under **Admin** > **Settings** > **Payments** > **Alternative payment methods**, check that the app has been successfully added. 
7. In your Shopify checkout, test the **MultiSafepay payments** gateway.  
  **Note:** If using a test API key, make sure you also enable **Test mode**. 
8. For existing merchants, under **Admin** > **Settings** > **Payments** > **Third-party payment providers**, disable the deprecated individual MultiSafepay payment method gateways.
9. Once testing is complete, disable password protection again.

## User guide

### Abandoned checkouts

MultiSafepay's [Second Chance](/features/second-chance/) feature is **not** supported because Shopify offers a similar native service.

See Shopify – [Recovering abandoned checkouts](https://help.shopify.com/en/manual/orders/abandoned-checkouts).

### Cancelling payments

If a customer cancels a payment to use another payment method instead, they must complete payment within **2 hours** to avoid errors.

### Countries

The app is unavailable in Norway and Finland. 

For more information, email <integration@multisafepay.com>

### Currencies

Payments are processed in the webshop's default currency only.

### Deprecated version

{{< details title="Installation and configuration">}}

1. To install payment methods, use the relevant links. For each, click the **Install** button on the bottom right:

    - [Alipay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052872)
    - [American Express](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052852)
    - [Bancontact](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052848)
    - [Bank Transfer](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052868)
    - [Belfius](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052846)
    - [CBC/KBC](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052862)
    - [Dotpay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052874)
    - [EPS](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052876)
    - [Giropay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052864)
    - [iDEAL](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052844), [iDEAL QR](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052850)
    - [Maestro](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052870)
    - [Mastercard](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052842)
    - [PayPal](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052854)
    - [Paysafecard](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052856)
    - [Request to Pay](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1055441)
    - [SEPA Direct Debit](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052858)
    - [Sofort](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1052866)
    - [Trustly](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1053945)
    - [Visa (including Cartes Bancaires & Dankort)](https://www.shopify.com/login?redirect=%2Fadmin%2Fauthorize_gateway%2F1030328)

2. Sign in to your Shopify backend.
3. Go to **Settings** > **Payment providers** > **Alternative payments**.
4. Search for and click on the payment methods you have installed.
5. Enter your [site ID and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
6. Activate the payment method.

**Note**: To bundle all payment methods under a single MultiSafepay payment gateway at checkout, under **Alternative payments**, activate the **MultiSafepay** payment method.
{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Wallets: [Alipay](/payment-methods/alipay), [PayPal](/payment-methods/paypal)
- Prepaid cards: [Paysafecard](/payment-methods/paysafecard)
- Banking methods: 
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

{{< /details >}} 

### Reconciliation

To match orders in your accounting system with your MultiSafepay account, use the MultiSafepay order ID and the Shopify payment ID.

### Refunds

[Full and partial refunds](/refunds/full-partial/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.
