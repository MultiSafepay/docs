---
title: 'Manual Capture'
category: 6298bd782d1cf4006032e765
order: 31
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: 'manual-capture'
---
Manual Capture is a MultiSafepay solution that reduces your risk by letting you capture credit card payments either partially or in full when you ship the order. 

# How it works

**Full capture** is when a customer places an order but you are unable to ship it right away. An authorization is created for the full amount of the transaction. The funds are settled when you ship the order.

**Partial capture** is when a customer places an order for multiple items but you can't ship them all at once, only in separate shipments. An authorization is created for the full amount of the transaction, and the amount for each shipment is settled when you send it.

# Activation

To activate Manual Capture for your MultiSafepay account, email <sales@multisafepay.com>

# Integration

Manual Capture is not supported in our [ready-made integrations](/docs/our-integrations/) by default, but you can customize it via our API.

See Recipes:
- [Manual capture: Initial payment](/recipes/manual-capture-initial-payment/)
- [Manual capture: Capture payment](/recipes/manual-capture-capture-payment/)

See API reference:
- [Create order](/reference/createorder/) > Set `manual` to `capture`.
- [Capture payment](/reference/capturepayment/)

<br>

---

# User guide

## Expiration periods

- VISA: 7 days
- Mastercard and Maestro: 30 days

After expiration, the <<glossary:issuer>> can cancel the authorization.

## Payment methods

- Maestro 
- Mastercard 
- Visa

## Statuses

| Action | Description | Order status | Transaction status |
|---|---|---|---|
| Authorize transaction | The transaction is authorized and the funds reserved. | Completed   | Initialized  |
| Partial capture | A partial amount is captured relating to a previous order ID. | Completed  | Completed |
| Full capture | The full amount is captured relating to a previous order ID. | Completed    | Completed  |
| Partial cancel reservation | The reserved or remaining amount that was partially captured has been canceled. | Void | Void |
| Full cancel reservation | The fully captured reserved amount has been canceled.  | Void | Void | 
| Partial authorization expiry | The remaining authorized amount expired without being captured. | Void | Void |
| Full authorization expiry | The full authorized amount expired without being captured. | Void    | Void  |
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
