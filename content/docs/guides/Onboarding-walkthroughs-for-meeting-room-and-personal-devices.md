---
title: "Onboarding walkthroughs for meeting room and personal devices"
description: ""
date: 2024-11-15T13:55:09Z
draft: false
---

This chapter enables an admin user to quickly onboard Jabra meeting room and/or personal devices (*Beta*) into **Jabra+** for admins for remote management, as well as choosing a configuration. 

## **Note** 

Before onboarding Jabra personal and meeting room devices, ensure to read and follow the procedures in the Getting Started with Jabra+ for admins chapter, including the limitations section. It is also mandatory to create an organization before performing any of the walkthroughs that follow. 

Every domain is restricted to three organizations, where each organization has a default device limit that enables admin users to provision and manage up to 500 Jabra meeting room and or personal devices. To request an increase, contact Jabra Support or your Jabra representative. 

**Jabra+** uses the following clients that act as a gateway for the relevant type of Jabra device to connect to **Jabra+** for admins: 

* **Jabra+** for installers: An application and client software for the Jabra PanaCast 50 Bring Your Own Device (P50 BYOD) 

* **Meeting room client**: A client software file for the Jabra PanaCast 50 Room System (P50 RS) in a Microsoft® Teams Rooms / Zoom Rooms setup 

* **Built-in client**: The Jabra PanaCast 50 Video Bar System (P50 VBS) meeting room device has the software client built into the device 

* **Jabra+** (desktop app): A Windows® application and software client for Jabra personal devices (*Beta*) 

To learn more about software clients and procedures, see the standalone Software Clients chapter. 

The following walkthroughs enable an admin user (*Owner* or *Members with edit rights*) to provision, inspect, and manage Jabra meeting room and personal devices remotely, as well as help an admin user create or choose a configuration for Jabra devices. Creating and/or choosing a predetermined configuration is not mandatory; admin users i.e. *Owners* or *Members with edit rights* for Meeting rooms, Personal devices or both, may manage Jabra devices individually, directly from **Jabra+** for admins. 

Other admin users (*Members with read only rights*) can view Jabra devices in their respective inventories, as well as view any configurations that have been created, but they cannot manage or change any settings in **Jabra+** for admins. 

Be aware that there are different onboarding procedures depending on the Jabra meeting room device and the required setup.   

## **Note** 

**P50 BYOD**: On the one hand, any admin user can provision the P50 BYOD using Wi-Fi or a cabled Ethernet connection. When connecting through Ethernet for P50 BYOD, **WPA-Personal** authentication can be used without certificates, or the **EAP** protocol to connect to the network and authenticate using certificates, credentials, or no authentication. 

**P50 VBS**: On the other hand, to provision a P50 VBS, it is mandatory to use a cabled Ethernet connection, as Wi-Fi provisioning is not yet available. When connecting P50 VBS through Ethernet, authentication is possible with a username and password, however certificates cannot be used. 

In **Jabra+** for admins, an *Owner* or *Member with edit rights* (for personal devices) can manage Jabra personal devices including firmware management via **Jabra+** desktop on behalf of end users in the organization. 

On the other hand – in the context of Jabra meeting room devices – an O*wner* or *Member with edit rights* (for meeting rooms) can provision, inspect, and manage Jabra meeting room devices (P50 BYOD, P50 RS, or P50 VBS) remotely. 

It is important that the admin user with necessary permissions completes all relevant procedures for the specific device setup, whether Jabra personal or meeting room devices, or both. 

## **Important note** 

During provisioning, the P50 VBS requires a firmware update. If prompted to do so, ensure to perform the update as it is mandatory before continuing with provisioning. For P50 BYOD you may also be asked to update. 

Be aware that the meeting room device is unavailable during the update. 

For any issues during firmware updates, see Appendix & Troubleshooting.  

To provision both a meeting room device and a personal device, the admin user must follow and complete both walkthroughs, the one relevant to the meeting room device(s) as well as the one for personal devices. 

After provisioning and adding the Jabra device(s) to **Jabra+** for admins, to complete the walkthroughs, an admin user can optionally choose and assign a configuration based on the specific Jabra meeting room device and setup or personal device. 

The following links provide quick access to the relevant Walkthrough: 

* Walkthrough: Jabra PanaCast 50 BYOD   
* Walkthrough: Jabra PanaCast 50 RS   
* Walkthrough: Jabra PanaCast 50 VBS – All-in-one   
* Walkthrough (*Beta*): Jabra personal device installation and onboarding 

## **4.1 Walkthrough: Jabra PanaCast 50 BYOD** 

To provision and add a Jabra PanaCast 50 BYOD (P50 BYOD) to **Jabra+** for admins, an admin user (*Owner* or *Member with edit rights)* must initiate the provisioning process by generating a provisioning code. 

The provisioning code links the P50 BYOD in a physical meeting room to an organization. For the provisioning procedure, see the Provisioning the Jabra PanaCast 50 BYOD topic. 

