---
weight: 608
meta_title: "API reference - payment_options (object) - MultiSafepay Docs"

---
{{< code-block >}}
```json 
{
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "notification_method": "POST",
    "close_window": true,
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


{{< /code-block >}}

{{< description >}}
## payment options (object)

URLs for sending notifications to, or redirecting customers to.

Contains:  

**Parameters**

----------------
`notification_url` | string | required

Webhook endpoint for MultiSafepay to send you order status updates and other notifications.   
For more information, see [Webhook](/developer/webhooks/).              

----------------
`redirect_url` | string | required

Your success/thank you page, where the customer is redirected after completing payment.   
For more information, see [Redirect URL](/developer/api/redirect-url/).          

----------------
`cancel_url` | string | required

The page the customer is redirected to if the payment fails. 

----------------
`notification_method` | string | optional

Enables push notifications.  
Options: `POST`, `GET`.  
Default: `GET`.   

----------------
`close_window` | boolean | optional

To display the [payment page](/payment-pages/) in a new window that automatically closes after the customer completes payment, set to `true`.   
Options: `true`, `false`. 

----------------
`settings` | object | optional

Configures options for the payment.

Contains:  

- `gateways` | object | optional

  Contains:  

  - `coupons` | object | optional

    Contains:  
    
    - `allow` | array of strings | optional
    
    An array specifying the vouchers to display to the customer.  
    If empty, no vouchers display.  
    If not included, then all activated vouchers display.  
    See [specify vouchers](/api/#specify-vouchers).

    - `disable` | boolean | optional

    Disables displaying all vouchers to the customer.  
    If set to `true`, the `allow` parameter is ignored.  
    
    Options: `true`, `false`.    


----------------

{{% /description %}}
