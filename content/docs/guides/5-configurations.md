---
title: "Configurations"
date: 2025-06-23T14:40:20.617Z
weight: 5
---

#### Configurations

A configuration is a collection of settings that includes firmware management for Jabra meeting room and personal devices.

When adding a Jabra device to the Jabra+ platform, a default configuration with Jabra-recommended settings is automatically applied. A configuration includes a default firmware policy. See the firmware management topic for more information.

The standard configuration and standard room configuration are the defaults for all Jabra meeting rooms and personal devices in the organization, respectively.

In the Configurations menu item, admin users can set exceptions for specific Jabra device models that apply to either all Jabra meeting room devices in the physical meeting rooms or all Jabra personal devices.

## Note

Setting exceptions overwrites and modifies the standard configuration or standard room configuration .

For example, admin users can designate a group of Jabra personal devices that require a specific setting or a specific firmware version; This can be achieved when you create a device group and then create a configuration and then assign it to the device group.

For Jabra meeting room devices, room configurations can be created to tailor specific room experiences. For example, you can select specific Jabra meeting room device models, customize the available model settings, and then assign or bulk assign the created room configuration to rooms in the room inventory .

Additionally, you can duplicate configurations or create configurations with customized firmware policies, ensuring that all Jabra devices in the organization benefit from the latest firmware releases.

## Configurations for Jabra personal devices

It is recommended that the configuration approach chosen by an admin user is based on the level of complexity for firmware and settings management.

The following are three approaches to configuring Jabra personal devices in the platform:

- - Standard configuration : This is the default configuration. This approach is suitable when the admin user wants the same configuration applied to all Jabra personal devices in the organization's device inventory . Therefore, the standard configuration affects all Personal devices not part of a device group , and applies immediately and automatically to the entire organization, ensuring all Jabra personal devices are continuously updated to the latest firmware versions, effectively deploying an organization-wide firmware policy.
- - Exceptions : You can set and add exceptions to the standard configuration when all Jabra personal device models require the same configuration settings, with some specific exceptions. This approach lets you set a specific setting for a specific Jabra personal device model across the board.

### 

- - Create configuration : In this approach you can create a new configuration to apply specific settings to one or many groups of Jabra personal devices and determine their firmware policy. With this approach, you can effectively replace the standard configuration for a group of specific Jabra personal devices with the settings that were previously chosen in the new configuration. Another way to use Create configuration is to test a Jabra personal device setting on a group of specific Jabra device models before mass deployment.

## Setting Exceptions to the standard configuration

You can edit the standard configuration and set exceptions for Jabra personal device model settings, such as firmware management (e.g.: force a specific Jabra personal device model to use a predetermined firmware) or device settings management. The exception(s) are then applied automatically to the device inventory .

For example, you may have an organization where specific settings need to apply to a model range of Jabra Evolve2 75 personal devices, such as a low or high Sidetone level, On-head detection , or other settings. With this approach, all Jabra Evolve2 75 personal devices in the organization automatically apply the setting.

## To do this:

- - On the left-hand navigation bar, click Personal devices > Configurations
- - On the Configurations page, click the Standard Configuration pane
- - On the Standard Configuration page, click the Model Configurations tab
- - On the top right-hand side of the page, click Add model and select the relevant Jabra personal device, for example, Jabra Evolve2 75
- - In the bottom ribbon, click Continue
- - On the Manage settings page, adjust the desired settings. You can also lock specific settings for end-users by toggling the relevant switches
- - To apply the changes, in the bottom ribbon, click Publish and in the Publish model settings? dialog box, click Publish again to confirm

For changes to take effect, ensure you restart the computer that the personal device is connected to. When the end-user logs in to Windows® again, the changes are applied.

## Walkthrough: Creating and assigning a configuration for personal devices

## Note

This walkthrough is best suited for admin users in organizations with specific requirements for their Jabra personal device models.

This walkthrough lets you create a new configuration for specific Jabra personal device models; This requires more effort and adds complexity when managing Jabra personal devices remotely.

In this approach, device groups play an important role because you deploy and manage Jabra device model configuration or settings for each group of Jabra personal devices (instead of all Jabra personal devices in the device inventory ).

An example of when you would create a configuration is in a call center scenario or an open office setting, where a group of people using Jabra headsets would prefer a quieter environment.

### 

