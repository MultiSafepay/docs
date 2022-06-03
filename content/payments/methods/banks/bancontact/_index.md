---
title: 'Bancontact'
weight: 30
meta_title: "Payment methods - Bancontact - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Bancontact.svg'
short_description: 'Leading Belgian payment method for online, mobile app, and POS payments.'
url: '/payment-methods/bancontact/'
aliases: 
    - /support-tab/magento2/payment-methods/bancontact
    - /payment-methods/banks/bancontact
    - /payments/methods/banks/bancontact/
    - /payments/methods/banks/bancontact-qr/
    - /payment-methods/bancontact/what-is-bancontact/
    - /payments/methods/banks/bancontact/about/
    - /payments/methods/bancontact/product-rules/
    - /payments/methods/bancontact-qr/product-rules/
    - /payment-methods/bancontact/product-rules/
    - /payment-methods/bancontact/overview/
    - /payment-methods/bancontact/activate-bancontact/
    - /payments/methods/banks/bancontact/activation/
    - /payments/methods/banks/bancontact-qr/activation/
    - /payment-methods/bancontact/activation/
    - /payment-methods/bancontact/bancontact-testing
    - /payments/methods/banks/bancontact/integration-and-testing/
    - /payments/methods/banks/bancontact-qr/integration-and-testing/
    - /payment-methods/bancontact/integration-testing/
    - /payment-methods/bancontact/how-does-bancontact-work/
    - /payments/methods/banks/bancontact/payment-flow/
    - /payments/methods/banks/bancontact-qr/payment-flow/
    - /payment-methods/bancontact/payment-flow/
    - /payment-methods/banks/bancontact/
---
[Bancontact](https://www.bancontact.com/en) is a leading Belgian payment method that supports online, mobile, QR, POS, and wallet payments. It is a household name and supported by over 80% of Belgian webshops. Once payment is completed, the customer cannot reverse it and Bancontact guarantees settlement. 

[See how Bancontact can help your business!](https://www.multisafepay.com/solutions/payment-methods/bancontact)

## Overview

|   |   |   
|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Supports**  | [Recurring Payments](/payments/recurring-payments/) (banking only) <br> [Second Chance](/features/second-chance/) <br> [3D Secure](/features/3d-secure/) for all non-mobile payments |
| **Transactions expire after** | Banking: 1 hour, QR: Doesn’t apply  |

## Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Bancontact (QR) at checkout
    Mu->>C: Redirects to payment page <br> to select their bank, <br> and then to their online banking
    C->>CB: Authenticates account/scans QR code and completes payment
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
| The customer has initiated a transaction. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| Bancontact has declined the transaction. | Declined | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| **Refunds** | ||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) <br> - Banking: [Current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/) <br> - QR: Current only |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Bancontact redirect/QR |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |

## Bancontact WIP Service

Bancontact WIP is a wallet initiated payment service you can use for:

- Bancontact One-Click Pay: customer-initiated one-click payments to make checkout faster and increase conversion
- Bancontact Recurring: merchant-initiated subscription payments

### How it works

Bancontact Payconiq gives you access to a merchant wallet to securely store customers' payment details in. Customers give one-time consent and only need to pass [strong customer authentication (SCA)](/payment-regulations/sca/) for their first purchase. 

There is no shift in liability for [chargebacks](/chargebacks/) from [issuer](/glossaries/multisafepay-glossary/#issuer) to [acquirer](/glossaries/multisafepay-glossary/#acquirer) since your fraud and disputes volumes are monitored quarterly. A maximum transaction amount applies. 

### Criteria and activation

- Bancontact WIP is only available to low-risk, high-volume merchants (25,000 transactions quarterly), within the SEPA area. 
- Applies to services only, not physical products. 
- You must have easy-to-use procedures in place for refunds, cancellations, and disputes.
- Customers must be able to add, update, and delete their stored payment details.  
- You must be able to continually demonstrate low rates of fraudulent transactions, or access to your merchant wallet may be revoked. 

Email a request to activate Bancontact WIP to <sales@multisafepay.com>

Requests are screened and approved by Bancontact Payconiq. 

### Integration

See [Recurring Payments](/payments/recurring-payments/).
