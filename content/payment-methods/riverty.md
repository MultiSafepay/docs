---
title: 'Riverty (AfterPay)'
category: 6298bd782d1cf4006032e765
order: 23
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'riverty'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/afterpay-riverty-transition-logo.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.riverty.com/nl-nl/" target="_blank">Riverty</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (formerly AfterPay) is a widely used <<glossary:BNPL>> method in the Netherlands and Belgium. Riverty bears the risk and guarantees <<glossary:settlement>>.

<!--Read how Riverty can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/afterpay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>-->

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Belgium, Germany, Netherlands | 
| [Currencies](/docs/currencies/)  | EUR  | 
| [Chargebacks](/docs/chargebacks/) | No  |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) <br> Activate at site level in your dashboard. |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.


<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/riverty-payment-flow.svg" alt="Riverty payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds. 

| Description | Order status | Transaction status |
|---|---|---|
| Riverty has authorized the transaction and the funds are awaiting capture. You can still cancel. <br> ❗️ **Note:** To capture the funds, when you ship the order you must manually [change the order status to Shipped](#shipment). | Completed  | Uncleared  |
| The funds are captured. <br> You can no longer cancel. You can only refund. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped | Completed |
| Riverty has declined the transaction. <br> Only the customer can contact Riverty to find out why (for privacy and compliance reasons).  | Declined | Declined |
| Riverty authorized the transaction, but you or the customer canceled it before capture. | Void | Void/Canceled |
| Riverty authorized the transaction, but you didn't ship within 90 days of creating the transaction **or** the customer didn't complete payment. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Completed |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

To activate Riverty for your account, email Riverty at <sales@riverty.nl>  

Riverty provides you with an API key per country and per site, and you must accept Riverty's terms and conditions for each. 

# Integration

### API

- You will need an API key from Riverty per country per [site](/docs/sites/).
- See API reference – [Create order](/reference/createorder/) > BNPL order.
  
  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Riverty direct/redirect**.
  Set `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – [Include shopping_cart in order](/recipes/include-shopping_cart-in-order).
- Transactions expire after 90 days.
- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout. 

### Ready-made integrations

Riverty is supported in many of our ready-made integrations.

<details id="supported-ready-made-integrations"> 
<summary>Supported ready-made integrations</summary>
<br>

- [Craft Commerce](/docs/craft-commerce/)
- [CS-Cart](/docs/cs-cart/)
- [Drupal 8](/docs/drupal/)
- [Magento 1](/docs/magento-1/) & [Magento 2](/docs/magento-2/)
- [Odoo](/docs/odoo/)
- [OpenCart](/docs/opencart/)
- [PrestaShop 1.6 and 1.7](/docs/prestashop-1-7/)
- [Shopware 5 and 6](/docs/shopware/)
- [WooCommerce](/docs/woocommerce/)
- [X-Cart](/docs/x-cart/)

---

</details>

### Testing

To test Riverty payments, see Testing payment methods – [BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.  
The **Transaction details** page in your dashboard only shows the billing address. To retrieve other details, see API reference – [Get order](/reference/getorder/).

## Collection period
If the customer returns some items from the order and this takes a long time to verify, you can pause the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

## Gift cards

When paying with a gift card and Riverty, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Riverty collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Shipment

When you ship the order, you **must** manually change the <<glossary:order status>> from **Completed** to **Shipped** to:

- Capture the funds
- Trigger sending the invoice to the customer
- Prevent the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Change order status**. 
4. Change the status to **Shipped**.
5. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

❗️ **Note:** Some third-party plugins may not support updating the status via our API.

</details>

## Surcharges  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

Riverty therefore strongly recommends discontinuing any surcharges. 

For more information, see Riverty – <a href="https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/" target="_blank">Merchant support</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
