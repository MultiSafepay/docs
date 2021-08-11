---
weight: 208
meta_title: "API Reference - Apply dynamic template - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "manual":false,
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "template_id":"123456",
    "template":{
      "version":"1.0",
      "settings":{
        "hide_logo":false,
        "hide_flags":false,
        "hide_powered":false,
        "hide_cart":false,
        "hide_btn_cancel":false,
        "hide_cc_logos":false,
        "hide_btn_all_methods":false
      },
      "header":{
        "logo":{
          "image":""
        },
        "cover":{
          "image":""
        },
        "background":"",
        "text":"#333"
      },
      "body":{
        "text":"#ab141b",
        "background":"#fdfcfc",
        "link":{
          "text":"#00acf1",
          "hover":{
            "text":"",
            "border":""
          }
        }
      },
      "container":{
        "text":"#ffffff",
        "label":"#a4a3a3",
        "background":"#080808",
        "link":{
          "text":""
        }
      },
      "cart":{
        "text":"#333333",
        "label":"#8b8b8b",
        "background":"#ffffff",
        "border":"#333333"
      },
      "payment_form":{
        "text":"#ab141b",
        "background":"#ffffff",
        "border":"#333333",
        "inputs":{
          "border":"#bdbbbb",
          "label":"#8b8b8b"
        }
      },
      "buttons":{
        "payment_method":{
          "background":"#ffffff",
          "text":"#ab141b",
          "border":"#333333",
          "hover":{
            "background":"#ab141b",
            "text":"#ffffff",
            "border":""
          },
          "active":{
            "background":"",
            "text":"",
            "border":""
          }
        },
        "secondary":{
          "background":"#00acf1",
          "text":"#ffffff",
          "hover":{
            "background":"",
            "text":""
          }
        },
        "primary":{
          "background":"#cccccc",
          "text":"#ffffff",
          "hover":{
            "background":"",
            "text":""
          }
        }
      }
    }
  },
  "customer":{
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
### Apply dynamic templates

To apply a template to the [MultiSafepay payment page](/payments/checkout/payment-pages/), include in the transaction request:

- The `template_id` of a template within your MultiSafepay account, **or**
- A template object structure. 

If you provide both, the template object is primary.

**Template object structures**

The template object structure must include full JSON CSS parameters. If you only send partial CSS settings, the parameter you send overrides the default MultiSafepay template.

When sending images in the template structure for the logo and header, you must use HTTPS, otherwise they will be ignored.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`.  

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

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
`template` | object | optional

A template object structure.  
The template structure overrides the `template_id`.

Contains:  

- `settings` | object

    See [settings (object)](/api/#settings-object).

- `header` | object
- `cover` | object
- `background` | object
- `body` | object
- `container` | object
- `cart` | object
- `payment_form` | object
- `buttons` | object

    Contains:  

    - `payment_methods` | object

        See [payment_methods (object)](/api/#payment_methods-object).

    - `active` | object
    - `secondary` | object
    - `primary` | object


----------------
`template_id` | string | optional

The identifier of a saved template from your MultiSafepay account. 
The template structure overrides the `template_id`.

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**  

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{% /description %}}