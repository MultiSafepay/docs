---
weight: 410
meta_title: "API - Cancel pre-transaction (sessionid) - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> PATCH - /orders 

```shell

{
    "status": "cancelled",
    "exclude_order": 1
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {}
}
```
{{< /code-block >}}
{{< description >}}
## Cancel pre-transaction (sessionid)

Cancellation of a transaction based on a sessionid

**Parameters**

----------------
__status__ | string

The status of the order. Options: cancelled

----------------
__exclude_order__ | integer

Indicates the outcome of the cancellation. When exclude_order is set to 1, the pre-transaction (sessionid) will be cancelled. When exclude_order is set to 0, the pre-transaction will be cancelled as well as the transaction itself. __Please note: this only works if transactions are marked as 'Initialized'. A 'Reserved' status cannot be cancelled.__
{{% /description %}}