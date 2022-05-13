---
title: 'SEPA Direct Debit'
weight: 90
meta_title: "Payment methods - SEPA Direct Debit - MultiSafepay Docs"
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/directdebit-en.svg' 
short_description: 'Debit European customers directly from their bank account.'
url: '/payment-methods/sepa-direct-debit/'
aliases:
    - /support-tab/magento2/payment-methods/direct-debit
    - /payment-methods/direct-debit/
    - /payment-methods/banks/direct-debit/
    - /payment-methods/banks/sepa-direct-debit
    - /payments/methods/banks/sepa-direct-debit/
    - /payment-methods/sepa-direct-debit/what-is-sepa-direct-debit/
    - /payment-methods/direct-debit/what-is-direct-debit/
    - /payment-methods/banks/direct-debit/what-is-direct-debit/
    - /payments/methods/banks/sepa-direct-debit/about/
    - /payments/methods/sepa/product-rules/
    - /payment-methods/sepa-direct-debit/product-rules/
    - /payment-methods/sepa-direct-debit/overview/
    - /payment-methods/direct-debit/how-does-direct-debit-work/
    - /payment-methods/banks/direct-debit/how-does-direct-debit-work/
    - /payment-methods/sepa-direct-debit/how-does-sepa-direct-debit-work/
    - /payment-methods/sepa-direct-debit/reason-codes/
    - /payments/methods/banks/sepa-direct-debit/payment-flow/
    - /payments/sepa-direct-debit/reason-codes
    - /payment-methods/sepa-direct-debit/payment-flow/
    - /payment-methods/direct-debit/activate-direct-debit/
    - /payment-methods/banks/direct-debit/activate-direct-debit/
    - /payment-methods/sepa-direct-debit/activate-sepa-direct-debit/
    - /payments/methods/banks/sepa-direct-debit/activation/
    - /payment-methods/sepa-direct-debit/activation/
    - /payment-methods/sepa-direct-debit/sepa-direct-debit-testing
    - /payments/methods/banks/sepa-direct-debit/integration-and-testing/
    - /payment-methods/sepa-direct-debit/integration-testing/
---

SEPA Direct Debit is a European banking payment method where customers authorize automatic one-off or recurring debits directly from their bank account. It is available in 36 countries and supports Sofort and iDEAL.

[See how SEPA Direct Debit can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/direct-debit)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | [SEPA region](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf)  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | Yes – See below. | 
| **Refunds** | [Full and partial](/refunds/full-partial/)  |
| **Payment features** | [Recurring Payments](/features/recurring-payments/) {{< br >}} [Second Chance](/features/second-chance/) | 

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    
    C->>Me: Selects SEPA Direct Debit at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to confirm their IBAN and account name, <br> then to your success page
    Me->>Mu: [Direct flow] Sends request and customer information
    end
    Mu->>CB: Conducts background check <br> and sends e-mandate
    CB->>Mu: Processes transaction and transfers funds 
    Note over CB,Mu: -500 EUR= 9 days <br> +500 EUR= 22 days <br> Processing time can be reduced on request. <br> Email sales@multisafepay.com
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;   

{{< details title= "E-mandates" >}}

MultiSafepay creates e-mandates automatically based on the customer's IBAN and your site ID, specifying if it is a first debit or recurring debit. We send all e-mandates to our bank at the end of every business day.  

{{< /details >}}

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| MultiSafepay's customer background check was successful and we've generated an e-mandate. | Initialized  | Initialized |
| We've sent the e-mandate to the customer's bank. {{< br >}} You can no longer cancel. | Uncleared | Uncleared |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction or requested a chargeback, or their bank declined the transaction. | Void | Void |
| The customer's bank declined the transaction. {{< br >}} See the [reason codes](/payment-methods/sepa-direct-debit/payment-flow/#reason-codes-for-declined-transactions) below. | Declined | Declined   |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed | 

{{< /details >}}

See also User guide – [Reason codes for declined transactions](/payment-methods/sepa-direct-debit/reason-codes/).

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment components](/payment-components/) {{< br >}} [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/))  |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> **Examples** > SEPA Direct Debit direct/redirect |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/) (direct). |

