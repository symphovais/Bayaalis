---
title: "6 Configurations"
description: ""
date: 2024-11-15T14:01:23Z
draft: false
---

# **7 Configurations** 

A configuration is a set of model settings that controls the firmware version for supported Jabra meeting room and personal devices. In **Jabra+** for admins, when an admin user adds a Jabra personal or meeting room device, a default configuration with Jabra-recommended settings is automatically assigned. 

The Firmware policy chapter provides more information about the default policy and procedures for firmware updates and management. 

## **Tip** 

Configurations for personal and meeting room devices are identical. Exceptions apply to all Jabra meeting room or personal devices in their respective inventory, while new configurations target specific rooms or device groups (for personal devices). 

The **Standard Room Configuration** and **Standard Configuration** are the default for all Jabra meeting room and personal devices in the organization respectively. Admin users can add and set exceptions based on recommended settings that apply to either all Jabra meeting room devices in the physical meeting rooms or all Jabra personal devices. 

## **7.1 Room Configurations for Jabra Meeting room devices** 

With room configurations, an admin user can mass manage Jabra meeting room devices with a shared firmware policy and settings as soon as they are added to the Room inventory. 

Changing **Model settings** for your Jabra meeting room devices lets an admin user configure the room experience depending on the size and typical usage of a physical room. 

The Room configuration approach you choose is based on the level of complexity of your firmware and settings management. **Standard Room Configuration** is the least complex approach and the most recommended.  

An admin user can also set exceptions to the **Standard Room Configuration,** or the most complex approach is when an admin user chooses to **Create a Configuration** from the ground up. 

### **Note** 

As changes are implemented, Jabra meeting room devices may automatically reboot unless they are on an active call. 

The following are approaches to configuring your Jabra meeting room devices in **Jabra+** for admins:   

* **Standard Room Configuration**: This is the default Room configuration. It is suitable when the admin user wants the same Room configuration applied to all Jabra meeting room devices that appear as Rooms in the Room inventory. Choosing **Standard Room Configuration** affects all Jabra meeting room devices not assigned a newly created configuration, and it applies immediately and automatically to the entire organization (irrespective of the location) ensuring all Jabra meeting room devices follow the same firmware policy and Jabra-recommended model settings.   

* **Exceptions**: In the Standard Room Configuration, an admin user can set model exceptions to set the same Room configuration settings for all of their Jabra meeting room devices, with specific exceptions applied to a Jabra meeting room device model configuration. For example, an *Owner* or *Member with edit rights* (for meeting rooms) can modify the default Jabra-recommended model setting for *image brightness* on the P50 VBS model variant; this exception replaces the default setting for *image brightness* on all P50 VBS meeting room devices that are provisioned to the Room inventory.   

* **Create** **Room Configuration**: In this approach, an admin user must create room configurations to apply specific settings to one or many Rooms with Jabra meeting room devices and determine the firmware policy of the Jabra meeting room devices. With this approach, it effectively replaces the **Standard Room Configuration** for specific Rooms and their associated Jabra meeting room devices with the previously chosen settings, enabling the admin user to configure Jabra meeting room device model variants that can be assigned to rooms depending on the room type or typical usage. 

### **Note** 

When setting exceptions or creating a new room configuration from scratch, the admin user must select the corresponding Jabra meeting room device model that matches with the Jabra meeting room device. 

### **7.1.1 Setting Exceptions to a Standard Room Configuration** 

An admin user can edit the **Standard Room Configuration**, set exceptions for specific Jabra Meeting room device models or set exceptions for device model configurations, settings and firmware. See the Firmware policy chapter. 

#### **Note** 

When you add a model configuration for the Jabra PanaCast 50 RS or Jabra PanaCast 50 BYOD, be aware that you must select the **PanaCast 50** option. 

Moreover, when you have both P50 RS and P50 BYOD in your organization’s Room inventory, and need to set an exception to either P50 RS or P50 BYOD, you must Create a Room Configuration for each model and assign it to the rooms where the specific P50 RS or P50 BYOD are located. 

On the other hand, the P50 VBS has *its own* collection of model settings, including the Jabra Meeting room device and the PanaCast Control/touchscreen tablet; therefore, when adding a model configuration, you must select **PanaCast 50 VBS**.  	 

The exception(s) are applied automatically to all Jabra meeting room devices in the **Room inventory** for the specified Jabra meeting room device model. The default Jabra recommended setting(s) for your Jabra meeting devices are then replaced by the model setting(s) you set. 

To set an exception in the standard room for model settings management: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room** **Configurations**   
2. In the **Room** **Configurations** page, click the **Standard Room** pane 

3. On the **Standard Room** page, click the **Model Configurations** tab 

4. Click **Add model** **configurations** and select the relevant Jabra meeting room device model o For Jabra PanaCast 50 RS – select **PanaCast 50** o For Jabra PanaCast 50 BYOD – select **PanaCast 50** 

