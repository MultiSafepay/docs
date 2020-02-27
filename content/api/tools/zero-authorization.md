---
weight: 1370
---
{{< code-block >}}
> POST - /orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "",
    "currency": "EUR",
    "amount": "0",
    "description": "Zero Authorization Test",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "80.123.456.78",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "state": "",
        "country": "NL",
        "birthday": "01011993",
        "gender": "male",
        "phone": "0208500500",
        "email": "example@multisafepay.com",
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
    "order_id": "My-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```
{{< /code-block >}}
{{< description >}}
## Zero Authorization

For a number of scenarios, it can be useful for our merchants to verify an account with Zero Authorization. An amount of zero will be reserved to check the authenticity of the card as well as establish an authorization to collect future payments. 

The _amount_ parameter should be set to 0.

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
|  type	|  string |    Specifies the payment flow for the checkout process. Options: redirect, direct, checkout, paymentlink. | 
|  order_id	|  string \| integer	|    The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string. Required. (max. 50 chars).|
| gateway  |	string  |	The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. | 
| currency   |	string	 |    The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. | 
| amount | integer |   The amount (in cents) that the customer needs to pay.| 
| description   |	string	|    A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. | 
|  payment_options 	|   object	 | 
| customer	| object	 | 



Read more about [Zero Authorization](/tools/zero-authorization/) on our documentation page.
{{% /description %}}