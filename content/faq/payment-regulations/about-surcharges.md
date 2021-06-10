---
title : "About surcharges"
weight: 3
meta_title: "FAQ Payment regulations - About surcharges - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/payment-regulations/surcharges
---
{{< blue-notice >}} Check this page regularly for updates on the implementation of the PSD2 directive. {{< /blue-notice >}}   

## Surcharges
Your right to apply [surcharges](/faq/general/multisafepay-glossary/#surcharge) varies by payment method and the customer’s country. 

The PSD2 applies to the whole European Economic Area, but individual states can decide how to implement certain aspects. Always check what rules apply in the country your business is registered in. In the Netherlands, the [Authority for Consumers & Markets (ACM)](https://www.acm.nl) is responsible for PSD2 oversight. The Dutch National Bank recommends always contacting ACM for inquiries. 

### Prohibited transactions
For most transactions, merchants are no longer allowed to charge fees for specific payment methods. 

Surcharges are banned for:

* Most credit card transactions when the bank/card issuer and the merchant's PSP are both located within the European Economic Area (EEA)
* Debit card transactions (for both individuals and business customers)
* Standard bank transfers (for both individuals and business customers)
* SEPA Direct Debit (for both individuals and business customers)

### Exempt payment methods
The following payment methods are exempt from the surcharge prohibition:

* For PayPal and pay-after-delivery (post-payment) methods, merchants can only charge customers for the actual cost the merchant incurs for using the payment method and no more.

* Credit card payments, including American Express and Diners Club, with a card issued outside the EEA, e.g. a tourist with a credit card issued in India

For hybrid card schemes such as American Express and Diners Club, each EU country can decide whether to permit surcharging. Surcharging is permitted under Dutch law.

### Customers outside the EU

The rules for surcharging customers outside the EU remain unchanged. The PSD2 aims to protect European customers.

### Settings changes in your backend and MultiSafepay Control

If you are currently surcharging prohibited transactions:

- You do not need to change any settings in your MultiSafepay Control.
- You may need to update your settings in your backend. 

For support, contact the support department of the webshop plugin or your web developer.

If you don't currently apply any surcharges, you don't need to do anything.

**Disclaimer:** This page is for information only. Given the changing nature of the law, rules, regulations and the risks of electronic communication, this page may contain omissions or inaccuracies. Always seek advice from a professional consultant or competent authority before taking any decision or action. We took the greatest possible care in writing this page, but cannot guarantee its completeness, timeliness, or accuracy. We accept no responsibility for direct or consequential damages resulting from the use of, reliance on, or actions taken based on this page.
