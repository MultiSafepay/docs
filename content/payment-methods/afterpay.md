---
title: 'AfterPay'
category: 6298bd782d1cf4006032e765
order: 301
hidden: false
parentDoc: 62a727567164d301522a67da
slug: afterpay
---
[AfterPay](https://www.afterpay.nl/en/) is a widely used pay later method in the Netherlands and Belgium. Customers pay for orders after receiving them, and are only charged for items they keep from the order. AfterPay bears the risk and guarantees settlement.

See how AfterPay can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/afterpay).

# Overview
 
|   |   | 
|---|---|
| **Countries**  | The Netherlands, Belgium  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Transactions expire after** | 90 days |

# Payment flow

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
<br>  

# Payment statuses

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| AfterPay has authorized the transaction and the funds are awaiting capture. You can still cancel. <br> **Important:** To capture the funds, when you ship the order you must [manually change the order status to shipped](#shipment). | Completed  | Uncleared  |
| The funds are captured. <br> You can no longer cancel. You can only refund. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped | Completed |
| AfterPay has declined the transaction. <br> Only the customer can contact AfterPay to find out why (for privacy and compliance reasons).  | Declined | Declined |
| AfterPay authorized the transaction, but you or the customer cancelled it before capture. | Void | Void/Cancelled |
| AfterPay authorized the transaction, but you didn't ship within 90 days of creating the transaction **or** the customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Completed |
| Refund complete. | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [AfterPay activation](/payments/activating-payment-methods/#afterpay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) <br> Activate at website level in your MultiSafepay dashboard. |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > AfterPay direct/redirect |
| **Ready-made integrations** | AfterPay is supported in [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 8](/drupal-8-9/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [Odoo](/odoo/), [OpenCart](/opencart/), [PrestaShop 1.6](/prestashop-1-6/), [PrestaShop 1.7](/prestashop-1-7/), [Shopware 5](/shopware-5/), [Shopware 6](/shopware-6/), [WooCommerce](/woo-commerce/), [X-Cart](/x-cart/). |
<br>

---

# User guide

### Addresses

Different billing and shipping addresses are supported.  
The **Transaction details** page in your dashboard only shows the billing address. To retrieve other details, see API reference – [Get order](https://docs-api.multisafepay.com/reference/getorder).

### Collection period
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

### Gift cards

When paying with a gift card and AfterPay, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because AfterPay collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

### Shipment

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

### Surcharges  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

AfterPay therefore strongly recommends discontinuing any surcharges. 

For more information, see AfterPay – [Merchant support](https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/).
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>