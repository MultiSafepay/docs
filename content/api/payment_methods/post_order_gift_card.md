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

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. All gateway name options of our standard gift cards are shown below. Note: we will only preselect the gift card supplied in the gateway.  

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/developer/api/notification-url)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: nl_NL | 

----------------    
__ip_address__ | string

The IP address of the customer. “Required” with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field.  [More info](/developer/api/validating-customer-ip-address) 

---------------- 
__country__ | string

Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)

---------------- 
__email__ | string

Customer’s provided email address. Used to send Second Chance emails and in fraud checks.  

---------------- 

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

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