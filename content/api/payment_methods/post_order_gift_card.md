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
    "description": "Test order description",
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

> JSON response
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
## Gift cards

- See also Payment methods – [Gift cards](/payments/methods/prepaid-cards/gift-cards).  
- Redirect only.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
**Note:** We only preselect the gift card supplied in the gateway.  

Baby Cadeaubon= BABYCAD  
Beautyandwellness= BEAUTYWELL  
Bloemencadeaukaart= BLOEMENCAD  
Boekenbon= BOEKENBON  
Degrotespeelgoedwinkel= DEGROTESPL  
Fashioncheque= FASHIONCHQ  
Fashiongiftcard= FASHIONGFT  
Fietsenbon= FIETSENBON  
Good4fun= GOOD4FUN     
Gezondheidsbon= GEZONDHEID   
Nationale bioscoopbon= NATNLBIOSC      
Nationaletuinbon= NATNLETUIN    
Parfumcadeaukaart= PARFUMCADE   
Sportenfit= SPORTENFIT    
Vuur & rook gift card= VRGIFTCARD    
VVV Cadeaukaart= VVVGIFTCRD   
Webshopgiftcard= WEBSHOPGFT  
Wijncadeau= WIJNCADEAU      
Yourgift= YOURGIFT     

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__currency__ | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__manual__ | string | required

Fixed value: `false`.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------

{{< /description >}}