---
weight: 216
meta_title: "API reference - Challenge chargebacks - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders/{order_id}/files

```json
{
  "type":"",
  "base64":"",
  "description":"",
  "name":""
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    
  }
}
```
{{< /code-block >}}

{{< description >}}
### Challenge chargebacks

MultiSafepay can challenge [chargebacks](/payments/chargebacks/) on your behalf. To do so, we need documented proof of the order.

You can upload the files or documents via a `POST /order/{order_id}/files` request.

**Parameters**

----------------
`type` | string | required

The type of order you want to create, in this case a chargeback challenge.  
Options: `chargeback`.

----------------
`base64` | string | required

The format of the file you're uploading.  
Format: PDF, JPEG, PNG. 

----------------
`description` | integer | required

A Description of or comments on the file you're uploading. 

----------------
`name` | string | required

The name of the file you're uploading.

----------------

{{% /description %}}

