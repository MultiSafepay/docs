---
title: "MultiSafepay glossary"
breadcrumb_title: MultiSafepay glossary
weight: 10
meta_title: "MultiSafepay glossary - MultiSafepay Docs"
short_description: "Get familiar with payments terminology and specific MultiSafepay uses."
layout: 'single'
logo: '/svgs/Guides.svg'
url: '/glossaries/multisafepay-glossary/'
aliases:
    - /faq/general/glossary
    - /getting-started/glossary/
---
### acquirer
A financial institution that processes credit and debit card payments with card issuers on behalf of merchants. MultiSafepay is an acquirer for Visa, Mastercard, and Bancontact.

### API endpoint
A specific URL in [our API](/api/) where merchants send requests to exchange information, e.g. about /orders, /gateways.

### backend
The part of a merchant's integration not accessible to customers. Here you can connect with MultiSafepay, configure settings, process refunds, make API requests, and receive notifications.

### collecting party
The party that receives the funds for a transaction directly from the customer, before transferring them to the merchant.

### conversion rate
How often customers visiting a merchant's integration place an order and complete payment.

### customer
A person or company that buys products and services from merchants.

### custom integration
A merchant's bespoke integration with MultiSafepay's services built using [our API](/api), SDKs, or wrappers.

### developer
A software developer a merchant employs to work on the technical side of their integration.

### ecommerce platform
An online [platform](/integrations/ready-made/) merchants use for accepting payments, e.g. website, mobile app, PWAs. 

### fraud
When a person tries to receive products without paying for them by tricking a customer or merchant.

### integration
Software merchants use to sell products and services and accept payments, e.g website, mobile app, [PWA](/payments/integrations/pwa/). Merchants may use [ecommerce platforms](/integrations/ready-made/) or [build their own integration](/integrations/self-made/).

### item
A product or service in a customer's shopping cart and/or order.

### issuer
The customer's bank, which verifies transaction information and sends funds to the collecting party. For credit or debit card payments, the bank issues the card.

### merchant
A company (legal entity) that sells products and services to customers.

### MultiSafepay account
A merchant's account with MultiSafepay, managed via a [web dashboard](https://merchant.multisafepay.com/).

### MultiSafepay balance
The balance of funds held in a MultiSafepay account.

### order
All information related to a single instance of products and/or services sold to a customer that is linked to one or more transactions.

### payment
The industry and the product MultiSafepay sells. For customers: When you confirm to transfer funds. For merchants and collecting parties: when you receive funds.

### payment details
The payment information for a specific customer, e.g. credit card number, CVC code.

### payment gateway
Transfers the customer's payment details to where the payment method is processed.

### payment page
A webpage the customer is redirected to from the merchant's checkout page where they complete payment. The page may be hosted by MultiSafepay (see [Activating MultiSafepay payment pages](/payment-pages/activation/), the issuer, or the payment method. 

### payment service provider (PSP)
MultiSafepay is a PSP and provides services that let merchants accept payments using different payment methods. 

### point of sale (POS) terminal
A terminal that accepts payments, usually by card or near-field communication (NFC), at a merchant's physical location, e.g. a store.

### RESTful API (application programming interface)
The interface and set of protocols merchants use to exchange data with the MultiSafepay server. Our [API reference](https://api-docs.multisafepay.com/reference/introduction) specifies the content and format of requests to our server and the responses the server sends back.

### SEPA
The Single Euro Payments Area (SEPA) is a European Union payment-integration initiative. Customers can quickly and securely transfer euros within the EU and to a number of non-EU countries.

### shopping cart
A container in the merchant's integration where customers place items for an order preparing for payment.

### transaction
An instance of funds being transferred, e.g. customers paying merchants, merchants refunding customers. In our system, the [transaction status](/about-payments/multisafepay-statuses/) changes as the funds move through the different stages of the payment flow.

### we
MultiSafepay

### you
Merchants and developers
