---
title: "Twinfield"
category: 62962dee7af1c800355771a1
order: 207
hidden: false
parentDoc: 629f40cdef2c3001bbd78848
slug: 'twinfield'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Twinfield.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

You can import MultiSafepay [accountant export](/docs/accountant-export/) reports (in MT940 format) into [Twinfield](https://taxnl.wolterskluwer.com/). 

# Prerequisites
You must first provide Twinfield with an additional international bank account number (IBAN). This can be a dummy (placeholder) IBAN.

# Generating dummy IBANs

<details id="generating-dummy-ibans">
<summary>Generating dummy IBANs</summary>
<br>

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** list, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.  
    A dummy IBAN and BIC code are generated.

</details>

# Generating accountant exports

<details id="generating-accountant-exports">
<summary>Generating accountant exports</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Reports** > **Accountant Export**. 
3. In **Data Selection**, select a date range.
4. In the **Report Type** field, select **MT940**.
5. Under **Special Format**, select **Twinfield**.
6. In the **Bank Account / IBAN** field, enter the dummy IBAN.
7. In the **BIC** field, enter the dummy BIC code.

</details >

# Importing into Twinfield

<details id="importing-into-twinfield">
<summary>Importing into Twinfield</summary>
<br>

1. Sign in to your Twinfield account.
2. From the menu, select **Cash & Banks**, and then select **Cash & Banks** again.
3. In the **Code** line, enter an identifier (e.g. MSPAY), and then click **Next**.
4. Fill the following fields:
   - **Account name**
   - **Account number**
   - **BIC**
   - **General ledger account**
   - **IBAN**
7. In **Cash & Banks**, select **Drag and drop bank statements** or **Browse**.
8. Upload the MultiSafepay MT940 file.

</details>

# Free trial

For a free 30-day trial including all accounting functions, see Twinfield – [Proef abonnement aanvragen](https://www.wolterskluwer.com/nl-nl/solutions/twinfield-accounting/twinfield-boekhouden-probeer-nu).

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]