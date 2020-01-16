---

title: "SSL Certificate Renewal January 2020"
Weight:
meta_title: "FAQ General - SSL Certificate renewal - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

### SSL Certificate Renewal January Update

MultiSafepay continuously works hard to ensure a secure payment infrastructure. We regularly carry out updates and maintenance as it is necessary to maintain a high level of security.
The TSL/SSL certificate is issued by a CA (Certification Authority) and requires periodic renewals and updates to be performed by MultiSafepay.

On January 22nd at 09:00 (GMT+1) MultiSafepay will update its SSL certificate to guarantee the safety of our infrastructure and communication. This renewal ensures that the communication uses the latest security standards to protect both you and us.

In general, this update will not affect your systems or payment processing of transactions. As we take all the measures to ensure that the updates and maintenance will not disrupt server communication, we expect web shops integrating our payment platform not to be affected.

If the certificate is being stored and validated on an outdated platform, you may run into issues. If this occurs, please contact us at <integration@multisafepay.com>

The affected systems are the following: 

* Domain
* Sub-domains
* Server communication

The new certificates are already loaded to our merchant test platform. If you want to validate whether your infrastructure can handle the renewed certificates, you can submit a transaction request to one of the following test addresses:

https://testapi.multisafepay.com/v1/json/  for JSON-api
https://testapi.multisafepay.com/ewx/     ([suitable for XML-api](/faq/api/xml-api/))

## Http or Https?

Commonly speaking, a domain is considered secure when the URL presents the wording “https”. It also indicates that the domain possesses a TSL/SSL certificate. More information on the certificate can be found clicking on the lock symbol appearing before the URL in the browser bar.

<div class="alert alert-warning" role="alert">
Please note: If you decide to cache the SSL-certificate, MultiSafepay will not hold responsibility, although we are happy to assist you in solving any issues that may arise.
</div>