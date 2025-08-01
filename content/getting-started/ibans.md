---
title: "IBANs"
category: 627bbcf80c1c9c0050320b60
order: 5
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'ibans'
---

International bank account numbers (IBANs) are sensitive data. For security reasons, we mask them so that only the last 4 digits are visible, e.g. `*** 1234`.

You can still perform most business operations with masked IBANs, e.g. processing refunds.

# How to unmask IBANs

To unmask IBANs for a specific website, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. Go to **Websites**, and then click the relevant website.
3. Under **Website functionality**, select the **Unmask IBANs in API requests and responses** checkbox.

When unmasked, the full IBAN is displayed, e.g. `NL87ABNA0000001234`.<br />

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