---
title: 'iFrame'
weight: 12
meta_title: "FAQ iFrame - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---
 
An iFrame, also known as an Inline Frame is HTML document embedded inside another HTML document on a [website](/faq/getting-started/glossary/#website) 
 
Although MultiSafepay does not prohibit the use of an iFrame, it is not recommended.
Due to privacy and security reasons it may occur that the selected payment method is non-responsive when using an iFrame.
 
Banks are loading scripts that cannot be loaded within the iFrame.
Also, the checks are very strict on the safety of iFrames when using Google Chrome.
You can adjust the iFrame, making it less safe, so that Chrome can load the script again.
 
This is possible with the following iFrame sandbox attributes:
 
* sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-top-navigation">
As additional information, also check: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
 
Therefore, the following option will be available to you.
 
* Request your developer to process the modification in the sandbox
* Refrain from using iFrame.
 
If any assistance is requested or needed, please contact our Integration Team at <integration@multisafepay.com>
 

