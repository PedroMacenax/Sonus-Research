<h1 align="center">
<img src="/resource/Logo.png" width="40%" height="40%">
</h1>
<h3 align="center">
	Open-source behavioral modifyer device.
</h3>
<p align="center">
	<strong>
		<a href="https://pedromacena.org/sonus">Website</a>
		•
		<a href="https://discord.gg/jARCsVb">Discord</a>
	</strong>
</p>

I’m <a href="https://www.instagram.com/pedromacenax/">Pedro Macena</a> and when my colleague Julia Andreassa and I faced a problem at dflkjbhsfdjfgkjgsdfjh natalia is boring.

2 years later: this idea became Sonus.

* Fully Open-source - **hardware**, **software**, **firmware**.


**This repo serves as a Build guide, to learn more about the project on <a href="https://pedromacena.org/sonus">pedromacena.org/sonus</a>**

# Building The Hardware
## 1. CURRENT RECOMMENDED BUILD - As of February 2024
### 1.1 Introduction
This is an updated build guide to help people who recently discovered Sonus. It aims to explain how to build the minimum functional product, which can be further improved upon and modified to the individual's liking.

            Following this guide to build a Sonus system assumes basic understanding of electronics and programming Raspberry Pico boards.
            If you encounter any issues, join our Discord and ask for help, we are happy to assist.

### 1.2 ELECTRONICS

The following electronic components are required:

- <a href="https://www.amazon.com/HiLetgo-RP2040-Type-C-Raspberry-Micropython/dp/B0CF53CNXL">Raspberry Pi Pico RP2040 16MB</a>
- <a href="https://www.amazon.com/ACROBOTIC-Real-Time-Breakout-Arduino-Raspberry/dp/B08HW22WNX">Module Rtc Ds1307</a>
- <a href="https://www.amazon.com/DIYables-Adapter-Arduino-ESP8266-Raspberry/dp/B0BXKLNN2L">Micro SD Module</a>.
- <a href="https://www.amazon.com/dp/B09222JFBX">Microphone Module Mems Inmp441</a>.
```
NOTES on VR DISPLAYS:
- The display does not connect to the Microcontroller, it only connects to the Computer running your VR Apps.
- Technically, any PC display/monitor can be configured as the display used by Relativty. Therefore, you can simply test your build on your PC monitor
first to make sure it works, before you decide to spend a significant amount of money on lenses, display(s) and other parts.
- High performance, small form factor displays are expensive, and often very delicate. Handle them with care! :)
```

<h1 align="center">
<img src="/resource/electrical_build.png" width="30%" height="30%">
</h1>

### 1.2.1 Electrical Build
The IMU needs to be connected to the MCU for power and communication.
The MCU connects to your computer via USB to send the IMU readings to SteamVR.

In case of an Arduino Pro Micro, you need to connect the following pins:
```
Pro Micro       IMU
VCC         ->  VCC  
GND         ->  GND  
SDA(pin 2)  ->  SDA  
SCL(pin 3)  ->  SCL  
```  
If you use a different MCU, the SDA and SCL pins might be mapped to different pin numbers.

Also, make sure that the VCC of your MCU is compatible with the rated operating voltage of your IMU.

Supplying incorrect voltage to electronic components may cause damage to them.

The MCU itself simply connets to your computer via the USB port.

### 1.2.2 Connecting the display
As mentioned previously, any display that is compatible with a personal computer should be able to function as your VR display.

In case you are using the recommended one or a similar component that is powered via micro-USB or other USB standard, it is possible that you will encounter situations where the board does not power up. This could be either because the micro-USB cable you are using is too long (so the board cannot power up because the voltage dropped too much), or the board is unable to turn on because the USB port it connects to on the computer side is simply unable to supply enough power. In this case, you might need to try different ports on your computer or a powered USB hub.

<h1 align="center">
<img src="/resource/images/Mechanical_Build.gif" width="25%" height="25%"/>
</h1>

### 1.3 MECHANICAL BUILD

The following parts are required for the Mechanical Build:

- Housing - .STL files for 3D-printable model provided in Relativty_Mechanical_build folder.
- Lenses -  for building the 3D-printable headset, Lenses with 40mm diameter/50mm focal length required. You can often find these on Aliexpress or similar.
- Strap and Facial Interface - e.g. replacement strap + foam for HTC Vive. You can often find these on Aliexpress or similar.

<p align="center"> <img src="ressources/img/front.jpg"> </p>

If you do not have access to 3D-printing, it is also possible (and MUCH simpler) to just use an Android VR Phone case, and modify it to fit your screen and so that you can attach your IMU and MCU to it.

The advantage of this approach is that you get everything in one package, often including IPD adjustment.

<p align="center"> <img src="ressources/img/android-vr.jpg"> </p>

### 1.4 SOFTWARE SETUP

### 1.4.1 Introduction

Relativty depends on 2 main software components:
- the Arduino firmware
- the SteamVR driver

As the system is designed to work with SteamVR, you need to have Steam installed and SteamVR downloaded on your computer.

### 1.4.2 Programming your MCU

As previously mentioned, we recommend you use an Arduino Pro Micro and an IMU supported by the FastIMU Library.
FastIMU is an awesome package that supports many commonly used IMUs and comes with a pre-written Arduino sketch that works with Relativty.

First, you will need to install the Arduino IDE and connect your MCU to your computer via the USB connector.

Once you have it connected and verified your Arduino IDE can work with your MCU, download FastIMU from the library manager.

<p align="center"> <img src="ressources/img/FastIMU-lib.jpg"> </p>

Wire up your IMU as recommended in Section 1.2.1.

