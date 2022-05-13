---
title: 'in3'
weight: 50
meta_title: "in3 - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/in3.svg' 
short_description: 'A Dutch pay later method where customers pay in three installments.'
url: '/payment-methods/in3/'
aliases:
    - /support-tab/magento2/payment-methods/billing-suite/in3/
    - /payment-methods/billing-suite/in3/activate-in3/
    - /payment-methods/billing-suite/in3/how-does-in3-work/
    - /payment-methods/billing-suite/in3/in3-testing/
    - /payment-methods/billing-suite/in3/refund-in3/
    - /payment-methods/billing-suite/in3/what-is-in3/
    - /payment-methods/billing-suite/in3
    - /payments/methods/billing-suite/in3/
    - /payments/methods/billing-suite/in3/about/
    - /payments/methods/in3/product-rules/
    - /payment-methods/in3/product-rules/
    - /payment-methods/in3/overview/
    - /payments/methods/billing-suite/in3/payment-flow/
    - /payments/methods/billing-suite/in3/user-guide/changing-order-status-to-shipped/
    - /payment-methods/in3/payment-flow/
    - /payments/methods/billing-suite/in3/integration-and-testing/
    - /payment-methods/in3/integration-testing/
    - /payments/methods/billing-suite/in3/activation/
    - /payment-methods/in3/activation/
---
[in3](https://payin3.eu/en/) is a Dutch online payment method where customers pay in 3 installments after receiving their order, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 processes all the installments and guarantees settlement after receiving the first one.

[See how in3 can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/in3)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands – in3 checks the customer's country, and billing/shipping address to confirm.  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) {{< br >}} You can request in3 to process a full or partial refund, either before payout or up to 1&nbsp;year afterwards. |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 2 hours |
| **Amount limits** | Default minimum: 100 EUR <br> Default maximum: 3000 EUR <br> You can adjust these limits in the [backend](/glossaries/multisafepay-glossary/#backend) of our [ready-made integrations](/payments/integrations/ecommerce-platforms/) to show or hide in3 on your checkout page depending on the order value. |
| **Addresses** | Different billing and shipping addresses are supported. |
| **Gift cards** | [Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/) |

{{< alert-notice >}} **Surcharges**  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 
{{< /alert-notice >}}

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as in3
    participant Me as Merchant

    C->>Mu: Selects in3 at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, title, and phone number, <br> then redirects to your success page
    else Direct flow
    Mu->>C: Redirects to in3 to select their bank, <br> and accept the payment periods and terms & conditions
    end
    I->>Mu: Authorizes the payment
    Mu->>I: Captures the funds
    C->>I: Pays 1st instalment within 5 mins (settlement is now guaranteed)
    Me->>C: Ships the order 
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 15 days of 1st instalment)
    C->>I: Pays 2nd instalment within 30 days, and 3rd within 60 days 

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| in3's credit check is in progress. {{< br >}} You can still cancel. | Initialized   | Initialized  |
| in3 is waiting for the customer to pay the first installment (within 5 mins). | Uncleared  | Initialized  |
| The customer has paid the first installment. {{< br >}} Settlement is now guaranteed. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| You can [manually change the order status to Shipped](/about-payments/pay-later-shipped-status/) for your records, but this is not required to trigger invoicing. | Shipped | Uncleared | 
| MultiSafepay has collected payment. | Completed | Completed |
| in3 declined the transaction. | Declined | Declined |
| The customer cancelled the transaction or abandoned payment of the first installment. | Void | Void |
| The customer didn't pay the first installment. | Expired | Expired |
|**Refunds**|||
| in3 has successfully processed a full or partial refund. | Completed | Completed |
| The refund was declined. | Declined | Declined   |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Appy to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> **Examples** > in3 direct/redirect |

{{< details title="Ready-made integrations" >}} 
in3 (direct) is supported in: 

- [Craft Commerce](/craft-commerce/) 
- [Magento 1](/magento-1/) 
- [OpenCart](/opencart/) 
- [PrestaShop 1.7](/prestashop-1-7/) 
- [VirtueMart](/virtuemart/) 
- [WooCommerce](/woo-commerce/)   
 {{< /details >}}