o For Jabra PanaCast 50 VBS – select **PanaCast 50 Video Bar System** 

5. In the bottom ribbon, click **Continue**   
6. On the **Manage settings** page, in the **Model Settings** pane, adjust the desired settings. You can also lock specific settings for end-users by toggling the relevant switches   
7. To apply the changes, in the bottom ribbon, click **Publish,** and in the **Publish model settings?** dialog box, click **Publish** again to confirm 

   Settings are published or applied now, and your Jabra meeting room devices may automatically reboot. 

### **7.1.2 Adjusting settings remotely of a single Jabra meeting room device** 

**Jabra+** for admins lets you remotely manage the settings of Jabra meeting room devices individually or in bulk. 

You can only change the settings of a single Jabra meeting room device, when you have not assigned a newly created configuration to the room that includes the specific Jabra meeting room device. You can adjust the settings on a single device via the **Room inventory**. 

Moreover, it is recommended that you Create a Room Configuration to adjust the settings of many Jabra meeting room devices simultaneously. When adjusting individual settings, the Jabra meeting room device must be connected/plugged in and online. 

#### **Tip** 

You can also use this procedure to test the settings of a single Jabra meeting room device and determine whether the changes are suitable prior to mass deployment. 

To adjust the settings of one Jabra meeting room device: 

1. On the left-hand navigation bar, click **Meeting Rooms** **\>** **Room inventory**   
2. In the **Room inventory** page, in your Locations tree structure, click the name of your organization   
3. In the Room inventory list, click the room name where your Jabra meeting room device is located   
4. In the **Room details** page, click the relevant Jabra meeting room device pane   
5. In the **Device details** page, click the **Settings** tab and make the necessary changes to settings   
6. To apply the changes and deploy them to the end-user, in the bottom ribbon, click **Publish changes**   

   After you click **Publish changes**, the setting changes are published or applied, and Jabra meeting room devices may automatically reboot. 

### **7.1.3 Walkthrough: Creating a Room Configuration** 

This walkthrough lets an admin user create room configurations for specific Jabra meeting room device models and assign the newly created room configuration to one or many specific rooms. This requires more effort and adds complexity when remotely managing Jabra meeting Room devices. 

The added complexity, however, enables the admin user to fine-tune the settings of the Jabra meeting room devices to create a customized experience for a specific type of meeting room. 

#### **Note** 

The **Create** (Room) **Configuration** is best suited for an organization with specific requirements for their Jabra device models. 

A sample use case for creating a room configuration can be as follows: In an organization, you may have a small room that fits a seat count of two and is typically used for face-to-face meetings. In this case, the admin user creates a configuration, whereby the *Field of view* setting is adjusted accordingly from the default 180° to a custom 120°. 

In this walkthrough, the admin user deploys and manages settings for a specific Jabra meeting room device model within a room, instead of all Jabra meeting room devices in the organization´s **Room inventory**. 

To create a new **Room Configuration**: 

1. On the left-hand navigation bar, click **Meeting Rooms \>** **Room configurations**   
2. In the **Room configurations** page, click **Create room configuration**, and in the **Create room configuration** dialog box, in the fields provided, enter a **Name** and optionally a **Description** and click **Create**   
3. In the **Add model configurations?** dialog box, click **Add models**  

#### **Note** 

Clicking **Skip adding models** means you can perform the following steps from the **Room** **configurations** menu item later. 

4. To select the specific meeting room device models on the list, find the Jabra meeting room devices you would like to assign a configuration to, and check the checkbox of the relevant   
   Jabra meeting room devices, i.e., **PanaCast 50** (P50 BYOD and P50 RS) or **PanaCast 50**   
   **Video Bar System** (P50 VBS) and in the bottom ribbon, click **Continue**   
5. In the **Manage settings** page, adjust the settings for the chosen Jabra device model(s). When you are finished, in the bottom ribbon, click **Publish**, and to confirm, click **Publish** again.   

   For changes to take effect, the next step is to assign a configuration to a room. To finish this walkthrough, you must assign a **Created Configuration** to a Room. Optionally, before you assign a **Created Configuration**, you can also lock settings for specific Jabra meeting room device models in a room. 

**Assigning a Created Room Configuration to a Room** 

For the Room Configuration (previously created) to take effect, you must assign the **Created** (room) **Configuration** to a Room in your Room inventory or a room that you have grouped into a Location. 

To assign a Created Room Configuration to a Room: 

1. On the left-hand navigation bar, click **Meeting Rooms** **\> Room inventory**   
2. On the Room inventory list, click the relevant room name    
3. In the **Room** page, in the **Room Configuration** pane, click the pencil icon (edit menu)   
4. In the **Change configuration** dialog box, in the drop-down menu, select the name of the configuration you previously created, and click **Change configuration** to confirm   

   After you click **Change configuration**, settings are published or applied, and your Jabra meeting room devices may automatically reboot. You have now created a new configuration and assigned it to a room. 

