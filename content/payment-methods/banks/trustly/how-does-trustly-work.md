---
title: "Trustly, How does it work?"
weight: 21
meta_title: "Trustly, how does it work? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/trustly/how-does-trustly-work/]
---
## How it works
When the customer selects Trustly as payment method, he/she needs to select the desired country.
By doing so, all online banks that are connected to the payment method Trustly will be presented to the customer.
The customer can finalize the payment by logging in with the banking details.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status | Transaction Status | Description                                                                                                                       |
|--------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                                          |
| Completed    | Completed        | A successful Trustly transaction has been received and the funds will be added to your MultiSafepay Control balance.              |
| Declined     | Declined         | Transaction has been rejected.                                                                                                    |
| Uncleared    | Uncleared        | Transaction is successful, but awaiting payment confirmation from Trustly. |
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                                    |
| Void         | Cancelled        | Transaction has been cancelled.                                                                                                   |


#### Refund flow

| Order Status   | Transaction Status  | Description                                                                             |
|----------------|-------------------|-----------------------------------------------------------------------------------------|
| Initialized    | Initialized       | A refund has been requested.                                                            |
| Completed      | Completed         | Refund has been successfully processed.                                                 |

The full API reference for Trustly cards can be found [here](/api/#trustly)


| Supported plugins                                                                                                                 | Version                      |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------|  
| [Magento 2](/integrations/plugins/magento2)                                                                                                   | Available from version 1.5.0 |  
| [Magento 1](/integrations/plugins/magento1)                                                                                                   | Available from version 2.4.1 |
| [WooCommerce](/integrations/plugins/woocommerce)                                                                                              | Available from version 3.2.0 |
| [OpenCart](/integrations/plugins/opencart)                                                                                                    | Available from version 2.2.0 |
| [PrestaShop 1.7](/integrations/plugins/prestashop-1-7)                                                                                        | Available from version 4.2.0 |
| [CS-Cart](/integrations/plugins/cs-cart)                                                                                                      | Available from version 1.3.0 |
| [Drupal 8](/integrations/plugins/drupal8)                                                                                                     | Available from version 1.0   |
| [Shopware 5](https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html) | Available from version 2.0.2 |
| [X-Cart](/integrations/plugins/x-cart)                                                                                                        | Available from version 2.2.0 |
| [Shopify](/integrations/hosted/shopify)                                                                                                      | Available from Shopify       |



### Product rules
Some rules may apply to certain payment methods. For Trustly, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with Trustly. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful Trustly transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page.



* In exceptional cases, the _uncleared_ status can occur for Trustly. In this case, it is up to Trustly to inform MultiSafepay of the correct status. This can be a _completed_ status, as well as a _declined_ and / or _expired_ status. The _uncleared_ status automatically expires after 5 days.

* Trustly can be offered in the following [currencies](/faq/general/which-currencies-are-supported-by-multisafepay):     

    * Euros (EUR)       
    * Pounds (GBP)       
    * Swedish krona (SEK)
