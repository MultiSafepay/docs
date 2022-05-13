---
title: 'Klarna'
weight: 40
meta_title: "Payment methods - Klarna - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Klarna.svg'
faq: '.'
short_description: 'A popular pay later method in Austria, Germany, and the Netherlands.'
url: '/payment-methods/klarna/'
aliases:
    - /support-tab/magento2/payment-methods/klarna
    - /payment-methods/klarna/
    - /payment-methods/billing-suite/klarna
    - /payments/methods/billing-suite/klarna/
    - /payments/methods/billing-suite/klarna/about/
    - /payments/methods/klarna/product-rules/
    - /payment-methods/klarna/product-rules/
    - /payment-methods/klarna/overview/
    - /payments/methods/billing-suite/klarna/payment-flow/
    - /payment-methods/klarna/payment-flow/
    - /payments/methods/billing-suite/klarna/integration-and-testing/
    - /payment-methods/klarna/integration-testing/
    - /payments/methods/billing-suite/klarna/activation/
    - /payment-methods/klarna/activation/
---
[Klarna](https://www.klarna.com/) is a flexible online payment method that lets customers pay now, in 30 days, or in 3-4 installments. It also offers financing. Customers are only charged for the items they keep from the order. Klarna bears the risk and guarantees settlement.

[See how Klarna can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/klarna)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Austria, Belgium, Denmark, Finland, France, Germany, Italy, Norway, Portugal, Spain, Sweden, Switzerland, The Netherlands  | 
| **Currencies**  | EUR, GBP, SEK, NOK, DKK  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Transactions expire after** | 1 hour |
| **Addresses** | The customer's billing and shipping addresses must be the **same**. |
| **Gift cards** | [Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/) |

{{< blue-notice >}}**Recent changes** {{< br >}} - Pay in 3 interest-free payments with a bank mandate or card is now available in the Netherlands. {{< br >}} - Pay Later 30 becomes the default in the Netherlands and Belgium from January 11, 2022. {{< br >}} 
For more information, see Klarna – [Betaal later](https://www.klarna.com/nl/zakelijk/producten/betaal-later/). {{< /blue-notice >}}

{{< alert-notice >}} **Surcharges**  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, see Klarna – [Welk bedrag kan ik maximaal doorberekenen aan mijn klant?](https://www.klarna.com/nl/zakelijk/webwinkelsupport/welk-bedrag-kan-ik-maximaal-doorberekenen-aan-mijn-klant/) 
{{< /alert-notice >}}

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant K as Klarna
    participant Me as Merchant

    C->>Mu: Selects Klarna at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, email address, and phone number, <br> and accept the terms & conditions, <br> then redirects to your success page
    else Direct flow
    Mu->>C: Redirects to Klarna
    end
    K->>Mu: Authorizes the payment
    Mu->>K: Captures the funds (settlement is now guaranteed)
    Me->>C: Ships the order (within 28 days, or extend the shipping period)
    Note over Me,C: Manually change the order status to Shipped. 
    K->>C: Sends invoice (you can customize the invoice) 
    C->>K: Completes payment with preferred payment method
    K->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 21 days)

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Klarna. {{< br >}} You can still cancel with Klarna (see [Reservation number](/payment-methods/klarna/reservation-invoice-numbers/)). | Initialized   | Initialized  |
| Klarna has authorized the transaction and the funds are awaiting capture. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} See also: {{< br >}} - [Extend the shipping period](/payment-methods/klarna/extending-shipping-period/) {{< br >}} - [Invoice number](/payment-methods/klarna/reservation-invoice-numbers/) (for queries to Klarna) {{< br >}} **Note:** The billing and shipping addresses must be the **same**. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| The transaction expired after 1 hour or you didn't [change the order status to Shipped](/about-payments/pay-later-shipped-status/) within 28 days. {{< br >}} See [Handling expired orders](/payment-methods/klarna/handling-expired-orders/).  | Expired    | Expired    |
| Klarna authorized the transaction, but either you or the customer cancelled it before capture. | Void   | Void |
| Klarna declined the transaction. {{< br >}} Only the customer can contact Klarna to find out why they declined the transaction. {{< br >}} For merchant support, email <klarna@multisafepay.com> {{< br >}} | Declined | Declined |
|**Refunds**|||
| Refund initiated. | Initialized | Completed |
| Refund complete.  | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Klarna activation](/payments/activating-payment-methods/#klarna) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> **Examples** > Klarna direct/redirect |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/) (redirect). |

Klarna makes your ecommerce platform available in their merchant portal, where your credentials are generated. Use your credentials to configure the Klarna gateway for your MultiSafepay account. 

For questions about your Klarna integration and the connection with your MultiSafepay account, email <integration@multisafepay.com>


