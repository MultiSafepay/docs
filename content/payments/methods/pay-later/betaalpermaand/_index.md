---
title: 'Betaal per Maand'
weight: 30
meta_title: "Payment methods - Betaal per Maand - MultiSafepay Docs"
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/betaalpermaand.svg'
short_description: 'A MultiSafepay pay later method with Santander paid in monthly installments.'
url: '/payment-methods/betaal-per-maand/'
aliases:
    - /support-tab/magento2/payment-methods/betaalplan
    - /payment-methods/billing-suite/betaalplan
    - /payment-methods/betaalplan/
    - /payment-methods/betaalpermaand/activate-betaalplan
    - /payment-methods/betaalpermaand/betaal-per-maand-testing
    - /payment-methods/betaalpermaand/how-does-betaalplan-work
    - /payment-methods/betaalpermaand/refund-betaalplan
    - /payment-methods/betaalpermaand/what-is-betaalplan
    - /payment-methods/billing-suite/betaalpermaand
    - /payments/methods/billing-suite/betaalpermaand/
    - /payments/methods/billing-suite/betaalpermaand/about/
    - /payments/methods/betaal-per-maand/product-rules/
    - /payment-methods/betaal-per-maand/product-rules/
    - /payment-methods/betaal-per-maand/overview/
    - /payments/methods/billing-suite/betaalpermaand/payment-flow/
    - /payment-methods/betaal-per-maand/payment-flow/
    - /payments/methods/billing-suite/betaalpermaand/integration-and-testing/
    - /payment-methods/betaal-per-maand/integration-testing/
    - /payments/methods/billing-suite/betaalpermaand/activation/
    - /payment-methods/betaal-per-maand/activation/
---
[Betaal per Maand](https://www.santander.nl/veelgestelde-vragen/betaal-per-maand) is a MultiSafepay pay later method for large amounts in collaboration with Santander. Customers pay for orders after receiving them as a one-off payment or in monthly installments. They are only charged for the items they keep. Santander bears the risk and guarantees settlement.

[See how Betaal per Maand can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/betaalpermaand-santander)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial refunds](/refunds/full-partial/) |
| **Minimum order amount** | 250 EUR |
| **Maximum order amount** | 8000 EUR |
| **Transactions expire after** | 1 day |
| **Gift cards** | [Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/) |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant S as Santander
    participant Me as Merchant

    C->>Mu: Selects Betaal per Maand at checkout
    alt Redirect flow
    Mu->>C: Redirects briefly to payment page, <br> then to Santander
    else Direct flow
    Mu->>C: Redirects to Santander
    end
    S->>Mu: Authorizes the payment
    Mu->>S: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped. 
    Me->>Mu: Provides track & trace code
    Mu->>S: Forwards track & trace code 
    S->>C: Sends invoice (settlement is now guaranteed)
    C->>S: Selects payment period and method, and completes payment 
    S->>Mu: Transfers funds within 5 business days <br> of Shipped status
    Mu->>Me: Settles funds within 5 business days

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Santander. {{< br >}} To cancel, email <support@multisafepay.com> | Initialized   | Initialized  |
| The customer has completed the pre-form and Santander is authorizing the transaction. | Uncleared | Initialized |
| Santander has authorized the transaction and the funds are awaiting capture. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** {{< br >}} - [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} - [Send us the track-and-trace code](/payment-methods/betaal-per-maand/track-and-trace/). {{< br >}} You must ship to receive payment. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| Santander declined the transaction. {{< br >}} They only provide the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| You cancelled the transaction before capture.   | Void   | Void   |
| The customer didn't complete payment or the funds weren't captured within 1&nbsp;day. | Expired | Expired  |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed      | Completed   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Betaal per Maand activation](/payments/activating-payment-methods/#betaal-per-maand) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/))  |
| **Testing** | You cannot test Betaal per Maand in your MultiSafepay test account. <br> When activating Betaal per Maand as a payment method in your live MultiSafepay account, you can test it before going live. |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> **Examples** > Betaal per Maand direct/redirect |

{{< details title="Ready-made integrations" >}} 

Supported in the following [ready-made integrations](/integrations/ready-made/): 

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


