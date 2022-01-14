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

The unique identifier of the website category.

----------------
`description` | string 

The website category name.

----------------

{{% /description %}}
