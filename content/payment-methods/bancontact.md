---
title: 'Bancontact'
category: 6298bd782d1cf4006032e765
order: 101
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'bancontact'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Bancontact.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

[Bancontact](https://www.bancontact.com/en) is a leading Belgian payment method that supports online, mobile, QR, POS, and wallet payments. It is a household name and supported by over 80% of Belgian webshops. Once payment is completed, the customer cannot reverse it and Bancontact guarantees settlement. 

Read how Bancontact can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/bancontact)

| Overview | Details |   
|---|---|
| **3D Secure 2.0** | [Yes](/3ds2/) (all non-mobile payments) |
| **Chargebacks**  | No | 
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Expiration** | Transactions expire after 1 hour (banking only).  |
| **Payment components** | [Yes](/payment-components/) |
| **Payment pages** | [Yes](/payment-pages/) (Current (banking and QR) and deprecated (banking) versions |
| **Recurring payments**  | [Yes](/recurring-payments/) (banking only) |
| **Refunds** | [Yes](/refunds/): Full and partial |
| **Second Chance** | [Yes](/second-chance/) | 

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/bancontact-payment-flow.svg" alt="Bancontact payment flow" style="display: block;
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
| The customer has initiated a transaction. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| Bancontact has declined the transaction. | Declined | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

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

You can activate Bancontact yourself in your dashboard. 

<details id="how-to-activate-bancontact"> 
<summary>How to activate in your Bancontact</summary>
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
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Bancontact redirect/QR |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> ℹ️ Testing
> To test Bancontact payments, see [Testing](/testing/#banking-methods).
<br>

---

# Bancontact WIP Service

Bancontact WIP is a wallet initiated payment service you can use for:

- Bancontact One-Click Pay: customer-initiated one-click payments to make checkout faster and increase <<glossary:conversion>>
- Bancontact Recurring: merchant-initiated subscription payments

## How it works

Bancontact Payconiq gives you access to a merchant wallet to securely store customers' payment details in. Customers give one-time consent and only need to pass [strong customer authentication](/pds2/) (SCA) for their first purchase. 

There is no shift in liability for [chargebacks](/chargebacks/) from <<glossary:issuer>> to <<glossary:acquirer>> since your fraud and disputes volumes are monitored quarterly. A maximum transaction amount applies. 

## Activation and criteria

- Bancontact WIP is only available to low-risk, high-volume merchants (25,000 transactions quarterly), within the SEPA area. 
- Applies to services only, not physical products. 
- You must have easy-to-use procedures in place for refunds, cancellations, and disputes.
- Customers must be able to add, update, and delete their stored payment details.  
- You must be able to continually demonstrate low rates of fraudulent transactions, or access to your merchant wallet may be revoked. 

Email a request to activate Bancontact WIP to <sales@multisafepay.com>

Requests are screened and approved by Bancontact Payconiq. 

## Integration

See [Recurring payments](/recurring-payments/).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
