---
title: 'AfterPay'
weight: 60
meta_title: "Payment methods - AfterPay - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/AfterPay.svg' 
short_description: 'A widely used pay later method in the Netherlands and Belgium.'
url: '/payment-methods/afterpay/'
aliases:
    - /support-tab/magento2/payment-methods/afterpay
    - /payment-methods/afterpay/
    - /payment-methods/afterpay/activate-afterpay
    - /payment-methods/afterpay/afterpay-testing
    - /payment-methods/afterpay/how-does-afterpay-work
    - /payment-methods/afterpay/refund-afterpay
    - /payment-methods/afterpay/what-is-afterpay
    - /payment-methods/billing-suite/afterpay
    - /payments/methods/billing-suite/afterpay/
    - /payments/methods/billing-suite/afterpay/about/
    - /payments/methods/afterpay/product-rules/
    - /payment-methods/afterpay/product-rules/
    - /payment-methods/afterpay/overview/
    - /payments/methods/billing-suite/afterpay/payment-flow/
    - /payments/methods/pay-later/afterpay/user-guide/changing-order-status-to-shipped/
    - /payment-methods/afterpay/payment-flow/
    - /payments/methods/billing-suite/afterpay/integration-and-testing/
    - /payment-methods/afterpay/integration-testing/
    - /payments/methods/billing-suite/afterpay/activation/
    - /payment-methods/afterpay/activation/
---
[AfterPay](https://www.afterpay.nl/en/) is a widely used pay later method in the Netherlands and Belgium. Customers pay for orders after receiving them, and are only charged for items they keep from the order. AfterPay bears the risk and guarantees settlement.

[See how AfterPay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/afterpay)

## Overview
 
|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands, Belgium  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Transactions expire after** | 90 days |
| **Gift cards** | [Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/) |
| **Addresses** | Different billing and shipping addresses are supported. <br> The **Transaction details** page in your dashboard only shows the billing address. <br> To retrieve other transaction details, see API reference – [Get order](https://docs-api.multisafepay.com/reference/getorder). | 

{{< alert-notice >}} **Surcharges**  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

AfterPay therefore strongly recommends discontinuing any surcharges. 

For more information, see AfterPay – [Merchant support](https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/).
{{< /alert-notice >}}

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as AfterPay
    participant Me as Merchant

    C->>Mu: Selects AfterPay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to accept terms & conditions <br> and provide their email address, date of birth, and phone number, <br> then redirects to your success page
    else Direct flow
    Mu->>C: Redirects to AfterPay
    end
    A->>Mu: Authorizes the payment
    Mu->>A: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped. 
    A->>C: Sends invoice (standard period of 14 days, settlement is now guaranteed)
    C->>A: Completes payment with preferred method
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
| AfterPay is authorizing the transaction. {{< br >}} You can still decline it. | Uncleared | Uncleared |
| AfterPay has authorized the transaction and the funds are awaiting capture. {{< br >}} You can still decline it. | Completed  | Uncleared  |
| The funds are captured. {{< br >}} **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} You must ship to receive payment. {{< br >}} You can no longer decline the payment; you can only refund. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped | Completed |
| AfterPay has declined the transaction. {{< br >}} AfterPay only provides the reason directly to the customer, for privacy and compliance reasons.  | Declined | Declined |
| AfterPay authorized the transaction, but you or the customer cancelled it before capture. | Void | Void/Cancelled |
| AfterPay authorized the transaction, but you did not ship within 90 days of creating the transaction **or** {{< br >}} The customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Completed |
| Refund complete. | Completed | Completed |

{{< /details >}}

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

## Activation and integration

| | |
|---|---|
| **Activation** | [AfterPay activation](/payments/activating-payment-methods/#afterpay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) {{< br >}} (Activate at website level in your MultiSafepay dashboard.) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> **Examples** > AfterPay direct/redirect |

{{< details title="Ready-made integrations" >}} 

Supported in: 

- [Craft Commerce](/craft-commerce/) 
- [CS-Cart](/cs-cart/) 
- [Drupal 8](/drupal-8-9/) 
- [Magento 1](/magento-1/), [Magento 2](/magento-2/) 
- [Odoo](/odoo/) 
- [OpenCart](/opencart/) 
- [PrestaShop 1.6](/prestashop-1-6/), [PrestaShop 1.7](/prestashop-1-7/) 
- [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/) 
- [WooCommerce](/woo-commerce/) 
- [X-Cart](/x-cart/) 
{{< /details >}}