## **7.2 Configurations for Personal devices** *(Beta)* 

It is recommended that the configuration approach chosen by an admin user is based on the level of complexity for firmware and settings management. 

The following are three approaches to configuring Jabra personal devices via **Jabra+** for admins: 

### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

* **Standard Configuration:** This is the default configuration. This approach is suitable when the admin user wants the same configuration applied to all Jabra personal devices in the organization’s Device inventory. Therefore, **Standard Configuration** affects all Personal devices not part of a Device group. Moreover, **Standard Configuration** applies immediately and automatically to the entire organization and ensures all Jabra personal devices are continuously updated to the latest firmware versions, effectively deploying an organization-wide firmware policy. 

* **Exceptions:** In the Standard Configuration, an admin user can set and add exceptions when all Jabra personal device models require the same configuration settings, with some specific exceptions. This approach lets the admin user set a specific setting for a specific Jabra personal device model across the board.   

* **Create Configuration:** In this approach, the admin user can also create a new configuration to apply specific settings to one or many groups of Jabra personal devices and determine the firmware policy of those Jabra personal devices. With this approach, the admin user effectively replaces the **Standard Configuration** for a group of specific Jabra personal devices with the settings that were previously chosen in the new configuration. Another way to use **Create Configuration** is to test a Jabra personal device setting on a group of specific Jabra device models before mass deployment. 

### **7.2.1 Setting Exceptions to the Standard Configuration** 

An admin user can edit the Standard Configuration and set exceptions for Jabra personal device model settings, such as firmware management (e.g.: force a specific Jabra personal device model to use a predetermined firmware) or device settings management. The exception(s) are then applied automatically to the Device inventory. 

For example, an admin user may have an organization where specific settings need to apply to a model range of Jabra Evolve2 75 personal (audio) devices, such as a low or high *Sidetone* level, *On-head detection*, or other settings. With this approach, all Jabra Evolve2 75 personal devices in the organization automatically apply the setting. 

To do this: 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Configurations**   
2. In the **Configurations** page, click the **Standard Configuration** pane 

3. In the **Standard Configuration** page, click the **Model Configurations** tab 

4. Click **Add model** **configurations** and select the relevant Jabra personal device, for example, Jabra Evolve2 75   
5. In the bottom ribbon, click **Continue**   
6. In the **Manage settings** page, in the **Model Settings** pane, adjust the desired settings. You can also lock specific settings for end-users by toggling the relevant switches   
7. To apply the changes, in the bottom ribbon, click **Publish** and in the **Publish model settings?** dialog box, click **Publish** again to confirm 

   For changes to take effect, ensure you restart the computer that the personal device is connected to. When the end-user logs in to Windows® again, the changes are applied. 

### **7.2.2 Adjusting settings remotely of a single Jabra personal device** *(Beta)* 

**Jabra+** for admins lets an admin user remotely manage the settings of Jabra personal devices individually or in bulk. 

#### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

If the Jabra meeting room device has a (new) created configuration assigned to it, the admin user cannot change the settings of a single Jabra personal device. To adjust the settings on a single device, the admin user can do so via the Device inventory. 

To adjust the settings of many Jabra devices at the same time, it is recommended to use configurations and choose a suitable approach. Be aware that when adjusting individual settings, the Jabra personal device must be online. 

#### **Tip** 

The admin user can also use this procedure to test the settings of a single Jabra device before mass deployment and determine whether the changes are suitable. 

To adjust the settings of one Jabra device: 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Device inventory**   
2. In the list of devices, find the Jabra device you would like to change settings for. You can search for the specific Jabra device using filtering based on *Model*, *Device group*, *Firmware Status*, or *Connection status*.   
3. Click the Jabra device name, for example, Jabra Evolve2 75 MS   
4. Click the **Settings** tab   
5. Adjust the settings of your relevant device   
6. To apply the changes and deploy them to the end-user, in the bottom ribbon, click **Publish changes**   

   For changes to take effect, ensure you restart the computer that the personal device is connected to. When the end-user logs in to Windows® again, the changes are applied. 

### **7.2.3 Walkthrough: Creating a configuration for personal devices** 

This walkthrough lets an admin user create a new configuration for specific Jabra personal device models; This requires more effort and adds complexity when managing Jabra personal devices remotely. 

#### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

In this approach, Device groups play an important role because the admin user deploys and manages Jabra device model configuration or settings for each group of Jabra personal devices (instead of all Jabra personal devices in the **Device inventory**). 

#### **Note** 

This walkthrough is best suited for admin users in organizations with specific requirements for their Jabra personal device models. 

An example of when an admin user creates a configuration is in a call center scenario or an open office setting, where a group of people using Jabra headsets would prefer a quieter environment. 

