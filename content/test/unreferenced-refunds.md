---
title: Unreferenced refunds
category:
  uri: Point-of-sale
slug: unreferenced-refunds
position: 3
privacy:
  view: anyone_with_link
---
Alternatively to regular refunds, you can process unreferenced refunds. This allows you to return funds to a customer without referring to the original transaction.

# Activation

To enable unreferenced refunds for your MultiSafepay account, email [sales@multisafepay.com](mailto:sales@multisafepay.com).

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<Image align="center" src="https://files.readme.io/8a2586105264041c63d79d6f30b8eeda255b4be5063c10c9bc12edaaca30a6a7-ctap-unreferenced-final-final.png" />

***

# User guide

An unreferenced refund is a payment process where you use the funds from your MultiSafepay [account balance](doc:account-balance) to process a refund.

## Amount limits

* Minimum refund amount: 0,01 EUR
* Maximum refund amount: 60 EUR

Maximum amounts can be adjusted. Send a request to [risk@multisafepay.com](mailto:risk@multisafepay.com).

**⚠️Note:** Remember that to process an unreferenced refund, you must have sufficient funds in your MultiSafepay account balance. To learn how to top your balance, see <a href="https://docs.multisafepay.com/docs/account-balance#top-ups" target="_blank">Top ups</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

## How it works

### SmartPOS terminals

#### Prerequisites

On your terminal:

* Enable the **unreferenced refunds** feature.
* For Cloud POS payments, additionally enable [Cloud mode](/docs/smartpos-features#how-to-enable-cloud-mode).

Check the general flow below:

1. You create an unreferenced refund via
   * **Cloud POS** OR
   * **Manual Input**
2. The customer presents their card.
3. The card details are sent to MultiSafepay.
4. The details are forwarded to the card scheme for authorization which can be accepted or declined.
5. Once we receive an authorization response, we forward it to the terminal. The result displays on the screen.

<details>
  <summary>How to process unreferenced refunds with Manual input</summary>

  <br />

  1. On your terminal, go to **Features** > **Unreferenced refunds**.
  2. Enter an **amount** and click **Refund**.
  3. Present the card at the terminal.
</details>

<details>
  <summary>How to process unreferenced refunds with cloud mode</summary>

  <br />

  1. Create an unreferenced refund order. See [Cloud POS payment: Unreferenced refunds](/recipes/cloud-pos-payment-unreferenced-refunds) .
  2. The terminal displays the amount set in the order.
  3. Present the card at the terminal.

  #### Example request

  ```curl
  curl --request POST \
  --location 'https://api.multisafepay.com/v1/json/orders?api_key={terminal_group_api_key}'\
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
      "type": "unreferenced_refund",
      "order_id": "order_id_example",
      "gateway": "",
      "currency": "EUR",
      "amount": 100,
      "description": "Example order description",
      "payment_options": {
          "notification_url": "https://www.example.com/client/notification?type=notification",
          "notification_method": "POST"
      },
      "customer": {
          "locale": "nl_NL",
          "phone": "031123123123",
          "email": "example@multisafepay.com"
      },
      "gateway_info": {
          "terminal_id": "00000ABC"
      }
  }'
  ```

  #### Example response

  ```json
  {
      "success": true,
      "data": {
          "order_id": "example_order_id",
          "session_id": "1045QwhsVpUeasAwdaQWGSACAafascdsa1y",
          "payment_url": "https://payv2.multisafepay.com/connect/fsadfwa4234qdejtcadx/?lang=nl_NL",
          "events_token": "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTU5NDc4MzUsImdydCI6WyJtYnVzOnNlc3Npb24ub3JkZXIiLCJtYnVzOnNlc3Npb24ucXIiXSwicGlkIjoiMTA0NVF3aHNWcFVeasfd21lR3UXVKYlZBRUZXd1N3bllDMXkiLCJzdWIiOiJwciJ9.bo7saa1rHZoAcdI7DXH0skVx4EMFm7-EM1P1WfoPCJA",
          "events_stream_url": "https://api.multisafepay.com/events/stream/"
      }
  }
  ```
</details>

***

### Traditional (CTAP) terminals

The steps to process an unreferenced refund may vary from one terminal model to another. Check the general flow below:

1. You initiate the refund by introducing the amount on the CTAP terminal.
2. The customer presents their card.
3. The card details are sent to MultiSafepay.
4. The details are forwarded to the card scheme for authorization which can be accepted or declined.
5. Once we receive an authorization response, we forward it to the terminal. The result displays on the screen.

## Payment statuses

Check the table below to learn more about the different statuses:

| Description                                            | Status        |
| :----------------------------------------------------- | :------------ |
| The transaction is initiated                           | `initialized` |
| The transaction is processing                          | `reserved`    |
| The transaction is completed and the funds are settled | `completed`   |
| The transaction was declined                           | `declined`    |

## Updates

Check the table below to learn more about how to receive updates for unreferenced refunds:

| Terminal     | How to handle notifications                                                                                                                                                                 |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SmartPOS** | To receive order updates, set up a <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">webhook</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>. For **cloud mode**, you can also subscribe to our [event notifications](doc:event-notifications). |
| **CTAP**     | Make a [Get order](/reference/getorder/) request. Retrieve the details from the response.                                                                                                   |

***

[Top of page](#)
