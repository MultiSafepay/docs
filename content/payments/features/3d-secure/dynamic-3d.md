---
title : "Dynamic 3D"
weight: 20
meta_title: "Dynamic 3D - MultiSafepay Docs"
read_more: "."
url: '/features/3d-secure/dynamic/'
aliases:
    - /tools/server2server/3d-dynamics
---
{{< alert-notice >}}MultiSafepay no longer supports Dynamic 3D in Europe due to [PSD2 regulations](/payment-regulations/psd2/). For more information, see [Disabling 3D Secure](/features/3d-secure/about/#disabling-3d-secure).
{{< /alert-notice >}}

[3D Secure](/features/3d-secure/about/) authentication is enabled by default for all credit card payments. 

Dynamic 3D lets you set rules to disable 3D Secure for specific credit card payments, e.g. based on:

- Transaction amount
- Card/customer/IP country

The most common reason for disabling 3D Secure is if you have a lot of customers outside Europe who don't have access to it. Consider setting a rule for transactions with a non-European card and a billing address outside of Europe.

{{< blue-notice >}} **Important:** Removing the layer of security provided by 3D Secure increases the risk of fraud. You bear the risk and become liable for any [fraud-related chargebacks](/payments/chargebacks/). {{< /blue-notice>}}

### Fees
MultiSafepay applies a different fee to non-3D Secure transactions. We may also charge a fee for implementing Dynamic 3D.

## Applying for Dynamic 3D
To apply to use Dynamic 3D, email <sales@multisafepay.com>

- State why you want to use Dynamic 3D.
- Provide evidence that you process a significant volume of transactions for customers outside of Europe.
- Confirm that you understand the increased fraud risk and the fee structure.
- Specify which websites under your account to apply the rule to.
- Show that you have excellent processing performance, especially for chargebacks. 

If approved, we will activate Dynamic 3D at website-level.