---
title: 'E-Invoicing'
category: 6298bd782d1cf4006032e765
order: 203
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'e-invoicing'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/e-invoicing.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

E-Invoicing is a MultiSafepay <<glossary:BNPL>> method with automation tools that gives you full control of credit management, the payment process, and customer communications.

Read how E-Invoicing can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/e-invoicing" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide  | 
| [Currencies](/docs/currencies/) | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds, and [discounts](/docs/discounts/) |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/e-invoicing-payment-flow.svg" alt="E-invoicing payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses 

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| MultiSafepay's risk analysis is in progress. You can still cancel. | Initialized   | Initialized  |
| E-Invoicing has authorized the transaction. <br> You can no longer cancel. You can only refund. | Completed  | Initialized  |
| ❗️ [Manually change the order status to Shipped](#shipment). <br> You must ship to receive payment. | Shipped | Initialized |
| MultiSafepay has collected payment. | Completed    | Completed  |
| E-Invoicing declined the transaction. | Declined | Declined |
| The transaction has been cancelled. | Void/Cancelled | Void/Cancelled |
| The customer didn't complete payment. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Initialized |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
    - All sites, go to **Settings** > **Payment methods**.
    - A specific site:
      - Go to **Integrations** > **Sites**, and then click the relevant site.
      - On the **Site profile** page, under **Payment methods**, click **Select payment methods**.
3. Select the checkbox for the payment method, and then click **Save changes**.

**Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > BNPL order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **E-Invoicing direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – [Include shopping_cart in order](/recipes/include-shopping_cart-in-order).
- Transactions don't expire.
- For direct orders, you must display your terms and conditions in your checkout.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (direct).

### Testing
To test E-Invoicing payments, see Testing payment methods –[BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Batches

You can generate E-Invoicing transactions in batches for subscription payments.

<details id="how-to-batch-transactions-for-subscriptions">
<summary>How to batch transactions for subscriptions</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **E-Invoicing** > **Batches**. 
3. Upload a file in .xls, .xlsx or .csv format.
4. Follow the templates in your MultiSafepay dashboard.

</details>

## Gift cards

When paying with a gift card and E-Invoicing, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. Otherwise our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Invoices

<details id="how-to-view-invoices">
<summary>How to view invoices</summary>
<br>

To see an overview of all successful transactions:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **E-Invoicing** > **Invoices**. 

</details>

<details id="how-to-customize-invoices">
<summary>How to customize invoices</summary>
<br>

To customize invoices:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **E-Invoicing** > **E-Invoice generator**. 

The invoice is sent to the email address provided. 

</details>

## Shipment

### Addresses

Different billing and shipping addresses are supported. Email a request to <sales@multisafepay.com> 

### Shipping policies

- <a href="https://www.multifactor.nl/voorwaarden/shipping-policies/" target="_blank">Shipping Policy Nederland</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 
- <a href="https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy" target="_blank">Herinnering aan onze shipping policy</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 

### Order status

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped**:

- Captures the funds
- Triggers sending the invoice to the customer
- Prevents the order from expiring

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

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
