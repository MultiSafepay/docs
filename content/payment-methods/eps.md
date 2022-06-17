---
title: 'EPS'
category: 6298bd782d1cf4006032e765
order: 108
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'eps'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/EPS.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

EPS is a widely accepted inter-bank payment method that links all major Austrian retail banks. 
Customers pay in their own online banking environment. Settlement is instant and guaranteed.

Read how EPS can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/eps)

| Overview | Details |
|---|---|
| **Chargebacks**  | No  |
| **Countries**  | Austria  | 
| **Currencies**  | EUR |  
| **Expiration** | Transactions don't expire. |
| **Payment pages** | [Yes](/payment-pages/) (current version only) |
| **Refunds** | [Yes](/refunds/): Full and partial |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects EPS at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}

# Payment statuses  

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction. | Void   | Void   |
| The customer didn't complete payment within 10 minutes. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

</details>

# Activation 

You can activate EPS yourself in your dashboard. 

<details id="how-to-activate-eps"> 
<summary>How to activate EPS</summary>
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

To test 

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > EPS redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> ℹ️ Testing
> To test EPS payments, see [Testing](/testing/#banking-methods).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
