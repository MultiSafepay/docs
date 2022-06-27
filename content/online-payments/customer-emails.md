---
title: 'Customer emails'
category: 6278c92bf4ad4a00361431b0
order: 10
hidden: false
slug: 'customer-emails'
excerpt: "Customize email templates to match your brand's look and feel."
---
MultiSafepay can help you manage your email communications with customers. Use our preformatted and/or prewritten templates and populate them with your content.

# How to customize emails

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com). 
2. Go to **Settings** > **Email templates**.  
3. Click the relevant site.  
4. Click **Add new template**.   
5. From the **Type** list, select the template type.  

    <details id="template-types">
    <summary>Template types</summary>
    <br>

    **Bank Transfer details email (to customer)**  
    For sending customers MultiSafepay's bank details when they select [Bank Transfer](/docs/bank-transfer/) as payment method and you send a [`redirect`](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) transaction request. 

    **Chargeback email (to merchant)**  
    For notifying you when a customer requests a [chargeback](/docs/chargebacks/) (recommended if you accept credit card payments).

    Make sure you add one or more email addresses to send these emails to in your MultiSafepay dashboard, under 
    **Contact information** > **Chargeback email**. 

    **Manual Capture reservation completed (to customer)**  
    For notifying customers that you have manually captured reserved funds for an [uncaptured transaction](/docs/uncaptured/). 

    **Manual Capture reservation completed (to merchant)**  
    For confirming that you have manually captured reserved funds for an [uncaptured transaction](/docs/uncaptured/).  

    **Partial and/or full capture completed (to customer)**  
    For notifying customers that you have partially or fully captured reserved funds for an [uncaptured transaction](/docs/uncaptured/). 

    **Partial and/or full capture completed (to merchant)**  
    For confirming that you have partially or fully captured reserved funds for an [uncaptured transaction](/docs/uncaptured/).

    **Refund complete email (to customer)**  
    For notifying customers that you have processed their refund. 

    **Second Chance email (to customer)**  
    For sending customers a friendly reminder to complete a payment. 

    Make sure you have enabled [Second Chance](/docs/second-chance/) in your MultiSafepay dashboard.

    **Transaction completed email (to customer)**  
    For sending payment confirmation to customers. 

    **Transaction completed email (to merchant)**  
    For notifying you that a customer has successfully completed a payment.

    </details>

