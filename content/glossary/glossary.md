---
title: "Glossary"
category: 64f71308dd215a026fa77609
order: 0
hidden: false
slug: 'glossary'
---
#### account balance
The balance of funds held in a MultiSafepay account.

---
#### acquirer
A financial institution that processes card payments with issuers on behalf of merchants. MultiSafepay is an acquirer for Visa, Mastercard, and Bancontact.

---
#### acquirer reference number (ARN)
A unique number assigned to card payments as they move from the merchant's bank (acquiring bank) to the cardholder's bank (issuer). Banks can use ARNs to trace refunds.

---
#### affiliated merchant (affiliate)
A merchant (a legal entity that sells products and services to customers) managed by a partner account.

---
#### API endpoint
A specific URL in [our API](/reference/) where merchants send requests to exchange information, e.g. about /orders, /gateways.

---
#### backend
The part of a merchant's integration not accessible to customers. Here you can connect with MultiSafepay, configure settings, process refunds, make API requests, and receive notifications.

---
#### BNPL
Buy now pay later methods let customers pay for their <<glossary:order>> after receiving it, and only for the items they keep. 

---
#### cardholder
A customer who uses a card issued by a bank to make cashless payments to a merchant.

---
#### card scheme
A financial institution that issues credit or debit cards, provides infrastructure, and processes payments for a fee, e.g. Visa, Mastercard, American Express.

---
#### card verification code (CVC)
A 3 or 4 digit code customers enter as an additional layer of security for online credit or debit card payments. Not required for all cards, or for [recurring payments](/docs/recurring-payments/).

---
#### collecting party
The party that receives the funds for a <<glossary:transaction>> directly from the customer, before transferring them to the merchant.

---
#### conversion rate
How often customers visiting a merchant's integration place an <<glossary:order>> and complete payment.

---
#### credit card
A card issued by a bank, building society, or card scheme that lets the holder pay for products or services on credit.

---
#### customer
A person or company that buys products and services from merchants.

---
#### debit card
A card issued by a bank that transfers funds directly from the customer's bank account.

---
#### developer
A software developer a merchant employs to work on the technical side of their integration.

---
#### direct flow
The customer selects the payment method in your embedded checkout and is connected directly to the payment method. Contrast with [redirect flow](#redirect-flow) below.

---
#### domestic transactions
A transaction occurring where the issuer and merchant are registered in the same country.

---

#### ecommerce platform
An online [platform](/docs/our-integrations/) merchants use for accepting payments, e.g. website, mobile app, PWAs. 

---
#### fraud
When a person tries to receive products without paying for them by tricking a customer or merchant.

---
#### integration
Software merchants use to sell products and services and accept payments, e.g website, mobile app, [PWA](/docs/pwa-studio-venia/). Merchants may use [ecommerce platforms](/docs/our-integrations/) or [build their own integration](/docs/api-integration/).

---
#### item
A product or service in a customer's shopping cart and/or order.

---
#### issuer
The customer's bank, which verifies transaction information and sends funds to the collecting party. For credit or debit card payments, the bank issues the card.

---
#### know your customer (KYC)
As a payment service provider and acquirer, MultiSafepay is legally required to perform KYC checks on the merchant and their website, business bank account, and the account holder.

---
#### merchant
A company (legal entity) that sells products and services to customers.

---
#### merchant of record
A legal entity that sells goods or services to an end customer, who must pay the merchant for their order. The merchant handles all payments and assumes liability for each transaction.

---
#### MultiSafepay account
A merchant's account with MultiSafepay, managed via a <a href="https://merchant.multisafepay.com/" target="_blank">web dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

---
#### order
A data element that contains all information about a single instance of products and/or services sold to a customer, which is linked to one or more transactions.

---
#### payment
The industry and the product MultiSafepay sells.  
- For customers: When you confirm to transfer funds
- For merchants and collecting parties: When you receive funds

---
#### payment details
The payment information for a specific customer, e.g. card number, CVC code.

---
#### payment gateway
Transfers the customer's payment details to where the payment method is processed.

---
#### payment page
A webpage the customer is redirected to from the merchant's checkout where they complete payment. The page may be hosted by MultiSafepay (see [payment pages](/docs/payment-pages/), the issuer, or the payment method. 

---
#### payment service provider (PSP)
MultiSafepay is a PSP and provides services that let merchants accept payments using different payment methods. 

---
#### payout
When you transfer funds from your account balance to your business bank account.
See [Payouts](/docs/payouts).

---
#### point of sale (POS) terminal
A terminal that accepts payments, usually by card or near-field communication (NFC), at a merchant's physical location, e.g. a store.

---
#### redirect flow
Redirect requests first send the customer to a [payment page](/docs/payment-pages/) and then connect them to the selected payment method.

---
#### RESTful API (application programming interface)
The interface and set of protocols merchants use to exchange data with the MultiSafepay server. Our [API reference](/reference/introduction/) specifies the content and format of requests to our server and the responses the server sends back.

---
#### reversal
When a customer cancels an <<glossary:order>> paid by credit or debit card and takes the funds back.

---
#### SEPA
The Single Euro Payments Area (SEPA) is a European Union payment-integration initiative. Customers can quickly and securely transfer euros within the EU and to a number of non-EU countries.

---
#### settlement
When MultiSafepay collects the funds for a transaction and puts them in your account balance.
To withdraw funds, make a [payout](/docs/payouts).

---
#### shopping cart
A container in the merchant's integration where customers place items for an <<glossary:order>> preparing for payment.

---
#### transaction
An instance of funds being transferred, e.g. customers paying merchants, merchants refunding customers. In our system, the <<glossary:transaction status>> changes as the funds move through the different stages of the payment flow.

---
### pre-transaction
The initial stage in the payment process, before a transaction is fully processed. This may involve authorization or reservation of funds, but no funds are transferred yet.

---
#### we
MultiSafepay

---
#### you
Merchants, partners, and developers

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)