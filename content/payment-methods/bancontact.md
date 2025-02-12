---
title: 'Bancontact'
category: 6298bd782d1cf4006032e765
order: 2
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'bancontact'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/bancontact.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.bancontact.com/en" target="_blank">Bancontact</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a leading Belgian payment method that supports online, mobile, QR, POS, and wallet payments. It is a household name and supported by over 80% of Belgian webshops. Once payment is completed, the customer cannot reverse it and Bancontact guarantees <<glossary:settlement>>. 

Read how Bancontact can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/bancontact" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |   
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Belgium  | 
| [Currencies](/docs/currencies/)  | EUR | 
| [3D Secure 2.0](/docs/3ds2/) | Yes (all non-mobile payments)|
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (Current (banking and QR) and deprecated (banking) versions |
| [Recurring payments](/docs/recurring-payments/) | Yes (banking only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes | 

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/bancontact-payment-flow.svg" alt="Bancontact payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction (non-mobile only). | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| Bancontact has declined the transaction. | Declined | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API

- See API reference – [Create order](/reference/createorder/) > Banking order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Bancontact redirect/QR**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

  **⚠️ Note:** Bancontact doesn't support **direct** requests.

- By default, transactions expire after 1 hour. 

-  If `seconds_active` is set, the QR code will expire at the time specified. See recipes - <a href="https://docs.multisafepay.com/recipes/days_active-seconds_active" target="_blank">Seconds_active</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.


### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/). 

### Testing
To test Bancontact payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).

<br>

---

# User guide

## Bancontact WIP Service

Bancontact WIP is a wallet initiated payment service you can use for:

- Bancontact One-Click Pay: customer-initiated one-click payments to make checkout faster and increase <<glossary:conversion>>
- Bancontact Recurring: merchant-initiated subscription payments

### How it works

Bancontact Payconiq gives you access to a merchant wallet to securely store customers' payment details in. Customers give one-time consent and only need to pass [strong customer authentication](/docs/psd2/) (SCA) for their first purchase. 

There is no shift in liability for [chargebacks](/docs/chargebacks/) from <<glossary:issuer>> to <<glossary:acquirer>> since your fraud and disputes volumes are monitored quarterly. A maximum transaction amount applies. 

### Activation and criteria

- Bancontact WIP is only available to low-risk, high-volume merchants (25,000 transactions quarterly), within the SEPA area. 
- Applies to services only, not physical products. 
- You must have easy-to-use procedures in place for refunds, cancellations, and disputes.
- Customers must be able to add, update, and delete their stored payment details.  
- You must be able to continually demonstrate low rates of fraudulent transactions, or access to your merchant wallet may be revoked. 

Email a request to activate Bancontact WIP to <sales@multisafepay.com>

Requests are screened and approved by Bancontact Payconiq. 

### Integration

See [Recurring payments](/docs/recurring-payments/).
<br>


## Deferred Sales

Our Deferred Sales functionality allows you to  [manually capture](/docs/manual-capture) Bancontact transactions. 

### How it works

**Full capture** can be useful when a customer places an order but you are unable to ship it right away, or when you need to verify customer details before approving an order. An authorization is created for the full amount of the transaction. The funds are settled when you ship the order.

**Partial capture** can be useful when a customer places an order for multiple items but you can't ship them all at once, only in separate shipments. An authorization is created for the full amount of the transaction, and the amount for each shipment is settled when you send it.

You can perform 1 partial capture. The remaining amount will be released by the issuer automatically.

### Activation

1. You sign an agreement with Bancontact. 
2. Bancontact evaluates your requests, and enables the service. 
3. Bancontact defines **maximum amounts** and **expiry times** for authorizations. 

For a complete user guide, see  [Manual Capture](/docs/manual-capture).


---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
