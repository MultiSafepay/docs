---
title: Paysafecard
weight: 250
meta_title: "Payment methods - Paysafecard - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Paysafecard.svg'
short_description: 'Accept online payments using secure prepaid vouchers.'
url: '/payment-methods/paysafecard/'
aliases:
    - /support-tab/magento2/payment-methods/paysafecard
    - /payment-methods/paysafecard/
    - /payment-methods/prepaid-cards/paysafecard
    - /payments/methods/prepaid-cards/paysafecard/
    - /payments/methods/prepaid-cards/paysafecard/about/
    - /payments/methods/paysafecard/product-rules/
    - /payment-methods/paysafecard/product-rules/
    - /payment-methods/paysafecard/overview/
    - /payment-methods/paysafecard/how-does-paysafecard-work
    - /payments/methods/prepaid-cards/paysafecard/payment-flow/
    - /payment-methods/paysafecard/payment-flow/
    - /payment-methods/paysafecard/integration-testing/
    - /payment-methods/paysafecard/activate-paysafecard
    - /payments/methods/prepaid-cards/paysafecard/activation/
    - /payment-methods/paysafecard/activation/
---

[Paysafecard](https://www.paysafecard.com/en/) lets customers make online payments using secure prepaid vouchers, available for purchase locally. The customer chooses a fixed voucher amount: 10, 25, 50 or 100 EUR. The funds are available immediately.

Customers enter the voucher code, without providing any personal payment details. Vouchers for different amounts are available in the local currency in 46 countries.

The card balance remains available for 12 months free of charge. After 12 months, customers are charged a monthly administration fee of 3 EUR, which is deducted from the balance.

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide – Go to [paysafecard.com](https://www.paysafecard.com/en-gb/), and click the globe icon in the banner.  | 
| **Currencies**  | EUR, GBP, USD  | 
| **Chargebacks**  | No | 
| **Refunds** | Paid with Paysafecard only: You can't refund via MultiSafepay because we don't receive any customer payment details to refund to. Refund in your own online banking. {{< br >}} {{< br >}} Paid with Paysafecard **and** another payment method: [Full refunds](/refunds/#full-and-partial-refunds).  |
| **Transactions expire after** | 3 hours |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as Paysafecard
    participant Me as Merchant

    C->>Mu: Selects Paysafecard at checkout
    Mu->>C: Redirects to payment page
    C->>P: Enters 16-digit card PIN and completes payment
    P->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Paysafecard. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction at Paysafecard. | Void   | Void   |
| The customer didn't complete payment within 3&nbsp;hours. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | Paysafecard doesn't require activation. <br> Search for outlets that sell Paysafecard: <br> - [Find sales outlets](https://www.paysafecard.com/en/find-sales-outlet-1/) <br> - [Verkooppunten zoeken](https://www.paysafecard.com/nl/verkooppunt-vinden-1/) <br> For any questions, email <sales@multisafepay.com> |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | You can’t test Paysafecard in your MultiSafepay test account. <br> You can only make test payments in your MultiSafepay live account. <br> For any questions, email <integration@multisafepay.com> |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Gift card redirect |

{{< details title="Ready-made integrations" >}} 

Supported in: 

- [OsCommerce](/oscommerce/) 
- [Magento 1](/magento-1/) 
- [VirtueMart](/virtuemart/) 
- [X-Cart](/x-cart/) 
- [Zen Cart](/zen-cart/)

{{< /details >}}
