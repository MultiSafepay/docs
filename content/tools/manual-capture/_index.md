---
title: 'Manual capture'
weight: 40
meta_title: "Manual capture - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "single"
logo: '/svgs/Manual_capture.svg'
short_description: 'Receive credit card payments from your customers in full or partial captures.'
aliases:
    - /tools/manual-capture/full-capture/
    - /tools/manual-capture/partial-capture/
    - /tools/manual-capture/what-is-a-manual-capture/
    - /tools/manual-capture/how-to-activate-manual-capture/
---
Manual Capture is a MultiSafepay tool that lets you capture credit card payments either partially or in full. It supports Maestro, Mastercard, and Visa.

{{< details title="Full capture" >}}

Full capture is when a customer places an order but you are unable to ship it right away. An authorization is created for the full amount of the transaction. The funds are settled when you ship the order.

{{< /details >}}

{{< details title="Partial capture" >}}

Partial capture is when a customer places an order for multiple items but you can't ship them all at once, only in separate shipments. An authorization is created for the full amount of the transaction, and the amount for each shipment is settled when you send it.

{{< /details >}}

For how Manual Capture can benefit your business, see [Capture your payments](https://www.multisafepay.com/blog/capture-your-payments).

## Payment flow

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

| Action | Description | Order status | Transaction status |
|---|---|---|---|
|  Authorize transaction | The transaction is authorized and the funds reserved. | Completed   | Initialized  |
| Partial capture | A partial amount is captured relating to a previous order ID. | Completed  | Completed |
| Full capture | The full amount is captured relating to a previous order ID. | Completed    | Completed  |
| Partial cancel reservation | The reserved or remaining amount that was partially captured has been cancelled. | Void | Void |
| Full cancel reservation | The fully captured reserved amount has been cancelled.  | Void | Void | 
| Partial authorization expiry | The remaining authorized amount expired without being captured. | Void | Void |
| Full authorization expiry | The full authorized amount expired without being captured. | Void    | Void  |

{{< details title="Expiration periods" >}}

Expiration period for supported payment methods: 

* VISA: 7 days
* Mastercard / Maestro: 30 days

After expiration, the issuer can cancel the authorization and the funds are returned to the customer’s account.

{{< /details >}}

## Activation

To activate Manual Capture in your MultiSafepay account, email the Risk Team at <risk@multisafepay.com>

## Integration
To integrate Manual Capture using our API, see API Reference – [Manual Capture authorization](/api/#manual-capture-authorization).

Manual Capture is not supported in our [ecommerce integrations](/integrations/ecommerce-integrations) by default, but you can customize it via our API.

For any questions, email the Integration Team at <integration@multisafepay.com>