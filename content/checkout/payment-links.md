---
title: 'Payment links'
category: 62bd999547298d001abc714c
order: 20
hidden: false
slug: 'payment-links'
---
You can manually generate a link to a [payment page](/docs/payment-pages/) to pass to a customer to complete payment. 

# How it works

Use cases include:

- A customer wants to adjust an existing order and instead of starting over with a new order.
- You need to create a transaction for a manually generated order.
- MultiSafepay collects a payment for an amount that doesn't match any order. If you accept the payment, you need to manually generate a payment link and email it to <support@multisafepay.com>
- A [Bank Transfer](/docs/bank-transfer/) transaction has expired.

# Activation

No activation is required.

# Integration

You can generate payment links via the API:

- API reference – [Create order](/reference/createorder/) > Payment page/link
- API recipe – [Create a payment page/link](/reference/createorder/)

Or via your dashboard:

<details id="how-to-generate-link-for-new-transaction">
<summary>How to generate a link for a new transaction</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Click **New payment link**.
4. From the **Site** list, select the relevant site.
5. Under **Amount**, select the currency from the list, and then enter the whole value and cents.
6. In the **Order ID** field, enter the order ID from your webshop.  
**Note:** The order ID for every payment link must be unique.
7. In the **Description** field, enter a description of the order. 
8. In the **Link expiration (days)** field, enter the number of days for the link to remain active. Default: 30 days.
9. To send [Second Chance emails](/docs/second-chance/), select the **Second chance email** check box. 
10. Optionally, enter the customer's:  
    - **First name** and **Last name**
    - **Email address**
    - **Country**
    - **Language**
11. To include additional information, in the top-right corner, click **Advanced mode** to display more fields. 
12. Click **Generate payment link**.
13. In the green bar that appears, copy the link from the green bar and pass it to the customer.

</details>

<details id="how-to-generate-link-for-existing-transactions">
<summary>How to generate a link for existing transactions</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Click on the relevant transaction.
4. In the **Transaction details** page, under **Order summary**, click **Payment link** > **Duplicate this order**.

> **Note:** The order ID must be unique.

</details>
<br>

---

# User guide

## Cancellation

<details id="how-to-cancel-a-payment-link">
<summary>How to cancel a payment link</summary>
<br>

**Via API** 

See API reference – [Update or cancel an order](/reference/updateorder/).

**Via dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the red cross icon.  
The <<glossary:order status>> changes to **cancelled**. 

</details>

## Duplication

If you need to generate multiple payment links, you can speed up the process by duplicating existing links.

<details id="how-to-duplicate-a-payment-link">
<summary>How to duplicate a payment link</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Next to the relevant payment link, click the blue copy icon.  
A new link generator window opens with the same details prefilled.  
4. Click **Generate payment link**.

</details>

## Link lifetimes

The lifetime of a payment link is how long it remains active for the customer to access the payment page and complete payment. The default is 30 days.

<details id="how-to-adjust-link-lifetimes">
<summary>How to adjust link lifetimes</summary>
<br>

To set or adjust the lifetime of a payment link, see API reference – [Create order](/reference/createorder/): `days_active` parameter.

> **Note:** This is different to [transaction expiration times per payment method](/reference/transaction-expiration/). 

This only applies to certain payment methods:

| Adjustable | Non-adjustable |
|---|---|
| Banking methods, except SEPA Direct Debit | SEPA Direct Debit |
| Gift cards | Edenred, Paysafecard |
| Wallets | PayPal – Links are valid for 14 days. The lifetime is set by PayPal. |
| Credit cards |  |

</details>

## Number of attempts

The customer can open the link to the payment page up to 20 times, after which the link is disabled.

Each attempt creates a new transaction. If the customer completes payment in one of these transactions, the [status](/docs/payments-statuses/) of the other transactions remains **Initialized** until they expire.

## Overview and statuses

<details id="overview-and-statuses"> 
<summary>Overview and statuses</summary>
<br>

For an overview of all payment links:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.

| Payment link status | Description |
|---|---|
| Active | The customer hasn't paid yet.  | 
| Completed | The customer has paid. | 
| Cancelled | You cancelled the link.| 
| Expired | The link lifetime has expired.  | 

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

**All** payment methods are supported. 

The payment page displays **all** payment methods activated for the relevant site. If you want to display specific payment methods, you need to create a new site profile with only the relevant methods activated. 

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)