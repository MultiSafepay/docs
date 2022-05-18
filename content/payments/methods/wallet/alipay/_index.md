---
title: 'Alipay'
weight: 230
meta_title: "Payment methods - Alipay - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Alipay.svg' 
short_description: 'Leading global digital wallet for Chinese customers.'
url: '/payment-methods/alipay/'
aliases:
    - /support-tab/magento2/payment-methods/alipay
    - /payment-methods/alipay/
    - /payment-methods/wallet/alipay
    - /payments/methods/wallet/alipay/
    - /payments/methods/wallet/alipay/about/
    - /payments/methods/alipay/product-rules/
    - /payment-methods/alipay/product-rules/
    - /payment-methods/alipay/overview/
    - /payment-methods/wallet/alipay/alipay-how-does-it-work
    - /payments/methods/wallet/alipay/payment-flow/
    - /payment-methods/alipay/payment-flow/
    - /payment-methods/wallet/paypal/paypal-testing
    - /payments/methods/wallet/alipay/integration-and-testing/
    - /payment-methods/alipay/integration-testing/
    - /payment-methods/wallet/alipay/activate-alipay
    - /payments/methods/wallet/alipay/activation/
    - /payment-methods/alipay/activation/
---
[Alipay](https://global.alipay.com/platform/site/ihome) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online, QR, and contactless POS payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.

[See how Alipay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/alipay)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR, USD (currency conversion in EUR only)  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial refunds](/refunds/full-partial/), [discounts](/refunds/discounts/), [API refunds](/refunds/pay-later/)  |
| **Payment features**  | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 5 hours |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Alipay
    participant Me as Merchant

    C->>Mu: Selects Alipay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page
    else Direct flow
    Mu->>A: Payment is processed with Alipay
    end
    A->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Alipay. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 5&nbsp;hours, or it was cancelled. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved   |
| Refund complete.  | Completed | Completed   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only)  |
| **Testing** | [Test payment details](/testing/test-payment-details/#wallets) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > Alipay direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (direct), **except** PrestaShop 1.6, OsCommerce, and Zen Cart.   |
