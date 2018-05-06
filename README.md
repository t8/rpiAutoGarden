# Custom RPI Plant Maintainer
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
- Water Tank (Optional if you just want to connect directly to a hose)
- Outdoor Case of some kind (I used plastic box)
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
- Type `resin login` and follow the instructions to login to your Resin.io account
- CD into **this** repository, wherever you downloaded it
- Then type `git remote add resin <your_username>@git.resin.io:<your_username>/rpiautogarden.git`
  - Replace <your_username> with **your** Resin.io username
- After that, type `git push resin master`
  - Give it some time and you should see a unicorn after this - this means BUILD WAS SUCCESSFUL

Everything should run automatically after this.

**Note:** You must change the WOEID of the watering system to your location. Here's how -
- Find the WOEID assigned to your location [here](http://woeid.rosselliot.co.nz/)
- Go to the `main.py` file located at this repository's root
- Change line 9 from `lookup = weather.lookup(2487365)` to `lookup = weather.lookup(<your_woeid_here>)` then save the file
- Push your local changes to the cloned repository
- Then type: `git push resin master`

### Images of my system:
##### Supplies:
![Hardware](https://tate.ate-a-ta.co/8116d2f9.JPG)
![Materials](https://tate.ate-a-ta.co/c92b1977.JPG)
![Water Tank](https://tate.ate-a-ta.co/25276227.JPG)
##### Before/Middle/After:
![Beginning](https://tate.ate-a-ta.co/72f413ea.JPG)
![Middle](https://tate.ate-a-ta.co/e6dadd9f.JPG)
![End Coming soon](Coming soon)