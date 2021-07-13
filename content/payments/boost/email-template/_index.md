---
title: 'Email template'
weight: 5
meta_title: "Email template - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "single"
logo: '/svgs/Email_template.svg'
short_description: 'Customize templates to make your customer emails unique'
aliases:
    - /tools/email-template/customizing-email-templates/
    - /tools/email-template/about-email-templates/
    - /tools/email-template/basic-information-on-email-template/
    - /tools/email-template/customizing-email-templates/
    - /tools/email-template/about-email-templates/
    - /tools/email-template
---

To speed up and customize customer emails, you can use preformatted and/or prewritten templates that you populate with relevant content.

**Step 1.** Set an email template.

- Sign in to your MultiSafepay account. 
- Go to **Settings** > **Email templates**.  
- Click the relevant website.  
- Click **Add new template**.   

**Step 2.** From the **Type** dropdown menu, select the template type.  

{{< details title="Template types" >}}

**Bank transfer details email (to customer)**  
For sending customers MultiSafepay's bank details when they select [Bank Transfer](/payments/methods/banks/bank-transfer) as payment method and you send a [`redirect`](/developer/api/difference-between-direct-and-redirect/) transaction request. 

**Chargeback email (to merchant)**  
For notifying you when a customer requests a [chargeback](/payments/methods/credit-and-debit-cards/user-guide/chargebacks/) (recommended if you accept credit card payments).

Make sure you add one or more email addresses to send these emails to in your MultiSafepay account, under 
**Contact information** > **Chargeback email**. 

**Manual capture reservation completed (to customer)**  
For notifying customers that you have manually captured reserved funds for an [Uncleared transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). 

**Manual capture reservation completed (to merchant)**  
For confirming that you have manually captured reserved funds for an [Uncleared transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/).  

**Partial and/or full capture completed (to customer)**  
For notifying customers that you have partially or fully captured reserved funds for an [Uncleared transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). 

**Partial and/or full capture completed (to merchant)**  
For confirming that you have partially or fully captured reserved funds for an [Uncleared transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/).

**Refund complete email (to customer)**  
For notifying customers that you have processed their refund. 

**Second Chance email (to customer)**  
For sending customers a friendly reminder to complete a payment. 

Make sure you have enabled [Second Chance](/payments/boost/second-chance/) in your MultiSafepay account.

**Transaction completed email (to customer)**  
For sending payment confirmation to customers. 

**Transaction completed email (to merchant)**  
For notifying you that a customer has successfully completed a payment.

{{< /details >}}

**Step 3.** To set the email language either select one from the **Language** dropdown menu, or set the locale. 

{{< details title="Setting the locale" >}}

A locale is a set of parameters that defines the user’s language and region for:

- Payment pages
- Emails sent by MultiSafepay

Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes, e.g. 'nl_NL' or 'en_US'.

When no locale is provided or the language is not supported by MultiSafepay, American English is used by default. 

For example, if an email template is set for a German customer, but the locale is received as en_US, the email template will be sent in English and not in German.

{{< /details >}}

**Step 4.** You can click **Load default template** or fill in the fields as required.

- In the **From address** field, enter the email address you want the email sent from.
- In the **From name** field, enter the name you want the email sent by.
- In the **Subject** field, enter a subject.

**Step 5.** You can edit the text in the **Body plain** field, or if you know HTML and CSS, you can fully customize the content and layout in the **Body HTML** field. 

To view the HTML/CSS code, click **Source**.

{{< details title="Adding links" >}}

1. Click the **Link** icon.
2. Select the link type: URL, anchor link, or mail to link
3. Fill in the additional fields as required.
4. Click **OK**. 

{{< /details >}}

{{< details title="Using @tokens@" >}}

To save time, you can use @tokens@ to auto-fill personalized details into emails, e.g.:

- Order amount 
- Customer's first and last name
- Payment method 
- Order description

Follow these steps:

1. Go to the Body HTML editor on the email template page.
2. Click the **Token** icon.
3. Select a token from the dropdown menu.
4. Click **OK**.

{{< /details >}}

{{< details title="Adding your logo" >}}

To add your logo to emails to increase customers' recognition and trust, follow these steps:

1. Sign in to your MultiSafepay account.
2. Upload your logo to [Payment page templates](merchant.multisafepay.com/payment-page-templates).
3. Go to **Settings** > **Email templates**.
4. Click the relevant website.
5. Click the orange pen icon to edit the template.
6. Click the **Image** icon in the first row of the editor.
7. In the **Image properties** window:  
    - Retrieve the link to your uploaded logo.
    - Enter your account ID and the logo filename to the following URL: `media.multisafepay.com/merchants/{accountid}/{filename}`  
    **OR**
    - Go to **Files** where you uploaded the logo. Under **Actions**, click **Copy to clipboard**.
8. In the **URL field**, enter the URL.
9. Edit other parameters as required: height, border, horizontal space, vertical space, and alignment.
10. Click **OK**. 

{{< /details >}}

{{< details title="Adding an inline frame" >}}

Inline frames (Iframes) are HTML documents embedded inside another HTML document, which you can use to insert content from another source into the email template. 

1. Go to the Body HTML editor on the email template page.
2. Click the **Iframe** icon. 
3. In the **Iframe window**, enter the URL of the Iframe.
4. Edit other parameters as required: width, height, alignment, name, and title.
5. Click **OK**. 

{{< /details >}}

**Step 6.** Click **Save**.

For support, email the Integration Team at <integration@multisafepay.com>

