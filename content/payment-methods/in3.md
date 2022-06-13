---
title: 'in3'
category: 6298bd782d1cf4006032e765
order: 304
hidden: false
parentDoc: 62a727567164d301522a67da
slug: in3
---
[in3](https://payin3.eu/en/) is a Dutch online payment method where customers pay in 3 installments after receiving their order, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 processes all the installments and guarantees settlement after receiving the first one.

See how in3 can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/in3).

# Overview

|   |   |
|---|---|
| **Countries**  | The Netherlands – in3 checks the customer's country, and billing/shipping address to confirm.  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/), [discounts](/discounts/) <br> You can request in3 to process a full or partial refund, either before payout or up to 1 year afterwards. |
| **Supports** | [Second Chance](/second-chance/) |
| **Transactions expire after** | 2 hours |
| **Amount limits** | Minimum amount: 100 EUR Maximum amount: 3000 EUR <br> You can adjust these limits in the backend of our [ready-made integrations](/integrations/ready-made/) to show or hide in3 on your checkout page depending on the order value. |
| **Addresses** | Different billing and shipping addresses are supported. |
<br>

# Payment flow

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
| in3's credit check is in progress. You can still cancel. | Initialized   | Initialized  |
| in3 is waiting for the customer to pay the first installment (within 5 mins). | Uncleared  | Initialized  |
| The customer has paid the first installment. Settlement is now guaranteed. <br> You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| You can [manually change the order status to shipped](#shipment) for your records, but this is not required to trigger invoicing. | Shipped | Uncleared | 
| MultiSafepay has collected payment. | Completed | Completed |
| in3 declined the transaction. | Declined | Declined |
| The customer cancelled the transaction or abandoned the first installment. | Void | Void |
| The customer didn't pay the first installment. | Expired | Expired |
|**Refunds**|||
| in3 has successfully processed a full or partial refund. | Completed | Completed |
| The refund was declined. | Declined | Declined   |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Appy to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > in3 direct/redirect |
| **Ready-made integrations** | in3 (direct) is supported in [Craft Commerce](/craft-commerce/), [Magento 1](/magento-1/), [OpenCart](/opencart/), [PrestaShop 1.7](/prestashop-1-7/), [VirtueMart](/virtuemart/), [WooCommerce](/woo-commerce/). |
<br>

---

# User guide

### Gift cards

When paying with a gift card and in, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. This is because in3 collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

### Shipment

When you ship the order, you can change the order status to **shipped** for your records, bu this is not required to trigger invoicing.

<details id="how-to-change-order-status-to-shipped">
<summary>How to change the order status to shipped</summary>
<br>

You can change the [order status](/payment-statuses/) from **completed** to **shipped**:

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

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 

<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>