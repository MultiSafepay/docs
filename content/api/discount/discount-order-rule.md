---
weight: 51
meta_title: "API - Discount added as order rule - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---


{{< code-block >}}

> Example with discount in separate order rule:

```shell 
{
	"type": "redirect",
	"gateway": "PAYAFTER",
	"order_id": "apitool_7670065",
	"currency": "EUR",
	"amount": 20800,
	"description": "Test Order Description",
	"var1": "",
	"var2": "",
	"var3": "",
	"items": "",
	"manual": "false",
	"gateway_info": {
		"birthday": "1980-01-30",
		"bank_account": "0417164300",
		"phone": "0208500500",
		"email": "example@multisafepay.com"
	},
	"payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
	},
	"plugin": {
		"shop": "ApiTestTool",
		"plugin_version": "1.0.0",
		"shop_version": "1",
		"partner": "partner",
		"shop_root_url": "https://multisafepay.com"
	},
	"customer": {
		"locale": "us",
		"ip_address": "80.123.456.789",
		"first_name": "Testperson-nl",
		"last_name": "Approved",
		"address1": "Kraanspoor",
		"address2": "",
		"house_number": "39c",
		"zip_code": "1033 SC",
		"city": "AMSTERDAM",
		"state": "",
		"country": "NL",
		"email": "example@multisafepay.com",
		"referrer": "http://multisafepay-demo.com/plugingroup/dev/magento/1901/checkout/cart/",
		"user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
	},
	"delivery": {
		"first_name": "Testperson-nl",
		"last_name": "Approved",
		"address1": "Kraanspoor",
		"address2": "",
		"house_number": "39c",
		"zip_code": "1033 SC",
		"city": "AMSTERDAM",
		"state": "",
		"country": "NL",
		"phone": "",
		"email": ""
	},
	"shopping_cart": {
		"items": [{
				"name": "Geometric Candle Holders",
				"description": "",
				"unit_price": 90,
				"quantity": 2,
				"merchant_item_id": "111111",
				"tax_table_selector": "none",
				"weight": {
					"unit": "KG",
					"value": 12
				}
			},
			{
				"name": "Nice apple",
				"description": "",
				"unit_price": 35,
				"quantity": 2,
				"merchant_item_id": "333333",
				"tax_table_selector": "none",
				"weight": {
					"unit": "KG",
					"value": 20
				}
			},
			{
				"name": "Flat Rate - Fixed",
				"description": "Shipping",
				"unit_price": 10,
				"quantity": 1,
				"merchant_item_id": "msp-shipping",
				"tax_table_selector": "none",
				"weight": {
					"unit": "KG",
					"value": 0
				}
			}, {
				"name": "20% discount on all items",
				"description": "Discount",
				"unit_price": -52,
				"quantity": 1,
				"merchant_item_id": "discount",
				"tax_table_selector": "none",
				"weight": {
					"unit": "KG",
					"value": 0
				}
			}
		]
	},
	"checkout_options": {
		"tax_tables": {
			"default": {
				"shipping_taxed": "true",
				"rate": 0.21
			},
			"alternate": [{
					"name": "BTW21",
					"rules": [{
						"rate": 0.21
					}]
				},
				{
					"name": "BTW6",
					"rules": [{
						"rate": 0.06
					}]
				},
				{
					"name": "BTW0",
					"rules": [{
						"rate": 0.00
					}]
				},
				{
					"name": "0.0000",
					"rules": [{
						"rate": 0
					}]
				},
				{
					"name": "0.0000",
					"rules": [{
						"rate": 0
					}]
				},
				{
					"name": "FEE",
					"rules": [{
						"rate": 0.00
					}]
				},
				{
					"name": "none",
					"rules": [{
						"rate": 0.00
					}]
				},
				{
					"name": "2",
					"rules": [{
							"rate": 0.0825,
							"country": "US"
						},
						{
							"rate": 0.08375,
							"country": "US"
						}
					]
				}
			]
		}
	}
}
```
{{< /code-block >}}
{{< description >}}
## Discount added as order rule (which is non-refundable)
Adding a discount as order rule is a common way to add a discount before submitting a transaction request at MultiSafepay. However, adding a discount as order rule may result in a conflict when partial refunding a postpaid [payment method](/faq/getting-started/glossary/#payment-method) transaction. This is most common when the discount is a percentage. Adding a discount as seperate discount rule, will conflict with partially refunding a postpaid payment method transaction as the negative amount cannot be undone. It is not possible to partially refund a negative amount that is added as a discount rule. 
{{< /description >}}