---
title: "Twinfield"
weight: 20
meta_title: "Twinfield - MultiSafepay Docs"
logo: '/svgs/Twinfield.svg'
layout: 'single'
title_short: "Twinfield"
read_more: "."
short_description: "Read about how you can generate a MultiSafepay export and import to your Twinfield platform"
description_short: "Generate MultiSafepay Accountant Export Reports easily and import to your Twinfield bookkeeping system."
aliases:
    - /faq/finance/set-up-twinfield-instructions
    - /faq/finance/setting-up-twinfield/
    - /tools/accounting/accounting-integrations/twinfield/
---

You can import MultiSafepay [accountant export](/accounting/reports/accountant-export/) reports (in MT940 format) into [Twinfield](https://taxnl.wolterskluwer.com/). 

## Prerequisites
You must first provide Twinfield with an additional international bank account number (IBAN). This can be a dummy (placeholder) IBAN.

## Generating dummy IBANs

{{< details title="Generating dummy IBANs">}}

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** list, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.  
    A dummy IBAN and BIC code are generated.

{{< /details >}}

## Generating accountant exports

{{< details title="Generating accountant exports">}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Reports** > **Accountant Export**. 
3. In **Data Selection**, select a date range.
4. In the **Report Type** field, select **MT940**.
5. Under **Special Format**, select **Twinfield**.
6. In the **Bank Account / IBAN** field, enter the dummy IBAN.
7. In the **BIC** field, enter the dummy BIC code.

{{< /details >}}

## Importing into Twinfield

{{< details title="Importing into Twinfield">}}

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

{{< /details >}}

## Free trial

For a free 30-day trial including all accounting functions, see Twinfield – [Proef abonnement aanvragen](https://www.wolterskluwer.com/nl-nl/solutions/twinfield-accounting/twinfield-boekhouden-probeer-nu).

{{< blue-notice >}}**Support** <br> Email support@multisafepay.com {{< /blue-notice >}}