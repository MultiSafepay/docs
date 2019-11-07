---
weight: 323
meta_title: "API - Create Trustly order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## Trustly

> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "TRUSTLY",
    "description": "Test Order Description",
    "custom_info": {},
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "country": "NL",
        "email": "test@example.com"
    }
}
```
> JSON Response

```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```

* All parameters shown are required field(s)

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string   | Specifies the payment flow for the checkout process. Options: redirect, direct, paymentlink.  |
| gateway                        | string   | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request] (#retrieve-all-gateways). Option: TRUSTLY.  |
| order_id                       | string   | The unique identifier from your system for the order.                                     |
| currency                       | string   | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                  |
| description                    | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 character. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this.  |
| payment_options                | object   |                                                                                        |
| notification_url               | string   | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                                                                                  |
| redirect_url                   | string   |Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. | 
| cancel_url                     | string   | Customer will be redirected to this page after a failed payment.                        | 
| customer                       | object   | Contains the personal information of the customer.                                      |


Please make sure you check out our dedicated documentation for [Trustly](/payment-methods/trustly/).