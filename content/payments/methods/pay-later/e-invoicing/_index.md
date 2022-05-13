---
title: 'E-Invoicing'
weight: 10
meta_title: "Payment methods - E-Invoicing - MultiSafepay Docs"
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/e-invoicing.svg' 
short_description: 'A MultiSafepay pay later method that is highly flexible and gives you full control.'
url: '/payment-methods/e-invoicing/'
aliases:
    - /support-tab/magento2/payment-methods/e-invoicing
    - /payment-methods/e-invoicing/
    - /payment-methods/e-invoicing/activate
    - /payment-methods/e-invoicing/e-invoicing-testing
    - /payment-methods/e-invoicing/how-does-e-invoicing-work
    - /payment-methods/e-invoicing/refund
    - /payment-methods/e-invoicing/what-is-it
    - /payment-methods/billing-suite/e-invoicing
    - /payments/methods/billing-suite/e-invoicing/
    - /payments/methods/billing-suite/e-invoicing/about/
    - /payments/methods/e-invoicing/product-rules/
    - /payment-methods/e-invoicing/product-rules/
    - /payment-methods/e-invoicing/overview/
    - /payments/methods/billing-suite/e-invoicing/payment-flow/
    - /payment-methods/e-invoicing/payment-flow/
    - /payments/methods/billing-suite/e-invoicing/integration-and-testing/
    - /payment-methods/e-invoicing/integration-testing/
    - /payments/methods/billing-suite/e-invoicing/activation/
    - /payment-methods/e-invoicing/activation/
---
E-Invoicing is a MultiSafepay pay later method with automation tools that gives you full control of credit management, the payment process, and customer communications.

[See how E-Invoicing can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/e-invoicing)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | 
| **Currencies** | EUR  | 
| **Chargebacks**  | No | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | Doesn't apply |
| **Addresses** | Different billing and shipping addresses are supported. <br> Email a request to <sales@multisafepay.com> |
| **Gift cards** | [Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/) |
| **Shipping policies** | [Shipping Policy Nederland](https://www.multifactor.nl/voorwaarden/shipping-policies/) <br> [Herinnering aan onze shipping policy](https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy) |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects E-Invoicing at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to provide <br> birth date, bank account, email address, and phone number, <br> then redirects to your success page
    else Direct flow
    Mu->>MF: Sends order details
    end
    MF->>Mu: Authorizes the payment
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped. 
    MF->>C: Sends invoice (settlement is now guaranteed)
    C->>MF: Completes payment 
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| MultiSafepay's risk analysis is in progress. {{< br >}} You can still cancel. | Initialized   | Initialized  |
| E-Invoicing has authorized the transaction. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Initialized  |
| **Important**: [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} You must ship to receive payment. | Shipped | Initialized |
| MultiSafepay has collected payment. | Completed    | Completed  |
| E-Invoicing declined the transaction. | Declined | Declined |
| The transaction has been cancelled. | Void/Cancelled | Void/Cancelled |
| The customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete.  | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> **Examples** > E-Invoicing direct/redirect |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/) (direct).  |



