---
title: "Yuki"
category: 62962dee7af1c800355771a1
order: 210
hidden: false
parentDoc: 629f40cdef2c3001bbd78848
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Yuki.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

This page sets out ways of integrating MultiSafepay with [Yuki](https://www.yuki.nl/nl/).

# Importing accountant exports

You can import MultiSafepay [accountant export](/accounting/reports/accountant-export/) reports (in MT940 format) into Yuki.

<details id="importing-accountant-exports">
<summary>Importing accountant exports</summary>
<br>

1. Sign in to your Yuki domain ending in **@yukiworks.be**.
2. Go to **Yuki Postbus** > **Submit**.
3. Click **Upload**, and select the relevant MT940 file, or choose one of the other upload methods.

For more information, see Yuki - [Upload files from PO box](https://support.yuki.nl/en/support/solutions/articles/80000786497-upload-files-from-po-box).

</details >

# Automating reconciliation

<details id="reconciling-automatically-using-bank-recognition-rules">
<summary>Reconciling automatically using bank recognition rules</summary>
<br>

1. Go to **Bank transactions to be processed** > **(New) Processing rule**.
2. Create a new rule. 

For more information, see Yuki - [Create bank processing rule](https://support.yuki.nl/nl/support/solutions/articles/80000787813-bank-verwerkingsregel-aanmaken).

</details >

# Duopact integration

You can also integrate with [Duopact](https://www.snelkoppeling.eu/productoverzicht/webwinkelkoppelingen). MultiSafepay transactions are automatically imported daily at midnight.

<details id="connect-duopact-with-multiSafepay" >
<summary>Connect Duopact with MultiSafepay</summary>
<br>

To connect Duopact with your MultiSafepay account, see Duopact – [Contact](https://www.duopact.nl/nl/contact/).  

Provide Duopact with your MultiSafepay [site API key](/websites/#site-id-api-key-and-secure-code). They will set up a Yuki account for you. 

</details >

<details id="manually-importing-transactions" >
<summary>Manually importing transactions</summary>
<br>

1. Sign in to your [Duopact account](https://portal.yukiconnector.nl/).
2. If you operate multiple websites, select the relevant site from the top-left menu.
3. Go to **Bankmutaties** > **MultiSafepay**.
4. Click the green button under the **Status** tab.

> **Note:** Manually importing transactions doesn't affect automatic imports.

</details>

> 💬  Support
> Email <support@multisafepay.com>
