---
title : "Shopify app"
category: 62962dd7e272a6002ebbbbc5
order: 105
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free app to integrate MultiSafepay payment solutions with Shopify."
slug: 'shopify'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Shopify.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

:warning: **Urgent action required:** [Migrate to our updated app](#installation) before March 31, 2022.

This technical manual is for installing/migrating to MultiSafepay's free app for integrating with Shopify. This new app leverages a single, powerful gateway for a faster, safer integration.

<details id="requirements">
<summary>Requirements</summary>
<br>

You will need a [MultiSafepay account](/getting-started/).

</details>

# How to install

To install or migrate, follow these steps:

1. For increased security and stability, wait for off-peak hours and temporarily enable password protection for your webshop.
2. From the [Shopify app store](https://apps.shopify.com/), install the [MultiSafepay Payments app](https://apps.shopify.com/multisafepay-payments).  
3. Check that the app is successfully added under **Admin** > **Settings** > **Payments** > **Alternative payment methods**.
4. In your Shopify checkout, test the **MultiSafepay Payments** gateway.  
  **Note:** If using a test [API key](/websites/#site-id-api-key-and-secure-code), make sure you also enable **Test mode**. 
5. For existing merchants, you must disable the deprecated individual MultiSafepay payment method gateways under **Admin** > **Settings** > **Payments** > **Third-party payment providers**.
6. Once testing is complete, disable password protection again.

# User guide

## Abandoned checkouts

MultiSafepay's [Second Chance](/second-chance/) feature is **not** supported because Shopify offers a similar native service.

See Shopify – [Recovering abandoned checkouts](https://help.shopify.com/en/manual/orders/abandoned-checkouts).

## Cancelling payments

If a customer cancels a payment to use another payment method instead, they must complete payment within **2 hours** to avoid errors.

## Countries

The app is unavailable in Norway and Finland. 

For more information, email <integration@multisafepay.com>

## Currencies

Payments are processed in the webshop's default currency only.

## Deprecated version

<details id="installation-and-configuration">
<summary>Installation and configuration</summary>
<br>

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
5. Enter your [site ID and secure code](/websites/#site-id-api-key-and-secure-code).
6. Activate the payment method.

**Note**: To bundle all payment methods under a single MultiSafepay payment gateway at checkout, under **Alternative payments**, activate the **MultiSafepay** payment method.
</details>

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Wallets: [Alipay](/alipay), [PayPal](/paypal)
- Prepaid cards: [Paysafecard](/paysafecard)
- Banking methods: 
  - [Bancontact](/bancontact)
  - [Bank Transfer](/bank-transfer)
  - [Belfius](/belfius)
  - [CBC/KBC](/cbc-kbc)
  - [Dotpay](/dotpay)
  - [EPS](/eps)
  - [Giropay](/giropay)
  - [iDEAL and iDEAL QR](/ideal)
  - [Request to Pay](/request-to-pay)
  - [Sofort](/sofort)
  - [Trustly](/trustly)

</details> 

## Reconciliation

To match orders in your accounting system with your MultiSafepay account, use the MultiSafepay order ID and the Shopify payment ID.

## Refunds

[Full and partial refunds](/refunds/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

> 💬  Support
> Contact MultiSafepay:
> 
> - Telephone: +31 (0)20 8500 500
> - Email: <integration@multisafepay.com>
