---
title : "Surcharges"
weight: 40
meta_title: "Surcharges - MultiSafepay Docs"
read_more: "."
short_description: "About surcharges and European regulations."
url: '/surcharges/'
layout: single
logo: '/svgs/General.svg'
aliases:
    - /faq/payment-regulations/surcharges
    - /faq/payment-regulations/about-surcharges
    - /security-and-legal/payment-regulations/about-surcharges/
    - /about-payments/surcharges/
---
{{< blue-notice >}} Check this page regularly for updates on implementing the PSD2. {{< /blue-notice >}}   

A surcharge is a fee merchants may charge customers on top of the total order amount to cover the cost of accepting certain payment methods. This may be a fixed amount or a percentage of the total order amount.

Your right to apply surcharges varies per payment method and the customer’s country. 

## PSD2

The PSD2 applies to the whole European Economic Area (EEA), but individual states can decide how to implement certain aspects. Always check what rules apply in the country your business is registered in. 

In the Netherlands, the [Authority for Consumers & Markets (ACM)](https://www.acm.nl) is responsible for PSD2 oversight. The Dutch National Bank recommends always contacting ACM for inquiries. 

## Surcharges prohibited

Surcharges are banned for both individual and business customers on:

- Most credit card transactions when the bank/card issuer and the merchant's PSP are both located within the EEA
- Debit card transactions 
- Standard bank transfers 
- SEPA Direct Debit payments 

If you are currently surcharging prohibited transactions, you may need to update your settings in your backend. For support, contact your ecommerce platform or your developer. 
You do **not** need to change any settings in your MultiSafepay dashboard.

## Surcharges permitted

Surcharges are permitted for:

- Card payments with cards issued outside the EEA, e.g. a tourist with a credit card issued in India

- Hybrid card schemes such as American Express: Each EU state can decide whether to permit surcharging. Under Dutch law, surcharges **are** permitted.

- [PayPal](/payment-methods/paypal) and [pay later methods](/payment-methods/pay-later/): You can only charge customers for the actual cost you incur for using the payment method and no more.

{{< alert-notice >}}**Attention Dutch merchants** <br> Due to changes to the Wet op het consumentenkrediet, Dutch merchants who apply surcharges to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM). <br> We therefore strongly recommend **not** applying surcharges. <br> For more information, email <sales@multisafepay.com>  {{< /alert-notice >}}

| |
|---|
| **Disclaimer:** This page is for information only. <br> Given the changing nature of the law, rules, regulations and the risks of electronic communication, this page may contain omissions or inaccuracies. We took great care in writing it, but cannot guarantee its completeness, timeliness, or accuracy. <br> Always seek advice from a professional consultant or competent authority before taking any decision or action. <br> We accept no responsibility for direct or consequential damages resulting from the use of, reliance on, or actions taken based on this page. |
