---
title: SmartPOS solutions
category:
  uri: Point-of-sale
slug: smartpos-solutions
parent:
  uri: smartpos-terminal
position: 0
privacy:
  view: public
---
We currently offer this product in the following countries:

<table>
  <tr>
    <td>Countries</td>
    <td>Netherlands, Belgium</td>
  </tr>

  <tr>
    <td>Countries for partners</td>
    <td>Netherlands, Belgium, Italy, Spain</td>
  </tr>
</table>

If you are interested in our Point of Sale solutions, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

Our SmartPOS solutions let you initiate payments through:

* Manual input
* Cloud POS payment
* On-same device third-party applications
  * Web application
  * Native application

# Manual input

To start processing payments manually:

1. Enter **Amount due** and select **Pay**.
2. The customer can either tap or insert their card to make the payment.
3. Once the payment is completed, a notification is displayed.

# Cloud POS payment

With cloud <Glossary>POS</Glossary> payment, you can initiate payments from an external application.

This diagram shows a successful cloud-based POS payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/cloud-POS-flow.svg" alt="cloud-POS" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

**⚠️ Note:** Before you start initiating payments, you must ensure **cloud mode** is enabled - see [SmartPOS features](/docs/smartpos-features).

* Create an order. See Recipe - <a href="https://docs.multisafepay.com/recipes/cloud-pos-payment" target="_blank">Cloud POS payment</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
* Cancel an order. See [cancellation](#cancellation).

To receive payments updates subscribe to [Event notifications.](/docs/event-notifications)

***

# On-same device third-party applications

## Web applications

Web applications let you initiate payments on-same devices from a browser to the payment app.

This diagram shows a successful web application payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/web-flow.svg" alt="web-app-POS" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

### Initiate payments

1. Before initiating web application payments, you need to create an order.

**Example**

```curl
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "redirect",
  "order_id": "my_order_id",
  "gateway": "",
  "currency": "EUR",
  "amount": 10,
  "description": "Order Description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}
'
```

2. Initiate a payment using the URL below:

```URL
msp://?amount={$amount}&order_id={$order_id}&callback={$callback_url}&printing=true&tipping=true&notification_url={$notification_url}
```

* `amount`: the amount specified in EUR cents.
* `order_id`: your unique identifier for order ID. - `order_id`: your unique identifier for order ID. Maximum 50 characters. Can only contain **a-z**, **A-Z**, **0-9** and the special characters `/ - _`.
* `callback_url`: this URL redirects the customer to receive payment status notifications.
* Optionally, you can set `notification_url` to receive order payment updates notifications.
* `tipping`: include a tip.
* `printing`: activate printing function.

Payment status received can either be  **Completed** or **Cancelled**.

<br />

***

## Native applications

Native applications let you initiate payments on-same devices from app to payment app.

This diagram shows a successful native application payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/native-flow.svg" alt="native-app-POS" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

### Initiate payments

1. Before initiating native application payments, you need to create an order.<br />When creating an order, the `order_id` must have a maximum length of 50 characters and can only contain **a-z**, **A-Z**, **0-9** and the special characters `/ - _`.

**Example**

```curl
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '
{
  "type": "redirect",
  "order_id": "my_order_id",
  "gateway": "",
  "currency": "EUR",
  "amount": 10,
  "description": "Order Description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}
'
```

2. To initiate payments - see <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">MultiSafepay Android POS integration </a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

***

# User guide

## Authentication

To create an order, always use the **API key** of your device's [terminal group](/docs/sites#terminal-group-id-and-api-key).

**⚠️Note:** Using an incorrect **API key** can cause any subsequent API calls associated with that order to fail.

## Cancellation

To cancel an order, make a **POST** request to our cancellation endpoint. This requires the use of an `order_id` and a group **API** key, which you can find at your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />  under **Manage groups**.

Insert the `order_id` and the **API** key in the URL.

**⚠️Note:** To cancel a POS order, use a **POST** method. **PATCH** methods are not supported. For more information, see [Cancelling declined transactions](/docs/pos-troubleshooting#cancelling-declined-transactions) .

**Example request**

```curl
curl -X POST 
"https://api.multisafepay.com/v1/json/orders/{order_id}/cancel?api_key={your-api-key}"
```

**Example response**

```json
{
  "success": true,
  "data": {
    "costs": [],
    "created": "dateTtime",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "fastcheckout": "NO",
    "financial_status": null,
    "modified": "dateTtime",
    "payment_details": {},
    "payment_methods": null,
    "status": "cancelled"
    }
}
```

## Refunds

You can process refunds:

**Via the API**

See API reference – [Refund order](/reference/refundorder).

**From your terminal**

1. Open the MultiSafepay application from your terminal and go to **Features**.
2. Click **History** and select the relevant transaction.
3. Click **Refund**. Enter the desired amount you want to refund and click **OK**.
4. Click **Confirm** to finalize the transaction. The refund will be processed.
5. Click **Close**.

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
2. Go to **Transactions** > **Transaction overview**, and click the relevant transaction.
3. On the **Transaction details** page, click **Refund order**.
4. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
5. In the **Comment** field, enter any additional information.
6. In the **Amount** fields, enter the amount to refund.
7. Click **Continue**.
8. Review **Refund confirmation**, and then click **Confirm**.

## Updates

The table below sets out options available for receiving updates on the payments:

| POS Solutions       | Required                                                                                                                                                                                                      | Optional                                                                                            |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| Cloud POS payment   | Subscribe to the [event notifications.](/docs/event-notifications)                                                                                                                                            | Configure a [webhook](/docs/webhook#configure-your-webhook-endpoint.).                              |
| Web applications    | Set `callback_url` in the [ link.](/docs/solutions#web-applications-pos)                                                                                                                                      | Set `notification_url` in the [ link](/docs/solutions#web-applications-pos) to configure a webhook. |
| Native applications | Set `package_name` in your <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">intent call.</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> | Configure a [webhook.](/docs/webhook#configure-your-webhook-endpoint.)                              |

**⚠️ Note:** Finalized POS transactions will always have a status of `completed` or `cancelled`. A `declined` status might indicate a **soft decline**, which is not a final state. For more information, see [Soft declines](/docs/smartpos-solutions#soft-declines).

Make a [Get order](/reference/getorder) request to retrieve POS-specific details, including the **Terminal ID** that processed a transaction.

<Accordion title="Example response" icon="fa-code">
  ```json
  {
    "success": true,
    "data": {
      "amount": 1,
      "amount_refunded": 0,
      "completed": "2024-06-04T15:50:18",
      "costs": [
        {
          "amount": 2,
          "description": "2 For Visa Transactions",
          "transaction_id": 899813954,
          "type": "SYSTEM"
        },
        {
          "amount": 0.6,
          "description": "2.9 % For Visa CreditCards Transactions (min 60)",
          "transaction_id": 899813955,
          "type": "SYSTEM"
        }
      ],
      "created": "2024-06-04T15:50:17",
      "currency": "EUR",
      "custom_info": {
        "custom_1": null,
        "custom_2": null,
        "custom_3": null
      },
      "customer": {
        "address1": null,
        "address2": null,
        "city": null,
        "country": null,
        "country_name": null,
        "email": null,
        "first_name": null,
        "house_number": null,
        "last_name": null,
        "locale": "en_US",
        "phone1": null,
        "phone2": null,
        "state": null,
        "zip_code": null
      },
      "description": "12341234",
      "fastcheckout": "NO",
      "financial_status": "completed",
      "items": null,
      "modified": "2024-06-04T15:50:18",
      "order_id": "TestGetOrder123123",
      "payment_details": {
        "account_holder_name": "card holder",
        "account_id": null,
        "application_id": "a0000000031010",
        "authorization_code": "705151",
        "card_acceptor_id": "1001001",
        "card_acceptor_location": "Amsterdam",
        "card_acceptor_name": "TestMSP",
        "card_additional_response_data": {
          "sca_details": {}
        },
        "card_authentication_result": null,
        "card_entry_mode": "ICC_CONTACTLESS",
        "card_expiry_date": "3112",
        "card_funding": "D",
        "card_product": "F",
        "card_product_type": 1,
        "card_sequence_number": "0000",
        "card_verification_result": "2",
        "cardholder_verification_method": "FAILED",
        "cardholder_verification_result": "UNKNOWN",
        "emv": {
          "91": "ab1231231234"
        },
        "external_transaction_id": "12312312312",
        "issuer_bin": "123123",
        "issuer_country_code": "ES",
        "last4": "1234",
        "recurring_flow": null,
        "recurring_id": "1231213123",
        "recurring_model": null,
        "response_code": "00",
        "scheme_reference_id": "123123123123123",
        "terminal_id": "0000004d",
        "type": "VISA"
      },
      "payment_methods": [
        {
          "account_holder_name": "card holder",
          "amount": 1,
          "card_expiry_date": "3112",
          "currency": "EUR",
          "description": "12341234",
          "external_transaction_id": "123123412341234",
          "payment_description": "Visa",
          "status": "completed",
          "type": "VISA"
        }
      ],
      "reason": "Approved",
      "reason_code": "1000",
      "related_transactions": null,
      "status": "completed",
      "transaction_id": 123412342341234,
      "var1": null,
      "var2": null,
      "var3": null
    }
  }
  ```
</Accordion>

## Testing

POS transactions cannot be simulated in out **TEST** environment. All testing must be conducted in your **LIVE** MultiSafepay account.

<br />

***

[Top of page](#)