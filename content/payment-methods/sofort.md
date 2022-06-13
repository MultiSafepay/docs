---
title: 'Sofort'
category: 6298bd782d1cf4006032e765
order: 114
hidden: false
parentDoc: 62a1c6c5612f5700137f3640
slug: /payment-methods/sofort/
---
[Sofort](https://www.klarna.com/pay-now/) is a banking payment method by Klarna. It integrates directly with the customer's bank like a direct bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers. 
Once payment is completed, the customer cannot reverse it and Sofort guarantees settlement.

See how Sofort can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/sofort).

# Overview

|   |   |  
|---|---|
| **Countries**  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland <br> :warning: Transactions processed in non-supported countries return a [1024 error](/errors/handling-errors/#error-1024-transaction-refused).  | 
| **Currencies**  | EUR (GBP, CHF, PLN **not** supported) | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/#full-and-partial-refunds)  |
| **Supports** | [Recurring payments](/recurring-payments/), [Second Chance](/second-chance/) |
| **Transactions expire after** | 1 day |
| **Minimum amount** | 0,10 EUR |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Sofort at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects to online banking
    end
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Note over CB,Mu: May take 3 business days <br> Don't ship yet!
    Me->>C: Ships order
    Mu->>Me: Settles funds

{{< /mermaid >}}
<br>  

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
| The customer's bank has authorized the transaction and is transfering the funds. <br> This may take up to 3 business days for all amounts. <br> Do **not** ship yet! MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via Sofort. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 1 day. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
<br>

**Note:** Amounts less than 100 EUR are completed immediately. The status of orders over 100 EUR changes to **uncleared** and then to **completed** after 24 hours.

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Sofort direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>