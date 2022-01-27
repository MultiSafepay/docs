---
weight: 217
meta_title: "API reference - FastCheckout orders - MultiSafepay Docs"
---

{{< code-block >}}
> POST - /orders

```json
{
  "type":"checkout",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":"9743",
  "description":"Order description",
  "var1":"",
  "var2":"",
  "var3":"",
  "payment_options":{
    "notification_url":"http://10.1.10.111/testtool/client/json-live/notification?type=notification",
    "redirect_url":"http://10.1.10.111/testtool/client/json-live/notification?type=redirect",
    "cancel_url":"http://10.1.10.111/testtool/client/json-live/notification?type=cancel",
    "settings":{
      "fco":{
        "version":"1.0",
        "redirect_mode":null,
        "checkout":{
          "user_login":{
            "enabled": true
          },
          "flow":"primary"
        },
        "qr":{
          "enabled": true
        },
        "cart":{
          "disabled": false,
          "edit": false
        },
        "shipping":{
          "address":{
            "required": true
          },
          "invoice":{
            "enabled": true
          }
        }
      }
    }
  },
  "plugin":{
    "shop":"ApiTestTool",
    "plugin_version":"1.0.0",
    "shop_version":"1",
    "partner":"parner",
    "shop_root_url":"http://multisafepay.com"
  },
  "customer":{
    "locale":"en",
    "ip_address":"213.127.71.72",
    "disable_send_email":0,
    "forwarded_ip":"",
    "firs_tname":"Test name",
    "last_name":"Test Last name",
    "address2":"Delivery  address 2",
    "address1":"Hogehilweg",
    "house_number":"8",
    "zip_code":"1101 CC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"66633311155",
    "email":"example@multisafepay.com",
    "referrer":"http://multisafepay-demo.com/plugingroup/dev/magento/1901/checkout/cart/",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "delivery":{
    "first_name":"Delivery name",
    "last_name":"Delivery Last name",
    "address2":"Delivery  address 2",
    "address1":"Hogehilweg",
    "house_number":"8",
    "zip_code":"1101 CC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"66633311155",
    "email":"example@multisafepay.com"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":"60",
        "quantity":"1",
        "merchant_item_id":"hdd006",
        "tax_table_selector":2,
        "weight":{
          "unit":"KG",
          "value":"1"
        }
      },
      {
        "name":"Mordern Candle Holders",
        "description":"",
        "unit_price":"30",
        "quantity":"1",
        "merchant_item_id":"hdd006",
        "tax_table_selector":2,
        "weight":{
          "unit":"KG",
          "value":"1"
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
      "pickup":{
        "name":"PostNL pickup points",
        "provider":"PostNL",
        "price":"6"
      },
      "flat_rate_shipping":[
        {
          "name":"TNT - verzending NL",
          "price":"7",
          "allowed_areas":[
            "NL",
            "ES"
          ]
        },
        {
          "name":"Seur - Spain",
          "price":"7",
          "allowed_areas":[
            "NL",
            "ES"
          ]
        },
        {
          "name":"TNT - verzending BE en FR",
          "price":"12",
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
              "rate":"0.00"
            }
          ]
        },
        {
          "name":"2",
          "rules":[
            {
              "rate":"0.09",
              "country":"US"
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
            "nl":"Ik ga akkoord met de <a href='http://test.nl' target='_blank'>algemene voorwaarden</a>"
          },
          {
            "en":"I accept the <a href='http://test.nl' target='_blank'>terms and conditions</a>"
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
    },
    {
      "standard_type":"salutation",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"sex"
    },
    {
      "standard_type":"comment",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"newsletter",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"vatnumber",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"birthday",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"chamberofcommerce",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"passportnumber",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    },
    {
      "standard_type":"driverslicense",
      "validation":{
        "type":"regex",
        "data":"",
        "error":null
      }
    }
  ]
}
```
{{< /code-block >}}

{{< description >}}
## FastCheckout orders

Create a hosted or embedded checkout. See [FastCheckout](/fastcheckout).

**Parameters**

