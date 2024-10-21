---
title: 'Manual Capture'
category: 6298bd782d1cf4006032e765
order: 6
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: 'manual-capture'
---
Manual Capture is a MultiSafepay solution that reduces your risk by letting you capture card payments either partially or in full when you ship the order. 

# How it works

**Full capture** is when a customer places an order but you are unable to ship it right away. An authorization is created for the full amount of the transaction. The funds are settled when you ship the order.

**Partial capture** is when a customer places an order for multiple items but you can't ship them all at once, only in separate shipments. An authorization is created for the full amount of the transaction, and the amount for each shipment is settled when you send it.

# Activation

To activate Manual Capture for your MultiSafepay account, email <sales@multisafepay.com>

# Integration

Manual Capture is supported for our [Magento 2](/docs/magento-2) integration.

To activate it in other [ready-made integrations](/docs/our-integrations/), you can customize it via our API.

See Recipes:
- <a href="https://docs.multisafepay.com/recipes/manual-capture-initial-payment/" target="_blank">Manual capture: Initial payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://docs.multisafepay.com/recipes/manual-capture-capture-payment/" target="_blank">Manual capture: Capture payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://docs.multisafepay.com/recipes/manual-capture-cancel-reservation/" target="_blank">Manual capture: Cancel reservation</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

See API reference:
- [Create order](/reference/createorder/) > Set `manual` to `capture`.
- [Capture payment](/reference/capturepayment/)
- [Cancel authorized payment](/reference/cancelauthorizedorder)

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

## Cancellation

You can cancel a reservation created via manual capture. In case a partial capture has been made, the cancellation will apply to the remaining amount. 

<details id="cancel-authorization">
<summary>How to cancel an authorized transaction</summary><br>

**Via API**: 

- See API reference - <a href="https://docs.multisafepay.com/reference/cancelauthorizedorder" target="_blank">Cancel authorized payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 

**Via dashboard**:

- Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
- On the **Transaction summary** page, in **Order Summary**, click **Cancel Reservation**.
- Add a description of what happened with the order, and then click **Complete**.  
  The <<glossary:order status>> changes to **Void** and the <<glossary:transaction status>> to Void.

</details>

## Statuses

| Action | Description | Order status | Transaction status |
|---|---|---|---|
| Authorize transaction | The transaction is authorized and the funds reserved. | Completed   | Initialized  |
| Partial capture | A partial amount is captured relating to a previous order ID. | Completed  | Completed |
| Full capture | The full amount is captured relating to a previous order ID. | Completed    | Completed  |
| Partial cancel reservation | The reserved or remaining amount that was partially captured has been cancelled. | Void | Void |
| Full cancel reservation | The fully captured reserved amount has been cancelled.  | Void | Void | 
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
