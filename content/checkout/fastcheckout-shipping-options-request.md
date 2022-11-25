---
title: 'FastCheckout shipping options request'
category: 62bd999547298d001abc714c
order: 3
hidden: false
slug: 'fastcheckout-shipping-options'
parentDoc: 62fcc05ac034cb06771c46fc
---

If you cannot send your available shipping options for the shipping element on the [FastCheckout page](/docs/fastcheckout/) in your [create order](/reference/createorder) request, you can trigger a `GET` or `POST` request from MultiSafepay to your [webhook endpoint](/docs/webhook/) to retrieve the options.

# How it works

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/fastcheckout-shipping-options.svg" alt="FastCheckout shipping options" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Integration

To trigger the shipping options request, in your [create order](/reference/createorder) request, set `checkout_options.use_shipping_notification` (boolean) to `true`.

See Recipe – [Create a FastCheckout page](/recipes/create-a-fastcheckout-page) > Step 6. Configure shipping options. 

# Request

## Via notification_url

1. In `payment_options.notification_url`, specify your webhook endpoint.
2. Set `payment_options.notification_method` to `POST` (recommended) or `GET`. 

See Recipe – [Create a FastCheckout page](/recipes/create-a-fastcheckout-page) > Step 1. Create an order. 

### POST

The following is an example `POST` request from MultiSafepay to you. 

```json
{
  "order_id":"my-order-id-1",
  "amount":"9810",
  "currency":"EUR",
  "customer":{
    "locale":"nl_NL",
    "ip_address":"127.0.0.1",
    "forwarded_ip":"127.0.0.1",
    "first_name":"Simon",
    "last_name":"Smit",
    "address1":"Kraanspoor",
    "address2":"",
    "house_number":"39",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0612345678",
    "email":"simon.smit@example.com"
  },
  "delivery":{
    "locale":"nl_NL",
    "ip_address":"127.0.0.1",
    "forwarded_ip":"127.0.0.1",
    "company_name":"",
    "first_name":"Delivery name",
    "last_name":"Delivery Last name",
    "address1":"Kraanspoor",
    "address2":"",
    "house_number":"39",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "state":"Noord-Holland",
    "country":"NL",
    "phone":"0612345678",
    "email":"simon.smit@example.com"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":60,
        "quantity":"1",
        "merchant_item_id":"hdd0061",
        "tax_table_selector":"2",
        "weight":{
          "unit":"KG",
          "value":"1"
        }
      },
      {
        "name":"Mordern Candle Holders",
        "description":"",
        "unit_price":30,
        "quantity":"1",
        "merchant_item_id":"hdd006",
        "tax_table_selector":"2",
        "weight":{
          "unit":"KG",
          "value":"1"
        }
      }
    ]
  }
}
```

<details id="Parameters-key">
<summary>Parameters key</summary>
<br>

| Parameter | Type | Description |
|---|---|---|
| `order_id` | string | Your unique (client-defined) identifier for the order. |
| `amount` | integer | The payment amount in the currency's smallest unit: <br> - Decimal currencies: Value for 10 EUR = 1000 (1000 cents) <br> - Zero-decimal currencies: Value for 10 YEN = 10 |
| `currency` | The currency of the payment. <br> Format: <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO-4217 currency code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. |
| `customer` | object | See Recipes – [customer object](/recipes/customer-object-1). |
| `delivery` | object | See Recipes – [delivery object](/recipes/delivery-object). |
| `shopping_cart` | object | See Recipes – [Display shopping cart](/recipes/display-shopping-cart). |

</details>

### GET

The following is an example `GET` request from MultiSafepay to you.

The data is sent as query parameters. 

```
%notification_url%?
identifier=shipping&
country=Netherlands&
countrycode=NL&
weight=2&
transactionid=my-order-id-1&
currency=EUR&
amount=9810&
total_incl_vat=9810&
total_incl_vat_excl_shipping=9810&
items_count=2
```

<details id="query-parameters-key">
<summary>Query parameters key</summary>
<br>

| Parameter | Description |
|---|---|
| `notification_url` | The [webhook endpoint](/docs/webhook/) for MultiSafepay to send order updates and other notifications for this site. <br> See also [feed_url](#via-feedurl) below. |
| `identifier` | The identifier of the request. Set to `shipping`. |
| `country` | The customer's country. |
| `countrycode` | The country code. <br> Format: <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, e.g. `NL`. |
| `weight` | The weight of the item to be shipped. |
| `transactionid` | MultiSafepay's unique identifier for the transaction. |
| `currency` | The currency of the shipping cost. <br> Format: <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO-4217 currency code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. | 
| `amount` | The total amount of the order. |
| `total_incl_vat` | The total amount of the order including VAT. |
| `total_incl_vat_excl_shipping` | The total amount of the order, including VAT and excluding the shipping cost. |
| `items_count` | The total number of items in the order. |

</details>

## Via feed_url

An alternative to `payment_options.notification_url` is `payment_options.feed_url`, which is a dedicated webhook URL for non-order related updates, particularly shipping options. It defaults to `POST`. 

# Response

We expect to receive your response formatted as follows:

```json
{
  "pickup":{
    "name":"PostNL pickup points",
    "provider":"PostNL",
    "price":6
  },
  "flat_rate_shipping":[
    {
      "name":"TNT - Netherlands",
      "price":7,
      "allowed_areas":[
        "NL"
      ]
    },
    {
      "name":"Seur - Spain",
      "price":7,
      "allowed_areas":[
        "ES"
      ]
    },
    {
      "name":"TNT - Belgium & France",
      "price":12,
      "allowed_areas":[
        "BE",
        "FR",
      ]
    }
  ]
}
```

<details id="attributes-key">
<summary>Attributes key</summary>
<br>

| Attribute | Type | Description |
|---|---|---|
| `pickup` | object | Information about available pickup points. |
| `pickup.name` | string | The name of the pickup point. |
| `pickup.provider` | string | The name of the shipping company. |
| `pickup.price` | number (float) | The shipping cost as a whole number or decimal number. <br> Example: 5 EUR = 5 and 5.50 EUR = 5.5 |
| `flat_rate_shipping` | array | Information about shipping options for a fixed cost. |
| `flat_rate_shipping.name` | string | The name of the fixed-rate shipping option. |
| `flat_rate_shipping.price` | number (float) | The cost of the fixed-rate shipping option. <br> Example: 5 EUR = 5 and 5.50 EUR = 5.5 |
| `flat_rate_shipping.allowed_areas` | array | A list of available countries for the shipping option. All other countries are excluded. <br> The availability is based on the country of the customer's shipping address. <br> Format: <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, e.g. `NL`, `ES`. |
| `flat_rate_shipping.excluded_areas` | array | A list of unavailable countries for the shipping option. All other countries are included. <br> The availability is based on the country of the customer's shipping address. <br> Format: <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, e.g. `NL`, `ES`. |

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
