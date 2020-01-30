---
weight: 608
meta_title: "API - Tokenization - Get token info - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}

> GET - recurring/{your_customer_reference}/token/{your_token}

> JSON Response

```shell
{
    "success": true,
    "data": {
        "token": "azbkvsE0up4",
        "code": "MASTERCARD",
        "display": "Card xxxx xxxx xxxx 4444",
        "bin": 555555,
        "name_holder": "Testperson-nl",
        "expiry_date": 3611,
        "expired": 0,
        "last4": 4444,
        "model": "cardOnFile"
    }
}
```

{{< /code-block >}}

{{< description >}}

### Get info of a token

This API call allows you to retreive the information related to a single token.

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
|token                            | string   | The unique token linked to the customer reference. |

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization/)

{{< /description >}}