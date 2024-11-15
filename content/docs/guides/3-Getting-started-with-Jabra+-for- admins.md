---
title: "Getting started with Jabra+ for admins"
description: ""
date: 2024-11-15T13:53:53Z
draft: false
---

# **3 Getting started with Jabra+ for admins** 

To get started with **Jabra+** for admins, an admin user can enable SSO or set up a manual sign-up and sign-on process for themselves and other admin users. 

## **Warning** 

If an organization wants to use SSO, an admin user (*Owner*) must set it up *before* following any procedures in this guide. To do this, follow the Setting up Single sign-on procedure. 

Admin users must not manually sign up for an individual **Jabra+** account, and the *Owner* must only create an organization after first setting up SSO. 

Otherwise, if an *Owner* first signs up for an account manually and sets up SSO *afterwards*, all admin users risk losing access to the organization, any configurations that were created, Jabra devices added to inventories, user accounts, and other information in **Jabra+** for admins. 

For more information, see the Troubleshooting section. 

After the sign-up process, the admin user logs in, and they are prompted to create an organization. An organization (such as a business or corporation) is a representation of the company/business in **Jabra+** for admins and has a unique organization ID. 

Admin users in any organization can provision and manage up to 500 Jabra meeting room and or personal devices. To increase the device limit, contact Jabra Support or your Jabra representative. 

To understand how organizations work in **Jabra+** for admins, see the Organizations chapter. 

Upon first-time registration in **Jabra+** for admins, the admin user takes up the *Owner* (of the organization) role. The *Owner* can then invite other admin users (i.e.: additional *Owner* roles and/or *Members* with either *edit rights* or *read only rights*) granting access to the specific organization. 

Only *Owners* and *Members* *with edit rights* in **Jabra+** for admins, can download organizationspecific software clients, onboard Jabra devices into virtual inventories (for personal and meeting room devices), manage Jabra devices remotely, set the settings for one or a group of Jabra devices, manage the firmware, and others. 

## **Note** 

*Owners* can perform all procedures in this guide. However, for *Members with edit rights* for Meeting rooms and/or Personal devices, ensure they have permission to perform the relevant procedures.  

For example, to remove Jabra personal devices from the Device inventory, the *Member* with edit rights must have permissions enabled for Personal devices. Consequently, a *Member* with edit rights for Meeting room devices cannot remove Jabra personal devices from the Device inventory, but they can remove Meeting room devices from the Room inventory. 

For details, see the Roles and permissions chapter. 

For conceptual information on the different components of **Jabra+** for admins, read the Jabra+ for admins chapter. 

After completing all the relevant procedures in this chapter, continue to the Onboarding walkthroughs for meeting room and personal devices chapter to provision and add Jabra personal and/or meeting room devices to **Jabra+** for admins. 

## **3.1 Setting up Single sign-on** 

An organization *Owner* can set up single sign-on before inviting other admin users (*Owners* or *Members*) to **Jabra+** for admins. This ensures that only admin users from pre-approved domain(s) can log in. 

If the organization does *not* want to use SSO, continue to Manual sign up for a Jabra+ account. 

Currently, the following Identity Providers (IdP) are supported by **Jabra+** for admins: 

* Microsoft Entra ID (formerly Azure Active Directory IdP)   
* OpenID Connect 

To set up SSO, an admin user must have the following information at hand before filling out the Single sign-on request form: 

* Company name (e.g.: your organization)   
* Contact e-mail for SSO confirmation   
* Type of single sign-on preferred, **Azure Active Directory** or **OpenID Connect** 

* **ClientID** identifier o Ensure you have your *ClientID* and are able to provide it 

* **ClientSecret** o Ensure you have your *ClientSecret* and expiration date 

* OpenID Connect discovery endpoint   
* List of domains supported by your IdP   
* (Optional) Your Group´s endpoint (If your IdP provides group information) 

### **Note** 

**Jabra+** for admins does not currently support Security Assertion Markup Language (SAML) for SSO. 

