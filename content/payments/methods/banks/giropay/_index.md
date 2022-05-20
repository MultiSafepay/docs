---
title: 'Giropay'
weight: 140
meta_title: "Payment methods - Giropay - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Giropay.svg' 
short_description: 'Leading payment method in Germany connecting all major German banks.'
url: '/payment-methods/giropay/'
aliases:
    - /support-tab/magento2/payment-methods/giropay
    - /payment-methods/banks/giropay
    - /payments/methods/banks/giropay/
    - /payment-methods/giropay/what-is-giropay/
    - /payments/methods/banks/giropay/about/
    - /payments/methods/giropay/product-rules/
    - /payment-methods/giropay/product-rules/
    - /payment-methods/giropay/overview/
    - /payment-methods/giropay/how-does-giropay-work/
    - /payments/methods/banks/giropay/payment-flow/
    - /payment-methods/giropay/payment-flow/
    - /payment-methods/giropay/giropay-testing
    - /payments/methods/banks/giropay/integration-and-testing/
    - /payment-methods/giropay/integration-testing/
    - /payment-methods/giropay/activate-giropay/
    - /payments/methods/banks/giropay/activation/
    - /payment-methods/giropay/activation/
---
[Giropay](https://www.giropay.de/) is the leading inter-bank payment method in Germany, connecting all major German retail banks. Customers pay from their own online banking environment. Settlement is instant and guaranteed.

[See how Giropay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/giropay)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Germany  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Supports** | [Second Chance](/features/second-chance/) |

## Payment flow

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
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |
{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) <br> ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Giropay redirect  |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |

