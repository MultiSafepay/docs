---
weight: 608
meta_title: "API reference - payment_options (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
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

Endpoint for MultiSafepay to send status updates and other notifications to you.   
For more information, see [Notification URL](/developer/api/notification-url).              

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

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `true`.   
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