To set up single sign-on: 

	• 	Fill out and submit the [Single sign-on Request Form](https://forms.office.com/e/yD2942hdLG) 

After the admin user fills out and sends the form, they receive a confirmation e-mail from a Jabra representative containing the Unique Identity Provider (IDP) return URL. Be aware that the admin user may be asked to provide further information. 

When the setup of SSO is completed, the admin user is now ready to log in to **Jabra+** for admins at [http://cloud.jabra.com](http://cloud.jabra.com/) and create an organization. 

## **3.2 Manual sign up for a Jabra+ account** 

In **Jabra+** for admins, an admin user can sign up for a **Jabra+** account. After doing so and logging in for the first time, the admin user is prompted to create an organization, of which they become the *Owner*. 

### **Warning** 

If the organization would like to make use of SSO or access control, *do not* sign up manually for an account first. Signing up for a manual account *before* setting up SSO, risks losing any configurations that were created, Jabra devices added to inventories, user accounts and other information. 

To sign up for SSO, follow the Setting up Single sign-on procedure. Be aware that an admin user (*Owner*) must only create an organization after setting up SSO; otherwise, signing up manually first may prevent access to the organization when SSO is enabled. 

For more information, see the Troubleshooting section.  

To sign up as a first-time admin user: 

1. In a web browser, enter the following URL: [https://cloud.jabra.com](https://cloud.jabra.com/)   
2. Click **Sign up now** 

3. Follow and complete the sign-up wizard 

At this point, the admin user (*Owner)* receives a confirmation email with a verification code. The *Owner* must check their email inbox, copy the verification code, and then return to [https://cloud.jabra.com.](https://cloud.jabra.com/) 

To create an account in **Jabra+** for admins, fill out personal details and choose the relevant country/region. Additionally, enter a name in the *Display name* field, as this serves as the username within **Jabra+** for admins and then create a password following the guidelines. 

After your initial sign in to **Jabra+** for admins, the *Owner* is prompted to create an organization. 

## **3.3 Creating an organization** 

After an admin user completes the sign-up process for an account and logs in to **Jabra+** for admins with their email domain, the admin user, now the *Owner*, is prompted to create an organization, for example, *ABC Company*. 

Every domain is restricted to three organizations, where each organization has a default device limit that enables admin users to provision and manage up to 500 Jabra meeting room and/or personal devices. To request an increase, contact Jabra Support or your Jabra representative. 

For conceptual information and additional procedures, see the Organizations topic. 

To create an organization upon first-time login: 

1\. In the **Create organization** dialog box, in the field provided, enter a name for your organization. Ensure you provide a meaningful name, as there may be a need to invite additional admin users to the organization. 

### **Note** 

**Jabra+** for admins supports ASCII and non-ASCII characters, such as accented letters, non-Latin alphabets, and symbols, however admin users cannot rename an organization, so ensure the naming of the organization is correct. 

2. In the **Create organization** dialog box, click **Continue** 

3. In the **Set up device metadata** dialog box, check the relevant device metadata checkboxes, and to save your selections, click **Continue**. If you click **Skip**, **Jabra+** for admins checks all device metadata collection checkboxes by default. For more information about device metadata, see the Appendix & Troubleshooting section.   
4. In the **Welcome** dialog box, ensure you read the Privacy Policy and License Agreement, and then click **Get started** 

You are now the *Owner* of the organization you created and are directed to the Dashboard. 

## **3.4 Inviting additional admin users (Optional)** 

This procedure is not mandatory and can be completed later. If additional admin users (*Members* or *Owners*) are not required, continue with the Onboarding walkthroughs for meeting room and personal devices.   

Adding a second *Owner* to the organization is advisable, as it can be helpful if access to **Jabra+** for admins is lost. Only an *Owner* can invite a new admin user, send, resend or revoke invitations, and edit permissions on behalf of all admin users in the organization.  

### **Note** 

Only *Owners can* invite other admin users to **Jabra+** for admins. 

An *Owner* can invite multiple admin users, and invitations sent to additional admin users are valid for seven days.  

To invite an additional admin user to the organization: 

1. On the bottom left-hand side of the navigation bar, click the name of the organization you are currently the owner of, and then click **Admin users**   
2. In the **Admin users** page, on the top-right hand side of the screen, click **Invite new user** 

3. In the **Invite new user** dialog box, in the *Email* field, enter the new admin user’s business email address o To invite multiple *Members* with the same permissions or additional *Owners*, separate the email addresses with a comma (,) or semicolon (;)   
4. In the **Role** section, click the relevant radio button for **Member** or **Owner** o When selecting the *Member* role, in the **Permissions** section, for **Meeting rooms** and/or **Personal devices** management, click **Edit** or **Read only**   
5. Click **Invite**   

   At this point, the **Jabra+** for admins sends an email prompting the recipient to create a **Jabra+** account using a unique sign-up link. After creating an account, the added admin user can log in to **Jabra+** for admins. 

   You can read more about inviting additional users and editing permissions in the Roles and Permissions chapter.
