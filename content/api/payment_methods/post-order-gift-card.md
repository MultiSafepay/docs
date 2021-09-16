---
weight: 315
meta_title: "API Reference - Create a gift card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - / order 


```json 
{
  "type":"redirect",
  "order_id":"my-order-id",
  "gateway":"VVVGIFTCRD",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "manual":false,
  "payment_options":{
    "notification_url":"http://www.example.com/client/json-live/notification?type=notification",
    "redirect_url":"http://www.example.comclient/json-live/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/json-live/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "country":"NL",
    "email":"simonsmit@example.com"
  }
}
```

> JSON response
```json 
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
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
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

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
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Fixed value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
