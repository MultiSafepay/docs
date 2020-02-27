---
weight: 650
meta_title: "API - Dynamic Styling - MultiSafepay Support"
meta_description: In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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

Read more about [dynamic styling](https://docs.multisafepay.com/tools/payment-pages/dynamic-templates/) for a payment page.

{{% /description %}}