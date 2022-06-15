---
title: 'iDEAL'
category: 6298bd782d1cf4006032e765
order: 110
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: ideal
---
[iDEAL](https://www.ideal.nl/en/) is the leading payment method in the Netherlands and links all major Dutch retail banks. Customers pay via mobile banking app, QR code, or in their own online banking environment. Once a payment is completed, the customer cannot reverse it and iDEAL guarantees settlement.

See how iDEAL can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/ideal).

# Overview

|   |   |
|---|---|
| **Countries**  | The Netherlands  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/) |
| **Supports** | [Second Chance](/second-chance/), [Recurring payments](/recurring-payments/) (banking only) |
| **Transactions expire after** | 1.5 hours |

**Note:** To increase transparency for customers, the name of your website appears on the iDEAL payment page and "Your-website-name by MultiSafepay" on the customer's bank statement.

## iDEAL QR
 
[iDEAL QR](https://www.ideal.nl/en/businesses/offer-ideal-qr/) has a wide range of applications. Customers can scan QR codes off screens or paper (e.g. invoices, receipts), and change the amount to pay. This makes it particularly suitable for hospitality, charity collectors, and home deliveries. You can specify whether the same QR code can be used more than once.

Not all Dutch banking apps support iDEAL QR yet, so we recommend that customers scan QR codes with their camera or a general QR reader. This redirects to the ideal.nl payment page, which works for all banks. 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    alt Redirect flow
    C->>Mu: Selects iDEAL (QR) at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    else Direct flow
    C->>Mu: Selects iDEAL (QR) and their bank at checkout
    Mu->>C: Redirects to online banking
    end
    C->>CB: Authenticates account/scans QR code and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

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
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via their bank. | Void   | Void/Cancelled   |
| iDEAL processing error. | Declined   | Declined   |
| The customer didn't complete payment within 1.5 hours. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund pending (banking only).  | Reserved | Reserved |
| Refund complete. | Completed | Completed |
</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) (Banking: Current and deprecated versions, QR: Current only) |
| **Testing** | [Test payment details](/testing/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > iDEAL direct/redirect/QR |
| **Ready-made integrations** | Banking is supported in all our [ready-made integrations](/integrations/ready-made/), **except** ZenCart. <br> QR is supported in [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 8](/drupal/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [Odoo](/odoo/), [OpenCart](/opencart/), [PrestaShop 1.7](/prestashop/), [Shopware 5](/shopware/), [VirtueMart](/virtuemart/), [WooCommerce](/woo-commerce/), [X-Cart](/x-cart/). |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