Be aware that after provisioning the P50 BYOD, the meeting room device is automatically assigned a Standard Room configuration. To change the configuration and read more about Standard Room configuration, see the Room configurations for meeting room devices procedure. 

### **Note** 

If the admin user prefers to use the (default) **Standard Room** **Configuration** for the organization, without creating or assigning a new configuration, skip to End of Walkthroughs – What to do next? 

## **4.2 Walkthrough: Jabra PanaCast 50 Room System** 

To provision a Jabra PanaCast 50 Room System (P50 RS) in a Microsoft® Teams Rooms / Zoom Rooms (MTR/ZR) setup, an admin user (*Owner* or *Member with edit rights)* must first create, download, and install a **Meeting room client**. This client connects or links a P50 RS to **Jabra+** for admins. 

A more significant number of P50 RS meeting room devices can be installed and provisioned in a mass deployment context. For reference information, see the Client installation options subchapter. 

After successfully provisioning/onboarding and naming the Jabra meeting room device, it appears in the **Room inventory**. Complete all procedures that follow in this walkthrough. 

**Generating, downloading, and installing the Meeting room client** 

The **Meeting room client** is a gateway that links or connects a P50 RS to **Jabra+** for admins. Read more about it in the Software clients chapter. 

To do this, perform the installation of the **Meeting room client** directly on the ThinkSmart™ Core / meeting room computer, so **Jabra+** for admins can recognize the meeting room device. 

### **Tip** 

For details regarding optional installation parameters or mass deployment options, read the Before you begin section. 

For example, any admin user can distribute the **Meeting room client** by storing the .msi file on an external USB drive or transfer and run the installation file on every ThinkSmart™ Core/meeting room computer connected to a P50 RS. 

Another way to distribute the **Meeting room client** is to use a deployment system such as SCCM or Microsoft Intune. 

The **Meeting room client** is a Microsoft® Software Installer (.msi) file, which is exclusive to the organization once created in **Jabra+** for admins. 

For example, suppose in ten physical meeting rooms, each room has one Jabra P50 RS meeting room device with a ThinkSmart™ Core/meeting room computer. In that case, the same.msi file is distributed and installed on each of the ThinkSmart™ Core / meeting room computers connected to each P50 RS. 

It is recommended that after generating the **Meeting room client**, the admin user saves it with a meaningful name related to the organization, such as *ABC Company Meeting Room client*. 

To do this: 	 

• 	Create, download, and install the **Meeting room client**, see the following procedure: Creating, deploying, and installing the Meeting room client 

After the **Meeting room client** installation, restart the ThinkSmart™ Core/meeting room computer in the P50 RS bundle. After restarting, the P50 RS is added to the Room inventory and is automatically assigned a Standard Room Configuration.   

If necessary, continue with the procedure to choose a different Room configuration approach. 

### **Note** 

If the admin user does *not* want to create or assign a configuration or prefers to use the (default) **Standard Room** **Configuration** for the organization, skip to End of Walkthroughs – What to do next? 

## **4.3 Walkthrough: Jabra PanaCast 50 Video Bar System** 

The provisioning of the Jabra PanaCast 50 VBS (P50 VBS) takes place through the Jabra   
PanaCast Control (Touchscreen tablet) and through a computer with an active Internet connection. 

* To perform this onboarding walkthrough, complete the Provisioning Jabra PanaCast 50 VBS to Jabra+ for admins procedure. 

* After onboarding, and if necessary, an admin user (*Owner* or *Member with edit rights)* can choose a configuration for the P50 VBS meeting room device. The procedure is described in the Choosing a Room configuration approach topic. 

### **Note** 

If the admin user does *not* want to create or assign a configuration or prefers to use the (default) **Standard Room** **Configuration** for the organization, skip to End of Walkthroughs – What to do next? 

## **4.4 Choosing a Room configuration approach for P50 BYOD, RS, or VBS (Optional)** 

To complete the walkthrough to onboard Jabra meeting room devices, an admin user (*Owner* or *Member with edit rights)* must choose one of the three configuration approaches to manage settings. 

If an admin user manages one Jabra meeting room device, they can adjust the settings of a single device remotely, without using a predetermined configuration and/or without having the Jabra device in a grouping (such as Locations). 

Upon onboarding, your Jabra meeting room device(s) appears in the **Room inventory** and is automatically assigned Jabra´s Standard Room Configuration. 

### **Note** 

Choosing a Room configuration is optional. If further configuration of Jabra meeting room device(s) is not planned, using Jabra´s default **Standard Room** configuration is recommended. 

To choose a room configuration, see the following options and click the relevant link. 

* **Standard Room Configuration** (Recommended): This default configuration applies automatically to meeting room devices after onboarding or provisioning is completed. This approach is suitable when the same configuration must apply to all Jabra devices in the Room inventory. If an admin user chooses this approach, continue to End of Walkthroughs – Next steps.   

