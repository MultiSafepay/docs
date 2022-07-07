---
title: 'Request to Pay'
category: 6298bd782d1cf4006032e765
order: 112
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: request-to-pay
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/RTP.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

Request to Pay is a Deutsche Bank payment method based on the PSD2 Open Banking API. Customers are redirected to Deutsche Bank online banking to authenticate themselves, and authorize a secure SEPA transfer. Settlement is instant (if supported) or within 24 hours. 

The funds are transferred directly to your business bank account, instead of your account balance, which simplifies reconciliation.

> ⚠️ Availability
> Request to Pay is currently not available to new merchants. It is still supported for existing merchants. 

# Overview

|   |   |
|---|---|
| **Countries**  | Germany – More countries will follow as more banks migrate to PSD2 APIs.  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/) – All refunds are processed by Deutsche Bank. |
| **Supports** | [Second Chance](/second-chance/) |
| **Transactions expire after** | 1 hour |
| **Minimum amount** | 1 EUR |
| **Maximum amount** | 15,000 EUR |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant D as Deutsche Bank
    participant Me as Merchant

    C->>Mu: Selects Request to Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects customer to online banking
    end
    C->>D: Authenticates account and authorizes SEPA bank transfer
    D->>Mu: Transfers funds (within 24 hours, <br> if Instant SEPA not supported)
    Mu->>Me: Settles funds
    
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
| The customer has been redirected to Deutsche Bank. | Initialized | Initialized |
| Deutsche Bank has authorized the transaction and is transfering the funds. | Completed  | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Deutsche Bank declined the transaction. | Declined | Declined   |
| The customer cancelled the transaction at Deutsche Bank. | Void | Void |
| The customer didn't complete payment within 1 hour. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) (current version only) |
| **Testing** | You can't test Request to Pay in your MultiSafepay test account. <br> You can only make test payments in your MultiSafepay live account. |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Request to Pay direct/redirect |
| **Ready-made integrations** | **Not** supported in our [ready-made integrations](/integrations/ready-made/). |
<br>

> 💬  Support
> Email <support@multisafepay.com>
