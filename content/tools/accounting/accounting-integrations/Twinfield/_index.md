---
title: "Twinfield"
weight: 20
meta_title: "Twinfield - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/Twinfield.svg'
layout: 'single'
title_short: "Twinfield"
read_more: "."
short_description: "Read about how you can generate a MultiSafepay export and import to your Twinfield platform"
description_short: "Generate MultiSafepay Accountant Export Reports easily and import to your Twinfield bookkeeping system."
extra_button:
    url: "https://taxnl.wolterskluwer.com/" 
    text: "Go to site" 
    type: "primary"
aliases:
    - /faq/finance/set-up-twinfield-instructions
    - /faq/finance/setting-up-twinfield/
---

You can export MT940 accountant reports from your MultiSafepay account and import them into your Twinfield account. 

You must first provide Twinfield with an additional international bank account number (IBAN). This can be a _dummy_, or placeholder, IBAN.

## Generating dummy IBANs

To generate a dummy IBAN, follow these steps:

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** drop-down menu, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.
6. A dummy IBAN and BIC code are generated.

## Exporting from your MultiSafepay account
To export a MT940 accountant report from your MultiSafepay account, follow these steps:

1. Sign in to your MultiSafepay account.
2. Go to **Reports** > **Accountant Export**. 
3. In **Data Selection**, select a date range.
4. In the **Report Type** field, select **MT940**.
5. Under **Special Format**, select **Twinfield**.
6. In the **Bank Account / IBAN** field, enter the dummy IBAN.
7. In the **BIC** field, enter the dummy BIC code.

## Importing into Twinfield
To import at MT940 report into Twinfield, follow these steps:

1. Sign in to your Twinfield account.
2. From the menu, select **Cash & Banks**.
3. Select **Cash & Banks** again.
4. In the **Code** line, enter an identifier, e.g. MSPAY.
5. Click **Next**.
6. Fill the following fields:
   - **Account number**
   - **Account name**
   - **IBAN**
   - **BIC**
   - **General ledger account**
7. In **Cash & Banks**, select **Drag and drop bank statements or Browse**.
8. Upload the MultiSafepay MT940 file.

For any questions, email the Support Team at <support@multisafepay.com>

For a free 30-day trial including all accounting functions, see Twinfield - [Proef abonnement aanvragen](https://e.wolterskluwer.com/proefabonnement-aanvragen).

