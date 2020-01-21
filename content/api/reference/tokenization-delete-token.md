---
weight: 609
meta_title: "API - Tokenization - Delete token - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
|token                            | string   | The unique token linked to the customer reference. |

{{< /description >}}