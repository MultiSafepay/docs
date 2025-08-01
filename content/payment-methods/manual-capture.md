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

Applying **manual capture** to your orders authorizes the card payment but doesn't immediately transfer the customer's funds to your account. Using **manual capture**, you can **fully** or **partially** capture the authorized funds after shipping the order:

* **Full Capture**: Transfers the full authorized amount for the order.
* **Partial Capture**: Transfers a portion of the authorized amount for the order. Use this option for separate shipments.

# Activation

To activate Manual Capture for your MultiSafepay account, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

# Integration

Manual Capture is supported for our [Magento 2](/docs/magento-2) integration.

To activate it in other [ready-made integrations](/docs/our-integrations/), you can customize it via our API.

See Recipes:

* <a href="https://docs.multisafepay.com/recipes/manual-capture-initial-payment/" target="_blank">Manual capture: Initial payment</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
* <a href="https://docs.multisafepay.com/recipes/manual-capture-capture-payment/" target="_blank">Manual capture: Capture payment</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
* <a href="https://docs.multisafepay.com/recipes/manual-capture-cancel-reservation/" target="_blank">Manual capture: Cancel reservation</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

See API reference:

* [Create order](/reference/createorder/) > Set `manual` to `capture`.
* [Capture payment](/reference/capturepayment/)
* [Cancel authorized payment](/reference/cancelauthorizedorder)

<br />

***

# User guide

## Expiration periods

* VISA: 7 days
* Mastercard and Maestro: 30 days

After expiration, the <Glossary>issuer</Glossary> can cancel the authorization.

## Payment methods

* Maestro
* Mastercard
* Visa

## Capture payments

You can capture payments:

* Via our API - <a href="https://docs.multisafepay.com/reference/capturepayment" target="_blank">Capture payment</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
* Via your dashboard

<details id="cancel-authorization">
  <summary>How to capture an authorized payment</summary><br />

  1. Sign in to your MultiSafepay dashboard.
  2. Go to **Transactions** > **Transactions overview**, and then click on the relevant transaction.
  3. On the **Transaction summary** page, under **Order summary**, click **Capture**:
     * **Full capture**: Fill the total authorized amount.
     * **Partial capture**: Fill the amount according to the items you will ship.
  4. Click **Save**.

  After a **full capture**, the <Glossary>transaction status</Glossary> updates to **Completed**.

  **Partial captures** create a new transaction in the **Transaction overview** with a separate **order ID**, with both <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> set to **Completed**. The original transaction retains its initial statuses. The remaining amount available for capture is shown under **Transaction details**.
</details>

## Cancellation

You can cancel a reservation created via manual capture:

* Via our API - <a href="https://docs.multisafepay.com/reference/capturepayment" target="_blank">Cancel authorized payment</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
* Via your dashboard

For partial captures, the cancellation will apply to the remaining amount.

<details id="cancel-authorization">
  <summary>How to cancel an authorized transaction</summary><br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transaction overview**, and then select the relevant transaction.
  3. On the **Transaction summary** page, in **Order Summary**, click **Cancel Reservation**.
  4. Add a description of what happened with the order, and then click **Complete**.\
     The <Glossary>order status</Glossary> changes to **Void** and the <Glossary>transaction status</Glossary> to **Void**.
</details>

## Statuses

| Action                       | Description                                                                      | Order status | Transaction status |
| ---------------------------- | -------------------------------------------------------------------------------- | ------------ | ------------------ |
| Authorize transaction        | The transaction is authorized and the funds reserved.                            | Completed    | Initialized        |
| Partial capture              | A partial amount is captured relating to a previous order ID.                    | Completed    | Completed          |
| Full capture                 | The full amount is captured relating to a previous order ID.                     | Completed    | Completed          |
| Partial cancel reservation   | The reserved or remaining amount that was partially captured has been cancelled. | Void         | Void               |
| Full cancel reservation      | The fully captured reserved amount has been cancelled.                           | Void         | Void               |
| Partial authorization expiry | The remaining authorized amount expired without being captured.                  | Void         | Void               |
| Full authorization expiry    | The full authorized amount expired without being captured.                       | Void         | Void               |

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)