In this case, the admin user creates a configuration whereby the Sidetone feature ( audio feedback from the person s own voice to improve a call experience ' ) is adjusted accordingly, letting headset users hear themselves when speaking on the headset microphone.

Be aware that when you delete an assigned configuration, Jabra personal devices are automatically reassigned the standard configuration.

To begin the walkthrough, perform all procedures from A to D:

## A. Creating a device group

You must create a device group before Jabra personal devices can be sorted into one or many device groups. To do this, see the following procedure. After creating a device group, the admin user must add the Jabra personal device(s) to the device group.

## B. Adding Jabra devices to a device group

After creating a device group , the admin user must add the Jabra personal device(s) to a device group. To do this see the following procedure. After adding Jabra personal devices to a device group, you must continue with creating a configuration that applies to Jabra personal devices in the device group.

## C. Creating a configuration

To assign specific settings to a group of Jabra personal devices in a device group , you must first create a configuration.

### 

After you create and save your configuration, you can optionally duplicate the configuration and use it for other device groups you may have. For the procedure, see the Duplicating a configuration for personal or meeting room devices topic.

To create a configuration:

- - On the left-hand navigation bar, click Personal devices > Configuration
- - On the Configurations page, click Create configuration , and in the Create configuration dialog box, in the fields provided, enter a Name and optionally a Description and click Create
- - In the Add model configurations? dialog box, click Add models

### 

- - When you click Skip adding models , you can perform the following steps from the Configurations menu item later.

- - To select models, find the Jabra personal devices you want to assign a configuration to, and check the checkbox of the relevant Jabra device models and when you are finished, in the bottom ribbon, click Continue
- - On the Manage settings page, adjust the settings for the chosen Jabra personal device model. When you are finished, in the bottom ribbon, click Publish , and to confirm, click Publish again.

### 

## Tip

When selecting multiple models, the Publish button changes to Next model so you can seamlessly configure all models within the configuration.

For changes to take effect, you must assign a configuration to a device group . Optionally, before you assign a configuration, you can lock settings for end-users for Jabra personal devices in a device group. For the procedure, see the Locking settings topic.

## D. Assigning a configuration to a device group

After creating a new configuration for Jabra personal devices, you must assign it to a device group . See the procedure on Assigning a created configuration to a device group or a room.

## Room configurations for Jabra meeting room devices

With room configurations, an admin user can mass manage Jabra meeting room devices with a shared firmware policy and settings as soon as they are added to the room inventory.

Changing model settings for your Jabra meeting room devices lets you configure the room experience depending on the size and typical usage of a physical room.

The room configuration approach you choose is based on the level of complexity of your firmware and settings management. Standard room configuration is the least complex approach and the most recommended.

An admin user can also set exceptions to the standard room configuration , or the most complex approach is when you create a configuration from the ground up.

## Note

As changes are implemented, Jabra meeting room devices may automatically reboot unless they are on an active call.

The following are approaches to configuring your Jabra meeting room devices in the platform:

- - Standard Room Configuration : This is the default room configuration and is suitable when you want the same room configuration applied to all Jabra meeting room devices that appear as rooms in the room inventory . Choosing standard room configuration affects all Jabra meeting room devices not assigned to a newly created configuration, and it applies immediately and automatically to the entire organization (irrespective of the location) ensuring all Jabra meeting room devices follow the same firmware policy and Jabrarecommended model settings.
- - Exceptions : In the standard room configuration , you can set model exceptions to set the same room configuration settings for all their Jabra meeting room devices, with specific exceptions applied to a Jabra meeting room device model configuration. For example, an owner or member with edit rights (for meeting rooms) can modify the default Jabra-recommended model setting for image brightness on the PanaCast 40/50 VBS; this exception replaces the default setting for image brightness on all PanaCast 40/50 VBS meeting room devices that are provisioned to the room inventory .

### 

## Note

When setting exceptions or creating a room configuration, you must select the corresponding Jabra meeting room device model, for example, when you add a model configuration for the Jabra PanaCast 50 RS or Jabra PanaCast 50 BYOD, you must select the PanaCast 50 option.

When you have a Jabra PanaCast 40/50 VBS, you must select one of the PanaCast Video Bar System options (i.e. the video service provider MTR, ZR or BYOD), however, there are exceptions. See the Firmware bundles and specific firmware versions topic for guidance.

- - Create room configuration : In this approach, you must create room configurations to apply specific settings to one or many rooms with Jabra meeting room devices and determine their firmware policy. With this approach, you effectively replace the standard room configuration for specific rooms and their associated Jabra meeting room devices with the previously chosen settings, enabling you to configure Jabra meeting room device model variants that can be assigned to rooms depending on the room type or typical usage.

## Setting exceptions to a standard room configuration

An admin user can edit the standard room configuration , set exceptions for specific Jabra meeting room device models or set exceptions for device model configurations, settings and firmware. For firmware updates, see the firmware management chapter.

When you have both Jabra PanaCast 50 Room System (RS) and Jabra PanaCast 50 -Bring Your Own Device (BYOD) in your organization's room inventory , and want to set an exception to either PanaCast 50 RS or PanaCast 50 BYOD, you must Create a room configuration selecting the PanaCast 50 card, and assign it to the rooms where the specific PanaCast 50 RS or PanaCast 50 BYOD are located.

### 

Depending on the video service provider that you chose during provisioning for your PanaCast 40/50 VBS, when selecting models in a configuration, ensure you select the matching card, as each variant has their own collection of model settings.

For example, if you have a PanaCast 50 VBS and during provisioning you select the Microsoft® Teams variant as video service provider, ensure you select the PanaCast Video Bar Systems (Microsoft Teams) card.

### 

The exception(s) are applied automatically to all Jabra meeting room devices in the room inventory for the specified Jabra meeting room device model. The default Jabra recommended setting(s) for your Jabra meeting devices are then replaced by the model setting(s) you set.

To set an exception in the standard room for model settings management:

- - On the left-hand navigation bar, click Meeting rooms > Room Configurations
- - On the RoomConfigurations page, click the Standard Room pane
- - On the Standard Room page, click the Model Configurations tab
- - On the top right-hand side of the page, click Add model and select the relevant Jabra meeting room device model
- - In the bottom ribbon, click Continue
- - On the Manage settings page, adjust the desired setting you would like to set as an exception.
- - To apply the changes, in the bottom ribbon, click Publish, and in the Publish model settings? dialog box, click Publish again to confirm

Settings are published or applied now, and your Jabra meeting room devices may automatically reboot.

## Walkthrough: Creating and assigning a room configuration

## Note

Creating a configuration is best suited for an organization with specific requirements for their Jabra device models.

This walkthrough lets you create room configurations for specific Jabra meeting room device models and assign the newly created room configuration to one or many specific rooms. This requires more effort and adds complexity when remotely managing Jabra meeting room devices.

The added complexity, however, enables you to fine-tune the settings of the Jabra meeting room devices to create a customized experience for a specific type of meeting room.

A sample use case for creating a room configuration can be as follows: In an organization, you may have a small room that fits a seat count of two and is typically used for face-to-face meetings. In this case, you can create a configuration, whereby the Field of view setting is adjusted accordingly from the default 180° to a custom 120°.

### 

In the walkthrough that follows, you can deploy and manage settings for a specific Jabra meeting room device model within a room, instead of all Jabra meeting room devices in the organization´s room inventory .

To begin the walkthrough, continue with both the A and B procedures that follow:

## A. Creating a room configuration

To create a new room configuration :

- - On the left-hand navigation bar, click Meeting rooms > Room configurations
- - On the Room configurations page, click Create room configuration , and in the Create room configuration dialog box, in the fields provided, enter a Name and optionally a Description and click Create
- - In the Add model configurations? dialog box, click Add models

### 

- - When you click Skip adding models , you can perform the following steps from the Room configurations menu item later.

- - To select the specific meeting room device models on the list, find the Jabra meeting room devices you would like to assign a configuration to, and check the checkbox of the relevant Jabra meeting room device, and in the bottom ribbon, click Continue
- - On the Manage settings page, adjust the settings for the chosen Jabra device model(s). When you are finished, in the bottom ribbon, click Publish , and to confirm, click Publish again.

For changes to take effect and to finish this walkthrough, the next step is to assign the room configuration to a room. Optionally, before you assign an already created configuration, you can also see the locking settings for specific Jabra meeting room device models in a room procedure.

## B. Assigning a created room configuration to a room

You have created a new configuration and must assign it to a room. See the procedure Assigning a created configuration to a device group or a Room.

## Assigning a created configuration to a device group or a room

For a configuration to take effect on a group of Jabra personal devices and replace the default standard configuration for the group of Jabra devices, you must change the assigned configuration of the device group .

For the previously created room configuration to take effect, you must assign the configuration to a room in your room inventory or a room that you have grouped into a Location. Optionally, to bulk assign a previously created room configuration to many rooms, see the procedure in the appendix.

### 

- - To assign a configuration to a device group:

- - On the left-hand navigation bar, click Personal devices > Device groups
- - On the Device groups page, find and click the relevant device group pane
- - In the upper-right hand of the screen, click the action menu (three-dot menu) and click Change configuration
- - In the Change configuration dialog box, in the drop-down menu, select the configuration name you created, and click Apply .

For changes to take effect on the Jabra personal devices in a device group, ensure you restart the computer that the Jabra personal device is connected to. Changes are applied when the end-user (of the Jabra personal device) logs in to Windows® again.

At this point, you have now assigned a configuration to a device group.

### 

- - To assign an already created room configuration to a room:

- - On the left-hand navigation bar, click Meeting rooms > Room inventory
- - On the Meeting room inventory table, click the relevant room name
- - On the Room page, in the Room configuration pane, click the pencil icon (edit menu)
- - In the Change configuration dialog box, in the drop-down menu, select the name of the configuration you previously created, and click Apply to confirm

After you click Apply , settings are published or applied, and your Jabra meeting room devices may automatically reboot. In the case of firmware management, any pending firmware updates are performed based on the schedule for device updates.

At this point, you have now assigned a room configuration to a room.

## Settings lock for Jabra device models

You can lock specific settings that affect specific Jabra meeting room or personal device model(s) in their respective inventories or can also lock settings in a configuration that is assigned to either a room or device group .

Locking a setting ensures that when different admin users adjust settings of a single Jabra meeting room device or adjust settings remotely of a single Jabra personal device, the other admin users can only change settings that have not been previously locked.

When you set exceptions to the standard configuration or standard room configuration and wants a specific setting to apply as a locked setting for a Jabra meeting room or personal device model, you are locking settings for all Jabra meeting room or personal devices of a model variant, globally.

For example, your business may follow a specific audio or hearing protection standard, and you want to lock this setting, globally. In this case you can apply and deploy the Hearing Protection setting as a locked setting in the standard configuration or standard room configuration .

You can also lock settings for a specific meeting room device model in a specific room only, to do this, see the locking settings for Jabra meeting room devices in specific rooms topic.

### 

On the other hand, to lock settings for a specific Jabra personal device variant in a specific device group, see the topic locking settings for end-users for Jabra personal devices in a device group.

## Locking settings for specific Jabra device models globally

You can lock settings for specific meeting room device models in the Room configurations menu item and/or lock settings for specific personal devices in the Configurations menu item.

For example, the locked settings can apply to all Jabra PanaCast 50 RS located within the entire room inventory or can apply to all Jabra Evolve2 85 headphones within the entire device inventory .

The locked settings apply to all devices in the room inventory or device inventory .

To lock settings for a specific Jabra meeting room device model or personal device globally:

- - On the left-hand navigation bar, click Meeting rooms > Room configurations or Personal devices > Configurations
- - Click the Standard Room pane or Standard Configuration pane
- - On the upper-right-hand side of the page, click the +Add model button
- - On the list, click to select the name of the relevant Jabra meeting room or Jabra personal device, and then click Continue
- - On the Manage settings page, toggle the relevant switches on the settings that you want to lock
- - To apply the locked settings, in the bottom ribbon, click Publish , and in the Publish model settings? dialog box, to confirm, click Publish again.

After you click Publish , settings are applied immediately, and Jabra meeting room devices may automatically reboot.

## Locking settings for Jabra meeting room devices in specific rooms

You can lock settings for a Jabra meeting room device in a specific room. For example, the locked settings can apply only to the Jabra PanaCast 50 RS within a specific room.

To lock settings for a Jabra meeting room device in a specific room:

- - On the left-hand navigation bar, click Meeting rooms > Room configurations
- - Click the Room configuration pane that you have previously created
- - On the upper-right hand side of the page, click the +Add model button, and on the list, select the name of the relevant Jabra meeting room device, for example, Jabra PanaCast 50 RS, and then click Continue
- - On the Manage settings page, toggle the Lock for end user switch for the setting that you want to lock
- - In the bottom ribbon, click Publish , and in the Publish model settings? dialog box, click Publish again to confirm
- - To assign the locked settings, on the left-hand navigation bar, click Meeting rooms > Room inventory , find the relevant room name and in the Room Configuration pane, click the pencil icon (edit menu)
- - In the Change configuration dialog box, in the drop-down menu, select the name of the configuration with the locked setting(s), and click Change configuration to confirm

### 

After you click Change configuration , settings are published immediately, and your Jabra meeting room devices may automatically reboot.

## Locking settings for Jabra personal devices in a device group

You can also lock settings for one or a group of specific Jabra personal devices within a device group .

For example, locked settings can apply to specific personal device models, such as Jabra Evolve2 85 headphones, Jabra Engage 40 Stereo, whereby the first model would always have Sidetone switched ON , while for the other model it is switched OFF .

To lock settings for Jabra personal devices in a device group:

- - On the left-hand navigation bar, click Personal devices > Configurations
- - On the Configurations page, find and click the pane with the previously created configuration, and on the upper-right-hand side of the page, click the +Add model button
- - In the list of Jabra device models, click to select the name of the relevant device(s) for example, Jabra Evolve2 65, and Jabra Evolve2 85 and click Continue
- - On the Manage Settings page, find the setting you would like to lock, and toggle the Lock for end user switch
- - In the bottom ribbon, click Publish and to confirm, click Publish again.
- - If you selected more than one personal device in step four, click Next model and lock the desired setting(s)
- - To assign the configuration to a device group, on the left-hand navigation bar, click Personal devices > Device groups and then click the device group pane you would like to assign the configuration to, and on the top right-hand side, click the action menu and then click Change configuration
- - In the Change configuration dialog box, in the drop-down menu, click to select the configuration name where you locked settings and click Apply .

Settings are locked the next time an end-user restarts their computer with the connected Jabra personal device.