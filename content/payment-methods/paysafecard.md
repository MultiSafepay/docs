---
title: 'Paysafecard'
category: 6298bd782d1cf4006032e765
order: 403
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: 'paysafecard'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Paysafecard.svg" width="45" align="right" style="margin: 20px; max-height: 75px"/>

[Paysafecard](https://www.paysafecard.com/en/) lets customers make online payments using secure prepaid vouchers, available for purchase locally. 
The funds are available immediately. The customer chooses a fixed voucher amount: 10, 25, 50 or 100 EUR. 

Customers enter the voucher code, without providing any personal payment details. Vouchers for different amounts are available in the local currency in 46 countries.

The card balance remains available for 12 months free of charge. After 12 months, customers are charged a monthly administration fee of 3 EUR, which is deducted from the balance.

Read how Paysafecard can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/paysafecard)

| Overview | Details |
|---|---|
| **Chargebacks**  | No | 
| **Countries**  | Worldwide – Go to [paysafecard.com](https://www.paysafecard.com/en-gb/), and click the globe icon in the banner.  | 
| **Currencies**  | EUR, GBP, USD  | 
| **Expiration** | Transactions expire after 3 hours. |
| **Payment pages** | [Yes](/payment-pages/) (current version only) |
| **Refunds** | Paid with Paysafecard only: You can't refund via MultiSafepay because we don't receive any customer payment details to refund to. Refund in your own online banking. <br> Paid with Paysafecard **and** another payment method: [Full refunds](/refunds/).  |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/paysafecard-payment-flow.svg" alt="Paysafecard payment flow" style="display: block;
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
| The customer has been redirected to Paysafecard. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction at Paysafecard. | Void   | Void   |
| The customer didn't complete payment within 3 hours. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

</details>

# Activation 

Paysafecard doesn't require activation. 

To find outlets that sell Paysafecard, see: 

- [Find sales outlets](https://www.paysafecard.com/en/find-sales-outlet-1/) 
- [Verkooppunten zoeken](https://www.paysafecard.com/nl/verkooppunt-vinden-1/) 

For any questions, email <sales@multisafepay.com>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Gift card redirect |
| **Ready-made integrations** | Supported in [OsCommerce](/oscommerce/), [Magento 1](/magento-1/), [VirtueMart](/virtuemart/), [X-Cart](/x-cart/), [Zen Cart](/zen-cart/). |
<br>

> ℹ️ Testing
> You can’t test Paysafecard in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. 
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
