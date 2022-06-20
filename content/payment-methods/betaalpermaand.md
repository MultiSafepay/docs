---
title: 'Betaal per Maand'
category: 6298bd782d1cf4006032e765
order: 302
hidden: false
parentDoc: 62a727567164d301522a67da
slug: 'betaal-per-maand'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/betaalpermaand.svg" width="200" align="right" style="margin: 20px; max-height: 75px"/>

[Betaal per Maand](https://www.santander.nl/veelgestelde-vragen/betaal-per-maand) is a MultiSafepay pay later method for large amounts in collaboration with Santander. Customers pay for orders after receiving them as a one-off payment or in monthly installments. 
They are only charged for the items they keep. Santander bears the risk and guarantees settlement.

See how Betaal per Maand can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/betaalpermaand-santander).

# Overview

|   |   |
|---|---|
| **Countries**  | The Netherlands  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial refunds](/refunds/) |
| **Amount limits** | Minimum amout: 250 EUR, maximum amount: 8000 EUR |
| **Transactions expire after** | 1 day |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center">

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

# Payment statuses  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your account balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| The customer has been redirected to Santander. <br> To cancel, email <support@multisafepay.com> | Initialized   | Initialized  |
| The customer has completed the pre-form and Santander is authorizing the transaction. | Uncleared | Initialized |
| Santander has authorized the transaction and the funds are awaiting capture. <br> You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** To capture the funds, manually change the order status to Shipped and send us the track-and-trace code (see [Track-and-trace codes](#track-and-trace-codes) below).  | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| Santander declined the transaction. <br> Only the customer can contact them to find out why (for privacy and compliance reasons). | Declined   | Declined   |
| You cancelled the transaction before capture.   | Void   | Void   |
| The customer didn't complete payment or the funds weren't captured within 1 day. | Expired | Expired  |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed      | Completed   |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Betaal per Maand activation](/payment-methods/#betaal-per-maand) |
| **Checkout options** | [Payment pages](/payment-pages/) (current and deprecated versions)  |
| **Testing** | You cannot test Betaal per Maand in your MultiSafepay test account. <br> When activating Betaal per Maand as a payment method in your live MultiSafepay account, you can test it before going live. |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > Betaal per Maand direct/redirect |
| **Ready-made integrations** | Supported in the following [ready-made integrations](/integrations/ready-made/) [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 8](/drupal/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [Odoo](/odoo/), [OpenCart](/opencart/), [PrestaShop 1.7](/prestashop/), [Shopware 5 and 6](/shopware/), [VirtueMart](/virtuemart/), [WooCommerce](/woo-commerce/), [X-Cart](/x-cart/). |
<br>

---

# User guide

## Collection period

If the return process takes too long to verify, you can pause the collection period for 2–4 weeks. 

Have your Betaal per Maand client number ready, and email <klantenservice@santander.nl>

## Gift cards

When paying with a gift card and Betaal per Maand, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Santander collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Known error

The customer's first and last name, and the delivery details must be at least 2 characters long. Anything shorter can cause errors. 

We recommend always requiring full names, not initials, abbreviations, or acronyms.

## Shipment

### Changing orders before shipment

You can still change an order between approval from Santander and shipment.

<details id="how-to-change-orders-before-shipment">
<summary>How to change orders before shipment</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Under **Order summary**, click **Change order status**.
5. Change the status of the initial order to **Shipped**, and then add a **Memo**.
6. Refund the required amount [in full or in part](/refunds/). 

You cannot increase the amount of the initial order by default. Email a request to <sales@multisafepay.com>

</details>

### Changing the order status

When you ship the order, you **must** manually change the [order status](/payment-statuses/) from **completed** to **shipped** to:

- Capture the funds
- Trigger sending the invoice to the customer
- Prevent the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/integrations/ready-made/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

</details>

### Providing track-and-trace codes

<details id="how-to-provide-track-trace-to-multisafepay">
<summary>How to provide track-and-trace codes to MultiSafepay</summary>
<br>

You can provide track-and-trace codes to MultiSafepay:

- In your dashboard when you change the order status to **shipped**, **or**  
- Via our API – [Update order](https://docs-api.multisafepay.com/reference/updateorder) > Ship order
</details>
<br>

> 💬  Support
> Email <support@multisafepay.com>
