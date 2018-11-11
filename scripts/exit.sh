echo "Killing roscore and scripts..."
sudo killall -9 roscore
killall -9 rosmaster
killall -9 master_discovery
killall -9 master_sync
echo ""
rostopic list
echo "so, DONE"
