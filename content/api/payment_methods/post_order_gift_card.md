---
weight: 314
meta_title: "API Reference - Create a gift card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - / order 


```json 

{
    "type": "redirect",
    "order_id": "my-order-id",
    "gateway": "VVVGIFTCRD",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "manual": false,
    "payment_options": {
        "notification_url": "http://www.example.com/client/json-live/notification?type=notification",
        "redirect_url": "http://www.example.comclient/json-live/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/json-live/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "country": "NL",
        "email": "simonsmit@example.com"
    }
}
```

> JSON Response
```json 

{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```  
{{< /code-block >}}

{{< description >}}
## Gift card
Creates a Gift Card [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). All gateway name options of our standard gift cards are shown below. Note: we will only preselect the gift card supplied in the gateway.  

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------
__locale__ | string

Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: nl_NL | 

----------------    
__ip_address__ | string

The customer's IP address.   
**Required** for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods because MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address). 

---------------- 
__country__ | string

The customer’s country of residence.   
Format: [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html).

---------------- 
__email__ | string

The customer’s email address.   
Used to send Second Chance emails and to conduct fraud checks.  

---------------- 

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

The gateway names of the standard gift cards MultiSafepay offers

| Gift card name                 | Gateway name, gift card     |                         |
|--------------------------------|-----------------------------|-------------------------| 
| Baby Cadeaubon                 | BABYCAD                     |   |
| Beautyandwellness              | BEAUTYWELL                  |   |
| Bloemencadeaukaart             | BLOEMENCAD                  |   |
| Boekenbon                      | BOEKENBON                   |   |
| Degrotespeelgoedwinkel         | DEGROTESPL                  |   | 
| Fashioncheque                  | FASHIONCHQ                  |   |
| Fashiongiftcard                | FASHIONGFT                  |   |
| Fietsenbon                     | FIETSENBON                  |   |
| Good4fun                       | GOOD4FUN                    |   |
| Gezondheidsbon                 | GEZONDHEID                  |   |
| Nationale bioscoopbon          | NATNLBIOSC                  |   | 
| Nationaletuinbon               | NATNLETUIN                  |   |
| Parfumcadeaukaart              | PARFUMCADE                  |   | 
| Sportenfit                     | SPORTENFIT                  |   | 
| Vuur & rook gift card           | VRGIFTCARD                  |   | 
| VVV Cadeaukaart                | VVVGIFTCRD                  |   |
| Webshopgiftcard                | WEBSHOPGFT                  |   |
| Wijncadeau                     | WIJNCADEAU                  |   | 
| Yourgift                       | YOURGIFT                    |   |           

Read more about the [gift cards](/payments/methods/prepaid-cards/gift-cards) we offer on our documentation page.
{{< /description >}}