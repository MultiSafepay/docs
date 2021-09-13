---
weight: 608
meta_title: "API reference - payment_options (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
url: '/api/#payment-options-object'
---
{{< code-block >}}
```json 
{
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "notification_method":"POST",
    "close_window":true,
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

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------
`settings` | object | optional

To configure options for the payment.

Contains:
- `gateways` | object | optional

  Contains:
  - `coupons` | object | optional

    Contains:
    - `allow` | string (single value or array of values) | optional
    
    An array of the vouchers to display to the customer. No vouchers will show if the array is empty. If this parameter is not present then all activated vouchers are shown. See [manage vouchers](/api/#manage-vouchers).

    - `disable` | boolean | optional

    To disable the display of all vouchers to the customer. If this is set to `True` then the `allow` parameter is ignored.

    Options: `True`, `False`. 

----------------

{{% /description %}}
