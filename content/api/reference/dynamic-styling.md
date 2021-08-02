---
weight: 650
meta_title: "API Reference - Dynamic Styling - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}


```json
{
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
}
```

{{< /code-block >}}

{{< description >}}

## Dynamic styling (template)

To [dynamically style]((/payments/checkout/payment-pages/dynamic-styling-payment-pages/)) your payment page, include this template in your transaction request.

| Setting                         | Description                  |
|-----------------------------------|-------------------------------|
| hide_logo                | Hides header logo                               | 
| iframe_mode                        | Hides various sections, e.g. logo, header                     |                 
| hide_flags                       | Hides flags container                       |                
| hide_powered                       | Hides powered link                     | 
| hide_cart                       | Hides cart container                   |               
| hide_btn_cancel                      | Hides **Cancel** button                   |               
| hide_cc_logos                        | Hides credit card logos                   |                
| hide_btn_all_methods                     | Hides **All methods** button               |                 

{{< /description >}}