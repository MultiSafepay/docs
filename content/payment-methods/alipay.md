---
title: 'Alipay'
category: 6298bd782d1cf4006032e765
order: 501
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'alipay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Alipay.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[Alipay](https://global.alipay.com/platform/site/ihome) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online, QR, and contactless POS payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.


Read how Alipay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/alipay)

| Overview | Details |
|---|---|
| **Chargebacks**  | No  |
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR, USD (currency conversion in EUR only)  | 
| **Expiration** | Transactions expire after 5 hours. | 
| **Payment pages** | [Yes](/payment-pages/) (current version only)  |
| **Refunds** | [Yes](/refunds/): Full, partial, and API refunds, and [discounts](/discounts/)  |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/alipay-payment-flow.svg" alt="Alipay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to Alipay. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 5 hours, or it was cancelled. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved | Reserved   |
| Refund complete.  | Completed | Completed   |

</details>

# Activation 

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-Alipay"> 
<summary>How to activate Alipay</summary>
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
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > Alipay direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (direct), **except** PrestaShop 1.6, OsCommerce, and Zen Cart.   |
<br>

> ℹ️ Testing
> To test Alipay payments, see [Testing](/testing/#wallets).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
