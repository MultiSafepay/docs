---
title: 'E-Invoicing'
category: 6298bd782d1cf4006032e765
order: 303
hidden: false
parentDoc: 62a727567164d301522a67da
slug: 'e-invoicing'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/e-invoicing.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

E-Invoicing is a MultiSafepay pay later method with automation tools that gives you full control of credit management, the payment process, and customer communications.

Read how E-Invoicing can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/e-invoicing)

| Supports | Details |
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies** | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds, and [discounts](/discounts/) |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/e-invoicing-payment-flow.svg" alt="E-invoicing payment flow" style="display: block;
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
| ❗️ [Manually change the order status to shipped](#shipment). <br> You must ship to receive payment. | Shipped | Initialized |
| MultiSafepay has collected payment. | Completed    | Completed  |
| E-Invoicing declined the transaction. | Declined | Declined |
| The transaction has been cancelled. | Void/Cancelled | Void/Cancelled |
| The customer didn't complete payment. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Initialized |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

You can activate E-Invoicing yourself in your dashboard. 

<details id="how-to-activate-e-invoicing"> 
<summary>How to activate E-Invoicing</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order. 
- Examples > E-Invoicing direct/redirect.
- Transactions don't expire.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (direct).

### Testing
To test E-Invoicing payments, see [Testing](/docs/testing#pay-later-methods).
<br>

---

# User guide

## Batches

You can generate E-Invoicing transactions in batches for subscription payments.

<details id="how-to-batch-transactions-for-subscriptions">
<summary>How to batch transactions for subscriptions</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
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

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **E-Invoicing** > **Invoices**. 

</details>

<details id="how-to-customize-invoices">
<summary>How to customize invoices</summary>
<br>

To customize invoices:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **E-Invoicing** > **E-Invoicing generator**. 

The invoice is sent to the email address provided. 

</details>

## Shipment

### Addresses

Different billing and shipping addresses are supported. Email a request to <sales@multisafepay.com> 

### Shipping policies

- [Shipping Policy Nederland](https://www.multifactor.nl/voorwaarden/shipping-policies/) 
- [Herinnering aan onze shipping policy](https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy) 

### Order status

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped**:

- Captures the funds
- Triggers sending the invoice to the customer
- Prevents the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change the order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **delivered** in your backend.

For other ready-made integrations, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request.

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
