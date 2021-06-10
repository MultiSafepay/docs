---
title : "Setting up Twinfield"
meta_title: "FAQ Finance - Setting up Twinfield - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/finance/set-up-twinfield-instructions
---

You can export MultiSafepay MT940 accountant reports from your MultiSafepay Control and import them into your Twinfield account. 

You must first provide Twinfield with an additional international bank account number (IBAN). This can be a _dummy_, or placeholder, IBAN.

## Generating dummy IBANs

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** drop-down menu, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.
6. A dummy IBAN and BIC code are generated.

## Exporting from MultiSafepay Control

1. In your MultiSafepay Control, navigate to **Reports** > **Accountant Export**. 
2. In **Data Selection**, select a date range.
3. In the **Report Type** field, select **MT940**.
4. Under **Special Format**, select **Twinfield**.
5. In the **Bank Account / IBAN** field, enter the dummy IBAN.
6. In the **BIC** field, enter the dummy BIC code.

## Importing into Twinfield

1. Log in to your Twinfield account.
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
