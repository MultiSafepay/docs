---
title: 'Betaal per Maand'
weight: 30
meta_title: "Payment methods - Betaal per Maand - MultiSafepay Docs"
layout: 'single'
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
    - /payments/methods/billing-suite/betaalpermaand/user-guide/changing-orders-before-shipment/
    - /payment-methods/betaal-per-maand/changing-orders/
    - /payments/methods/billing-suite/betaalpermaand/user-guide/known-errors/
    - /payment-methods/betaal-per-maand/known-errors/
    - /payments/methods/billing-suite/betaalpermaand/user-guide/pauzing-collection-period/
    - /payment-methods/betaal-per-maand/pauzing-collection/
    - /payments/methods/billing-suite/betaalpermaand/user-guide/providing-track-and-trace/
    - /payment-methods/betaal-per-maand/track-and-trace/
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
| **Amount limits** | Min: 250 EUR Max: 8000 EUR |
| **Transactions expire after** | 1 day |

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
| The customer has been redirected to Santander. <br> To cancel, email <support@multisafepay.com> | Initialized   | Initialized  |
| The customer has completed the pre-form and Santander is authorizing the transaction. | Uncleared | Initialized |
| Santander has authorized the transaction and the funds are awaiting capture. <br> (You can no longer cancel; you can only refund.) | Completed  | Uncleared  |
| **Important:** To capture the funds, manually change the order status to Shipped and send us the track-and-trace code (see [Providing track-and-trace codes](/payment-methods/betaal-per-maand/#providing-track-and-trace-codes)).  | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| Santander declined the transaction. <br> Only the customer can contact them to find out why (for privacy and compliance reasons). | Declined   | Declined   |
| You cancelled the transaction before capture.   | Void   | Void   |
| The customer didn't complete payment or the funds weren't captured within 1&nbsp;day. | Expired | Expired  |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed      | Completed   |

{{< /details >}}

### Changing orders before shipment

You can still change an order between approval from Santander and shipment.

{{< details title="Changing orders before shipment" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Under **Order summary**, click **Change order status**.
5. Change the status of the initial order to **Shipped**, and then add a **Memo**.
6. Refund the required amount [in full or in part](/refunds/full-partial/). 

You cannot increase the amount of the initial order by default. Email a request to <sales@multisafepay.com>

{{< /details >}}

### Shipping orders

When you ship the order, you **must** manually change the [order status](/about-payments/multisafepay-statuses/) from **Completed** to **Shipped** to:

- Capture the funds
- Trigger sending the invoice to the customer
- Prevent the order from expiring

{{< details title="Changing order status to shipped" >}}

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

### Providing track-and-trace codes

You can provide track-and-trace codes to MultiSafepay:

- In your dashboard when you change the order status to Shipped, **or**  
- Via our API. See API reference – [Update order](https://docs-api.multisafepay.com/reference/updateorder) > Ship order.

### Pauzing the collection period

If the return process takes too long to verify, you can pauze the collection period for 2 to 4 weeks. Contact Betaal per Maand.

## Activation and integration

| | |
|---|---|
| **Activation** | [Betaal per Maand activation](/payments/activating-payment-methods/#betaal-per-maand) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/))  |
| **Testing** | You cannot test Betaal per Maand in your MultiSafepay test account. <br> When activating Betaal per Maand as a payment method in your live MultiSafepay account, you can test it before going live. |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > Betaal per Maand direct/redirect |

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

{{< details title="Gift cards" >}}

When paying with a gift card and Betaal per Maand, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Santander collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

{{< /details >}}

{{< details title="Known errors" >}}

The customer's first and last name, and the delivery details must be at least 2 characters long. Anything shorter can cause errors. 

We recommend always requiring full names, not initials, abbreviations, or acronyms.

{{< /details >}}