* **Exceptions**: An admin user can set and add exceptions when all Jabra meeting room devices must have the same configuration settings, with some specific exceptions. To choose this approach, see the following procedure. 

* **Create a Room Configuration**: This approach is suitable to set specific settings for one or many groups of Jabra meeting room devices. To do this, an admin user must create and assign a configuration to the room. To choose this approach, see the following walkthrough. 

After choosing a configuration approach and/or performing the procedure(s), Jabra meeting room devices are ready to be managed remotely.   

At this point, if an admin user has chosen a configuration for Jabra meeting room devices, continue to End of Walkthroughs – What to do next?.   

## **4.5 Walkthrough** (*Beta*)**: Jabra personal device installation and onboarding** 

This walkthrough lets an admin user (*Owner* or *Member with edit rights*) onboard a Jabra personal device, i.e., headsets, headphones, and conference speakerphones, into **Jabra+** for admins. 

### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

After getting started and creating an organization, the *Owner* is directed to the Device inventory of the organization. To perform this walkthrough, the *Owner* or *Member with edit rights* (for Personal devices) must first create, download, and install the **Jabra+** desktop app**/**software client to link or connect Jabra personal device(s) to the organization in **Jabra+** for admins. 

Any admin user can perform the software client installation and onboarding in a mass deployment context. Then, the admin user with the relevant permissions can choose a configuration for remote and bulk firmware management of Jabra personal devices, i.e., **Standard configuration**, setting **exceptions** or **Create a configuration**. 

After choosing and applying a configuration, the personal devices are ready to be managed remotely. See the Firmware management chapter for further details. 

**Creating, downloading, and installing the Jabra+ desktop app** 

For an admin user (*Owner* or *Member with edit rights*) to discover and manage Jabra personal devices in **Jabra+** for admins, it is mandatory to have the **Jabra+** desktop app installed and running on all computers that connect to Jabra personal device(s). More about the clients can be found in the Software clients chapter. 

The **Jabra+** desktop app is exclusive to an organization. Therefore, it must be created and downloaded from within **Jabra+** for admins, while being logged in under the relevant organization. When the admin user creates the **Desktop client**, it is recommended to save it with a meaningful name related to the organization. For example, *My Company´s desktop application*. 

To create, download, and install the **Jabra+** desktop app, see the Creating, deploying, and installing the Jabra+ desktop app/client procedure. 

### **Tip** 

For details regarding optional installation parameters or mass deployment options, read the Before you begin section. 

After installing the **Jabra+** desktop app, the admin user can either choose a suitable configuration or use the default one. If using the default one, skip to End of Walkthroughs – What to do next?. 

**Choosing a configuration (Optional)** 

The next and final step is to choose one of the three configurations to manage the settings of the Jabra personal device(s). However, an admin user (*Owners* or *Members with edit rights*) can adjust the settings of a single device remotely, without using a predetermined configuration. 

For more detailed information on configurations and approaches that help manage settings and firmware on Jabra personal or meeting room devices, see the Configurations chapter. 

* **Standard Configuration** (Recommended): This default configuration is applied automatically to Jabra personal devices as soon as they are connected to a computer with the **Jabra+** desktop app already installed and running. This approach is suitable when the same configuration must apply to all Jabra personal devices in the Device inventory. If an admin user chooses this approach, continue to End of Walkthroughs – What to do next?.   

* **Exceptions**: An admin user can set and add exceptions when all Jabra personal devices must have the same configuration settings, with some specific exceptions. To choose this approach, see the following set of procedures.   

* **Create Configuration**: This is suitable when an admin user wants to set specific settings for one or many Device groups of personal devices. This approach adds complexity to the setup as an admin user must manually add and/or remove the specific Jabra devices that 

  are in the specific Device group. To choose this configuration, see the following set of procedures. 

At this point, if you have chosen a configuration for your Jabra personal device, continue to the section that follows, End of Walkthroughs – What to do next?. 

**4.6 End of Walkthroughs – What to do next?** 

If an admin user (*Owners* or *Members with edit rights*) has performed any of the meeting room or personal device walkthroughs, added a meeting room or personal device to **Jabra+** for admins, created an organization, linked a Jabra meeting room or personal device to it, and assigned a configuration then an admin user can also expand on these walkthroughs; for example, create additional organizations, configurations, etc. 

In the case of Jabra meeting room devices, it is recommended that the admin user sets up a locations structure based on how the business organization is organized. Refer to the Locations subchapter for guidance on creating this structure. 

In the case of Jabra personal devices (*Beta*), continue to the Device groups conceptual topics to sort the Jabra personal devices into groups.  

For both meeting room and personal devices, it is recommended to continue reading the Jabra+ for admins chapter. This chapter provides the foundation for understanding **Jabra+** for admins capabilities and provides guidance regarding the remote management of Jabra devices according to your organization´s needs.
