---
weight: 317
meta_title: "API reference - Create E-Invoicing order - MultiSafepay Docs"

---
{{< code-block >}}
> POST -/orders
```json
{
  "type": "redirect",
  "gateway": "EINVOICE",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": "10000",
  "description": "Test Order Description",
  "manual": "false",
  "gateway_info": {
    "birthday": "1980-01-30",
    "bank_account": "0417164300",
    "phone": "0208500500",
    "email": "example@multisafepay.com"
  },
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "102.129.255.0",
    "forwarded_ip": "",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "email": "example@multisafepay.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "referrer": "https://example.com"
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
  "gateway": "EINVOICE",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": "10000",
  "description": "Test Order Description",
  "manual": "false",
  "gateway_info": {
    "birthday": "1980-01-30",
    "bank_account": "0417164300",
    "phone": "0208500500",
    "email": "example@multisafepay.com"
  },
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "102.129.255.0",
    "forwarded_ip": "",
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
    "email": "example@multisafepay.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "referrer": "https://example.com"
  },
  "delivery": {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "Neherkade",
    "address2": "",
    "house_number": "1",
    "zip_code": "2521VA",
    "city": "Gravenhage",
    "state": "",
    "country": "NL",
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
    "created": "2021-11-15T15:24:03",
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
      "house_number": 1,
      "last_name": "Doe",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "phone2": "",
      "state": null,
      "zip_code": "2521VA"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "uncleared",
    "items": "...",
    "modified": "2021-11-15T15:24:03",
    "order_adjustment": {
      "total_adjustment": "0.00",
      "total_tax": "0.00"
    },
    "order_id": "my-order-id-1",
    "order_total": "100.00",
    "payment_details": {
      "collecting_flow": 0,
      "external_transaction_id": null,
      "invoice_url": "https://example.com",
      "paylink_url": null,
      "recurring_flow": null,
      "recurring_id": null,
      "recurring_model": null,
      "type": "EINVOICE"
    },
    "payment_methods": [
      {
        "amount": 10000,
        "currency": "EUR",
        "description": "Test Order Description",
        "payment_description": "Einvoice",
        "status": "uncleared",
        "type": "EINVOICE"
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
    "status": "uncleared",
    "transaction_id": 5118993,
    "var1": null,
    "var2": null,
    "var3": null,
    "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-order-id-1",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-order-id-1"
  }
}
```
{{< /code-block >}}

{{< description >}}
## E-Invoicing
See also Payment methods – [E-Invoicing](/payment-methods/e-invoicing).

### E-Invoicing - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Value: `EINVOICE`.

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

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string 

Value: `false`.

----------------
`gateway_info` | object

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
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

----------------

### E-Invoicing - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Value: `EINVOICE`.

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
`manual` | string 

Value: `false`.

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.                                                                

Contains:  

`birthday` | string

The customer's date of birth.  
Format: yyyy-mm-dd.                             

`bank_account` | string

The customer's (formatted) international bank account number (IBAN).  
This is required for credit checks. 

`phone` | string

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment. 

`email` | string

The email address for sending payment instructions to the customer.

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

The definitions for the VAT class. See [checkout_options (object)](/api/#checkout-options-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`description` | string 

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).  

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`items` | object
 
See [items (object)](/api/#items-object).

----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

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
`shopping_cart.items` | required

See [shopping_cart.items object](/api/#shopping-cart-items-object).

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
