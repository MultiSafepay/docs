---
title: 'Belfius'
weight: 80
meta_title: "Payment methods - Belfius - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Belfius.svg' 
short_description: 'Accept online banking payments from Belfius customers in Belgium.'
url: '/payment-methods/belfius/'
aliases:
    - /support-tab/magento2/payment-methods/belfius
    - /payment-methods/banks/belfius
    - /payments/methods/banks/belfius/
    - /payment-methods/belfius/what-is-belfius/
    - /payments/methods/banks/belfius/about/
    - /payments/methods/belfius/product-rules/
    - /payment-methods/belfius/product-rules/
    - /payment-methods/belfius/overview/
    - /payment-methods/belfius/activate-belfius/
    - /payments/methods/banks/belfius/activation/
    - /payment-methods/belfius/activation/
    - /payment-methods/belfius/how-does-belfius-work/
    - /payments/methods/banks/belfius/payment-flow/
    - /payment-methods/belfius/payment-flow/
    - /payment-methods/belfius/belfius-testing
    - /payments/methods/banks/belfius/integration-and-testing/
    - /payment-methods/belfius/integration-testing/
---
Belfius is a popular online banking payment method for Belfius bank customers in Belgium.

[See how Belfius can help your business!](https://www.multisafepay.com/solutions/payment-methods/belfius)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/full-partial/) <br> (1 business day after payment is completed) |
| **Supports** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 5 days  |

## Payment flow
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
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Belfius. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 5 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and finalize all incoming payments. 

{{< /details >}}

**Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. 

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Belfius direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/), **except** OsCommerce and ZenCart. |


