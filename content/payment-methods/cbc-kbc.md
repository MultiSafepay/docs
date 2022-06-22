---
title: 'CBC/KBC'
category: 6298bd782d1cf4006032e765
order: 106
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'cbc-kbc'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/CBC.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

An online banking payment method of two of Belgium's largest banks: [CBC](https://www.cbc.be/particuliers/fr.html) which serves the French speaking population, and [KBC](https://www.kbc.be/particulieren/nl.html) which serves the Dutch-speaking population.

The payment method functions the same for both the CBC branch and the KBC branch. However, MultiSafepay's payment <<glossary:gateway>> includes the branches as separate options because customers of one branch can't pay through the other.

Read how CBC/KBC can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/kbccbc)

| Overview | Details |
|---|---|
| **Chargebacks**  | No | 
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Expiration** | Transactions expire after 5 days. |
| **Payment pages** | [Yes](/payment-pages/) (current version only) |
| **Refunds** | [Yes](/refunds/): Full and partial (1 business day after payment is completed) |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CK as CBC/KBC
    participant Me as Merchant

    C->>Mu: Selects CBC/KBC at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects to online banking
    end
    C->>CK: Authenticates account and completes payment
    CK->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}

> **Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed.

# Payment statuses  

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The transaction was cancelled by you or the customer. | Void   | Void   |
| The customer didn't complete payment within 5 days. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |
<br>

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**. We import our bank statements daily and match all incoming payments. 

</details> 

# Activation 

You can activate CBC/KBC in your dashboard.

<details id="how-to-activate-cbc-kbc"> 
<summary>How to activate CBC/KBC</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > CBC/KBC direct/redirect |
| **Ready-made integrations** | [Craft Commerce](/craft-commerce/), [OpenCart](/opencart/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [PrestaShop 1.6 and 1.7](/prestashop/), [Shopware 5 and 6](/shopware/), [WooCommerce](/woo-commerce/) |
<br>

> ℹ️ Testing
> To test CBC/KBC payments, see [Testing](/testing/#banking-methods).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
