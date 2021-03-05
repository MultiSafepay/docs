---
weight: 610
meta_title: "API - Tokenization - Update token expiry date - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> PATCH - recurring/your_customer_reference/update/your_token

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

### Update token expiry date

This API call allows you to update the expiry date of a token associated with a credit card for when it has expired.

{{< /description >}}