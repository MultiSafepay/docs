---
title: "Surcharges"
category: 627bbcf80c1c9c0050320b60
order: 9
hidden: false
parentDoc: 62a087abb10eb40052c9fd04
slug: 'surcharges'
---
> ℹ ### ​Check this page regularly for updates on implementing the PSD2.

A surcharge is a fee merchants may charge customers on top of the total order amount to cover the cost of accepting certain payment methods. This may be a fixed amount or a percentage of the total order amount.

Your right to apply surcharges varies per payment method and the customer’s country.

# PSD2

The [PSD2](/docs/psd2/) applies to the whole European Economic Area (EEA), but individual states can decide how to implement certain aspects. Always check what rules apply in the country your business is registered in.

In the Netherlands, the <a href="https://www.acm.nl" target="_blank">Authority for Consumers & Markets (ACM)</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is responsible for PSD2 oversight. The Dutch National Bank recommends always contacting ACM for inquiries.

# Prohibited surcharges

Surcharges are banned for both individual and business customers on:

* Most card transactions when the bank/card <Glossary>issuer</Glossary> and the merchant's <Glossary>PSP</Glossary> are both located within the EEA
* Debit card transactions
* Standard bank transfers
* Direct debits

If you are currently surcharging prohibited transactions, you may need to update your settings in your <Glossary>backend</Glossary>. For support, contact your ecommerce platform or your developer. You do **not** need to change any settings in your MultiSafepay dashboard.

# Permitted surcharges

Surcharges are permitted for:

* Card payments with cards issued outside the EEA, e.g. a tourist with a card issued in India
* Hybrid <Glossary>card schemes</Glossary> such as American Express: Each EU state can decide whether to permit surcharging. Under Dutch law, surcharges **are** permitted.
* [PayPal](/docs/paypal/) and <Glossary>BNPL</Glossary> methods: You can only charge customers for the actual cost you incur for using the payment method and no more.
* Amazon Pay

<br />

> ⚠️ **Attention Dutch merchants**
>
> Due to changes to the Wet op het consumentenkrediet, Dutch merchants who apply surcharges to <Glossary>BNPL</Glossary> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM). We therefore strongly recommend **not** applying surcharges.<br />

> ❕ ### **Disclaimer**
>
> This page is for information only. Given the changing nature of the law, rules, regulations and the risks of electronic communication, this page may contain omissions or inaccuracies. We took great care in writing it, but cannot guarantee its completeness, timeliness, or accuracy. Always seek advice from a professional consultant or competent authority before taking any decision or action. We accept no responsibility for direct or consequential damages resulting from the use of, reliance on, or actions taken based on this page.<br />

***

<HTMLBlock>{`
<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>
`}</HTMLBlock>

[Top of page](#)