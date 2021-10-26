---
weight: 540
meta_title: "API reference - Retrieve website categories - MultiSafepay Docs"

---
{{< code-block >}}
> GET - /categories


> JSON response

```json
{
  "success":true,
  "data":[
    {
      "code":106,
      "description":"Child and toys"
    }
  ]
}
```
{{< /code-block >}}

{{< description >}}
## Retrieve website categories
Retrieves a list of website categories.

**Response**

----------------
`code` | string 

The unique identifier of the payment gateway.

----------------
`description` | string 

A description of the transaction, which is displayed in both your account and the affiliated account.

----------------

{{% /description %}}