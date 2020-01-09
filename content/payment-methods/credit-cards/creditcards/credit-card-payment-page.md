---
title: "Credit card payment page"
weight: 25
meta_title: "Credit card payment page - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
--- 
## Integrating credit cards

It is possible to either redirect to our credit card payment page, thus allowing MultiSafepay to handle all credit card payments for you __or__ redirecting to a specific credit card.

## Redirect for all credit cards
Choose this method if you would like for MultiSafepay to handle all credit cards for you. By bundling all the credit cards in the checkout, you will save space and collapse all the different credit card providers. MultiSafepay does the rest.

The customer will be redirected to our credit card payment page. The customer fills in his/her credentials and we will detect the credit card provider based on the first four digits.

The [credit card API page](/api/#credit-cards) illustrates the API implementation.

## Redirect specific credit cards
Choose this way if you wish to only accept credit cards from certain providers. Your customer will be redirected to our payment page for that specific credit card. After the credentials are filled in, MultiSafepay will ensure the payment is completed.

For implementation, see our pages per credit card provider:

* [American-Express](/api/#american-express)
* [Maestro](/api/#Maestro)
* [Mastercard](/api/#Mastercard)
* [VISA](/api/#VISA)