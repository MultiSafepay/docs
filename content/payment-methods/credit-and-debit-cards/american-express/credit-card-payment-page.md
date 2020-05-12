---
title: "American Express credit card payment page"
weight: 26
meta_title: "American Express credit card payment page - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
--- 
## Integrating American Express

It is possible to either redirect to our credit card payment page where American Express will be readily available, thus allowing MultiSafepay to handle American Express as well as other credit card payment methods for you __or__ redirecting specifically to American Express.

### Redirect for all credit cards including American Express
Choose this method if you would like for MultiSafepay to handle all credit cards for you. By bundling all the credit cards in the checkout, you will save space and collapse all the different credit card providers. American Express is included this bundle.

The customer will be redirected to our credit card payment page. The customer fills in his/her credentials and we will detect the credit card provider based on the first four digits.

The [credit card API page](/api/#credit-cards) illustrates the API implementation.

### Redirect specifically to American Express
Choose this way if you wish to only accept American Express. Your customer will be redirected to American Express. After the credentials are filled in, MultiSafepay will ensure the payment is completed.

For implementation, see the API calls for [American Express](/api/#american-express)