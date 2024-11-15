---
title: "Before you begin"
description: ""
date: 2024-11-15T13:51:12Z
draft: false
---

# **2 Before you begin** 

The following is a list of browser and security requirements and client installation options that allow **Jabra+** for admins to operate and help ease the onboarding of Jabra personal and meeting room devices. 

## **Important note** 

If an organization wants to use Single sign-on (SSO), an admin user (*Owner*) must set it up **before** following any procedures in this guide. First, follow the Setting up Single sign-on procedure, then return to the **Before you begin** chapter to continue. 

Admin users must **not** manually sign up for an individual **Jabra+** account, and the *Owner* must only create an organization after setting up SSO. 

Otherwise, if an *Owner* first signs up for an account manually and sets up SSO *afterwards*, all admin users risk losing access to the organization, any configurations that were created, Jabra devices added to inventories, user accounts, and other information in **Jabra+** for admins. 

## **2.1 Browser, security, and proxy server requirements to access Jabra+ for admins** 

To log in to **Jabra+** for admins, as a prerequisite, the computer must have the latest versions of the following browsers installed: 

* Google Chrome™   
* Microsoft® Edge 

**Proxy server settings for the desktop app and Meeting room clients** 

The client/desktop app, i.e.: **Jabra+** desktop, and **Meeting room clients** support and apply Windows proxy server settings automatically when connecting to **Jabra+** for admins. 

**Security requirements – Whitelisted domains and subdomains** 

For **Jabra+** for admins to work as intended, it is recommended that certain outbound TCP ports are open. The following domains, subdomains, and their outbound ports must be accessible. 

### **Important note** 

If the organization does *not* want to whitelist subdomains with a wildcard (\*), then it is a requirement to whitelist the domains denoted in red on the table that follows. 

However, be aware that if only the subdomains in red are whitelisted, future changes in the infrastructure could affect the organization. 

**Jabra+ core components domains and subdomains** 

| Domain (\*= wildcard)  | Outbound TCP Port(s)  |
| :---- | :---- |
| cloud.jabra.com/\*  | 80  443  |
| firmware-api.jabra.com/\*  | 80  443  |
| global.azure-devices-provisioning.net/\*  | 443  |
| \*.azure-devices.net/\* o jabra-prd-westeu-iothub.azure-devices.net/\*  | 443  5671  |
| api.cloud.jabra.com/\*  | 443  |
| file.cloud.jabra.com/\*  | 80  443  |
| \*.service.signalr.net/\*  o jabra-prd-westeu-signalr.service.signalr.net/\*   o wss://jabra-prd-westeu-signalr.service.signalr.net/\*  | 443  |
| jabra-prd-westeu-apimanagement.azure-api.net/\*  | 80  443  |
| prdwestblobmn4qoxfxnu466.blob.core.windows.net/\*  | 443  |
| images-ctfassets.net/\*  | 443  |

**Jabra+ analytics-related domains and subdomains** 

| Domain (\*= wildcard)  | Outbound TCP Port(s)  |
| :---- | :---- |
| googletagmanager.com/\*  | 443  |
| content.hotjar.io/\*  | 443  |
| \*.hotjar.com/\*  o ws.hotjar.com/\* o script.hotjar.com/\* static.hotjar.com/\*  | 443  |
| \*.google-analytics.com/\* o region1.google-analytics.com/\*  | 443  |
| \*.cookiebot.com/\*  o consentcdn.cookiebot.com/\* consent.cookiebot.com/\*  | 443  |
| ssl.gstatic.com/\*  | 443  |
| google-analytics.com/\*  | 443  |

**Jabra+ Security Framework Guide** 

For a complete overview of suggested security considerations, request the **Jabra+** **Security Framework Guide** from a Jabra representative. 

## **2.2 System requirements for software clients** 

On the one hand, to connect Jabra personal devices to **Jabra+** for admins, admin users must first create and download the organization-specific **Jabra+** desktop app (**Desktop client**) from within **Jabra+** for admins, and then install it on the computer(s) of the organization’s end users. 

