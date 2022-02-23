---
weight: 326
meta_title: "API reference - Create a Klarna order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type": "redirect",
  "gateway": "KLARNA",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": "10000",
  "description": "Test order description",
  "var1": "",
  "var2": "",
  "var3": "",
  "items": "",
  "manual": "false",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "84.71.117.69",
    "forwarded_ip": "",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1/XI",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "email": "example@multisafepay.com",
    "referrer": "https://example.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "delivery": {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1/XI",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "gateway_info": {
    "birthday": "1970-07-10",
    "gender": "male",
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
    "order_id": "my-order-id-1",
    "payment_url": "https://example.com"
  }
}
```

> POST - /orders

```json
{
  "type": "direct",
  "gateway": "KLARNA",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": "10000",
  "description": "Test order description",
  "var1": "",
  "var2": "",
  "var3": "",
  "items": "",
  "manual": "false",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "plugin":{
    "shop":"my-shop",
    "plugin_version":"1.0.0",
    "shop_version":"1",
    "partner":"partner",
    "shop_root_url":"https://multisafepay.com"
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "84.71.117.69",
    "forwarded_ip": "",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1/XI",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "email": "example@multisafepay.com",
    "referrer": "https://example.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "delivery": {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1/XI",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "phone": "0612345678",
    "email": "example@multisafepay.com"
  },
  "gateway_info": {
    "birthday": "1970-07-10",
    "gender": "male",
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
              "rate": "0.00"
            }
          ],
          "standalone": ""
        },
        {
          "name": "FEE",
          "rules": [
            {
              "country": "",
              "rate": "0.00"
            }
          ],
          "standalone": ""
        }
      ],
      "default": {
        "rate": "0.00",
        "shipping_taxed": false
      }
    },
    "costs": [],
    "created": "2021-11-15T16:10:47",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Neherkade",
      "address2": null,
      "city": "Gravenhage",
      "country": "NL",
      "country_name": null,
      "email": "example@multisafepay.com",
      "first_name": "John",
      "house_number": "1/XI",
      "last_name": "Doe",
      "locale": "nl_NL",
      "phone1": "0612345678",
      "phone2": "",
      "state": null,
      "zip_code": "2521VA"
    },
    "description": "Test order description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": "...",
    "modified": "2021-11-15T16:10:47",
    "order_adjustment": {
      "total_adjustment": "0.00",
      "total_tax": "0.00"
    },
    "order_id": "my-order-id-1",
    "order_total": "100.00",
    "payment_details": {
      "collecting_flow": null,
      "external_transaction_id": "d0b93b5a-facd-3bf9-a24b-0409ee9e7d96",
      "recurring_flow": null,
      "recurring_id": null,
      "recurring_model": null,
      "type": "KLARNA"
    },
    "payment_methods": [
      {
        "amount": 10000,
        "currency": "EUR",
        "description": "Test order description",
        "external_transaction_id": "d0b93b5a-facd-3bf9-a24b-0409ee9e7d96",
        "payment_description": "Klarna",
        "status": "initialized",
        "type": "KLARNA"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "shopping_cart": {
      "items": [
        {
          "cashback": "",
          "currency": "EUR",
          "description": "",
          "image": "",
          "merchant_item_id": 1111,
          "name": "Test",
          "options": [],
          "product_url": "",
          "quantity": 1,
          "tax_table_selector": "none",
          "unit_price": "100.00",
          "weight": {
            "unit": "KG",
            "value": 12
          }
        }
      ]
    },
    "status": "initialized",
    "transaction_id": 5119189,
    "var1": null,
    "var2": null,
    "var3": null,
    "qr_url": "https://example.com",
    "payment_url": "https://example.com"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Klarna

See also Payment methods – [Klarna](/payment-methods/klarna).

The old Klarna environment only supports `redirect` orders.

The new **Klarna payments** environment supports `redirect` orders, and `direct` orders if using a custom integration.

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

The currency of the payment.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The payment amount in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.  
Format: Maximum 500 characters.

----------------
`items` | object

See [items (object)](/api/#items-object).

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
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

### Klarna - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`.  

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

The currency of the payment.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.  
Format: Maximum 500 characters.

----------------
`items` | object

See [items (object)](/api/#items-object).

----------------
`manual` | string | required

Value: `false`.

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
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

**Response**

----------------
`amount` | integer

The amount (in cents) the customer needs to pay.

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`checkout_options` | object

The definitions for the VAT class.

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string

The currency of the payment.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`customer` | object

See [customer (object)](/api/#customer-object).

----------------
`description` | string

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`financial_status` | string

The [transaction status](/about-payments/multisafepay-statuses/) of the order.

----------------
`items` | object

See [items (object)](/api/#items-object).

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`order_id` | string

Your unique identifier for the order.   

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`reason` | string

----------------
`related_transactions` | object

Information about linked transactions.

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object). 

----------------
`status` | string

The [order status](/about-payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

{{< /description >}}
