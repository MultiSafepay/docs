---
weight: 550
meta_title: "API reference - Specify vouchers - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
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
  "description": "Test Order Description",
  "manual": "false",
  "payment_options": {
    "notification_url": "http://www.example.com/client/notification?type=notification",
    "redirect_url": "http://www.example.com/client/notification?type=redirect",
    "cancel_url": "http://www.example.com/client/notification?type=cancel",
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
## Specify vouchers

Specify which vouchers are displayed as options to the customer for the transaction.

**Parameters**

Use the following optional parameters in the [payment_options (object)](#payment-options-object) to specify which vouchers to display.

------------------
`allow` | array of strings | optional

An array specifying the vouchers to display to the customer.  
If empty, no vouchers display.  
If not included, then all activated vouchers display.
    
Options:  
Baby Cadeaubon= `BABYCAD`  
Beautyandwellness= `BEAUTYWELL`  
Bloemencadeaukaart= `BLOEMENCAD`  
Boekenbon= `BOEKENBON`  
Degrotespeelgoedwinkel= `DEGROTESPL`  
Edenred Ticket Compliments= `EDENCOM`  
Edenred Ticket EcoCheque= `EDENCO`  
Edenred Ticket Restaurant= `EDENRES`  
Edenred Ticket Sport & Culture= `EDENSPORTS`  
Fashioncheque= `FASHIONCHQ`   
Fashiongiftcard= `FASHIONGFT`  
Fietsenbon= `FIETSENBON`   
Good4fun= `GOOD4FUN`  
Gezondheidsbon= `GEZONDHEID`   
Nationale bioscoopbon= `NATNLBIOSC`      
Nationaletuinbon= `NATNLETUIN`    
Parfumcadeaukaart= `PARFUMCADE`   
Sportenfit= `SPORTENFIT`    
Vuur & rook gift card= `VRGIFTCARD`    
VVV Cadeaukaart= `VVVGIFTCRD`   
Webshopgiftcard= `WEBSHOPGFT`  
Wijncadeau= `WIJNCADEAU`      
Yourgift= `YOURGIFT`    

------------------
`disable` | boolean | optional

Disables displaying all vouchers to the customer.  

If set to `true`, the `allow` parameter is ignored.

Options: `true`, `false`.    

------------------



{{% /description %}}