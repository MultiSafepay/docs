---
title: 'Pay After Delivery'
category: 6298bd782d1cf4006032e765
order: 306
hidden: false
parentDoc: 62a727567164d301522a67da
slug: pay-after-delivery
---
Pay After Delivery is MultiSafepay's own pay later method that lets customers pay for orders after receiving them, increasing customer confidence and conversion. 

Customers are only charged for the items they keep. MultiSafepay bears the risk, based on the customer's history, and guarantees settlement.

See how Pay After Delivery can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/pay-after-delivery).

# Overview

|   |   |
|---|---|
| **Countries**  | The Netherlands  | 
| **Currencies** | EUR  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/), [discounts](/discounts/) |
| **Transactions expire after** | 90 days |
| **Amount limits** | Minimum and maximum order amounts apply. Email <sales@multisafepay.com> |
| **Addresses** | The delivery and invoice addresses must be the **same** to prevent fraud. |
| **Shipping policies** | [MultiFactor shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies) <br> [Shipping Policy Nederland](https://www.multifactor.nl/voorwaarden/shipping-policies/) <br> [Herinnering aan onze shipping policy](https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center">

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects Pay After Delivery at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, email address, bank account and phone numbers, <br> and accept the terms & conditions, <br> then redirects to your success page
    else Direct flow
    Mu->>MF: Sends order details
    end
    MF->>Mu: Authorizes the payment (within 2 business days)
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped.
    MF->>C: Sends invoice (within 24 hours of Shipped status, settlement is now guaranteed)
    C->>MF: Completes payment (within 14 days)
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 30 days of Shipped status)

{{< /mermaid >}}

# Payment statuses  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your account balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| MultiSafepay's risk analysis is in progress. You can still cancel. | Initialized | Initialized | 
| We have authorized the transaction and the funds are awaiting capture. You can no longer cancel. You can only refund. <br> See [Closing transactions](#closing-transactions). | Completed | Uncleared | 
| **Important:** To capture the funds, [manually change the order status to shipped](#shipment). | Shipped | Uncleared |
| MultiSafepay has collected payment.  | Shipped | Completed |
| The transaction was cancelled. | Void/Cancelled   | Void/Cancelled | 
| MultiSafepay declined the transaction. | Declined | Declined |
| The customer didn't complete payment within 90 days. | Expired | Expired | 
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |  
| Refund complete. | Completed | Completed | 

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Pay After Delivery activation](/payment-methods/#pay-after-delivery) |
| **Checkout options** | [Payment pages](/payment-pages/) (current and deprecated versions) |
| **Testing** | [Test payment details](/testing/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > Pay After Delivery direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (direct).   |
<br>

---

# User guide

## Closing transactions

If a customer pays into your business bank account directly instead of paying MultiFactor, you need to manually change the transaction status to **completed**. This closes the transaction and stops MultiFactor sending the customer payment requests. 

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

**Note:** Once the transaction status changes to **completed**, the **Complete own funds** button is hidden. You must process a [full refund](/refunds/) instead. 

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

When you ship the order, you **must** manually change the [order status](/payment-statuses/) from **completed** to **shipped** to:

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
5. Change the status to **shipped**.
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

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>