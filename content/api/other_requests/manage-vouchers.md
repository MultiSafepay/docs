---
weight: 550
meta_title: "API Reference - Manage coupons - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
> POST - / orders
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
        "notification_url":"http://www.example.com/client/notification?type=notification",
        "redirect_url":"http://www.example.com/client/notification?type=redirect",
        "cancel_url":"http://www.example.com/client/notification?type=cancel",
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
## Manage vouchers

Manage which vouchers are displayed as options to the customer for the transaction.

**Parameters**

Use the following optional parameters in the [payment_options (object)](#payment-options-object) to control which vouchers are displayed.

------------------
`allow` | string (single value or array of values) | optional

An array of the vouchers to display to the customer. No vouchers will show if the array is empty. If this parameter is not present then all activated vouchers are shown.
    
Options:  
Baby Cadeaubon= BABYCAD  
Beautyandwellness= BEAUTYWELL  
Bloemencadeaukaart= BLOEMENCAD  
Boekenbon= BOEKENBON  
Degrotespeelgoedwinkel= DEGROTESPL  
Edenred Ticket Compliments=EDENCOM  
Edenred Ticket EcoCheque=EDENCO  
Edenred Ticket Restaurant=EDENRES  
Edenred Ticket Sport & Culture=EDENSPORTS  
Fashioncheque= FASHIONCHQ  
Fashiongiftcard= FASHIONGFT  
Fietsenbon= FIETSENBON  
Good4fun= GOOD4FUN     
Gezondheidsbon= GEZONDHEID   
Nationale bioscoopbon= NATNLBIOSC      
Nationaletuinbon= NATNLETUIN    
Parfumcadeaukaart= PARFUMCADE   
Sportenfit= SPORTENFIT    
Vuur & rook gift card= VRGIFTCARD    
VVV Cadeaukaart= VVVGIFTCRD   
Webshopgiftcard= WEBSHOPGFT  
Wijncadeau= WIJNCADEAU      
Yourgift= YOURGIFT    

------------------
`disable` | boolean | optional

To disable the display of all vouchers to the customer. If this is set to `True` then the `allow` parameter is ignored.

Options: `True`, `False`.    

------------------



{{% /description %}}