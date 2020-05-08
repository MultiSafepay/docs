---
weight: 650
meta_title: "API - Dynamic Styling - MultiSafepay Support"
meta_description: The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}


```shell
    
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
    },
```

{{< /code-block >}}

{{< description >}}

## Dynamic Styling

This template can be added to your transaction request for dynamic styling of your payment page.

Below you can find an explanation of the settings which can be included in the transaction request:

| Setting                         | Description                  |
|-----------------------------------|-------------------------------|
| hide_logo                | Hides header logo                               | 
| iframe_mode                        | Hides various sections e.g. logo, header                     |                 
| hide_flags                       | Hides flags container                       |                
| hide_powered                       | Hides powered link                     | 
| hide_cart                       | Hides cart container                   |               
| hide_btn_cancel                      | Hides button cancel                   |               
| hide_cc_logos                        | Hides credit card logos                   |                
| hide_btn_all_methods                     | Hides all methods button               |                 

Read more about [dynamic styling](https://docs.multisafepay.com/tools/payment-pages/dynamic-templates/) for a payment page.

{{< /description >}}