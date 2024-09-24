---
title: 'iDEAL in3'
category: 6298bd782d1cf4006032e765
order: 2
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'in3'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/ideal-in3.svg" width="80" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://payin3.eu/en/ideal-in3/for-merchants/" target="_blank">iDEAL in3</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a Dutch <<glossary:BNPL>> method where customers pay in 3 installments, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). iDEAL in3 guarantees <<glossary:settlement>> after receiving the first installment.

Read how iDEAL in3 can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/in3" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Netherlands – iDEAL in3 checks the customer's country, and billing/shipping address to confirm.  | 
| [Currencies](/docs/currencies/)  | EUR  |  
| [Chargebacks](/docs/chargebacks/)  | No  |
| [Discounts](/docs/discounts/) | Yes <br> You can request iDEAL in3 to process a full or partial refund, either before <<glossary:payout>> or up to 1 year afterwards. |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/in3-payment-flow.svg" alt="in3 payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| iDEAL in3's credit check is in progress. You can still cancel. | Initialized   | Initialized  |
| iDEAL in3 is waiting for the customer to pay the first installment (within 5 minutes). | Uncleared  | Initialized  |
| The customer has paid the first installment. Settlement is now guaranteed. <br> You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| You can [manually change the order status to shipped](#shipment) for your records, but this is not required to trigger invoicing. | Shipped | Uncleared | 
| MultiSafepay has collected payment. | Completed | Completed |
| iDEAL in3 declined the transaction. | Declined | Declined |
| The customer cancelled the transaction or abandoned the first installment. | Void | Void |
| The customer didn't pay the first installment. | Expired | Expired |
| **Refunds:** iDEAL in3 has successfully processed a full or partial refund. | Completed | Completed |
| **Refunds:** The refund was declined. | Declined | Declined   |

# Activation 

1. Email a request to <sales@multisafepay.com> 
   We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > BNPL order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **in3 direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- Transactions expire after 2 hours.
- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout.

### Ready-made integrations
iDEAL in3 (direct) is supported in:
- [Craft Commerce](/docs/craft-commerce/)
- [Magento 1](/docs/magento-1/) and [Magento 2](/docs/magento-2/) 
- [OpenCart](/docs/opencart/)
- [PrestaShop](/docs/prestashop/)
- [VirtueMart 3](/docs/virtuemart-3/)
- [VirtueMart 4](/docs/virtuemart-4/)
- [WooCommerce](/docs/woocommerce/)

### Testing
To test iDEAL in3 payments, see Testing payment methods – [BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.

## Amount limits

- Minimum amount: 50 EUR 
- Maximum amount: 5000 EUR 

You can adjust these limits in the <<glossary:backend>> of our [ready-made integrations](/docs/our-integrations/) to show or hide iDEAL in3 on your checkout page depending on the order value.

## Gift cards

When paying with a gift card and in, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. This is because iDEAL in3 collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Shipment

When you ship the order, you can change the <<glossary:order status>> to **Shipped** for your records, bu this is not required to trigger invoicing.

<details id="how-to-change-order-status-to-shipped">
<summary>How to change the order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Change order status**. 
4. Change the status to **Shipped**.
5. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

❗️ **Note:** Some third-party plugins may not support updating the status via our API.

---

</details>

### Surcharges

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 
<br>

# in3 Business 

We are currently in the pilot phase with in3 Business. 
To activate this payment method, email <sales@multisafepay.com> 


<a href="https://payin3.eu/en/in3-business/" target="_blank">in3</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a Dutch <<glossary:BNPL>> method where customers pay in 3 installments, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 guarantees <<glossary:settlement>> after receiving the first installment.

Read how in3 Business can benefit your webshop on <a href="https://www.multisafepay.com/solutions/payment-methods/in3-business" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>


## User guide

### Amount limits: 

- Minimum amount: 150 EUR 
- Maximum amount: 30000 EUR 

### Integration:

For `direct` requests: 

- Gateway: IN3B2B
- Required fields: First name, last name, address, email, business name, chamber of commerce number. 

Ready-made integrations: 

- [Magento 2](/docs/magento-2/) 
- Shopware 6
- Prestashop 1.6
- [PrestaShop 1.7](/docs/prestashop-1-7/)
- Lightspeed 
---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
