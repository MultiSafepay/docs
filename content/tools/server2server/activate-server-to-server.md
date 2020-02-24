---
title: "Activate Server to Server credit card payments"
weight: 72
meta_title: "Server to Server, how to active it? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

>_Before you proceed with processing direct credit card transactions, check with your account manager at MultiSafepay if you are eligible for the payment method_. 

## Activation and requirements

In order to process direct credit card transactions, the following is required of the merchant:

1. Register for a [MultiSafepay Control](https://merchant.multisafepay.com/signup) account.
2. Make sure you are [PCI](/faq/risk-and-fraud/what-do-i-need-to-know-about-credit-card-payments/) compliant and receive final approval by MultiSafepay Risk Team <screening@multisafepay.com> to enable this feature.
3. Your merchant file and performance of the company will undergo screening and if you have received approval, our Integrations team will begin the integration of Server to Server.
4. Integrate with MultiSafepay via JSON [API](/api/#server-to-server) following the instructions provided in this documentation after our Integrations team have activated the feature for you.
5. Credit card transactions with MultiSafepay accounts are by default 3D secure enabled. Certain MultiSafepay accounts can be totally 3D disabled or can be processed with a 3D Dynamic filter based on a pre-configured set of rules.

>_All options require approval and enabling by our Risk Team_.

## 3D Secure Processing

3D Secure is a protocol designed to reduce fraud and chargebacks during ecommerce Internet transactions. Cardholders are redirected during the payment process to their issuing bank in order to identify themselves before the purchase can be completed. This usually means entering a PIN or a password after entering their card details. In the event of a dispute with the transaction at a later date, the card issuer will usually take responsibility of the chargeback instead of the merchant. This only applies for charges with no authorization and/or fraud, not for situations where the product is not delivered or where customer is dissatisfied with the quality of the order.

The liability issues involved with 3D secure transactions are outside of the scope of this document. For a detailed indication of the liabilities involved, contact our Risk Team at <screening@multisafepay.com>.

>_MultiSafepay only supports Mastercard Secure Code, Verified by Visa, American Express Safekey and Bancontact 3D_.




