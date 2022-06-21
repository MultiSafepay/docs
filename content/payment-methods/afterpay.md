---
title: 'AfterPay'
category: 6298bd782d1cf4006032e765
order: 301
hidden: false
parentDoc: 62a727567164d301522a67da
slug: 'afterpay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/AfterPay.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

[AfterPay](https://www.afterpay.nl/en/) is a widely used pay later method in the Netherlands and Belgium. Customers pay for orders after receiving them, and are only charged for items they keep from the order. AfterPay bears the risk and guarantees settlement.

Read how AfterPay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/afterpay)

| Overview | Details |
|---|---|
| **Chargebacks**  | No  | 
| **Countries**  | The Netherlands, Belgium  | 
| **Currencies**  | EUR  | 
| **Expiration** | Transactions expire after 90 days. |
| **Payment pages** | [Yes](/payment-pages/) (current version only) <br> Activate at website level in your dashboard. |
| **Refunds** | [Yes](/refunds/): Full, partial, and API refunds, and [discounts](/discounts/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

![AfterPay payment flow](https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/afterpay-payment-flow.svg)

# Payment statuses

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| AfterPay has authorized the transaction and the funds are awaiting capture. You can still cancel. <br> **Important:** To capture the funds, when you ship the order you must [manually change the order status to shipped](#shipment). | Completed  | Uncleared  |
| The funds are captured. <br> You can no longer cancel. You can only refund. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped | Completed |
| AfterPay has declined the transaction. <br> Only the customer can contact AfterPay to find out why (for privacy and compliance reasons).  | Declined | Declined |
| AfterPay authorized the transaction, but you or the customer cancelled it before capture. | Void | Void/Cancelled |
| AfterPay authorized the transaction, but you didn't ship within 90 days of creating the transaction **or** the customer didn't complete payment. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Initialized | Completed |
| Refund complete. | Completed | Completed |

</details>

# Activation 

You need to contact AfterPay to activate it for your account.

<details id="how-to-activate-afterpay"> 
<summary>How to activate AfterPay</summary>
<br>

1. To check you are eligible for AfterPay, email <sales@multisafepay.com>
2. For new AfterPay clients, apply directly to AfterPay:
    - The Netherlands: [Offerte](https://www.afterpay.nl/nl/zakelijk/offerte)
    - Belgium: [Offerte aanvragen](https://www.afterpay.be/be/footer/zakelijke-partners/offerte-aanvragen)
3. For existing AfterPay clients, to activate AfterPay for your MultiSafepay account, email AfterPay Sales at <sales@afterpay.nl>  

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > AfterPay direct/redirect |
| **Ready-made integrations** | AfterPay is supported in [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 8](/drupal/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [Odoo](/odoo/), [OpenCart](/opencart/), [PrestaShop 1.6 and 1.7](/prestashop/), [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/), [WooCommerce](/woo-commerce/), [X-Cart](/x-cart/). |
<br>

> ℹ️ Testing
> To test AfterPay payments, see [Testing](/testing/#pay-later-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.  
The **Transaction details** page in your dashboard only shows the billing address. To retrieve other details, see API reference – [Get order](https://docs-api.multisafepay.com/reference/getorder).

## Collection period
If the customer returns some items from the order and this takes a long time to verify, you can pause the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

## Gift cards

When paying with a gift card and AfterPay, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because AfterPay collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Shipment

When you ship the order, you **must** manually change the [order status](/payment-statuses/) from **Completed** to **Shipped** to:

- Capture the funds
- Trigger sending the invoice to the customer
- Prevent the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/integrations/ready-made/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

</details>

## Surcharges  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

AfterPay therefore strongly recommends discontinuing any surcharges. 

For more information, see AfterPay – [Merchant support](https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
