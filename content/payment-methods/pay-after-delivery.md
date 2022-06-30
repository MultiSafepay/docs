---
title: 'Pay After Delivery'
category: 6298bd782d1cf4006032e765
order: 206
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'pay-after-delivery'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Pay_After_Delivery.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

Pay After Delivery is MultiSafepay's own <<glossary:BNPL>> method for increasing customer confidence and <<glossary:conversion>>. MultiSafepay bears the risk, based on the customer's history, and guarantees settlement.

Read how Pay After Delivery can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/pay-after-delivery)

| Supports | Details |
|---|---|
| **Amount limits** | Minimum and maximum order amounts apply. Email <sales@multisafepay.com> |
| **Countries**  | The Netherlands  | 
| **Currencies** | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No  | 
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds| 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/pay-after-delivery-payment-flow.svg" alt="Pay After Delivery payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| MultiSafepay's risk analysis is in progress. You can still cancel. | Initialized | Initialized | 
| We have authorized the transaction and the funds are awaiting capture. You can no longer cancel. You can only refund. <br> See [Close transactions](#close-transactions). | Completed | Uncleared | 
| **Important:** To capture the funds, [manually change the order status to shipped](#shipment). | Shipped | Uncleared |
| MultiSafepay has collected payment.  | Shipped | Completed |
| The transaction was cancelled. | Void/Cancelled   | Void/Cancelled | 
| MultiSafepay declined the transaction. | Declined | Declined |
| The customer didn't complete payment within 90 days. | Expired | Expired | 
| **Refunds:** Refund initiated. | Initialized | Initialized |  
| **Refunds:** Refund complete. | Completed | Completed | 

# Activation 

First apply to MultiSafepay, and then activate in your dashboard.

<details id="how-to-activate-pay-after-delivery"> 
<summary>How to activate Pay After Delivery</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, to activate the method in your dashboard, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the relevant payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > BNPL order. 
- Examples > Pay After Delivery direct/redirect.
- Transactions expire after 90 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (direct).

### Testing
To test Pay After Delivery payments, see [Testing](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

The billing and shipping addresses must be the **same** to prevent fraud. 

## Close transactions

If a customer pays into your business bank account directly instead of paying MultiFactor, you need to manually change the <<glossary:transaction status>> to **Completed**. This closes the transaction and stops MultiFactor sending the customer payment requests. 

<details id="how-to-close-transactions">
<summary>How to close transactions</summary>
<br>

To close a transaction manually, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Complete own funds**. 
5. Enter a comment about what happened with the order, and click **Complete**.  
    The total amount of the transaction is deducted from your account balance. 

> **Note:** Once the <<glossary:transaction status>> changes to **Completed**, the **Complete own funds** button is hidden. You must process a [full refund](/docs/refund-payments/) instead. 

</details>

## Failure to pay

If the customer fails to pay within the initial 14 day period, MultiFactor emails them reminders with new payment links, each valid for 6 days: 

- Reminders 1 and 2: No additional fee 
- Reminder 3: Additional fee of 7.50 EUR 
- Reminder 4: Additional fee of 12.50 EUR  

If the customer still fails to pay, the total invoice is transferred to a debt collection agency. 

<details id="how-to-stop-reminders">
<summary>How to stop reminders</summary>
<br>

To stop sending reminders, you can either:

- Credit the invoice for a zero amount, or
- Request to place the transaction on hold for up to 1 month

Email requests to place transactions on hold to <klantenservice@multifactor.nl>  

Provide the following information:

- Transaction details
- Reason for your request
- When you expect to start the billing process again

</details>

## Gift cards

When paying with a gift card and Pay After Delivery, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. Otherwise our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Refunds

- You can't process refunds after the invoice is passed to a collection agency (usually 6 weeks after shipment). This is not visible in your dashboard. To check when the invoice was passed to the agency, email <support@multifactor.nl>
- You can't see whether the customer has paid the invoice. If they have already paid, they receive a refund. If not, they receive an adjusted payment request or the invoice is cancelled.
- For both full and partial refunds, any additional administration costs for the customer are deducted from the invoice. The customer has a further 14 days to complete the payment. 
- You cannot reverse full refunds. 

## Shipment

### Change the order status

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped** to:

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

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

</details>

### Shipping policies

- [MultiFactor shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies)
- [Shipping Policy Nederland](https://www.multifactor.nl/voorwaarden/shipping-policies/) 
- [Herinnering aan onze shipping policy](https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy) 

## Surcharges  

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)