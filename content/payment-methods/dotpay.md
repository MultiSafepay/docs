---
title: 'Dotpay'
wcategory: 6298bd782d1cf4006032e765
order: 107
hidden: false
parentDoc: 62a1c6c5612f5700137f3640
slug: /payment-methods/dotpay/
---

Dotpay is an inter-bank payment method that links all major Polish retail banks. 
Customers pay from their own online banking environment.

[See how Dotpay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/dotpay)

# Overview

|   |   |
|---|---|
| **Countries**  | Poland  | 
| **Currencies**  | EUR, PLN | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/#full-and-partial-refunds) |
| **Supports** | [Second Chance](/second-chance/) |
| **Transactions expire after** | 3 days  |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Dotpay at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| The customer has been redirected to their bank. | Initialized | Initialized|
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 3 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Dotpay redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |

> 📘 **Support**
> Email <support@multisafepay.com>