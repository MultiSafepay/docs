---
weight: 610
meta_title: "API Reference - Transaction statuses - MultiSafepay Docs"
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


**Parameters**

__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
See also [notification_url](/developer/api/notification-url).              

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.              

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails. 

----------------
__notification_method__ | string

Enables push notifications (POST,GET) default: GET.   

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

{{% /description %}}