In this case, the admin user creates a configuration whereby the *Sidetone* feature (*audio feedback from the person*'*s own voice to improve a call experience*) is adjusted accordingly, allowing headset users to hear themselves when speaking on the headset microphone. 

Be aware that when the admin user removes an assigned configuration, Jabra devices are automatically re-assigned to the Standard Configuration. 

To begin the walkthrough, continue with the procedure that follows, Creating a Device group. 

**Creating a Device group** 

An admin user must create a Device group before Jabra personal devices can be sorted into one or many Device groups. To do this, see the following procedure. After creating a Device group, the admin user must add the Jabra personal device(s) to the Device group. 

**Adding Jabra devices to a Device group** 

After creating a Device group, the admin user must add the Jabra personal device(s) to a Device group. To do this see the following procedure. After adding Jabra personal devices to a device group, the admin user must continue with creating a configuration that applies to Jabra personal devices in the Device group. 

**Creating a Configuration** 

To assign specific settings to a group of Jabra personal devices in a Device group, an admin user must first create a configuration. 

#### **Tip** 

After you create and save your configuration, you can optionally duplicate the configuration and use it for other Device groups you may have. See the Appendix & Troubleshooting section for the procedure. 

To create a configuration: 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Configuration**   
2. In the **Configurations** page, click **Create Configuration**, and in the **Create configuration** dialog box, in the fields provided, enter a **Name** and optionally a **Description** and click **Create**   
3. In the **Add model configurations?** dialog box, click **Add models** 

#### **Note** 

When you click **Skip adding models**, it means you can perform the following steps from the **Configurations** menu item later. 

4. To select models, find the Jabra personal devices you want to assign a configuration to, and check the checkbox of the relevant Jabra device models and when you are finished, in the bottom ribbon, click **Continue**   

5. In the **Manage settings** page, adjust the settings for the chosen Jabra personal device model. When you are finished, in the bottom ribbon, click **Publish**, and to confirm, click **Publish** again. 

   #### **Tip** 

   When selecting multiple models, the **Publish** button changes to **Next model**, so you can seamlessly configure all models within the configuration. 

For changes to take effect, you must assign a configuration to a Device group. Optionally, before you assign a configuration, you can lock settings for end-users for Jabra personal devices in a Device group. See the Locking settings subchapter for procedures. 

**Assigning a configuration to a Device group** 

For a configuration to take effect on a group of Jabra personal devices and replace the default **Standard Configuration** for the group of Jabra devices, you must change the assigned configuration of the Device group. 

To assign a configuration to a Device group: 

1. On the left-hand navigation bar, click **Personal devices** **\> Device groups**   
2. In the upper-right hand of the screen, click the action menu (three-dot menu) and click **Change configuration**   
3. In the **Change configuration** dialog box, in the drop-down menu, select the configuration name you created, and click **Change configuration** 

For changes to take effect on the Jabra personal devices in a Device group, ensure you restart the computer that the Jabra personal device is connected to. When the end-user (the user of the Jabra personal device) logs in to Windows® again, the changes are applied. 

You have now created a configuration for personal devices. 

## **7.3 Firmware management** 

In **Jabra+** for admins, admin users can manage remotely the firmware and firmware policy of Jabra personal and meeting room devices. 

On the one hand, Jabra personal devices´ firmware is managed through the **Jabra+** desktop app, whereby end users are prompted to update – or in exceptional cases downgrade – the firmware of their Jabra personal device, based on the firmware policy of the organization that has been set up in **Jabra+** for admins. 

There are also mitigation strategies when a firmware update fails, such as a firmware recovery process through the **Jabra+** desktop app. This is only necessary for cabled or wired Jabra personal devices. 

On the other hand, Jabra meeting room devices can have their firmware managed directly via **Jabra+** for admins, where you can also update or downgrade firmware according to the organization´s firmware policy. 

Firmware updates for Jabra meeting room devices, however, are pushed directly to the device and are governed by the schedule for device updates. 

### **7.3.1  Firmware policy** 

The Firmware policy — contained within Configurations — enables admin users with the relevant permissions to manage Meeting rooms and or Personal devices to manage firmware in **Jabra+** for admins, giving your end-users access to the latest updates and features. 

Governed by a firmware policy, relevant admin users can ensure Jabra meeting room, and personal devices get the latest firmware from Jabra or set a firmware update exception for a specific Jabra device model variant. For example, setting an exception for all Jabra Evolve2 75 personal devices in your organization, whereby they only use a specific firmware version, or a specific active noise cancellation level. 

The default firmware policy — which updates Jabra meeting rooms and personal devices to the latest firmware version — is part of the **Standard Configuration** and works differently for Jabra meeting room and for personal devices. Whether an admin user chooses **Standard Configuration** or has **Created a Configuration**, the default firmware policy applies in both cases. 

Whenever the default firmware policy is modified, the admin user is effectively creating a *custom* firmware policy. However, an admin user cannot give a name to the different firmware policies since they are contained within configurations. 

Therefore, if you would like to have different firmware policies for different Jabra meeting rooms and personal devices, ensure that the admin user first creates a configuration or creates a room configuration and then modify the firmware policy for that configuration created. 

For both Jabra meeting room and personal devices, a firmware policy consists of the following toggle switches: 

* **Update devices using Jabra+ for admins**: primary toggle switch that enables or disables Jabra device firmware management in **Jabra+** for admins 

* **Always keep devices updated**: secondary toggle switch that updates all Jabra meeting room devices to the latest firmware version when available 

Also, the default firmware policy acts differently according to the type of Jabra device, and as follows: 

**Personal devices**: The default option is **ON** (enabled) for the **Update devices using Jabra+ for admins** toggle switch. This means the default firmware policy or **Standard Configuration** manages the firmware on personal devices. 

Additionally, the **Always keep devices updated** (to the latest firmware version) toggle switch is also **ON** (enabled) by default, notifying end-users when the latest firmware version is available for their Jabra personal device, and the end-user performs the update. 

An admin user can also switch the firmware policy **OFF** (disabled) by toggling the **Update devices using Jabra+ for admins** switch. This means that whenever a Jabra personal device is added to the Device inventory, the firmware policy keeps the currently installed firmware version. End-users are also not prompted when a new firmware update is available. 

Admin users can also create and set a created firmware policy for a specific Jabra meeting room or personal device model that applies globally, regardless of whether or not the Jabra device is in a Device group or in a Location. 

Moreover, in any Created configuration that was saved and assigned to specific Device groups, admin users can also create and set a created firmware policy for specific Jabra device models in a specific device group or room. 

**Meeting Room Devices**: In the case of Jabra meeting room devices, however, when a Jabra PanaCast meeting room device is provisioned (P50 BYOD, RS, VBS), the default firmware policy does ***not*** control, manage, or update the firmware on its own, and the devices keep the currently installed firmware version. 

In other words, the default option for the **Update devices using Jabra+ for admins** toggle switch is **OFF** (disabled). This means you are turning **off** the ability to manage the firmware. Consequently, the default option for the **Always keep devices updated** to the latest firmware version toggle switch is also **OFF** (disabled). 

| Note  When you enable firmware updates in Jabra+ for admins, you must disable firmware updates from other platforms, such as Windows® Update.  This means whenever a Jabra Meeting room device is added to the Room inventory, you can manage the firmware exclusively in Jabra+ for admins.  |
| :---- |

When a firmware update is made available, Jabra meeting room devices only perform the update according to the organization’s schedule for device updates. 

You can also set a specific firmware version for a Jabra meeting room device model in the Standard Room Configuration that is automatically assigned to all your meeting room devices in the **Room inventory**, as well as any Created Room Configuration that you saved and assigned to specific rooms. 

You can also restrict the **Always use latest firmware** feature only to a specific Jabra device model. The admin user can do this by creating a custom firmware policy. The Room inventory list shows *Firmware status* for all rooms, displaying whether or not an update is scheduled. 

| Important note  Although there may be a firmware policy in place for the organization´s Jabra meeting room devices, the following requirements must be met before firmware updates can begin:  The Jabra meeting room device must not be in an active meeting or call  Your organization has a weekday and time set in the schedule for device updates  During the firmware update, ensure that the Jabra Meeting room device remains connected.  |
| :---- |

### **7.3.2 Enabling or disabling firmware management for Jabra devices** 

The default firmware policy for Meeting room devices applies automatically to the **Standard Room Configuration** and is switched **OFF** (disabled) by default. 

To enable firmware management, the admin user must first decide to **Update devices using**   
**Jabra+ for admins** (primary toggle switch) **ON** and then decide whether or not to switch **ON** the **Always keep devices updated** (secondary toggle switch) to update all Jabra Meeting room devices to the latest firmware version when available. 

For Jabra personal devices, the default firmware policy applies automatically to the **Standard Configuration**, which is switched **ON** (enabled) by default. 

When enabled, firmware-related notifications are sent to end-users using Jabra personal devices. The admin user can switch this **OFF** (disabled) the default firmware policy in Standard Configuration, disabling firmware management in **Jabra+** for admins across the board. 

#### **Tip** 

When an admin user wants to update the firmware of a Jabra meeting room or personal device model in their respective inventories, they can create a custom firmware policy that includes an exception for firmware in the Standard Configuration or choose to assign a custom firmware policy to a specific Room or Device group. 

See the Creating and setting a Firmware Policy for specific Jabra device models in a specific device group or room procedure. 

To enable or disable firmware management for Meeting room devices: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room Configurations**   
2. In the **Room Configurations** page, click the **Standard Room** pane 

3. In the **Standard Room** page, in the **Firmware Policy** tab, in the **Update devices using Jabra+ for admins** pane, you can toggle the switch **ON**, to enable firmware management in **Jabra+** for admins. When you switch it **OFF**, you manage firmware through a third-party platform.   
4. In the **Standard Room** page, in the **Firmware Policy** tab, in the **Always keep devices updated** pane, you can toggle the switch **ON** to always use the latest firmware for all Jabra Meeting room devices in the Room inventory. When you switch it **OFF**, all Jabra meeting room devices continue using their current firmware version.   
5. In the bottom ribbon, click **Publish Changes** and confirm. At this point, you are now, by default, managing firmware for Jabra meeting room devices in **Jabra+** for admins. 

To enable or disable firmware management for personal devices: 

1. On the left-hand navigation bar, click **Personal Devices** **\>** **Configurations**   
2. In the **Configurations** page, click the **Standard Configuration** pane 

3. In the **Standard Configuration** page, in the **Firmware Policy** tab, in the **Update devices using Jabra+ for admins** pane, you can toggle the switch **OFF** to disable firmware management in **Jabra+** for admins. When you switch it **OFF**, you cannot manage firmware for Jabra personal devices, and all Jabra personal devices continue using their current firmware version.   
4. In the bottom ribbon, click **Publish Changes** and confirm 

   The desired firmware policy applies when the end-user restarts their computer with the connected Jabra personal device. 

| Important note  Although there may be a firmware policy in place for the organization´s Jabra personal devices, the following requirements must be met before firmware updates can begin:  The end-user must not be in an active call  If using a wireless Jabra personal device, the battery must be charged at over 30 percent    During the firmware update, ensure that end-users keep their Jabra personal device connected and do not adjust any settings on their Jabra device until the firmware update process is complete. If you or end-users experience any issues while updating firmware, see the Appendix & Troubleshooting section.  |
| :---- |

### **7.3.3 Setting an existing firmware policy for specific Jabra device models globally** 

Admin users with relevant permissions can edit the **Standard Configuration** and set exceptions for managing firmware for specific Jabra meeting room and personal device models that apply to all Jabra meeting room devices in the **Room** and **Device inventory**. 

The admin user can configure the specific firmware version for a Jabra meeting room device model variant, with an exception that applies to all Jabra meeting room and personal devices of the specific model variants specified. 

For example, there may be an organization where the admin user would like to apply a specific firmware version to a model range of e.g. Jabra Evolve2 75 personal devices. With this approach, all Jabra Evolve2 75 personal devices in the organization would have the (exception) setting, in this case, a specific firmware version applied automatically. 

One common exception that can be set is to toggle the switch **Always use latest firmware** **ON** that then lets a specific variant of the Jabra meeting room or personal device model routinely update to the latest firmware version from Jabra. 

The admin user can also toggle the **Always keep devices updated** switch **OFF**. This means that all of the organization´s Jabra personal and meeting room devices retain their current firmware version, and end-users are *not* prompted to update to the latest firmware when it is made available by Jabra. 

When you want to update the firmware of a Jabra meeting room or personal device model in their respective inventory, you can create a custom firmware policy which requires you to assign or set the created Firmware policy to a specific Room or Device group. 

To set an exception for firmware updates of a specific Jabra device model: **Meeting room devices** 

1. On the left-hand navigation bar, click **Meeting Rooms** **\>** **Room configurations**   
2. On the **Room configurations** page, click the **Standard Room** pane 

3. In the **Standard Room** page, in the **Firmware Policy** tab, in the **Update devices using Jabra+ for admins** pane, toggle the switch **ON** to enable firmware management for all Jabra Meeting room devices in the Room inventory. When you switch it **OFF**, you manage firmware through a third-party platform.   
4. In the **Standard Room** page, in the **Firmware Policy** tab, in the **Always keep devices updated** pane, keep the toggle switch **OFF**   
5. In the bottom ribbon, when you click **Publish changes** and confirm, all Jabra meeting room devices continue using their current firmware version   
   1. To instead select a specific firmware version or to **Always use latest firmware** for a specific Jabra device model, click **Add model** and on the list, select the relevant   
      Jabra meeting room device model 

      * For Jabra PanaCast 50 RS or BYOD – select **PanaCast 50**   
      * For Jabra PanaCast 50 VBS – select **PanaCast 50 Video Bar System**   
   2. In the bottom ribbon, click **Continue**   
   3. In the **Manage settings** page, in the **Firmware** pane, toggle the switch **Always use latest firmware** or in the *Firmware update* drop-down menu, select the desired   
      Firmware version   
   4. If you choose an older firmware than the one you are currently using, in the **Changing firmware version** dialog box, click **Yes, I am sure**   
6. To apply the changes, in the bottom ribbon, click **Publish** and in the **Publish model settings?** dialog box, click **Publish** again to confirm   

   After you click **Publish**, the desired custom firmware policy is applied, and any pending firmware updates are performed based on the schedule for device updates. 

**Personal devices** (*Beta*) 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Configurations**   
2. In the **Configurations** page, click the **Standard Configuration** pane 

3. In the **Standard Configuration** page, in the **Firmware Policy** tab, toggle the **Update devices using Jabra+ for admins** switch **ON** to manage firmware in **Jabra+ for admins** 

4. In the **Standard Configuration** page, in the **Firmware Policy** tab you can switch **OFF** the **Always keep devices updated** to the latest firmware for all Jabra Personal devices in the Device inventory. In the bottom ribbon, when you click **Publish changes** and confirm, all Jabra Personal devices continue using their current firmware version.   
   1. To choose a specific firmware version for a specific Jabra device model, click the   
      **Model Configurations** tab 

   2. Click **Add model** and select the Jabra devices that you want to set exceptions for   
   3. In the bottom ribbon, click **Continue**   
   4. In the **Manage settings** page, in the **Firmware** pane, in the *Firmware update* dropdown menu, select the desired Firmware version   
5. To apply the changes, in the bottom ribbon, click **Publish,** and in the **Publish model settings?** dialog box, click **Publish** again to confirm   

   #### **Tip** 

   If you have more than one Jabra device model, click **Next model** until you see the button **Publish**. 

For changes to take effect, ensure you restart the computer to which the Jabra personal device is connected. The changes are applied when the end-user logs in to Windows® again. 

### **7.3.4 Creating and setting a firmware policy for Jabra device models** 

For a Jabra meeting room device model, an admin user can create a custom firmware policy in a **Room Configuration** that you created, which lets you set a specific firmware version for a Jabra meeting room device model which you can assign to a room. 

For Jabra personal devices, an admin user can create a custom firmware policy for a Device group and apply the specific firmware version to all personal device models within the group. 

For example, there may be a group of Jabra Evolve2 65 headsets within a specific device group, and the admin user wants a specific firmware policy that was created to apply to that specific device group. In the case of meeting room devices, the admin user may have a specific firmware policy that was created and would like it applied to a specific room (with a meeting room device within the room). 

**Meeting room devices** 

To set a previously created firmware policy for a specific Jabra meeting room device model in a Room, you must follow the procedure and assign the firmware policy to a Room. 

1. On the left-hand navigation bar, click **Meeting Rooms \> Room configurations**   
2. Click the pane with the configuration that you previously created where you would like to set a custom firmware policy   
3. In the **Firmware Policy** tab, in the **Update devices using Jabra+ for admins** pane, toggle the switch **ON** and in the **Always keep devices updated** pane, toggle the switch **OFF** 

4. In the top right-hand side of the page, click **Add model** to select the Jabra device model(s), for example, **PanaCast 50 Video Bar System** or **PanaCast 50** for P50 BYOD/P50 RS, to which the custom firmware policy applies   
5. At the bottom of the **Select models** page, on the ribbon, click **Continue**   
6. In the **Manage settings** page, in the **Firmware** pane, select a specific firmware version or switch **ON** the toggle **Always use latest firmware** for a specific Jabra device model in the relevant configuration 

   a. If you choose an older firmware than the one you are currently using, in the **Changing firmware version** dialog box, click **Yes, I am sure** 

7. At the bottom of the page, on the ribbon, click **Publish** and click **Publish** again to confirm.   

**Assigning the firmware policy to a Room** 

1. On the left-hand navigation bar, click **Meeting Rooms** **\> Room inventory**   
2. On the Room inventory list, click the relevant room name    
3. On the **Room** page, in the **Room Configuration** pane, click the pencil icon (edit menu)   
4. In the **Change configuration** dialog box, in the drop-down menu, select the name of the configuration you previously created, and click **Change configuration** to confirm 

After you click **Change configuration**, the firmware policy you chose is assigned to the Room, and any pending firmware updates are performed based on the schedule for device updates. When this happens, Jabra meeting room devices automatically reboot. 

**Personal devices** (*Beta*) 

To set a previously created firmware policy for a specific Jabra personal device model in a Device group: 

1. On the left-hand navigation bar, click **Personal devices \> Configurations**   
2. Click the pane with the relevant configuration where you would like to set a custom firmware policy. For example, *Call center devices configuration*   
3. In the **Firmware Policy** tab, in the **Update devices using Jabra+ for admins** pane, toggle the switch **ON** 

4. In the **Firmware Policy** tab, in the **Always keep devices updated** pane, toggle the switch **OFF** 

5. In the top right-hand side of the page, click **Add model**   
6. Select the Jabra device model(s) to which the custom firmware policy applies   
7. At the bottom of the page, on the ribbon, click **Continue**   
8. In the **Manage settings** page, in the **Firmware** pane, click the drop-down menu and select the firmware you want to use for the relevant configuration 

   a. If you choose an older firmware than the one you are currently using, in the **Changing firmware version** dialog box, click **Yes, I am sure** 

9. At the bottom of the page, on the ribbon, click **Publish** and confirm.   

**Assigning the Firmware policy to a Device group** 

Next, ensure you assign a firmware policy to a Device group that you have previously created; otherwise, your firmware policy is not applied. 

To assign a configuration to a Device group: 

1. On the left-hand navigation bar, click **Personal devices** **\> Device groups**   
2. In the upper-right hand of the screen, click the action menu (three-dot menu) and click **Change configuration**   
3. In the **Change configuration** dialog box, in the drop-down menu, select the name of the configuration you created, and click **Change configuration**   

   For changes to take effect on the Jabra devices in a Device group, ensure you restart the computer that the Jabra device is connected to. When the end-user logs in to Windows® again, the changes are applied. 

## **7.4 Locking settings for specific Jabra meeting room and personal device models** 

An admin user (*Owner* or *Member with edit rights* for meeting rooms or personal devices) can lock specific settings that affect specific Jabra meeting room or personal device model(s) in their respective inventories, or they can lock settings in a configuration that is assigned to either a Room or Device group. 

Locking a setting ensures that when different admin users adjust settings on a single Jabra meeting room device or adjust settings remotely of a single Jabra personal device, the other admin users can only change settings that have not been previously locked. 

When an admin user sets **Exceptions** to the **Standard** or **Standard Room Configuration** and wants a specific setting to apply as a locked setting for a Jabra meeting room or personal device model, they are locking settings for all Jabra meeting room or personal devices of a model variant, globally. 

For example, your business may follow a specific audio or hearing protection standard, and you want to lock this setting, globally. In this case you can apply and deploy the *Hearing Protection* setting as a locked setting in the **Standard** or **Standard Room Configuration**. 

### **7.4.1 Locking settings for specific Personal or Meeting Room device models globally** 

An admin user can lock settings for specific meeting room device models in the **Room**   
**Configurations** menu item and/or lock settings for specific personal devices in the **Configurations** menu item. The locked settings apply to all devices in the Room or Device inventory. 

To lock settings for a specific Jabra meeting room device model or personal device globally: 

1. On the left-hand navigation bar, click **Meeting rooms \> Room configurations** or **Personal devices \> Configurations** 

2. Click the **Standard Room** pane or **Standard Configuration** pane 

3. On the upper-right-hand side of the page, click the **\+Add model** button   
4. On the list, click to select the name of the relevant Jabra meeting room or Jabra personal device, for example, **PanaCast 50** for P50 RS/P50 BYOD or **PanaCast 50 Video Bar System**, and then click **Continue**   
5. In the **Manage settings** page, toggle the relevant switches on the settings that you want to lock   
6. To apply the locked settings, in the bottom ribbon, click **Publish**, and in the **Publish model settings?** dialog box, to confirm, click **Publish** again.   

   After you click **Publish**, settings are applied immediately, and Jabra meeting room devices may automatically reboot. 

**7.4.2 Locking settings for Jabra meeting room devices in specific Rooms** An admin user can lock settings for Jabra meeting room devices in specific Rooms. 

To lock settings for a Jabra meeting room device in a specific room: 

1. On the left-hand navigation bar, click **Meeting rooms \> Room configurations**   
2. Click on a Room configuration pane that you have previously created   
3. On the upper-right hand side of the page, click the **\+Add model** button   
4. On the list, click to select the name of the relevant Jabra meeting room device, for example, Jabra PanaCast 50, and then click **Continue**   
5. In the **Manage settings** page, toggle the relevant switches for the settings that you want to lock 

6. To apply the locked settings, in the bottom ribbon, click **Publish**, and in the **Publish model settings?** dialog box, click **Publish** again to confirm   
7. On the left-hand navigation bar, click **Meeting Rooms** **\> Room inventory** and find the relevant room name    
8. In the **Room** page, in the **Room Configuration** pane, click the pencil icon (edit menu)   
9. In the **Change configuration** dialog box, in the drop-down menu, select the name of the configuration with the locked settings you previously created, and click **Change configuration** to confirm   

   After you click **Change configuration**, settings are published immediately, and your Jabra meeting room devices may automatically reboot. 

### **7.4.3 Locking settings for end-users for Jabra personal devices in a Device Group** 

When an organization manages Jabra personal devices, i.e., an admin user has a Device group to which specific Jabra personal device(s) belong to, they can lock the Jabra device's settings for an end-user. This feature works for one or a group of Jabra personal devices within a Device group. 

#### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services.    
To lock settings for end-users: 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Configurations**   
2. In the **Configurations** page, find the pane with the configuration name of where the Jabra device you want settings locked has been added, for example, *My call-center configuration*, and click it.   
3. On the upper-right-hand side of the page, click the **\+Add model** button   
4. In the list of Jabra device models, click the name of the relevant device, for example, Jabra Evolve2 65   
5. In the relevant setting, toggle the **Lock for end user** switch   
6. To apply the locked settings, in the bottom ribbon, click **Publish** and confirm. 

   Settings are locked the next time an end-user restarts their computer with the connected Jabra personal device.
