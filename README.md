# Custom RPI Plant Maintainer Thing
### Features
- Waters your plants
	- Should prevent your plants from dying (idk)
		- Unless you're trying to plant something outside in the middle of Winter

### Hardware
- Raspberry Pi
- Micro-USB cord
- Mirco-SD card
- Header Pins (only if you are using the RPI Zero or Zero W)
- Mega-IO Expansion Card for Raspberry Pi (Link [here](https://www.sequentmicrosystems.com/))
- Wires
- 12V Power Brick/Supply
- Solenoid Valve (Link [here](https://www.amazon.com/gp/product/B071JDFVNQ/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1))
- Water Tank
- Soldering Iron (obviously)

### To start it up:

- Download this Respoitory
- Have a [Resin.io](https://resin.io/) account
- Make an application on the Resin Dashboard
- Download the custom image file and write it to a Micro-SD card (I used [Etcher](https://etcher.io/))
- Insert the Micro-SD card into your Raspberry PI and power it on
- If you don't see your device on the Resin.io Dashboard after 10 minutes, you have done something wrong
- Install the [Resin CLI](https://github.com/resin-io/resin-cli) onto your computer (not the Raspberry Pi)
  - This should not be installed into the root of this repository
- CD into this repository, wherever you downloaded it
- Type `resin login` and follow the instructions to login to your Resin.io account

# MORE INSTRUCTIONS COMING WHEN I ACTUALLY MAKE MY OWN