Find the Examples/Fastimu/Calibrated_relativty sketch in your Arduino IDE:
<p align="center"> <img src="ressources/img/FastIMU-sketch.jpg"> </p>

And finally, Upload it to your MCU.

FastIMU also includes a built-in calibration tool that can store the calibration data on the IMUs EEPROM.

Calibrating the IMU may help with sensor drift that you can experience over time while using Relativty.

After uploading Calibrated_relativty sketch to the IMU, you can open the Arduino Serial Monitor to initiate a calibration sequence:

<p align="center"> <img src="ressources/img/FastIMU-calib.jpg"> </p>

      NOTE: you only have to do this once, but make sure to follow the instructions given to you in the serial monitor.


### 1.4.3 Installing The SteamVR Driver

To install the Relativty SteamVR driver:
- download the <a href="https://github.com/relativty/Relativty/archive/refs/heads/master.zip">master repository</a>
- inside Relativty-master find the Relativty_Driver\Relativty folder and copy it to your SteamVR installation's drivers directory.
<p align="center"> <img src="ressources/img/driver-copy.jpg"> </p>


### 1.4.4 Configuring The SteamVR Driver

Once you copied the driver files, it is time to configure the driver to work with your setup and computer.

Inside drivers\Relativty\resources\settings, there should be a file called default.vrsettings.

This is the configuration file for the driver.

There are a few things that you need to change.


### Configuring the driver to talk to the MCU
ASSUMING you use an Arduino Pro Micro and the FastIMU library:

In the Relativty_hmd segment find these values:
- hmdPid
- hmdVid
- hmdIMUdmpPackets

and change the values like so:

```
      "hmdPid" : 32823,
      "hmdVid": 9025,
      "hmdIMUdmpPackets":  false,
```

If you are using a different MCU, you need to figure out the USB PID and VID values.

Easiest way is to connect it to your computer via USB and check in Arduino IDE.

In the menu bar, select Tools/Get Board Info:
<p align="center"> <img src="ressources/img/board-info.jpg"> </p>

Take the PID and VID values and convert them to decimal with a <a href="https://www.rapidtables.com/convert/number/hex-to-decimal.html">hex converter</a>.

The converted values then go into the hmdPid and hmdVid values in default.vrsettings.

### Configuring the Display Settings
Now let's look at configuring the driver to work with your Display.

The config variables for the display are in the Relativty_extendedDisplay segment:


For the VR Viewport window's point of origin:
```
      "windowX" : 3440,
      "windowY" : 0,
```

For the VR Viewport's actual size
```
      "windowWidth" : 1920,
      "windowHeight" : 1080,
```

For the VR Viewport's rendering resolution - this should be normally the same as the size
```
      "renderWidth" : 1920,
      "renderHeight" : 1080,
```

And some miscellaneous settings:
```
      "DistortionK1" : 0.4,
      "DistortionK2" : 0.5,
      "ZoomWidth" : 1,
      "ZoomHeight" : 1,
      "EyeGapOffsetPx" : 0,
      "IsDisplayRealDisplay" : true,
      "IsDisplayOnDesktop" : true
```
If the point of origin and size is not configured correctly, the driver will crash and SteamVR will not display anything!

Therefore we need to have a look at and understand the coordinate system SteamVR uses for displays.

Windows always assumes one of the connected displays as your Primary Display.

You can verify which one is your Primary in Display Settings.

You can select each of your displays with the mouse. The one that has "Make this my main display" checkbox greyed out is your Primary Display.

THIS GUIDE ASSUMES THAT THE TOP EDGE OF ALL OF YOUR DISPLAYS ARE ALIGNED IN WINDOWS DISPLAY SETTINGS (as seen on the screenshots)

<p align="center"> <img src="ressources/img/display-settings.jpg"> </p>

Consequently, checking the same on another, non-primary display will make that one your Primary.

The TOP LEFT corner of your Primary Display is the ORIGIN POINT of SteamVR's display coordinate system.

To be able to tell SteamVR where to draw the VR Viewport on your displays, you need to make sure you understand this fact and as a result can identify the correct point of origin for the Viewport.

For example, in a setup like this:

<p align="center"> <img src="ressources/img/display-coordinates.jpg"> </p>

Because the "1" screen is the primary, and the "3" screen is the VR Display, the origin point (the 0,0 coordinate) is on the top left of the "1" screen.

This screen has 3440x1440 resolution.

This means it occupies the X axis from 0 to 3439, and the next screen on its right starts at point 3440.

Therefore, in this case the correct windowX and windowY values are:

```
      "windowX" : 3440,
      "windowY" : 0,
```

If "2" screen was the VR display (and "1" is still the Primary), the correct values would be:

```
      "windowX" : -1920,
      "windowY" : 0,
```
Because the "2" screen's coordinates occupy space over the other side of the origin point.

For windowWidth,windowHeight,renderWidth,renderHeight, simply set the Native Resolution of your VR display.

Once this is all set, save the settings file.

Now you should be ready to start SteamVR.

If everything is set up right, you should get straight into the vr holodeck area:

<p align="center"> <img src="ressources/img/electronics-assembled.jpg"> </p>

If you are encountering any issues with your build:
- open the SteamVR Web Console and copy the entire log file
- Join <a href="https://discord.gg/F8GNKjy6RF">Relativty's Guild on Discord</a>, tell us about the issues you are facing, and upload the log file in the chat. 
<p align="center"> <img src="ressources/img/steamvr-logs.jpg"> </p>


# Sonus-Research
Research repository for the Sonus project

## License

The content of this project itself is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/), and the underlying source code used is licensed under the [GNU GPLv3](LICENSE).
