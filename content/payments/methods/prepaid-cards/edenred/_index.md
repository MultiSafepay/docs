---
title: Edenred
weight: 260
meta_title: "Payment methods - Edenred - MultiSafepay Docs"
layout: "single"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/edenred.svg"
short_description: "Accept payments using Edenred vouchers."
url: "/payment-methods/edenred/"
aliases:
    - /payments/methods/prepaid-cards/edenred/
    - /payments/methods/prepaid-cards/edenred/product-rules/
    - /payment-methods/edenred/product-rules/
    - /payment-methods/edenred/overview/
    - /payments/methods/prepaid-cards/edenred/payment-flow/
    - /payment-methods/edenred/payment-flow/
    - /payments/methods/prepaid-cards/edenred/integration-and-testing/
    - /payment-methods/edenred/integration-testing/
    - /payments/methods/prepaid-cards/edenred/activation/
    - /payment-methods/edenred/activation/
---
[Edenred](https://www.edenred.be/nl) lets employers provide their employees with a prepaid card loaded with Edenred vouchers:  

- Ticket Restaurant
- Ticket EcoCheques
- Ticket Compliments
- Ticket Sport & Culture

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Belgium  | 
| **Currencies** | EUR  | 
| **Chargebacks** | No | 
| **Refunds** | No |
| **Supports** | [Second Chance](/features/second-chance/) |

## How it works
  
- You must sign a contract with Edenred.
- For each voucher, you must comply with Edenred's rules regarding permitted products and services. 
- An Edenred prepaid card can contain multiple Edenred vouchers.
- Edenred vouchers can be used for partial payments in combination with another payment method.
- View all the Edenred transactions for your website in [My Edenred](https://myedenred.be).

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant E as Edenred
    participant Me as Merchant

    C->>Mu: Selects Edenred at checkout
    Mu->>C: Redirects to payment page <br> to select the relevant voucher, <br> then to their Edenred account
    C->>E: Authenticates account, and authorizes MultiSafepay access
    E->>Mu: Confirms authorization <br> and sufficient funds on voucher
    E->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Edenred activation](/payments/activating-payment-methods/#edenred) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Edenred redirect <br> By default, all activated Edenred vouchers display at checkout, but you can also specify which Edenred vouchers to display per transaction. |
| **Ready-made integrations** | Only supported in our [Magento 2](/magento-2/) integration.   |

