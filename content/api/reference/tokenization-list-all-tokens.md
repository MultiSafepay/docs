---
weight: 607
meta_title: "API - Tokenization - List all tokens - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}

> JSON Response

```shell
{
	"success": true,
	"data": {
		"tokens": [{
				"token": "QZTCh7jdk8",
				"code": "MASTERCARD",
				"display": "1234 5678 9101 2345",
				"bin": 555555,
				"name_holder": "Test-person-nl",
				"expiry_date": 0988,
				"expired": 0,
				"last4": 1111,
				"recurring_model": "cardOnFile"
			},
			{
				"token": "GVXjq3432o4",
				"code": "VISA",
				"display": "1234 5678 9101 2345",
				"bin": 411111,
				"name_holder": "WebcashierE2E",
				"expiry_date": 0988,
				"expired": 0,
				"last4": 2222,
				"recurring_model": "unscheduled"
			}
		]
	}
}
```

{{< /code-block >}}

{{< description >}}

### List all tokens for a customer reference

This API call allows you to list all tokens related to a single customer reference.

If you have many tokens, you can use the two parameters _limit_ and _offset_ to limit the number of tokens that will be listed.

Example: If the _limit_ is set to 15 and the _offset_ to 0, then 17 tokens will be listed (token 0 to token 16)

* All parameters shown are required field(s)

**Parameter**

__token__ | string

The unique token linked to the customer reference.  

----------------

__limit__ | integer

The number of tokens listed. If _limit_ is empty, the default value is 10.

----------------

__offset__ | integer

The position from which the tokens will be listed. If _offset_ is left empty, the default value is 0 (the first token)

----------------

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization)

{{< /description >}}