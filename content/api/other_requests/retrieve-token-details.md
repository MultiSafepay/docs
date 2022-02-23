---
weight: 511
meta_title: "API reference - Get token - MultiSafepay Docs"

---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}  
/token/{your_token}

> JSON response

```json
{
  "success":true,
  "data":{
    "token":"azbkvsE0up4",
    "code":"MASTERCARD",
    "display":"Card xxxx xxxx xxxx 4444",
    "bin":555555,
    "name_holder":"Testperson-nl",
    "expiry_date":3611,
    "expired":0,
    "last4":4444,
    "model":"cardOnFile"
  }
}
```

{{< /code-block >}}

{{< description >}}

### Get token

Get information about a [token](/features/recurring-payments).

**Parameter**

----------------
`token` | string | path parameter | required

The unique identifier of the token.  

**Response**

----------------
`token` | string | 

The unique identifier of the token.

----------------
`code` | string 

The unique identifier of the payment method.  
Options: `AMEX`, `DIREB`, `DIRECTBANK`, `IDEAL`, `MAESTRO`, `MASTERCARD`, `MISTERCASH`, `VISA`. 

For more information, see [Payment method gateway IDs](https://docs.multisafepay.com/developer/gateway-ids/).

----------------
`display` | string 

How the card number is displayed. 

----------------
`bin` | integer 

The bank identification number (BIN) of the card. 

----------------
`name_holder` | string 

The card holder's name.  

----------------
`expiry_date` | integer 

The card expiry date.  
Format: `monthnumberdatenumber`.  
Example: December 2025 is formatted as `1225`.

----------------
`expired` | boolean 

Whether the card has expired.

----------------
`last4` | string 

The last 4 digits of the card number. 

----------------
`model` | string 

The [recurring model](/features/recurring-payments/#recurring-models).  
Options: `cardOnFile`, `subscription`, `unscheduled`.  

----------------


{{< /description >}}