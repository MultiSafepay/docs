---
weight: 550
meta_title: "API reference - Specify gift cards - MultiSafepay Docs"

---

{{< code-block >}}
> POST - /orders
```json
{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "gateway": "",
  "currency": "EUR",
  "amount": "1000",
  "description": "Test order description",
  "manual": "false",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "settings": {
      "gateways": {
        "coupons": {
          "allow": [
            "EDENECO"
          ],
          "disabled": false
        }
      }
    }
  }
}
```

> JSON response

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL",
    "session_id": "session-id"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Specify gift cards

Specify which gift cards to display to the customer.

**Parameters**

Use the following optional parameters in the [payment_options (object)](#payment-options-object) to specify which gift cards to display.

------------------
`allow` | array of strings | optional

An array of gateway identifiers for the gift cards to display to the customer.  
If empty, no gift cards display.  
If not included, then all activated gift cards display.
    
For a full list of gateway IDs, see [Payment method gateway IDs](/developer/gateway-ids/).

------------------
`disabled` | boolean | optional

Disables displaying all gift cards to the customer.  

If set to `true`, the `allow` parameter is ignored.

Options: `true`, `false`.    

------------------



{{% /description %}}
