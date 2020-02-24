---
weight: 1350
---

{{< code-block >}}
> POST - /orders 

```shell
{
    "type": "redirect",
    "order_id": "order_id_0000001",
    "gateway": "",
    "currency": "EUR",
    "amount": "10000",
    "description": "Manual Capture Test",
    "manual": "false",
    "capture": "manual",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "10.1.5.1",
        "referrer": "http://test.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON Response

```shell
{
    "success": true,
    "data": {
        "order_id": "order_id_0000001",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
{{< /code-block >}}
{{< description >}}
## Manual Capture Authorization

Manual Capture is a feature that allows payments to be captured once an order has been shipped or received. The API calls mandate whether a transaction should be captured partially or fully, as well as the authorization and cancellation of the transaction.

The feature can only be used with specific credit card payment methods including MasterCard, VISA and Maestro.

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                          	|string	| Specifies the payment flow for the checkout process. Options: redirect, direct, checkout, paymentlink.|
| order_id	| integer / string	|    The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string. Required. Max 50 char. | 
| gateway  |	string  |	The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. | 
| currency   |	string	 |    The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. | 
| amount | integer |   The amount (in cents) that the customer needs to pay.| 
| description   |	string	|    A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. | 
| capture                           | string    | A manual capture has been generated.       |
|  payment_options 	|   object	 |
| customer	| object	 | 
| locale	|  string | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. | 
| ip_address	|   string	|    The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/) | 

Please make sure you check out our dedicated documentation for [Manual Capture](/tools/manual-capture/).
{{% /description %}}