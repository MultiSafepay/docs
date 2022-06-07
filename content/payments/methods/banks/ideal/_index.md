---
title: 'iDEAL'
weight: 10
meta_title: "Payment methods - iDEAL - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/iDeal.svg' 
short_description: 'Leading Dutch payment method connecting all major retail banks.'
url: '/payment-methods/ideal/'
aliases:
    - /support-tab/magento2/payment-methods/ideal
    - /payment-methods/ideal/
    - /payment-methods/banks/ideal/
    - /payments/methods/banks/ideal/
    - /payments/methods/banks/idealqr/
    - /payment-methods/ideal/what-is-ideal/
    - /payments/methods/banks/ideal/about/
    - /payments/methods/ideal/product-rules/
    - /payments/methods/ideal-qr/product-rules/
    - /payment-methods/ideal/product-rules/
    - /payment-methods/ideal/overview/
    - /payment-methods/ideal/how-does-ideal-work/
    - /payments/methods/banks/ideal/payment-flow/
    - /payments/methods/banks/idealqr/payment-flow/
    - /payment-methods/ideal/payment-flow/
    - /payment-methods/ideal/ideal-testing
    - /payments/methods/banks/ideal/integration-and-testing/
    - /payments/methods/banks/idealqr/integration-and-testing/
    - /payment-methods/ideal/testing/
    - /payment-methods/ideal/integration-testing/
    - /payment-methods/ideal/activate-ideal/
    - /payments/methods/banks/ideal/activation/
    - /payments/methods/banks/idealqr/activation/
    - /payment-methods/ideal/activation/
    - /payment-methods/banks/idealqr/
---

[iDEAL](https://www.ideal.nl/en/) is the leading payment method in the Netherlands and links all major Dutch retail banks. Customers pay via mobile banking app, QR code, or in their own online banking environment. Once a payment is completed, the customer cannot reverse it and iDEAL guarantees settlement.

[See how iDEAL can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/ideal)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/#full-and-partial-refunds) |
| **Supports** | [Second Chance](/features/second-chance/) {{< br >}} [Recurring Payments](/payments/recurring-payments/) (banking only) |
| **Transactions expire after** | 1.5 hours |

## iDEAL QR
 
[iDEAL QR](https://www.ideal.nl/en/businesses/offer-ideal-qr/) has a wide range of applications. Customers can scan QR codes off screens or paper (e.g. invoices, receipts), and change the amount to pay. This makes it particularly suitable for hospitality, charity collectors, and home deliveries. You can specify whether the same QR code can be used more than once.

Not all Dutch banking apps support iDEAL QR yet, so we recommend that customers scan QR codes with their camera or a general QR reader. This redirects to the ideal.nl payment page, which works for all banks. 

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    alt Redirect flow
    C->>Mu: Selects iDEAL (QR) at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    else Direct flow
    C->>Mu: Selects iDEAL (QR) and their bank at checkout
    Mu->>C: Redirects to online banking
    end
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
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via their bank. | Void   | Void/Cancelled   |
| iDEAL processing error. | Declined   | Declined   |
| The customer didn't complete payment within 1.5 hours. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund pending (banking only).  | Reserved | Reserved |
| Refund complete. | Completed | Completed |
{{< /details >}}

**Note:** To increase transparency for customers, the name of your website appears on the iDEAL payment page and "Your-website-name by MultiSafepay" on the customer's bank statement.

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) {{< br >}} [Payment pages](/payment-pages/) {{< br >}} - Banking: [Current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/) {{< br >}} - QR: Current only |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > iDEAL direct/redirect/QR |

{{< details title="Ready-made integrations" >}} 
Banking supported in: All our [ready-made integrations](/integrations/ready-made/), **except** ZenCart. 

QR supported in:
- [Craft Commerce](/craft-commerce/) 
- [CS-Cart](/cs-cart/) 
- [Drupal 8](/drupal-8-9/) 
- [Magento 1](/magento-1/), [Magento 2](/magento-2/) 
- [Odoo](/odoo/) 
- [OpenCart](/opencart/) 
- [PrestaShop 1.7](/prestashop-1-7/) 
- [Shopware 5](/shopware-5/) 
- [VirtueMart](/virtuemart/) 
- [WooCommerce](/woo-commerce/) 
- [X-Cart](/x-cart/) 
{{< /details >}} 


