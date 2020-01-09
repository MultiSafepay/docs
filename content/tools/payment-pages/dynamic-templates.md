---
title : "How to use dynamic styling for a Payment page?"
weight: 41
meta_title: "Payment pages - Dynamic templates - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
For merchants with a custom integration via [JSON API MultiSafepay](/api/), we also offers dynamic styling of the templates. This means you can change the look and feel of a payment page per transaction.

There are two options to dynamically style the payment page:

## 1. Load a saved template
Whenever you have stored a template, you can call it through the first-level JSON object "template_id": "value of the template".

## 2. Provide 'template' object structure within the transaction request
MultiSafepay also offers real-time styling of the templates. This means you can change the look and feel of a payment page per transaction on the fly. You need to add the following to your transaction request:
```
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
```
