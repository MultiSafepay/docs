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
   - <a href="https://apps.shopify.com/american-express" target="_blank">American Express</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-amazon-pay" target="_blank">Amazon Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/bancontact" target="_blank">Bancontact</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-bank-transfer" target="_blank">Bank Transfer</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-bizum" target="_blank">Bizum</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/card-payment" target="_blank">Card Payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-cbc" target="_blank">CBC</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/direct-debit" target="_blank">Direct debit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-ideal" target="_blank">iDEAL</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-kbc" target="_blank">KBC</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-maestro" target="_blank">Maestro</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-mb-way" target="_blank">MB WAY</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-mastercard" target="_blank">Mastercard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-mybank" target="_blank">MyBank</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/visa" target="_blank">Visa</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://apps.shopify.com/multisafepay-wechat-pay" target="_blank">WeChat Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
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

&nbsp; **💡 Tip!** We recommend first testing each payment method before setting your **live** API key. 
<br>

---

# Uninstallation

To uninstall, follow these steps:

1. Ensure that your Shopify user has <a href="https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions/staff-permissions-descriptions#apps-and-channels-permissions" target="_blank">the permissions</a> to uninstall apps.
2. On your admin page, go to **Settings** > **Apps and sales channels**.
3. Select the MultiSafepay payment app you want to uninstall, and clicking on the three dots icon, select the option **Uninstall**.
4. On the dialog window, select a reason and confirm the action by clicking in the **Uninstall** button.

<br>

---

# User guide

## Abandoned checkouts

MultiSafepay's [Second Chance](/docs/second-chance/) feature is **not** supported because Shopify offers a similar native service.

See Shopify – <a href="https://help.shopify.com/en/manual/orders/abandoned-checkouts" target="_blank">Recovering abandoned checkouts</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Checkout Configuration

To send an order request with as much information as possible, we recommend setting up the checkout by using the email as the primary customer contact method and, if required, adding the phone number in the customer information. This can be set up in Settings > Checkout Page.

## Currencies

Payments are processed only in the default currency of the webshop.

## Reconciliation

To match orders in your accounting system with your MultiSafepay account, use the MultiSafepay order ID and the Shopify payment ID.

## Payment capture method

Payment capture method needs to be set to **Automatically at checkout** in your Shopify settings.  This can be set up in Settings > Payments > Payment capture method.

## Refunds

[Full and partial refunds](/docs/refund-payments/) are supported via your MultiSafepay dashboard and backend.

<details id="how-to-process-refunds-in-your-shopify-backend">
<summary>How to process a refund in your backend</summary>
<br>

1. Sign in to your Shopify backoffice.
2. Go to **Orders**.
3. Select the order you want to refund.
4. Click on the **Refund** button.
- Enter the refund amount.
- Click on the **Refund** button.
4. A refund request is sent to MultiSafepay. The refund status is updated in your Shopify backend as **pending**.
5. The refund is processed by MultiSafepay. The refund status is updated in your Shopify backend as **refunded**.

**Notes**

- The refund amount cannot exceed the original transaction amount.
- Refunds are not processed in real-time. 
  - The refund status is updated in your Shopify backend as **pending** until the refund is processed by MultiSafepay.
  - While the refund is **pending** in your Shopify backend, refund will appear as **reserved** in your MultiSafepay account.

</details>

---

## Troubleshooting

### Payment Order ID

<details id="Shopify Troubleshooting">
<summary>How to troubleshoot Shopify issues</summary>
<br>

If you experience issues with order statuses, or refund statuses not updating, we will need the payment ID of the original transaction to investigate the issue. 

1. Sign in to your Shopify backoffice.
2. Go to **Orders**.
3. Select the order related to the issue you want to report.
4. In the timeline, look for the earliest payment event and find the Payment ID.
5. Include the payment ID when reporting your issue to <a href=\"mailto:integration@multisafepay.com\">MultiSafepay support</a>.

</details>
---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
