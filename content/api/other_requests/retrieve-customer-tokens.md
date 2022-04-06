---
weight: 512
meta_title: "API reference - List customer tokens - MultiSafepay Docs"

---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}

> JSON response

```json
{
  "success":true,
  "data":{
    "tokens":[
      {
        "token":"QZTCh7jdk8",
        "code":"MASTERCARD",
        "display":"1234 5678 9101 2345",
        "bin":555555,
        "name_holder":"Test-person-nl",
        "expiry_date":1234,
        "expired":0,
        "last4":1111,
        "recurring_model":"cardOnFile"
      },
      {
        "token":"GVXjq3432o4",
        "code":"VISA",
        "display":"1234 5678 9101 2345",
        "bin":411111,
        "name_holder":"WebcashierE2E",
        "expiry_date":1234,
        "expired":0,
        "last4":2222,
        "recurring_model":"unscheduled"
      }
    ]
  }
}
```

{{< /code-block >}}

{{< description >}}

### List customer tokens

List all [tokens](/features/recurring-payments) related to a customer reference.

If there are lots of tokens, you can use the `limit` and `offset` query parameters to limit the number of tokens returned.

Example: If `limit` is set to 15 and `offset` to 0, then 17 tokens are listed (tokens 0 to 16).

**Parameters**

----------------
`limit` | integer | query parameter | optional

The number of tokens to list.  
If empty, the default is 10.

----------------
`offset` | integer | query parameter | optional

The number of the token to start the list from.  
If empty, the default is 0, i.e. the first token.

**Response**

**Response**

----------------
`token` | string | 

The unique identifier of the token.

----------------
`code` | string 

The unique identifier of the payment method.  
Options: `AMEX`, `DIREB`, `DIRECTBANK`, `IDEAL`, `MAESTRO`, `MASTERCARD`, `MISTERCASH`, `VISA`. 

For more information, see [Payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids).

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