----------------
`type` | string | required

Creates a hosted FastCheckout page.

For embedded FastCheckout integrations, see [FastCheckout JavaScript integration](/fastcheckout/javascript/).

Value: `checkout`

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Value: `EUR`.

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit.  
Example: Value for 10 EUR = 1000 (1000 cents)

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`var1` / `var2` / `var3` | string | optional

Variables for storing additional data. 

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

Contains: `settings` | object | optional 

Contains: `fco` | object | optional

`fco` object contains:

**1.** `version` | string | optional

Specifies the version of FastCheckout.  
Value: `1.0`

**2.** `redirect_mode` | string | optional

Sets how the payment method is displayed to the customer, if relevant.

Options: 

- `redirect`: The customer is redirected to the payment method to complete the payment.
- `iframe`: The payment method is embedded as an iframe on the FastCheckout page.
- `modal`: The payment method is embedded in a modal window on the FastCheckout page.

**3.** `checkout` | object | optional

Specifies characteristics of the checkout.

- `user_login` | object | optional 
Sets whether the customer has to sign in to their FastCheckout account.
  - `enabled` | boolean  
  True: Customer must sign in.  
  False: Customer doesn't need to sign in. 

- `flow` | string | optional  
Sets the layout of the FastCheckout page.  
Values:  
`primary`: 3 column view  
`secondary`: 3 step flow

**4.** `qr` | object | optional

Sets whether to display a QR code for payment. 

- `enabled` | boolean  
True: Display a QR code.  
False: Don't display a QR code. 

**5.** `cart` | object | optional

Sets characteristics of the shopping cart.  

- `disabled` | boolean | optional 
True: Displays the shopping cart module.  
False: Hides the shopping cart module. 

- `edit` | boolean | optional  
True: Customer can edit the shopping cart?  
False: Customer cannot edit the shopping cart? 

**6.** `shipping` | object | optional

Sets characteristics of the shipping module.

- `address` | object | optional
Contains: `required` | boolean | required  
True: The customer must provide their address?  
False: The customer doesn't need to provide their address.  

- `invoice` | object | optional  
Contains: `enabled` | boolean | required  
True: ???  
False: ???

----------------
`plugin` | object | optional

Contains:  

- `shop` | string | optional
Sets the website the customer is buying from??  

- `plugin_version` | string | optional 
Sets the version of the ready-made integration you use, if any??

- `shop_version` | boolean? | optional
Sets ???  

- `partner` | string | optional
Sets ???  

- `shop_root_url` | string | optional 
The URL of the website the customer is buying from??

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object | required

See [delivery (object)](/api/#delivery-object).

----------------
`shopping_cart` | object | required

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class.

----------------
`custom_fields` | object | required

Sets whether to display additional fields in the FastCheckout page.

Contains:  

**1.** `name` | string | required?

????
Values: `acceptagreements`.??

**2.** `type` | string | required?  

Sets the layout of this field??  
Values: `checkbox`.  

**3.** `label` | string | required?

Specifies a label to display with the field.??  

**4.** `description_right` | object | required?

Sets the text of the label?? For example, provide texts to display in different languages.??

Contains: `value` | object | required?

- `nl` | string | optional  
Sets the text of the label in Dutch.??  

- `en` | string | optional  
Sets the text of the label in English??

**5.** `validation` | object | required?

Validates the customer's input and displays relevant error messages.??  

Contains:

`type` | string | required?  
Sets the mode of validating the customer's input??
Values: `regex`??

`data` | string | required?  
???  

`error` | object | required?  

- `nl` | string | optional  
Displays the error message in Dutch??

- `en` | string | optional  
Displays the error message in English??

**6.** `standard_type` | string/object | optional

There are several `standard_type` fields available:

**Company name**

`standard_type` | string | optional

Displays a field for the customer to enter their company name.

**Salutation**

**Sex**

**Comment**

**Newsletter**

**VAT number** 

**Birthday**

**Chamber of commerce number**

**Passport number**

**Driver's licence number**


----------------


{{% /description %}}