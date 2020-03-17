---
weight: 270
meta_title: "API - Dynamic template - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders 

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-5",
    "gateway": "",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "manual": "false",
   "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "template_id": "123456",
        "template": {
            "version": "1.0",
            "settings": {
                "hide_logo": false,
                "hide_flags": false,
                "hide_powered": false,
                "hide_cart": false,
                "hide_btn_cancel": false,
                "hide_cc_logos": false,
                "hide_btn_all_methods": false
            },
            "header": {
                "logo": {
                    "image": ""
                },
                "cover": {
                    "image": ""
                },
                "background": "",
                "text": "#333"
            },
            "body": {
                "text": "#ab141b",
                "background": "#fdfcfc",
                "link": {
                    "text": "#00acf1",
                    "hover": {
                        "text": "",
                        "border": ""
                    }
                }
            },
            "container": {
                "text": "#ffffff",
                "label": "#a4a3a3",
                "background": "#080808",
                "link": {
                    "text": ""
                }
            },
            "cart": {
                "text": "#333333",
                "label": "#8b8b8b",
                "background": "#ffffff",
                "border": "#333333"
            },
            "payment_form": {
                "text": "#ab141b",
                "background": "#ffffff",
                "border": "#333333",
                "inputs": {
                    "border": "#bdbbbb",
                    "label": "#8b8b8b"
                }
            },
            "buttons": {
                "payment_method": {
                    "background": "#ffffff",
                    "text": "#ab141b",
                    "border": "#333333",
                    "hover": {
                        "background": "#ab141b",
                        "text": "#ffffff",
                        "border": ""
                    },
                    "active": {
                        "background": "",
                        "text": "",
                        "border": ""
                    }
                },
                "secondary": {
                    "background": "#00acf1",
                    "text": "#ffffff",
                    "hover": {
                        "background": "",
                        "text": ""
                    }
                },
                "primary": {
                    "background": "#cccccc",
                    "text": "#ffffff",
                    "hover": {
                        "background": "",
                        "text": ""
                    }
                }
            }
        }
    },
    "customer": {
        "email": "test@example.com"
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-5",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Dynamic Template

You can define the template of the MultiSafepay payment page within a transaction request. This can be done by providing a template_id of a predefined template within your MultiSafepay Control or by providing a template object structure within the transaction request. When both are provided, the template object is primary.

The template object structure needs to include the JSON CSS parameters. When sending partial CSS settings within the template structure, only the sent parameter will override the default MultiSafepay template.

When sending images within the template structure for the "logo" and "header", you can use external references but they must be using HTTPS, otherwise they will be ignored.


| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| gateway                        | string   | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. |
| order_id                       | integer / string   | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string   | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object   |                             |
| notification_url               | string   | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                   | string   | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                     | string   | Customer will be redirected to this page after a failed payment.  | 
| template                       | object   | A template object structure.Template structure overrules template_id.   |
| template_id                    | string   | Saved template identifier. Template structure overrules template_id.    |

{{% /description %}}