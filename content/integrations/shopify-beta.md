---
title: "Shopify (Beta)"
category: 62962dd7e272a6002ebbbbc5
order: 16
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free app."
slug: 'shopify-beta'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Shopify.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation

To install or migrate, follow these steps:

1. Ensure that your Shopify user has <a href="https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions/staff-permissions-descriptions#apps-and-channels-permissions" target="_blank">the permissions</a> to install new apps.
2. Check that the payment methods you want to use in Shopify are [activated for your MultiSafepay account](/docs/payment-methods). 
3. Select the desired payment methods, installing their apps using one or more of the following links:
   - <a href="https://apps.shopify.com/card-payment" target="_blank">Card Payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://apps.shopify.com/multisafepay-ideal" target="_blank">iDEAL</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
5. Click on "Install" button.
6. If necessary, log in to your Shopify store.
7. On your admin page, select Install app. 
6. Under **Settings**:
   - **MultiSafepay API Key**: Enter your [site API key](/docs/sites#site-id-api-key-and-security-code).
   - **Test mode**: Turn on if you are using a Test API key. Turn off for a Live API key.
5. Click **Save**.
6. Under **Payment configuration** click on the button **Payment configuration**
   - Enable Test Mode if you are using a Test API key. Turn off for a Live API key.
   - Enable or disable payment icons according to your preferences.

✅ &nbsp; **Tip!** We recommend first testing each payment method before setting your **live** API key. 
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

## Currencies

Payments are processed in the webshop's default currency only.

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
