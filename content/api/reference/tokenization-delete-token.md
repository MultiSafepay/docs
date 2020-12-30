---
weight: 609
meta_title: "API - Tokenization - Delete token - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> DELETE - recurring/{your_customer_reference}/remove/{your_token}

> JSON Response
```shell
{
    "success": true,
    "data": {
        "removed": true
    }
}
```

{{< /code-block >}}

{{< description >}}

### Delete a token

This API call allows you to delete a token related to a single customer reference.

* All parameters shown are required field(s)

**Parameter**

__token__ | string

The unique token linked to the customer reference.  

----------------

{{< /description >}}