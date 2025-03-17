---
title: 'Event notifications'
parentDoc: 64674fbc74bc4007521ebbcb
category: 6477597e0e2961004638cd5d
order: 4
hidden: false
slug: 'event-notifications'
---



Subscribe to event notifications to receive order payments updates when, e.g.,

- A customer completes the payment.
- The payment has been cancelled or declined.

# Prerequisites

- SmartPOS terminal must be [activated in your MultiSafepay account](/docs/getting-started-guide/).
- Payments must be initiated via [cloud <<glossary:POS>> payment](/docs/solutions).

In other scenarios, you can make use of our <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">webhook </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>notifications.

# 1. Initiate payments

1. [Create an order](/reference/createorder/), and set`terminal_id` in your request. See Recipe - <a href="https://docs.multisafepay.com/recipes/cloud-pos-payment" target="_blank">Cloud POS payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. In response to the API request you made, you receive the `events_token`.

**⚠️Note:** You cannot initiate another payment until the current payment is **Cancelled** or **Completed**.

# 2. Subscribe to the event notifications

To subscribe to event notifications make a GET request, using the `events_token` from your response.

```
curl -H 'Authorization: events_token' 'https://api.multisafepay.com/events/stream/'
```
<details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

```
curl -H 'Authorization: eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTQwNzEyMDcsImdydtdfI6WyJtYnVzOnNlc3Npb24ub3JkZXIiLCJtYnVzOnNlc3Npb24ucXIiXSwicGlkIjoiNTk5TWM0VWhOWDhYczNmNU55b3JnaVZZMlhab1BsVVkxa28iLCJzdWIiOiJwciJ9.p1txKa0wlR6Pn-DvQW8oYmYcesU49GgZsPebME_EvYs' \
'https://api.multisafepay.com/events/stream/'
```

  </details>

<details id="example-response"> 
  <summary>Example response</summary>
  <br>

```
event: session.order
data: {"financial_status":"initialized","order_id":"ExampleOrderID1234567","session_id":"1025J8hXqtM9dLcilPp3gqkXi8Res3tvZZZ","status":"initialized","transaction_id":"89000000"}
event: session.order
data: {"financial_status":"completed","order_id":"ExampleOrderID1234567","session_id":"1025J8hXqtM9dLcilPp3gqkXi8Res3tvZZZ","status":"completed","transaction_id":"890000000"}
```
 </details>

**⚠️Note:** When making requests locally, you might encounter **CORS** (**Cross-Origin Resource Sharing**) errors. We recommend using a **backend proxy** to handle the API requests, bypassing browser CORS restrictions.

# 3. Payment statuses

The table below sets out possible payment statuses and what they commonly mean.

| Description                  | Payment status |
| :---------------------------| :-------------- |
| The <<glossary:card scheme>> is processing your payment request. | Initialized    |
| The payment has been initialized, but the <<glossary:card scheme>> requires authentication to continue the payment process. This is not a final status. For more information, see <a href="https://docs.multisafepay.com/docs/smartpos-solutions#soft-declines" target="_blank">Soft declines</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> - SmartPOS solutions. | Declined (**Soft decline**)
| The payment has been cancelled on the terminal or via API. For more information - see [Cancellation.](/docs/solutions#cancellation)  <br>**Note:**  You can now initiate another cloud POS payment.   | Cancelled.     |
| The customer has completed the payment.  <br>**Note:**  You can now initiate another cloud POS payment.  | Completed      |
| The <<glossary:card scheme>> has declined the payment. The customer will be redirected to the payment screen to retry the payment.  | Declined. |

***

[Top of page](#)