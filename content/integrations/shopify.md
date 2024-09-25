---
title: "Shopify"
category: 62962dd7e272a6002ebbbbc5
order: 15
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free app."
slug: 'shopify'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Shopify.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation

To install, follow these steps:

1. For increased security and stability, wait for off-peak hours and temporarily enable password protection for your webshop.
2. Check that the payment methods you want to use in Shopify are [activated for your MultiSafepay account](/docs/payment-methods). 
3. From the Shopify app store, install the <a href="https://apps.shopify.com/multisafepay-payments" target="_blank">MultiSafepay payments app</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
4. Under **Settings**:
   - **Website API key**: Enter your [site API key](/docs/sites#site-id-api-key-and-security-code).
   - **Environment**: Set whether it is a **live** or **test** API key.
5. Click **Save and continue** (this process might take a few seconds).
    You are redirected to **Settings** > **Payments**.
6. For each payment method you wish to activate, follow the below steps on the **app** page:
   - Select the payment method checkbox.
   - Under **Test mode**, select the **Enable test mode** checkbox.
   - Click **Activate <payment method>**.
    If the payment method is **not** activated for your MultiSafepay account, then in Shopify an error appears. 
7. [Activate the method for your MultiSafepay account](/docs/payment-methods), and then in Shopify, click **Retry**. 

&nbsp; **💡 Tip!** We recommend first testing each payment method before setting your **live** API key. 
<br>

---

# User guide

## Abandoned checkouts

MultiSafepay's [Second Chance](/docs/second-chance/) feature is **not** supported because Shopify offers a similar native service.

See Shopify – <a href="https://help.shopify.com/en/manual/orders/abandoned-checkouts" target="_blank">Recovering abandoned checkouts</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Cancellation

If a customer cancels a payment to use another payment method instead, they must complete payment within **2 hours** to avoid errors.

## Checkout Configuration

To send an order request with as much information as possible, we recommend setting up the checkout by using the email as the primary customer contact method and, if required, adding the phone number in the customer information. This can be set up in Settings > Checkout Page.

## Countries

The app is unavailable in Norway and Finland. 

For more information, email <integration@multisafepay.com>

## Currencies

Payments are processed in the webshop's default currency only.

## Order expiration

Shopify orders expire after **3** days. 

The `pendingExpiresAt` value matches the date and time when the order expires and must be within 3 days of calling the `paymentSessionPending` mutation (once only).

For more information, see Shopify.dev – <a href="https://shopify.dev/apps/payments/processing-a-payment#pend-a-payment" target="_blank">Pend a payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

**⚠️ Note:** If an order is not completed within **2** hours, the <<glossary:order status>> changes from **Pending** to **Expired**. 


## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Banking methods: 
  - [Bancontact](/docs/bancontact/)
  - [Bank transfer](/docs/bank-transfer/)
  - [Belfius](/docs/belfius/)
  - [Direct debit](/docs/direct-debit/)
  - [EPS](/docs/eps/)
  - [iDEAL](/docs/ideal/)
  - [Trustly](/docs/trustly/)
- Cards: [All](/docs/card-payments/)
- Prepaid cards: [Paysafecard](/docs/paysafecard/), Fashioncheque
- Wallets: [WeChat Pay](/docs/wechat-pay/)

</details> 

## Reconciliation

To match orders in your accounting system with your MultiSafepay account, use the MultiSafepay order ID and the Shopify payment ID.

## Refunds

[Full and partial refunds](/docs/refund-payments/) are supported via your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
