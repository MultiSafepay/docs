---
weight: 326
meta_title: "API reference - Create a Klarna order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "gateway":"KLARNA",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":26000,
  "description":"Test order description",
  "items":"",
  "manual":"false",
  "gateway_info":{
    "birthday":"1970-07-10",
    "gender":"male",
    "phone":"0208500500",
    "email":"example@multisafepay.com"
  },
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":""
  },
  "plugin":{
    "shop":"my-shop",
    "plugin_version":"1.0.0",
    "shop_version":"1",
    "partner":"partner",
    "shop_root_url":"https://multisafepay.com"
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"127.0.0.1",
    "forwarded_ip":"127.0.0.1",
    "first_name":"Testperson-nl",
    "last_name":"Approved",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0612345678",
    "email":"example@multisafepay.com",
    "disable_send_email":false,
    "referrer":"https://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "delivery":{
    "first_name":"Testperson-nl",
    "last_name":"Approved",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "country":"NL"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Item demo 1",
        "description":"",
        "unit_price":90,
        "quantity":2,
        "merchant_item_id":"111111",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"Item shipping - Flat Rate - Fixed",
        "description":"Shipping",
        "unit_price":10,
        "quantity":1,
        "merchant_item_id":"msp-shipping",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":0
        }
      }
    ]
  },
  "checkout_options":{
    "tax_tables":{
      "alternate":[
        {
          "name":"none",
          "rules":[
            {
              "rate":0.00
            }
          ]
        }
      ]
    }
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13sEMtA491h823BLOx5Upa9H9XGEpYeUEg9/?lang=en_US"
  }
}
```
{{< /code-block >}}

{{< description >}}

## Klarna

See also Payment methods – [Klarna](/payments/methods/billing-suite/klarna).

The old Klarna environment only supports `redirect` orders.

The new **Klarna payments** environment supports `redirect` orders, and `direct` orders if using a custom itegration.

JSON requests are the same for both environments.

### Klarna - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Value: `KLARNA`.

----------------
`order_id` | string | required

Your unique identifier for the order.   
Format: Maximum 50 characters.

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
`items` | object

See [items (object)](/api/#items-object).

----------------
`manual` | string | required

Value: `false`.

----------------
`gateway_info` | object  | required

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

`birthday` | object | required

The customer's date of birth.  
In the Netherlands and Belgium, this is required for credit checks.  
Format: yyyy-mm-dd. 

`gender` | string | required

The customer's personal title.  
Options: `mr`, `mrs`, `miss`. 

`phone` | string | required

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

`email` | string | required

The email address for sending payment instructions to the customer.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`plugin` | object | required

See [plugin (object)](/api/#plugin-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object

See [delivery (object)](/api/#delivery-object).

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class.   

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------    

{{< /description >}}
