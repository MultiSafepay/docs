---
weight: 520
meta_title: "API reference - Pay After Delivery customer credit score - MultiSafepay Docs"

---

{{< code-block >}}
> POST - /json/pad/ccs

```json
{
  "type":"checkout",
  "gateway":"PAYAFTER",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":9000,
  "description":"Order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel"
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "forwarded_ip":"",
    "first_name":"Simon",
    "last_name":"Smit",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "email":"simonsmit@example.com",
    "referrer":"https://multisafepay-demo.com/plugingroup/testtool/client/json-test",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "delivery":{
    "first_name":"Simon",
    "last_name":"Smit",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0208500500",
    "email":"simonsmit@example.com"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":90,
        "quantity":1,
        "merchant_item_id":"hdd006",
        "tax_table_selector":"BTW0",
        "weight":{
          "unit":"KG",
          "value":1
        }
      }
    ]
  },
  "checkout_options":{
    "rounding_policy":{
      "mode":"UP",
      "rule":"PER_ITEM"
    },
    "shipping_methods":{
      "flat_rate_shipping":[
        {
          "name":"TNT - verzending NL",
          "price":7,
          "allowed_areas":[
            "NL",
            "ES"
          ]
        },
        {
          "name":"Seur - Spain",
          "price":7,
          "allowed_areas":[
            "NL",
            "ES"
          ]
        },
        {
          "name":"TNT - verzending BE en FR",
          "price":12,
          "excluded_areas":[
            "NL",
            "FR",
            "ES"
          ]
        }
      ]
    },
    "tax_tables":{
      "alternate":[
        {
          "name":"BTW0",
          "rules":[
            {
              "rate":0.00
            }
          ]
        },
        {
          "name":"2",
          "rules":[
            {
              "rate":0.09,
              "country":"NL"
            }
          ]
        }
      ]
    }
  },
  "custom_fields":[
    {
      "name":"acceptagreements",
      "type":"checkbox",
      "label":"This label",
      "description_right":{
        "value":[
          {
            "nl":"Ik ga akkoord met de <a href='https://example.com' target='_blank'>algemene voorwaarden</a>"
          },
          {
            "en":"I accept the <a href='https://example.com' target='_blank'>terms and conditions</a>"
          }
        ]
      },
      "validation":{
        "type":"regex",
        "data":"^[1]$",
        "error":[
          {
            "nl":"U dient akkoord te gaan met de algemene voorwaarden"
          },
          {
            "en":"Please accept the terms and conditions"
          }
        ]
      }
    },
    {
      "standard_type":"companyname"
    }
  ]
}
```


> JSON response


```json
{
  "success":true,
  "data":{
    "result":true
  }
}

```
{{< /code-block >}}

{{< description >}}

## Pay After Delivery customer credit score

Submit data about a [Pay After Delivery](/payment-methods/pay-after-delivery/) order and customer. MultiSafepay conducts a pre-check and returns a customer credit score (CCS) to advise whether to accept the order. 

If the CCS recommends not accepting the order, the customer must select another payment method to complete payment.

**Request body parameters**

----------------
`type` | string | required

The payment flow.  
Value: `direct`.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

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
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object | required

See [delivery (object)](/api/#delivery-object).

----------------
`shopping_cart` | object | required – or use `items`

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class.

----------------

{{< /description >}}
