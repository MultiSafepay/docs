---
title: 'Belfius'
category: 6298bd782d1cf4006032e765
order: 105
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: belfius
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Belfius.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

Belfius is a popular online banking payment method for Belfius bank customers in Belgium.

See how Belfius can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/belfius).

# Overview

|   |   |
|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/) (1 business day after payment is completed) |
| **Supports** | [Second Chance](/second-chance/) |
| **Transactions expire after** | 5 days  |

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant B as Belfius
    participant Me as Merchant

    C->>Mu: Selects Belfius at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects to online banking
    end
    C->>B: Authenticates account and completes payment
    B->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}

**Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. 

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
| The customer has been redirected to Belfius. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 5 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
<br>

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **initialized**. We import our bank statements daily and finalize all incoming payments. 

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) (current version only) |
| **Testing** | [Test payment details](/testing/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Belfius direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/), **except** OsCommerce and ZenCart. |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
