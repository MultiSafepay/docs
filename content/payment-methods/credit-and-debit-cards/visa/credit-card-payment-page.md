---
title: "Visa credit card payment page"
weight: 26
meta_title: "Visa credit card payment page - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
--- 
## Integrating Visa

It is possible to either redirect to our credit card payment page where Visa will be readily available, thus allowing MultiSafepay to handle Visa as well as other credit card payment methods for you __or__ redirecting specifically to Visa.

### Redirect for all credit cards including Visa
Choose this method if you would like for MultiSafepay to handle all credit cards for you. By bundling all the credit cards in the checkout, you will save space and collapse all the different credit card providers. Visa is included this bundle, as well as Mastercard and American Express.

The customer will be redirected to our credit card payment page. The customer fills in his/her credentials and we will detect the credit card provider based on the first four digits.

The [credit card API page](/api/#credit-cards) illustrates the API implementation.

### Redirect specifically to Visa
Choose this way if you wish to only accept Visa. Your customer will be redirected to Visa. After the credentials are filled in, MultiSafepay will ensure the payment is completed.

For implementation, see the API calls for [Visa](/api/#visa)