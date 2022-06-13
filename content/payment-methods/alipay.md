---
title: 'Alipay'
category: 6298bd782d1cf4006032e765
order: 501
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: alipay
---
[Alipay](https://global.alipay.com/platform/site/ihome) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online, QR, and contactless POS payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.

See how Alipay can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/alipay).

# Overview

|   |   |
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR, USD (currency conversion in EUR only)  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial refunds](/refunds/#full-and-partial-refunds), [discounts](/discounts/), [API refunds](/refunds/)  |
| **Supports**  | [Second Chance](/second-chance/) |
| **Transactions expire after** | 5 hours |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Alipay
    participant Me as Merchant

    C->>Mu: Selects Alipay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page
    else Direct flow
    Mu->>A: Payment is processed with Alipay
    end
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
| The customer has been redirected to Alipay. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 5 hours, or it was cancelled. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved   |
| Refund complete.  | Completed | Completed   |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only)  |
| **Testing** | [Test payment details](/testing/test-payment-details/#wallets) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > Alipay direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (direct), **except** PrestaShop 1.6, OsCommerce, and Zen Cart.   |
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>