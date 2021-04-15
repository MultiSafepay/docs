---
weight: 51
meta_title: "API - Discount added as order rule - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---


{{< code-block >}}

> Example with discount in separate order rule:

```shell 

{
	"type": "redirect",
	"gateway": "PAYAFTER",
	"order_id": "my-order-id-1",
	"currency": "EUR",
	"amount": 17424,
	...
	"shopping_cart": {
		"items": [{
			"name": "Geometric Candle Holders",
			"description": "",
			"unit_price": 90.00,
			"quantity": 2,
			"merchant_item_id": "111111",
			"tax_table_selector": "none",
			"weight": {
				"unit": "KG",
				"value": 12
			}
		}, {
			"name": "20% discount on all items",
			"description": "Discount",
			"unit_price": -43.56,
			"quantity": 1,
			"merchant_item_id": "discount",
			"tax_table_selector": "none",
			"weight": {
				"unit": "KG",
				"value": 0
			}
		}]
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
					"name": "none",
					"rules": [{
						"rate": 0.00
					}]
				}
			]
		}
	}
}
```
{{< /code-block >}}
{{< description >}}
## Discount added as order rule (which is non-refundable)
Adding a discount as an order rule is a common way to add a discount before submitting a transaction request at MultiSafepay. However, adding a discount as an order rule may result in a conflict when partially refunding a post-paid [payment method](/faq/general/glossary/#payment-method) transaction. This is most common when the discount is a percentage. Adding a discount as a seperate discount rule, will conflict when partially refunding a post-paid payment method transaction as the negative amount cannot be undone. It is not possible to partially refund a negative amount that is added as a discount rule. 
{{< /description >}}