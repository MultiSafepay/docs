---
title : "Processing split payments"
weight: 82
meta_title: "Processing split payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/split-payments/how-do-i-get-split-payments
---

Split payments are not incorporated in our [ecommerce integrations](/integrations/ecommerce-integrations) by default. You can add this as a custom feature using our API. 

For more information, see API Reference - [Split payments](/api/#split-payments).

You can select to split by a "fixed" amount, a "percentage", or a combination of both. The amount for "fixed" payments is in cents and matches the currency the transaction was paid in. This data is stored in `var3`. Any value you provide for `var3` is overwritten.

Prerequisites:  

- Two active MultiSafepay accounts  
- Access to the code that creates the JSON request

To process split payments, add an `affiliate` object:

```shell
"affiliate": {
   "split_payments": [
        {
            "merchant": 987654321,
            "fixed": 123,
            "description": "Fixed fee"
        },
        {
            "merchant": 987654321,
            "percentage": 12.3,
            "description": "Relative fee"
        }
    ]
}
```
