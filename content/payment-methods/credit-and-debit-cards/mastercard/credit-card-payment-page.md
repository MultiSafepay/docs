---
title: "Mastercard credit card payment page"
weight: 26
meta_title: "Mastercard credit card payment page - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
--- 
## Integrating Mastercard

It is possible to either redirect to our credit card payment page where Mastercard will be readily available, thus allowing MultiSafepay to handle Mastercard as well as other credit card payment methods for you __or__ redirecting specifically to Mastercard.

### Redirect for all credit cards including Mastercard
Choose this method if you would like for MultiSafepay to handle all credit cards for you. By bundling all the credit cards in the checkout, you will save space and collapse all the different credit card providers. Mastercard is included this bundle.

The customer will be redirected to our credit card payment page. The customer fills in his/her credentials and we will detect the credit card provider based on the first four digits.

The [credit card API page](/api/#credit-cards) illustrates the API implementation.

### Redirect specifically to Mastercard
Choose this way if you wish to only accept Mastercard. Your customer will be redirected to Mastercard. After the credentials are filled in, MultiSafepay will ensure the payment is completed.

For implementation, see the API calls for [Mastercard](/api/#mastercard)