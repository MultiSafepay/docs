---
weight: 301
meta_title: "API reference - Create AfterPay order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type": "redirect",
  "gateway": "AFTERPAY",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 10000,
  "description": "Test Order Description",
  "manual": "false",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Hogehilweg",
    "house_number": "8",
    "zip_code": "1101 CC",
    "city": "Amsterdam",
    "country": "NL",
    "email": "example@multisafepay.com"
  },
  "delivery": {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Hogehilweg",
    "house_number": "8",
    "zip_code": "1101 CC",
    "city": "Amsterdam",
    "country": "NL",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "gateway_info": {
    "birthday": "1970-07-10",
    "gender": "mr",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "shopping_cart": {
    "items": [
      {
        "name": "Test",
        "description": "",
        "unit_price": 100,
        "quantity": 1,
        "merchant_item_id": "1111",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": "12"
        }
      }
    ]
  },
  "checkout_options": {
    "tax_tables": {
      "default": {
        "shipping_taxed": "false",
        "rate": 0
      },
      "alternate": [
        {
          "name": "none",
          "standalone": false,
          "rules": [
            {
              "rate": 0
            }
          ]
        },
        {
          "name": "FEE",
          "standalone": false,
          "rules": [
            {
              "rate": 0
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
    "payment_url":"https://example.com"
  }
}
```
> POST - /orders

```json
{
  "type": "direct",
  "gateway": "AFTERPAY",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 10000,
  "description": "Test Order Description",
  "manual": "false",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Hogehilweg",
    "house_number": "8",
    "zip_code": "1101 CC",
    "city": "Amsterdam",
    "country": "NL",
    "email": "example@multisafepay.com"
  },
  "delivery": {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Hogehilweg",
    "house_number": "8",
    "zip_code": "1101 CC",
    "city": "Amsterdam",
    "country": "NL",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "gateway_info": {
    "birthday": "1970-07-10",
    "gender": "mr",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "shopping_cart": {
    "items": [
      {
        "name": "Test",
        "description": "",
        "unit_price": 100,
        "quantity": 1,
        "merchant_item_id": "1111",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": "12"
        }
      }
    ]
  },
  "checkout_options": {
    "tax_tables": {
      "default": {
        "shipping_taxed": "false",
        "rate": 0
      },
      "alternate": [
        {
          "name": "none",
          "standalone": false,
          "rules": [
            {
              "rate": 0
            }
          ]
        },
        {
          "name": "FEE",
          "standalone": false,
          "rules": [
            {
              "rate": 0
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
  "success": true,
  "data": {
    "amount": 10000,
    "amount_refunded": 0,
    "checkout_options": {
      "alternate": [
        {
          "name": "none",
          "rules": [
            {
              "country": "",
              "rate": 0.00
            }
          ]
        }
      ],
      "default": {
        "rate": 0,
        "shipping_taxed": false
      }
    },
    "costs": [
      {
        "transaction_id": 2045938,
        "amount": 1000,
        "description": "",
        "type": "SYSTEM"
      }
    ],
    "created": "2019-01-12T13:55:38",
    "currency": "EUR",
    "custom_info": {},
    ...
    "status": "uncleared",
    "transaction_id": 4022655,
    "payment_url": "https://example.com",
    "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=my-order-id-1"
  }
}
```
{{< /code-block >}}
{{< description >}}

## AfterPay
See also Payment methods – [AfterPay](/payments/methods/billing-suite/afterpay/).

### AfterPay - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.

----------------
`gateway` | string | required

The unique gateway ID that immediately directs the customer to the payment method.  
Value: `AFTERPAY`. 

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`items` | object

See [items (object)](/api/#items-object).

----------------
`manual` | string | required

Value: `false`.

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object). 

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object

See [delivery (object)](/api/#delivery-object).


**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

### AfterPay - direct 

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`.

----------------
`gateway` | string | required

The unique gateway identifier that directs the customer straight to the payment method.  
Value: `AFTERPAY`. 

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`.  
Format: Maximum 35 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

Text displayed with the order in your MultiSafepay account, and on the customer's bank statement (if supported by the bank).  
Max. 200 characters.  
HTML formatting is not supported. To add descriptions in HTML format, use the `items` or `shopping_cart` objects instead.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object). 

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object

See [delivery (object)](/api/#delivery-object).

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
`shopping_cart` | object | required

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`items` | object

See [items (object)](/api/#items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

**Response**

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{< /description >}}