6. From the **Language** list, select the email language.  
    **Note:** The language set here is overridden by the `locale` parameter in [create order](https://docs-api.multisafepay.com/reference/createorder) API requests. 
7. Either click **Load default template**, or fill in the fields as required.
    - In the **From address** field, enter the email address you want the email sent from, e.g. sales@yourcompany.com
    **Note:** If you enter a different from address than noreply@multisafepay.com to avoid emails being marked as spam, we recommend adding the following DNS record to your domain:  
    **v=spf1 ip4:213.189.0.0/23 ip4:185.99.128.0/22 mx**
    - In the **From name** field, enter the name you want the email sent by, e.g. your company name.
    - In the **Subject** field, enter a subject.  

8. Edit the text **either** in the **Body plain** field, **or** if you know HTML and CSS, you can fully customize the content and layout in the **Body HTML** field. To view the HTML/CSS code, click **Source**.

    <details id="how-to-add-links">
    <summary>How to add links</summary>
    <br>

    1. Click the **Link** icon.
    2. Select the link type: URL, anchor link, or mail to link
    3. Fill in the additional fields as required, and then click **OK**. 

    </details>

    <details id="how-to-use-tokens">
    <summary>How to use tokens</summary>
    <br>

    To save time, you can use @tokens@ to auto-fill personalized details into emails.

    1. Go to the Body HTML editor on the email template page, and then click the **Token** icon.
    2. Select a token from the list, and then click **OK**.

    The table below describes all available tokens.

    | Tags                          |     Result    |      
    | ----------------------------- | ------------- | 
    | ACCOUNT                       | Account_id of FastCheckout customer |   
    | ACCOUNTADDRESS                | Customer address and street name   |  
    | ACCOUNTADDRESSAPARTMENT       | Customer house number |
    | ACCOUNTCITY                   | Customer city of residence |
    | ACCOUNTCOUNTRY                | Customer country of residence |
    | ACCOUNT EMAIL                 | Customer email address |
    | ACCOUNTFIRSTNAME              | Customer first name |
    | ACCOUNTLASTNAME               | Customer last name |
    | ACCOUNTNR                     | Your MultiSafepay AccountID |
    | ACCOUNTZIPCODE                | Customer zip code |
    | ADDRESS1                      | Your company address line 1 |
    | ADDRESS2                      | Your company address line 2 |
    | ADDRESS3                      | Your company address line 3 |
    | BANKHOLDERNAME                | Account holder used by the customer to process bank transfer transactions |
    | BANKIBAN                      | IBAN used by the customer to process bank transfer transactions |
    | BANKPAYMENTID                 | Reference used by the customer to process bank transfer transactions |
    | BANKTRANSFERBIC               | BIC used by the customer to process bank transfer transactions |
    | BANKTRANSFERHOLDER            | Account holder name of IBAN to receive the money |
    | BANKTRANSFERID                | Reference used with the bank transfer |
    | BIRTHYDAY                     | Customer date of birth |
    | CITY                          | Your company city of residence |
    | COMPANYNAME                   | Your company name given in your MultiSafepay account |
    | CONTENT                       | Shopping cart info |
    | COUNTRY                       | [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) code for your company country |
    | COUNTRYCODE                   | [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) code for your company country |
    | CURRENTDATE                   | Today's date |
    | DESCRIPTION                   | AccountID to receive money |
    | DESTAMOUNT                    | Amount to be received |
    | DESTAMOUNTFORMATCUR           | Amount including currency to be paid by the customer via bank transfer transactions |
    | DESTCURRENCY                  | Currency of amount to be received |
    | DESTFORMATAMOUNTCUR           | Currency and amount to be paid out |
    | EMAIL                         | Customer email address |
    | FINANCIAL EMAIL               | Email address for financial email |
    | FIRSTNAME                     | Customer first name and email address set as sender for emails |
    | FROMNAME                      | Name of the sender's email account |
    | GENDER                        | Customer gender |
    | LASTNAME                      | Customer last name |
    | MERCHANTCITY                  | Your company city of residence |
    | MERCHANTCOUNTRY               | Your company country of residence  |
    | MERCHANTLOGOHTML              | HTML code for your logo |
    | MERCHANTNAME                  | Your company full name |
    | MERCHANTPHONESUPPORT          | Your customer service phone number |
    | MERCHANTSUPPORT EMAIL         | Your customer service email address |
    | MERCHANTTRANSACTIONID         | Your reference number |
    | PAYLINK                       | Link to the [payment page](/docs/payment-pages/) for this transaction |
    | PAYMENTMETHOD                 | Payment method used for this transaction |
    | PHONE                         | Your company phone number given in your MultiSafepay account |
    | REFUNDDESTINATION             | Bank account number to receive the refund |
    | REPORT EMAIL                  | Email address to receive report emails |
    | SITENAME                      | Nname of your webshop given in your MultiSafepay account |
    | SITEURL                       | URL of your webshop given in your MultiSafepay account |
    | STATE                         | Province or state within the country |
    | STATUS                        | <<glossary:Transaction status>> |
    | SUBJECT                       | Subject of the email |
    | TOTALAMOUNT                   | Total of the order |
    | TRANSACTIONID                 | MultiSafepay PSP ID |
    | TRANSCOMP EMAIL               | Email address to receive transaction completed mails |
    | VARA                          | var1 from your transaction request |
    | VARB                          | var2 from your transaction request |
    | VARC                          | var3 from your transaction request |
    | VATNUMBER                     | Your VAT number given in your MultiSafepay account |
    | ZIPCODE                       | Your company zip code |

    </details>
    <details id="how-to-add-your-logo">
    <summary>How to add your logo</summary>
    <br>

    To add your logo to emails to increase customers' recognition and trust, follow these steps:

    1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
    2. Go to **Settings** > **Website settings** > **Upload a new file**.  
    3. In the **Files** directory, under **Actions**, click **Copy to clipboard** to copy the file's URL (starting with https://media.multisafepay.com/merchants/).
    4. Go to **Settings** > **Email templates**, and then click the relevant site.
    5. Click the orange pen icon to edit the template.
    6. Click the **Image** icon in the first row of the editor.
    7. In the **Image properties** window, in the **URL field**, paste the URL.
    8. Edit other parameters as required: height, border, horizontal space, vertical space, and alignment.
    9. Click **OK**. 

    </details>

    <details id="how-to-add-an-inline-frame">
    <summary>How to add an inline frame</summary>
    <br>

    Inline frames (Iframes) are HTML documents embedded inside another HTML document, which you can use to insert content from another source into the email template. 

    1. Go to the Body HTML editor on the email template page, and then click the **Iframe** icon. 
    2. In the **Iframe window**, enter the URL of the Iframe.
    3. Edit other parameters as required: width, height, alignment, name, and title.
    4. Click **OK**. 

    </details>

9. Click **Save**.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)