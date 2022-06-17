---
title: 'Belfius'
category: 6298bd782d1cf4006032e765
order: 105
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'belfius'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Belfius.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[Belfius](https://www.belfius.be/common/EN/fw/language.html) is a popular online banking payment method for Belfius bank customers in Belgium.

Read how Belfius can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/belfius)

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
    participant B as Belfius
    participant Me as Merchant

    C->>Mu: Selects Belfius at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects to online banking
    end
    C->>B: Authenticates account and completes payment
    B->>Mu: Transfers funds 
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
| The customer has been redirected to Belfius. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 5 days. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
<br>

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**. We import our bank statements daily and finalize all incoming payments. 

</details>

# Activation 

You can activate Belfius yourself in your dashboard. 

<details id="how-to-activate-belfius"> 
<summary>How to activate Belfius</summary>
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
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Belfius direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/), **except** OsCommerce and ZenCart. |
<br>

> ℹ️ Testing
> To test Belfius payments, see [Testing](/testing/#banking-methods).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
