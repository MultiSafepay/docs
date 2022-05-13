---
title: 'Sofort'
weight: 40
meta_title: "Payment methods - Sofort - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/SOFORT.svg' 
url: '/payment-methods/sofort/'
short_description: 'Accept secure bank transfers from a number of European countries.'
aliases:
    - /support-tab/magento2/payment-methods/sofort-banking
    - /payment-methods/sofort-banking/
    - /payment-methods/banks/sofort-banking
    - /payments/methods/banks/sofort-banking/
    - /payments/methods/banks/sofort/
    - /payment-methods/bancontact/what-is-sofort-banking/
    - /payments/methods/banks/sofort-banking/about/
    - /payments/methods/sofort-banking/product-rules/
    - /payment-methods/sofort/product-rules/
    - /payment-methods/sofort/overview/
    - /payment-methods/sofort-banking/how-does-sofort-banking-work/
    - /payments/methods/banks/sofort-banking/payment-flow/
    - /payments/methods/banks/sofort/payment-flow/
    - /payment-methods/sofort/payment-flow/
    - /payment-methods/bancontact/sofort-banking-testing
    - /payments/methods/banks/sofort-banking/integration-and-testing/
    - /payments/methods/banks/sofort/integration-testing/
    - /payment-methods/sofort/integration-testing/
    - /payment-methods/sofort-banking/activate-sofort-banking/
    - /payments/methods/banks/sofort-banking/activation/
    - /payments/methods/banks/sofort/activation/
    - /payment-methods/sofort/activation/
---
[Sofort](https://www.klarna.com/pay-now/) is a banking payment method by Klarna. It integrates directly with the customer's bank like a direct bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers. Once payment is completed, the customer cannot reverse it and Sofort guarantees settlement.

[See how Sofort can help your business!](https://www.multisafepay.com/solutions/payment-methods/sofort)

## Overview

|   |   |  
|---|---|
| **Countries**  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland {{< br >}} **Note:** Transactions processed in non-supported countries return a [1024 error](/errors/handling-errors/#error-1024-transaction-refused).  | 
| **Currencies**  | EUR {{< br >}} **Note:** GBP, CHF, PLN are **not** supported. | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/full-partial/)  |
| **Payment features** | [Recurring Payments](/features/recurring-payments/) {{< br >}} [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 1 day |
| **Minimum amount** | 0,10 EUR |

## Payment flow

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
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| The customer's bank has authorized the transaction and is transfering the funds.  {{< br >}} May take up to 3 business days for all amounts. {{< br >}} Do **not** ship yet! MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via Sofort. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 1 day. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

**Note:** Amounts less than 100 EUR are completed immediately. The status of orders over 100 EUR changes to **Uncleared** and then to **Completed** after 24 hours.

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) {{< br >}} [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> **Examples** > Sofort direct/redirect |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/). |
