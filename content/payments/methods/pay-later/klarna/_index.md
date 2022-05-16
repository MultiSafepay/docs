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
    - /payments/methods/billing-suite/klarna/user-guide/handling-errors/
    - /payment-methods/klarna/handling-errors/
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

### Recent changes

- Pay in 3 interest-free payments with a bank mandate or card is now available in the Netherlands. 
- Pay Later 30 becomes the default in the Netherlands and Belgium from January 11, 2022. 

For more information, see Klarna – [Betaal later](https://www.klarna.com/nl/zakelijk/producten/betaal-later/). 

### Surcharges  

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, see Klarna – [Welk bedrag kan ik maximaal doorberekenen aan mijn klant?](https://www.klarna.com/nl/zakelijk/webwinkelsupport/welk-bedrag-kan-ik-maximaal-doorberekenen-aan-mijn-klant/) 

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
| The customer has been redirected to Klarna. <br> You can still cancel with Klarna (see [Reservation number](/payment-methods/klarna/reservation-invoice-numbers/)). | Initialized   | Initialized  |
| Klarna has authorized the transaction and the funds are awaiting capture. <br> (You can no longer cancel; you can only refund.) | Completed  | Uncleared  |
| **Important:** To capture the funds, [manually change the order status to Shipped](/payment-methods/klarna/#shipping-orders). <br> See also: <br> - [Extend the shipping period](/payment-methods/klarna/extending-shipping-period/) <br> - [Invoice number](/payment-methods/klarna/reservation-invoice-numbers/) (for queries to Klarna) | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| The transaction expired after 1 hour or you didn't [change the order status to Shipped](/about-payments/pay-later-shipped-status/) within 28 days. <br> See [Handling expired orders](/payment-methods/klarna/handling-expired-orders/).  | Expired    | Expired    |
| Klarna authorized the transaction, but either you or the customer cancelled it before capture. | Void   | Void |
| Klarna declined the transaction. <br> Only the customer can contact Klarna to find out why (for privacy and compliance reasons). <br> For merchant support, email <klarna@multisafepay.com> | Declined | Declined |
|**Refunds**|||
| Refund initiated. | Initialized | Completed |
| Refund complete.  | Completed | Completed |

{{< /details >}}

### Shipping orders

When you ship the order, you **must** manually change the order status to **Shipped**:

- Captures the funds
- Triggers sending the invoice to the customer
- Prevents the order from expiring

{{< details title="Changing order status to Shipped" >}}

You can change the [order status](/about-payments/multisafepay-statuses/) from **Completed** to **Shipped**:

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/integrations/ready-made/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

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

{{< details title="Gift cards with pay later methods" >}}

When paying with a gift card and a [pay later method](/payments/methods/pay-later/), customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because pay later methods collect and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

{{< /details >}}

{{< details title="Known errors" >}}

If you receive a `code:BAD_VALUE, Bad value: order_lines[0].reference` error from Klarna, try using shorter SKU numbers, e.g. fewer than 9 characters. 

{{< /details >}}
