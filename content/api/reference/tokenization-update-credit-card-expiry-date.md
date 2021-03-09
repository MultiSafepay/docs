---
weight: 610
meta_title: "API - Tokenization - Update credit card expiry date of token - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> PATCH - recurring/{your_customer_reference}/update/{your_token}

```shell
{
    "expiry_date": "2903"
}
```
> JSON response

```shell
{
    "success": true,
    "data": {
        "updated": true
    }
}
```

{{< /code-block >}}

{{< description >}}

### Update credit card expiry date of a token

This API call allows you to update the credit card expiry date of a token for when it has expired.

Use __PATCH__ with the required placeholders in the URL:

* *your_customer_reference* refers to your internal unique customer reference
* *your_token* refers to the unique token associated with the customer

----------------
__expiry_date__ | integer

The updated value of the expiry date. E.g., December 2025 is formatted as `1225`

----------------
{{< /description >}}
