---
title: EPS
weight: 110
meta_title: "Payment methods - EPS - MultiSafepay Docs"
layout: "single"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/EPS.svg"
short_description: 'Accept online banking payments from customers of all Austrian banks.'
url: "/payment-methods/eps/"
aliases:
    - /support-tab/magento2/payment-methods/eps
    - /payment-methods/banks/eps
    - /payments/methods/banks/eps/
    - /payment-methods/eps/what-is-eps/
    - /payments/methods/banks/eps/about/
    - /payments/methods/eps/product-rules/
    - /payment-methods/eps/product-rules/
    - /payment-methods/eps/overview/
    - /payment-methods/eps/how-does-eps-work/
    - /payments/methods/banks/eps/payment-flow/
    - /payment-methods/eps/payment-flow/
    - /payment-methods/eps/eps-testing
    - /payments/methods/banks/eps/integration-and-testing/
    - /payment-methods/eps/integration-testing/
---
EPS is a widely accepted inter-bank payment method that links all major Austrian retail banks. Customers pay in their own online banking environment. Settlement is instant and guaranteed.

[See how EPS can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/eps)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Austria  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | Doesn't apply |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects EPS at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction. | Void   | Void   |
| The customer didn't complete payment within 10 minutes. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > EPS redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |

