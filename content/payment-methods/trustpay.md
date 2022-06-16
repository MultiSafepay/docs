---
title: 'TrustPay'
category: 6298bd782d1cf4006032e765
order: 116
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: trustpay
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/TrustPay.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

[TrustPay](https://www.trustpay.eu/) is a bank payment method in the Czech Republic. Customers pay from their own online banking environment.

# Overview

|   |   |  
|---|---|
| **Countries**  | Czech Republic  | 
| **Currencies**  | CZK | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/)  |
| **Supports** | [Second Chance](/second-chance/) |
| **Transactions expire after** | 10 days |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects TrustPay at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
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
| MultiSafepay has collected payment.| Completed | Completed |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 10 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) (current and deprecated versions) |
| **Testing** | You can't test TrustPay in your test MultiSafepay account. <br> You can only make test payments in your live MultiSafepay account. |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Trustpay redirect |
| **Ready-made integrations** | TrustPay (redirect) is supported in [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 7 and 8](/drupal/), [Magento 2](/magento-2/), [Odoo](/odoo/), [PrestaShop 1.7](/prestashop/), [Shopware 5 and 6](/shopware/), [WooCommerce](/woo-commerce/), [VirtueMart](/virtuemart/), [X-Cart](/x-cart/). |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
