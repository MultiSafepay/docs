---
title : "How to process a Split Payment?"
weight: 81
meta_title: "Split Payment, how to process it? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

Split Payments is a feature in our [API](/api/#split-payments) This is not incorporated within our plugins by default, but it can be added through customization from your side.  

In order to split a payment you need the following:  

* two active MultiSafepay accounts  
* access to the code that creates the JSON request.

For split payments, add the object "affiliate" like:

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

See our [API page](/api/#split-payments) for more detailed technical information.

## Important
* Amount for fixed is in cents and follows the currency settings for the transaction
* You can either choose "fixed" or "percentage" or a combination of both
* Keep in mind that our platform uses _var3_  to store this data, so if you provide any value for _var3_, it will be overwritten.
