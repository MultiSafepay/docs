---
title: 'CBC/KBC'
weight: 70
meta_title: "Payment methods - CBC/KBC - MultiSafepay Docs"
layout: 'single'
url: '/payment-methods/cbc-kbc/'
logo: '/logo/Payment_methods/CBC.svg'
short_description: 'Accept online banking payments from CBC/KBC customers in Belgium.'
aliases:
    - /support-tab/magento2/payment-methods/cbc
    - /payment-methods/banks/cbc
    - /payments/methods/banks/kbc/
    - /payments/methods/banks/cbc-kbc/
    - /payments/methods/banks/cbc/
    - /payment-methods/cbc/what-is-cbc/
    - /payments/methods/banks/cbc/about/
    - /payments/methods/cbc/product-rules/
    - /payments/methods/kbc/product-rules/
    - /payments/methods/cbc-kbc/product-rules/
    - /payment-methods/cbc-kbc/product-rules/
    - /payment-methods/cbc-kbc/overview/
    - /payment-methods/cbc/how-does-cbc-work/
    - /payments/methods/banks/cbc/payment-flow/
    - /payments/methods/banks/kbc/payment-flow/
    - /payments/methods/banks/cbc-kbc/payment-flow/
    - /payment-methods/cbc-kbc/payment-flow/
    - /payment-methods/cbc/activate-cbc/
    - /payments/methods/banks/kbc/activation/
    - /payment-methods/cbc-kbc/activation/
    - /payment-methods/cbc/cbc-testing
    - /payments/methods/banks/kbc/integration-and-testing/
    - /payments/methods/banks/cbc-kbc/integrating-testing
    - /payment-methods/cbc-kbc/integration-testing/
---
An online banking payment method of two of Belgium's largest banks: CBC which serves the French speaking population, and KBC which serves the Dutch-speaking population.

The payment method functions the same for both the CBC branch and the KBC branch. However, MultiSafepay's payment gateway includes the branches as separate options because customers of one branch can't pay through the other.

[See how CBC/KBC can help your business!](https://www.multisafepay.com/solutions/payment-methods/kbccbc)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/full-partial/) <br> (1 business day after payment is completed) |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 5 days  |

## Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CK as CBC/KBC
    participant Me as Merchant

    C->>Mu: Selects CBC/KBC at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects to online banking
    end
    C->>CK: Authenticates account and completes payment
    CK->>Mu: Transfers funds 
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
| MultiSafepay has collected payment.| Completed | Completed |
| The transaction was cancelled by you or the customer. | Void   | Void   |
| The customer didn't complete payment within 5 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and match all incoming payments. 
{{< /details >}}

**Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. 

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> **Examples** > CBC/KBC direct/redirect |

{{< details title="Ready-made integrations" >}} 
- [Craft Commerce](/craft-commerce/) 
- [OpenCart](/opencart/) 
- [Magento 1](/magento-1/), [Magento 2](/magento-2/) 
- [PrestaShop 1.6](/prestashop-1-6/), [PrestaShop 1.7](/prestashop-1-7/) 
- [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/) 
- [WooCommerce](/woo-commerce/) 
{{< /details >}}