---
weight: 608
meta_title: "API Reference - payment_options (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```json 
{
	"payment_options": {
		"notification_url": "http://www.example.com/client/notification?type=notification",
		"redirect_url": "http://www.example.com/client/notification?type=redirect",
		"cancel_url": "http://www.example.com/client/notification?type=cancel", 
		"notification_method": "POST",
		"close_window": true,
	}
}
```


{{< /code-block >}}

{{< description >}}
## payment_options (object)

URLs for sending notifications to, or to redirect customers to.

Contains:  

**Parameters**

----------------
`notification_url` | string | required

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).              

----------------
`redirect_url` | string | required

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.              

----------------
`cancel_url` | string | required

The page the customer is redirected to if the payment fails. 

----------------
`notification_method` | string | optional

Enables push notifications.  
Options: `POST`, `GET`.  
Default: `GET`.   

----------------
`close_window` | bool | optional

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

{{% /description %}}
