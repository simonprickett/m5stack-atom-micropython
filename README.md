# M5Stack Atom Matrix MicroPython Live Streams

![M5Stack Atom Matrix](m5stack_atom.png)

## Introduction

This repository contains the code that accompanies my live streaming series in which I played around with installing and running MicroPython code on the M5Stack Atom Matrix device.

## Videos

Check out the videos on YouTube (click the images to view -- come on GitHub we need YouTube embeds in README files!)...

[![Episode 1](m5stack_atom_matrix_micropython_episode_1.png)](https://www.youtube.com/watch?v=bwvli5pEA0A)

In episode 1 I installed MicroPython and wrote code to use the LEDs and button.  Then I demonstrated how to connect to WiFi and read and display the current Cheerlights color using an MQTT broker.

Episode 2 to follow!  I'm aiming to try to use the device's gyroscope next.

Subscribe on [YouTube](https://www.youtube.com/@simonprickett) or [follow me on Twitter](https://twitter.com/simon_prickett) to be notified when it's happening.  My live streams also go out on LinkedIn and Twitch if you prefer.

## The M5Stack Atom Matrix Device

The M5Stack Atom Matrix is a small (24mm square by 14mm tall) IoT device that packs a lot into a small space for a decent price.

It features:

* ESP32 chip with onboard WiFi.
* 4Mb flash memory.
* 5x5 RGB LED matrix - the LEDs are the "neopixel" type that can be individually addressed and set to RGB colors.
* A programmable button (press on the LED matrix!).
* Inertial sensor / gyroscope.
* Grove and USB C connectors.

Check out the full specification sheet on the M5Stack documentation site [here](https://docs.m5stack.com/en/core/ATOM%20Matrix).

There are other devices in the M5Stack Atom range, but this project specifically works with the Matrix model.

These devices cost around US$15 and you can buy them from the usual places:

* Direct from [M5Stack](https://shop.m5stack.com/products/atom-matrix-esp32-development-kit).
* [Pimoroni](https://shop.pimoroni.com/products/atom-matrix-esp32-development-kit?variant=31880178532435) (UK based, worldwide shipping).
* [Adafruit](https://www.adafruit.com/product/4497) (US based, worlwide shipping).
* Others...

## Installing MicroPython on the Device

The device doesn't come with MicroPython pre-installed (it's set up to work with C and the [Arduino IDE](https://www.arduino.cc/en/software)).  Installing MicroPython is a relatively simple process: use the `esptool` Python script to erase the flash, download the right MicroPython image for it, and use the same `esptool` to copy the image to the device.

Instructions are provided on the [device's page on the MicroPython site](https://micropython.org/download/M5STACK_ATOM/).

Once you've installed MicroPython you can start a REPL using [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html), [Thonny](https://thonny.org/), or your usual preferred MicroPython development toolchain.  I chose Thonny for the live streams.

When I installed MicroPython, I found that the `esptool` command to copy the runtime onto the device gave an error.  Omitting the baud rate option `--baud 460800` fixed it for me.

## Support for this Device in MicroPython

TODO.

TODO adding further support.

## Code from the First Live Stream

TODO.

## Find this Useful?

If you found this useful and would like to see me make more of this sort of thing, please consider [buying me a coffee](https://ko-fi.com/simonprickett).  All proceeds will be spent on purchasing more devices / sensors etc for future projects which will all be open sourced.  Thanks!
