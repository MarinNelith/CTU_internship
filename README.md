To installe Droidcam on unbuntu and use your phone camera

sudo apt-get update

sudo apt-get install libavutil-dev libswscale-dev libasound2-dev libspeex-dev libusbmuxd-dev libplist-dev libturbojpeg0-dev libgtk-3-dev libappindicator3-dev

install here 
https://github.com/dev47apps/droidcam-linux-client/releases

tar -xvzf droidcam.tar.gz
cd droidcam
make
sudo ./install-client

if error message about v4l2loopback 
sudo modprobe v4l2loopback

