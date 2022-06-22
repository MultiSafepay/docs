---
title: 'Dotpay'
category: 6298bd782d1cf4006032e765
order: 107
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'dotpay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Dotpay.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

[Dotpay](https://www.dotpay.pl/en) is an inter-bank payment method that links all major Polish retail banks. 
Customers pay from their own online banking environment.

Read how Dotpay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/dotpay)

| Overview | Details |
|---|---|
| **Chargebacks**  | No | 
| **Countries**  | Poland  | 
| **Currencies**  | EUR, PLN | 
| **Expiration** | Transactions expire after 3 days. |
| **Payment pages** | [Yes](/payment-pages/) (current and deprecated versions) |
| **Refunds** | [Yes](/refunds/): Full and partial |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/dotpay-payment-flow.svg" alt="Dotpay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized|
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 3 days. | Expired | Expired |

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

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-dotpay"> 
<summary>How to activate Dotpay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Dotpay redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> ℹ️ Testing
> To test Dotpay payments, see [Testing](/testing/#banking-methods).

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
