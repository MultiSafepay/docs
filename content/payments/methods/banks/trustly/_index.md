---
title: 'Trustly'
weight: 130
meta_title: "Payment methods - Trustly - MultiSafepay Docs"
layout: 'single'
logo: 'https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Trustly.svg' 
short_description: 'Accept online banking payments from a number of European countries.'
url: '/payment-methods/trustly/'
aliases:
    - /support-tab/magento2/payment-methods/trustly
    - /payment-methods/trustly/
    - /payment-methods/banks/trustly
    - /payments/methods/banks/trustly/
    - /payment-methods/trustly/what-is-trustly/
    - /payments/methods/banks/trustly/about/
    - /payments/methods/trustly/product-rules/
    - /payment-methods/trustly/product-rules/
    - /payment-methods/trustly/overview/
    - /payment-methods/trustly/how-does-trustly-work/
    - /payments/methods/banks/trustly/payment-flow/
    - /payment-methods/trustly/payment-flow/
    - /payment-methods/trustly/trustly-testing
    - /payments/methods/banks/trustly/integration-and-testing/
    - /payment-methods/trustly/integration-testing/
    - /payment-methods/trustly/activate-trustly/
    - /payments/methods/banks/trustly/activation/
    - /payment-methods/trustly/activation/
---
[Trustly](https://www.trustly.net/nl-NL) is a quick, secure banking payment method that is available in 29 European countries. Customers pay from their own online banking environment.

[See how Trustly can help your business!](https://www.multisafepay.com/solutions/payment-methods/trustly)

## Overview

|   |   |  
|---|---|
| **Countries**  | Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, United Kingdom  | 
| **Currencies**  | EUR, GBP, SEK | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/full-partial/)  |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** |  2 hours |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Trustly at checkout
    Mu->>C: Redirects to payment page <br> to select their country and bank, <br> then to online banking
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
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction at their bank. | Cancelled   | Cancelled   |
| The customer didn't complete payment within 2 days. | Expired | Expired |
| In rare cases, the transaction is marked as **Uncleared**. {{< br >}} Trustly then informs MultiSafepay of the correct status, which may be **Completed**, **Declined**, or **Expired**. {{< br >}} **Uncleared** status automatically expires after 5 days. | Uncleared | Uncleared   |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Trustly redirect |

{{< details title="Ready-made integrations" >}} 
Trustly (direct) is supported in: 

- [Craft Commerce](/craft-commerce/) 
- [CS-Cart](/cs-cart/) 
- [Drupal 8](/drupal-8-9/) 
- [Magento 1](/magento-1/), [Magento 2](/magento-2/) 
- [Odoo](/odoo/) 
- [OpenCart](/opencart/) 
- [PrestaShop 1.7](/prestashop-1-7/) 
- [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/) 
- [VirtueMart](/virtuemart/) 
- [WooCommerce](/woo-commerce/) 
- [X-Cart](/x-cart/) 
{{< /details >}} 