### **Note** 

The **Jabra+** desktop app is both a desktop client and an app that initially serves as a gateway to connect Jabra personal devices to **Jabra+** for admins. 

After installation on the end-user´s computer, it can be found on the Windows system tray, and is used as a firmware management tool for Jabra personal devices. 

On the other hand – for Jabra meeting room devices and depending on the Jabra meeting room device model being provisioned – an admin user must create either a **Meeting room client** or generate a provisioning code and use **Jabra+** for installers. 

The following are system requirements for the **Jabra+** desktop app, the **Meeting** **room client**, and **Jabra+** for installers. 

| Jabra device type or model  | Software client  | Requirements  |
| :---- | :---- | :---- |
| Compatible Jabra personal devices (*Beta* only)  | • 	The **Jabra+** desktop app  | Windows® compatible PC or Meeting room  computer/ThinkSmart™ Core device running  Microsoft® Windows® 10 or later.  An active Internet connection  Administrator rights or equivalent credentials to install software in Windows ®  |
| Jabra PanaCast 50 RS  Microsoft® Teams Rooms /  Zoom Rooms  | 	• 	Meeting room client  |  |
| Jabra PanaCast 50 BYOD  | 	• 	**Jabra+** for installers  |  |
| Jabra PanaCast 50 VBS  | 	• 	Built-in software client  |  |

### **2.2.1 Client installation options** 

Both the Desktop client (i.e.: **Jabra+** desktop app) and the **Meeting** **room client** are .msi files that serve as a gateway between both Jabra personal or meeting room devices and **Jabra+** for admins. The gateway is necessary for provisioning the Jabra devices into **Jabra+** for admins. 

The software clients must be installed in Windows® 10 or later using Administrator rights and clicking through the installer menus. However, in certain cases, an admin user can install software clients silently, without any GUI visible to the end-user, or by hiding the tray icon. 

On the other hand, **Jabra+** for installers is an application / software client to provision the Jabra PanaCast 50 BYOD meeting room device. Read more about the clients in the Software clients chapter. 

**Mass deployment options** 

In a mass deployment scenario, specifically for the **Jabra+** desktop app, the relevant software client must be deployed and installed on every end-user’s Windows® computer. 

For Jabra meeting room devices, an admin user can deploy the **Meeting** **room client** (For P50 RS only) to every ThinkSmart™ Core/meeting room computer connected to the Jabra meeting room devices. 

#### **Note** 

Mass deployment is not possible with Jabra meeting room devices that have a built-in software client or are provisioned using **Jabra+** for installers i.e.: Jabra P50 BYOD and Jabra P50 VBS meeting room devices. 

There are two suggested ways of installing the **Meeting** **room client** and **Jabra+** desktop app: 

* Perform a manual installation on every computer with the relevant Jabra device connected to it, especially if only a few Jabra devices require provisioning 

* Mass deploy the.msi file using a preferred method, for example, via group policy, script, or silent installation, etc. This might be the case if there is a more significant number of Jabra devices to provision. 

In the context of the **Meeting** **room client** and the **Desktop client** (**Jabra+** desktop app), use Microsoft's System Center Configuration Manager (SCCM) or Microsoft® PowerShell 7 or later and customize the installation of the clients with the following parameters when installing from the command line: 

| Parameter  | Values  | Description  |
| :---- | :---- | :---- |
| NO\_TRAYICON=YES  | \----  | The software client does not have a tray icon while it is running  |
| DISABLE\_AUTOSTART  | YES/NO  | (Default: NO) Setting this to YES prevents the client from starting up automatically after installation, e.g.: if installed remotely while no active user is on the computer or meeting room computer  |
| /qn  | \----  | Specifies there is no UI during the installation process  |

An example of a typical silent installation where the client does not have a tray icon while running is as follows:   

msiexec.exe /i \<path to package\> NO\_TRAYICON=YES
