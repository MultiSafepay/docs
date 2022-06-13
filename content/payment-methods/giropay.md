---
title: 'Giropay'
category: 6298bd782d1cf4006032e765
order: 109
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: giropay
---
[Giropay](https://www.giropay.de/) is the leading inter-bank payment method in Germany, connecting all major German retail banks. 
Customers pay from their own online banking environment. Settlement is instant and guaranteed.

See how Giropay can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/giropay).

# Overview

|   |   |
|---|---|
| **Countries**  | Germany  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/) |
| **Supports** | [Second Chance](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Giropay at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}} 

# Payment statuses   

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction. | Void   | Void   |
| The customer didn't complete payment within 10 minutes. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |
</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) (current and deprecated versions) |
| **Testing** | [Test payment details](/testing/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Giropay redirect  |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
