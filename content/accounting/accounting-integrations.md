---
title: "Accounting integrations"
category: 62962dee7af1c800355771a1
order: 100
hidden: false
slug: 'accounting-integrations'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/actuals-io.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Actuals

[Actuals](https://actuals.io/) imports new transactions daily, between 02:00 AM and 05:00 AM (CET/CEST).

<details id="how-to-integrate">
<summary>How to integrate</summary>
<br>

To connect your Actuals account to your MultiSafepay account:

1. Sign in to your [Actuals account](https://live.actuals.io).
2. Go to **Configuration**.
3. Under **Payment service provider** > **MultiSafepay**, click **Add**.
4. In the **Configuration name** field, rename the configuration, if relevant.
5. In the **MultiSafepay API Key** field, enter your MultiSafepay [site API key](/docs/sites#site-id-api-key-and-secure-code), and then click **Save**.
6. To check the connection, go to **Configuration**.
7. Under **In-use sources**, check that the **Status** of your MultiSafepay configuration is **Live**.

</details>

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/AFAS.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# AFAS

[AFAS](https://www.afas.nl/) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format).

For import instructions, see AFAS – [Contact](https://www.afas.nl/contact).

## Forque
For generating automated accounting reports, see Forque – [AFAS](https://www.forque.nl/afas-consultancy).

## De Viske ICT
For middleware solutions to automate processes and efficiently exchange data between AFAS and other applications, see De Viske ICT – [Applicaties](https://deviske.nl/applicaties/).

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/E-boekhouden.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# e-Boekhouden

[e-Boekhouden](https://www.e-boekhouden.nl/koppelingen/payment-service-providers/multisafepay?qsm=387) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 or CSV format).

For import instructions, see e-Boekhouden – [Contact](https://www.e-boekhouden.nl/contact).

To add MultiSafepay [payment links](/docs/payment-links/) to e-Boekhouden invoices to let customers pay directly, see e-Boekhouden – [How do I insert a payment link or image in my invoices](https://secure.e-boekhouden.nl/bh/kb.asp?ACTION=SHOW&ID=237&POPUP=1).

## PSP Betalingen integration

PSP Betalingen has developed an integration that connects your MultiSafepay account to e-Boekhouden, continually importing your transactions so you can automate reconciliation.

For more information, see PSP Betalingen – [Koppeling MultiSafepay e-Boekhouden](https://www.webwinkelfacturen.nl/koppelingpsp.php?shopsystem=multisafepay&invoicesystem=eboekhouden).

To connect your MultiSafepay account to e-Boekhouden, see PSP betalingen – [Handleiding: MultiSafepay e-Boekhouden](https://handleidingen.pspbetalingen.nl/handleiding-multisafepay-eboekhouden). (You will need a MultiSafepay [site API key](/docs/sites#site-id-api-key-and-secure-code).)

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Exact.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Exact

[Exact](https://www.exact.com/nl) Globe or Online support MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format). 

<details id="prerequisites">
<summary>Prerequisites</summary>
<br>

-  Exact Basic / Standard package doesn't support the MT940 import function. You need at least Exact Advanced.  
- Lightspeed users must request Lightspeed to make an adjustment to make sure order numbers appear in the correct fields in Exact Online to successfully match the MultiSafepay MT940.
- Exact Globe and Exact Online both import and match MultiSafepay MT940 reports provided that:
    - Your accounting package can process MT940 files.
    - The order numbers in the MT940 files also appear in the correct invoice fields in your accounting platform.
    - The customer's name and order amounts that appear in the exported MT940 files match your accounting platform.

</details>

1. You must first provide Exact with an additional international bank account number (IBAN). This can be a dummy (placeholder) IBAN. 

    <details id="how-to-generate-dummy-ibans">
    <summary>How to generate dummy IBANs</summary>
    <br>

    1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
    2. From the **Country** list, select **The Netherlands**.
    3. Under **Bank Code**, enter a bank, e.g. ING Group.
    4. In the **Account number** field, enter any 7 digits.
    5. Click **Calculate IBAN**.  
    A dummy IBAN and BIC code are generated.

    </details >

2. Submit the IBAN to:

    <details id="exact-globe">
    <summary>Exact Globe</summary>
    <br>

    1. Sign in and go to **Bank accounts**.
    2. Click **New**.
    3. Under **Type**, select **Payment service provider**. 
    4. Enter the dummy IBAN and select the same bank as before, e.g. ING Group.
    5. Click **Save**.  
        You can now register all transactions linked to this IBAN.

    </details>

    <details id="exact-online">
    <summary>Exact Online</summary>
    <br>

    1. Sign in and go to **Financial** > **Banking & Cash** > **Bank accounts** > **Overview**.
    2. Click **New**.
    3. Enter your dummy IBAN, and then click **Save**.  
        You can now register all transactions linked to this IBAN.

    </details>

3. Export a MT940 accountant export from your MultiSafepay dashboard.

    <details id="how-to-generate-accountant-exports" >
    <summary>How to generate accountant exports</summary>
    <br>

    1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
    2. Go to **Reports** > **Accountant Export**:  
        - In **Data Selection**, select a date range.
        - In the **Report Type** field, select **MT940**.
    3. Click **Advanced options**:
        - In the **Bank Account / IBAN** field, enter the dummy IBAN.
        - In the **BIC** field, enter the dummy BIC code.

    </details>

4. Import the MT940 accountant export into Exact Online.

    <details id="how-to-import-into-exact-online">
    <summary>How to import into Exact Online</summary>
    <br>

    1. Sign in to your Exact Online account.
    2. Go to **Financial** > **Banking & Cash** > **Statements** > **Import**.
    3. Click **Choose File**, and then select the MT940 file you want to upload.
    4. Click **Import**.

    </details>

## Denovit integration

You can automatically insert MultiSafepay [payment links](/docs/payment-links/) into Exact invoices using the [Denovit payment link module](https://www.denovit.nl/Exact-PaymentLink).

<details id="how-to-set-up-denovit">
<summary>How to set up Denovit</summary>
<br>

1. Sign in to your Denovit account.
2. Go to your **Dashboard**, and then select the **Paylink** module. 
3. Connect to your Exact account.
4. Under **PSP settings**, enter your [MultiSafepay API key](/docs/sites#site-id-api-key-and-secure-code) and the payment conditions you use in Exact. 
5. Adjust other settings as relevant, e.g. personalize your email template, thank-you page, or notification email to improve customer experience.

For each new invoice in Exact, if you:

- **Email**: The customer receives a second email containing a payment link, in addition to the normal email.
- **Print and process**: The customer receives an email containing a payment link.

</details >

## xCore integration

Automatically reconciling sales from your site with payments received via MultiSafepay saves time and increases accuracy.

xCore offers two reconciliation apps for Exact accounting tools. The apps automatically retrieve the details of all payments for the day from MultiSafepay, and then match each payment to the corresponding open item in Exact.

<details id="exact-online">
<summary>Exact Online</summary>
<br>

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FMc6_ZV1AoT8%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DMc6_ZV1AoT8&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FMc6_ZV1AoT8%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=Mc6_ZV1AoT8&feature=youtu.be",
  "title": "Demo - MultiSafepay Aflettermodule Exact Online xCore",
  "favicon": "https://www.youtube.com/s/desktop/d4eb50c8/img/favicon.ico",
  "image": "https://i.ytimg.com/vi/Mc6_ZV1AoT8/hqdefault.jpg"
}
[/block]
<br>

For more information, see xCore – [Afletteren 2.0 Exact Online with MultiSafepay](https://xcore.nl/afletteren-2-0-exact-online-multisafepay/).

</details>

<details id="exact-globe">
<summary>Exact Globe</summary>
<br>

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fa74k2vJVhxQ%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Da74k2vJVhxQ&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fa74k2vJVhxQ%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=a74k2vJVhxQ&feature=youtu.be",
  "title": "Demo - Afletteren Exact Globe",
  "favicon": "https://www.youtube.com/s/desktop/d4eb50c8/img/favicon.ico",
  "image": "https://i.ytimg.com/vi/a74k2vJVhxQ/hqdefault.jpg"
}
[/block]
<br>

For more information, see xCore – [Afletteren MultiSafepay met Exact Globe](https://xcore.nl/afletteren-exact-globe-multisafepay/).

</details>

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/King.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# King Business Software

[King Business Software](https://www.kingconnections.eu/MultiSafePay) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format).

For import instructions, see King Business Software – [Service](https://service.king.eu).

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Snelstart.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Snelstart

[Snelstart](https://www.snelstart.nl) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format).

For import instructions, see Snelstart – [Klantenservice](https://www.snelstart.nl/klantenservice).

To add MultiSafepay [payment links](/docs/payment-links/) to SnelStart invoices to let customers pay directly, see SnelKoppeling – [Betaallinks via payment service provider](https://snelkoppeling.eu/productoverzicht/boekhoudtechnisch/emailplus).

### Premarc plugins

[Premarc](https://www.snelkoppeling.eu/productoverzicht/webwinkelkoppelingen) offers plugins to reconcile Snelstart with popular ecommerce platforms.

<details id="supported-ecommerce-platforms">
<summary>Supported ecommerce platforms</summary>
<br>

- [CCVshop](https://www.snelkoppeling.eu/ccvshop)
- [Lightspeed](https://www.snelkoppeling.eu/lightspeed)
- [Magento](https://www.snelkoppeling.eu/magento)
- [Shopify](https://www.snelkoppeling.eu/shopify)
- [Woocommerce](https://www.snelkoppeling.eu/woocommerce)

</details>

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Twinfield.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Twinfield

[Twinfield](https://taxnl.wolterskluwer.com/) supports MultiSafepay [accountant exports](/docs/reports#accountant-exports) (MT940 format). 

You must first provide Twinfield with an additional international bank account number (IBAN). This can be a dummy (placeholder) IBAN.

<details id="how-to-generate-dummy-ibans">
<summary>How to generate dummy IBANs</summary>
<br>

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** list, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.  
    A dummy IBAN and BIC code are generated.

</details>

<details id="how-to-import">
<summary>How to import</summary>
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

> **Tip!** For a free 30-day trial including all accounting functions, see Twinfield – [Proef abonnement aanvragen](https://www.wolterskluwer.com/nl-nl/solutions/twinfield-accounting/twinfield-boekhouden-probeer-nu).

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Unit4.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Unit4

[Unit4](https://accountancygemak.nl/) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format).

For import instructions, see Unit4 – [Support](https://accountancygemak.nl/support/).

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Visma.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Visma

[Visma](https://nl.visma.com/) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 and CAMT053 formats).

For import instructions, see Visma – [Contact](https://nl.visma.com/accountview-support/contact).

---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Yuki.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

# Yuki

[Yuki](https://www.yuki.nl/nl/) supports MultiSafepay [accountant exports](/docs/reports#accountant-export) (MT940 format).

<details id="how-to-import">
<summary>How to import</summary>
<br>

1. Sign in to your Yuki domain ending in **@yukiworks.be**.
2. Go to **Yuki Postbus** > **Submit**.
3. Click **Upload**, and select the relevant MT940 file, or choose one of the other upload methods.

For more information, see Yuki - [Upload files from PO box](https://support.yuki.nl/en/support/solutions/articles/80000786497-upload-files-from-po-box).

</details >

<details id="how-to-reconcile-automatically">
<summary>How to reconcile automatically using bank recognition rules</summary>
<br>

1. Go to **Bank transactions to be processed** > **(New) Processing rule**.
2. Create a new rule. 

For more information, see Yuki - [Create bank processing rule](https://support.yuki.nl/nl/support/solutions/articles/80000787813-bank-verwerkingsregel-aanmaken).

</details >

### Duopact integration

[Duopact](https://www.snelkoppeling.eu/productoverzicht/webwinkelkoppelingen) imports MultiSafepay transactions automatically daily at midnight.

<details id="how-to-integrate" >
<summary>How to integrate</summary>
<br>

To connect Duopact with your MultiSafepay account, see Duopact – [Contact](https://www.duopact.nl/nl/contact/).  

Provide Duopact with your MultiSafepay [site API key](/docs/sites#site-id-api-key-and-secure-code). They will set up a Yuki account for you. 

</details >

<details id="how-to-manually-import-transactions" >
<summary>How to manually import transactions</summary>
<br>

1. Sign in to your [Duopact account](https://portal.yukiconnector.nl/).
2. If you operate multiple sites, select the relevant site from the top-left menu.
3. Go to **Bankmutaties** > **MultiSafepay**.
4. Click the green button under the **Status** tab.

> **Note:** Manually importing transactions doesn't affect automatic imports.

</details>

<br>

---

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
